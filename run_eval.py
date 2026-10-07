"""Прогон эталонных писем через doc_summarizer POST /summarize.

Примеры:
    python run_eval.py --pilot 50            # выбрать и прогнать пилот (seed фиксирован) → ids/pilot_ids.txt
    python run_eval.py --ids ids/pilot_ids.txt   # прогнать список id
    python run_eval.py --all                 # все письма
    python run_eval.py --all --ref-dir ../db_test_kirimXat_1000_2 --out runs/responses_2   # второй набор

Ответ  -> runs/responses/<id>.json
Мета   -> runs/responses/<id>.meta.json  (status, client_ms, server_ms, attempts, error)
Готовые (status 200/413/422/no_pdf) при перезапуске пропускаются; остальные повторяются.
Ключ берётся из .env и нигде не печатается и не сохраняется.
"""
import argparse
import asyncio
import collections
import glob
import json
import os
import random
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


async def process(client, sem, key, doc_id, pdf, counters):
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
    write_json(RESP_DIR / f"{doc_id}.meta.json", meta)
    counters[str(meta["status"])] += 1
    done = sum(v for k, v in counters.items() if k != "_total")
    print(f"[{done}/{counters['_total']}] {doc_id} status={meta['status']} "
          f"server_ms={meta['server_ms']} client_ms={meta['client_ms']} "
          f"attempts={meta['attempts']}", flush=True)


async def main_async(ids, refs, key, concurrency):
    sem = asyncio.Semaphore(concurrency)
    counters = collections.Counter()
    todo = [i for i in ids if not is_done(i)]
    counters["_total"] = len(todo)
    print(f"Всего {len(ids)}, уже готово {len(ids) - len(todo)}, к обработке {len(todo)}, "
          f"параллельно {concurrency}", flush=True)
    limits = httpx.Limits(max_connections=concurrency, max_keepalive_connections=concurrency)
    async with httpx.AsyncClient(timeout=httpx.Timeout(TIMEOUT), limits=limits) as client:
        await asyncio.gather(*(process(client, sem, key, i, refs[i][1], counters) for i in todo))
    del counters["_total"]
    print("Итог:", dict(counters), flush=True)


def main():
    global REF_DIR, RESP_DIR, URL
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
    ap.add_argument("--pilot-file", default="ids/pilot_ids.txt", help="куда записать выбранный пилот")
    ap.add_argument("--select-only", action="store_true", help="только выбрать пилот, не отправлять")
    args = ap.parse_args()

    REF_DIR, RESP_DIR, URL = Path(args.ref_dir).resolve(), Path(args.out).resolve(), args.url
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
    asyncio.run(main_async(ids, refs, key, concurrency))


if __name__ == "__main__":
    main()
