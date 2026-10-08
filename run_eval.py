"""Прогон эталонных писем через doc_summarizer POST /summarize.

Примеры:
    python run_eval.py --pilot 50            # выбрать и прогнать пилот (seed фиксирован) → ids/pilot_ids.txt
    python run_eval.py --ids ids/pilot_ids.txt   # прогнать список id
    python run_eval.py --all                 # все письма
    python run_eval.py --all --ref-dir ../db_test_kirimXat_1000_2 --out runs/responses_2   # второй набор
    python run_eval.py --ids ids/set4_ok_ids.txt --ref-dir test_docs/db_test_kirimXat_500_4 \
        --out runs/set4_<модель> --label <модель> --url http://localhost:8091/summarize   # сравнение моделей

Ответ  -> runs/responses/<id>.json
Мета   -> runs/responses/<id>.meta.json  (status, client_ms, server_ms, attempts, error)
Готовые (status 200/413/422/no_pdf) при перезапуске пропускаются; остальные повторяются.
Статистика прогона (для сравнения моделей, см. tools/tools_compare.py):
    <out>/run_info.json — по записи на запуск: метка, модель LLM (/props), параллельность, время;
    <out>/monitor.csv   — раз в MONITOR_EVERY с: загрузка и память GPU, занятые слоты llama.cpp.
В консоль каждые STATS_EVERY писем — скорость, ETA, медиана/p95 задержки, ошибки, GPU.
Ключ берётся из .env и нигде не печатается и не сохраняется.
"""
import argparse
import asyncio
import collections
import glob
import json
import os
import random
import signal
import statistics
import sys
import time
from pathlib import Path

import httpx

HERE = Path(__file__).resolve().parent
REF_DIR = HERE.parent / "db_test_kirimXat"
RESP_DIR = HERE / "runs" / "responses"
URL = "http://localhost:8092/summarize"
MAX_CONCURRENCY = 8          # жёсткий потолок: сервер больше не нагружаем
FINAL_STATUSES = {200, 413, 422, "no_pdf"}
RETRY_503_WAIT = 15
RETRY_503_ATTEMPTS = 5
TIMEOUT = 600
NET_RETRY_ATTEMPTS = 3
LLM_URL = "http://localhost:8001"   # llama.cpp сервер модели: /props, /slots
MONITOR_EVERY = 2                   # с, период опроса GPU и слотов
STATS_EVERY = 10                    # писем между строками статистики


def load_key(env_path: Path) -> str:
    for line in env_path.read_text(encoding="utf-8").splitlines():
        k, _, v = line.partition("=")
        if k.strip() == "DOC_API_KEY":
            return v.strip().strip('"').strip("'")
    sys.exit(f"DOC_API_KEY не найден в {env_path}")


def load_reference():
    """id -> (reference dict, pdf path | None)"""
    out = {}
    for d in sorted(REF_DIR.glob("DOC_*")):
        doc_id = d.name[4:]
        js = list(d.glob("*.json"))
        pdf = list(d.glob("*.pdf"))
        ref = json.loads(js[0].read_text(encoding="utf-8"))["rekvizit_document"]
        out[doc_id] = (ref, pdf[0] if pdf else None)
    return out


def pick_pilot(refs, n, seed):
    """Случайная выборка с фиксированным seed, но с покрытием журналов, ХДФУ, срочных
    и по возможности одним письмом на отправителя."""
    rng = random.Random(seed)
    ids = sorted(i for i, (_, pdf) in refs.items() if pdf)
    rng.shuffle(ids)

    def sender(i):
        return refs[i][0]["hujjat_junatuvchi_tashkilot"].lower()

    def journal(i):
        return (refs[i][0]["jurnal"] or "").split("/")[0].strip()

    chosen, senders = [], set()

    def take(pred, quota):
        got = 0
        for i in ids:
            if got >= quota or len(chosen) >= n:
                break
            if i in chosen or not pred(i):
                continue
            if sender(i) in senders:
                continue
            chosen.append(i)
            senders.add(sender(i))
            got += 1

    take(lambda i: journal(i) == "9", 4)
    take(lambda i: journal(i) == "11", 3)
    take(lambda i: journal(i) == "16", 2)
    take(lambda i: refs[i][0]["xdfu"] == 1, 6)
    take(lambda i: refs[i][0]["shoshilinch"] == 1, 6)
    take(lambda i: (fitz_pages(refs[i][1]) or 0) >= 3, 6)
    take(lambda i: True, n)               # остальное — разные отправители
    if len(chosen) < n:                   # если отправителей не хватило
        for i in ids:
            if len(chosen) >= n:
                break
            if i not in chosen:
                chosen.append(i)
    return chosen


def fitz_pages(pdf):
    try:
        import fitz
        return fitz.open(pdf).page_count
    except Exception:
        return None


def is_done(doc_id):
    meta = RESP_DIR / f"{doc_id}.meta.json"
    if not meta.exists():
        return False
    try:
        return json.loads(meta.read_text(encoding="utf-8")).get("status") in FINAL_STATUSES
    except Exception:
        return False


def write_json(path: Path, obj):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, path)


def pctl(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))] if xs else None


async def nvidia_smi(gpu):
    """→ (загрузка %, память MiB) или (None, None), если nvidia-smi недоступен"""
    try:
        proc = await asyncio.create_subprocess_exec(
            "nvidia-smi", "-i", str(gpu), "--query-gpu=utilization.gpu,memory.used",
            "--format=csv,noheader,nounits",
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.DEVNULL)
        out, _ = await proc.communicate()
        util, mem = out.decode().strip().split(",")
        return int(util), int(mem)
    except Exception:
        return None, None


async def llm_get(client, path):
    try:
        r = await client.get(LLM_URL + path)
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None


async def monitor(gpu, stop, samples):
    """Пишет monitor.csv, пока не выставлен stop; samples — те же строки в памяти."""
    path = RESP_DIR / "monitor.csv"
    new = not path.exists()
    async with httpx.AsyncClient(timeout=5) as client:   # под нагрузкой /slots отвечает медленно
        with open(path, "a", encoding="utf-8") as fh:
            if new:
                fh.write("ts,gpu_util,gpu_mem_mib,slots_busy\n")
            while not stop.is_set():
                util, mem = await nvidia_smi(gpu)
                slots = await llm_get(client, "/slots")
                busy = sum(1 for s in slots if s.get("is_processing")) if isinstance(slots, list) else None
                samples.append((util, mem, busy))
                fh.write(",".join("" if v is None else str(v)
                                  for v in (round(time.time(), 1), util, mem, busy)) + "\n")
                fh.flush()
                try:
                    await asyncio.wait_for(stop.wait(), MONITOR_EVERY)
                except asyncio.TimeoutError:
                    pass


def print_stats(stats, samples):
    el = time.time() - stats["t0"]
    n = stats["done"]
    rate = n / el * 60 if el else 0
    left = stats["total"] - n
    lat = [x / 1000 for x in stats["lat_ms"]]
    line = (f"--- {n}/{stats['total']} за {el / 60:.1f} мин, {rate:.1f} писем/мин, "
            f"ETA {left / rate:.0f} мин" if rate else f"--- {n}/{stats['total']}")
    if lat:
        line += (f" | задержка (200) медиана {statistics.median(lat):.1f} с, "
                 f"p95 {pctl(lat, 0.95):.1f} с, макс {max(lat):.1f} с")
    line += f" | ошибок {stats['errors']}"
    util = [u for u, _, _ in samples if u is not None]
    mem = [m for _, m, _ in samples if m is not None]
    if util:
        line += f" | GPU {statistics.mean(util):.0f}% (ср.), память макс {max(mem)} MiB"
    print(line, flush=True)


async def process(client, sem, key, doc_id, pdf, counters, stats, samples):
    meta = {"id": doc_id, "pdf": str(pdf) if pdf else None, "attempts": 0,
            "status": None, "client_ms": None, "server_ms": None, "error": None,
            "n_503": 0, "started": time.strftime("%Y-%m-%d %H:%M:%S")}
    if pdf is None:
        meta["status"] = "no_pdf"
        write_json(RESP_DIR / f"{doc_id}.meta.json", meta)
        counters["no_pdf"] += 1
        return
    data = pdf.read_bytes()
    async with sem:
        for attempt in range(1, RETRY_503_ATTEMPTS + 1):
            meta["attempts"] = attempt
            t0 = time.perf_counter()
            try:
                r = await client.post(
                    URL, headers={"X-API-Key": key},
                    files={"file": (pdf.name, data, "application/pdf")})
            except httpx.HTTPError as e:
                meta["client_ms"] = round((time.perf_counter() - t0) * 1000)
                meta["status"] = "net_error"
                meta["error"] = f"{type(e).__name__}: {e}"[:2000]
                meta["n_net_err"] = meta.get("n_net_err", 0) + 1
                # обрыв соединения (туннель) — повторяем, но не больше NET_RETRY_ATTEMPTS
                if meta["n_net_err"] < NET_RETRY_ATTEMPTS and not isinstance(e, httpx.ReadTimeout):
                    await asyncio.sleep(RETRY_503_WAIT)
                    continue
                break
            meta["client_ms"] = round((time.perf_counter() - t0) * 1000)
            meta["status"] = r.status_code
            meta["server_ms"] = r.headers.get("x-process-time-ms")
            if r.status_code == 503:
                meta["n_503"] += 1
                meta["error"] = r.text[:2000]
                if attempt < RETRY_503_ATTEMPTS:
                    await asyncio.sleep(RETRY_503_WAIT)
                    continue
                break
            if r.status_code == 200:
                meta["error"] = None
                try:
                    write_json(RESP_DIR / f"{doc_id}.json", r.json())
                except ValueError:
                    meta["status"] = "bad_json"
                    meta["error"] = r.text[:2000]
            else:
                meta["error"] = r.text[:2000]
            break
    meta["finished"] = time.strftime("%Y-%m-%d %H:%M:%S")
    meta["label"] = stats["label"]
    write_json(RESP_DIR / f"{doc_id}.meta.json", meta)
    counters[str(meta["status"])] += 1
    stats["done"] += 1
    if meta["status"] == 200:
        stats["lat_ms"].append(meta["client_ms"])
    else:
        stats["errors"] += 1
    done = sum(v for k, v in counters.items() if k != "_total")
    print(f"[{done}/{counters['_total']}] {doc_id} status={meta['status']} "
          f"server_ms={meta['server_ms']} client_ms={meta['client_ms']} "
          f"attempts={meta['attempts']}", flush=True)
    if stats["done"] % STATS_EVERY == 0:
        print_stats(stats, samples)


async def main_async(ids, refs, key, concurrency, label, gpu, ids_src):
    sem = asyncio.Semaphore(concurrency)
    counters = collections.Counter()
    todo = [i for i in ids if not is_done(i)]
    counters["_total"] = len(todo)
    print(f"Всего {len(ids)}, уже готово {len(ids) - len(todo)}, к обработке {len(todo)}, "
          f"параллельно {concurrency}", flush=True)
    async with httpx.AsyncClient(timeout=5) as c:
        props = await llm_get(c, "/props")
    llm = {k: props.get(k) for k in ("model_path", "total_slots", "build_info")} if props else None
    if props:
        llm["n_ctx"] = (props.get("default_generation_settings") or {}).get("n_ctx")
    print(f"Метка: {label}; LLM: {llm['model_path'] if llm else 'нет ответа от ' + LLM_URL + '/props'}",
          flush=True)
    stats = {"label": label, "t0": time.time(), "done": 0, "total": len(todo), "lat_ms": [], "errors": 0}
    samples, stop = [], asyncio.Event()
    mon = asyncio.create_task(monitor(gpu, stop, samples))
    info = {"label": label, "url": URL, "llm_url": LLM_URL, "llm": llm, "gpu": gpu,
            "concurrency": concurrency, "ids": ids_src, "n_todo": len(todo),
            "started": time.strftime("%Y-%m-%d %H:%M:%S")}
    limits = httpx.Limits(max_connections=concurrency, max_keepalive_connections=concurrency)
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(TIMEOUT), limits=limits) as client:
            await asyncio.gather(*(process(client, sem, key, i, refs[i][1], counters, stats, samples)
                                   for i in todo))
    finally:   # при Ctrl+C/SIGTERM задача monitor уже отменена — сначала сохраняем, потом гасим её
        stop.set()
        del counters["_total"]
        info.update(finished=time.strftime("%Y-%m-%d %H:%M:%S"),
                    wall_s=round(time.time() - stats["t0"], 1), n_done=stats["done"],
                    statuses=dict(counters))
        runs_p = RESP_DIR / "run_info.json"   # список запусков: прогон может идти в несколько заходов
        runs = json.loads(runs_p.read_text(encoding="utf-8")) if runs_p.exists() else []
        write_json(runs_p, runs + [info])
        try:
            await mon
        except asyncio.CancelledError:
            pass
    if stats["done"]:
        print_stats(stats, samples)
    print("Итог:", dict(counters), flush=True)


def main():
    global REF_DIR, RESP_DIR, URL, LLM_URL
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--pilot", type=int, help="выбрать N писем для пилота и прогнать")
    g.add_argument("--ids", help="файл со списком id (по одному в строке)")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--seed", type=int, default=20261005)
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--env", default=str(REF_DIR / ".env"))
    ap.add_argument("--ref-dir", default=str(REF_DIR), help="папка эталона с DOC_<id>/")
    ap.add_argument("--out", default=str(RESP_DIR), help="папка для ответов")
    ap.add_argument("--url", default=URL)
    ap.add_argument("--label", help="метка модели для сравнения (по умолчанию — имя папки --out)")
    ap.add_argument("--llm-url", default=LLM_URL, help="llama.cpp сервер модели (/props, /slots)")
    ap.add_argument("--gpu", type=int, default=0, help="индекс GPU для nvidia-smi")
    ap.add_argument("--pilot-file", default="ids/pilot_ids.txt", help="куда записать выбранный пилот")
    ap.add_argument("--select-only", action="store_true", help="только выбрать пилот, не отправлять")
    args = ap.parse_args()

    REF_DIR, RESP_DIR, URL = Path(args.ref_dir).resolve(), Path(args.out).resolve(), args.url
    LLM_URL = args.llm_url.rstrip("/")
    concurrency = max(1, min(args.concurrency, MAX_CONCURRENCY))
    refs = load_reference()
    if args.pilot:
        ids = pick_pilot(refs, args.pilot, args.seed)
        (HERE / args.pilot_file).write_text("\n".join(ids) + "\n", encoding="utf-8")
        print(f"Пилот: {len(ids)} писем -> {args.pilot_file}")
    elif args.ids:
        ids = [l.strip() for l in Path(args.ids).read_text(encoding="utf-8").splitlines() if l.strip()]
    else:
        ids = sorted(refs)
    if args.select_only:
        return
    RESP_DIR.mkdir(parents=True, exist_ok=True)
    key = load_key(Path(args.env))
    def interrupt(*_):   # SIGTERM/SIGHUP → как Ctrl+C, чтобы run_info.json успел записаться
        raise KeyboardInterrupt
    signal.signal(signal.SIGTERM, interrupt)
    signal.signal(signal.SIGHUP, interrupt)
    ids_src = args.ids or ("pilot" if args.pilot else "all")
    asyncio.run(main_async(ids, refs, key, concurrency, args.label or RESP_DIR.name, args.gpu, ids_src))


if __name__ == "__main__":
    main()
