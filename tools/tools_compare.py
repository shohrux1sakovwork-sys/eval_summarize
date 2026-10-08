"""Сравнение прогонов разных моделей на одних и тех же письмах: точность + скорость.

    python -m tools.tools_compare runs/set4_gemma4-12b runs/set4_<модель2> [--ids ids/set4_ok_ids.txt]
        [--md reports/compare_set4.md] [--no-accuracy]

Каждая папка — вывод run_eval.py (--out). Метрики считаются по общим письмам: тем, что у всех
моделей вернули 200 (статусы и ошибки — по всем письмам списка). Источники:
    <id>.meta.json   — client_ms (задержка без ожидания в очереди клиента), server_ms, статус;
    <id>.json        — pages_used, ocr_used, extracted_chars (разбивка задержки);
    run_info.json    — модель LLM, параллельность, время прогона (пропускная способность);
    monitor.csv      — загрузка/память GPU и занятые слоты llama.cpp.
"""
import argparse
import collections
import csv
import json
import statistics
import sys
from pathlib import Path

import analyze_eval as ae
from analyze_eval import FIELDS, FIELD_TITLES, HERE, accuracy, pct


def pctl(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))] if xs else None


def sec(ms):
    return "—" if ms is None else f"{ms / 1000:.1f}"


def load_run(d: Path, ids):
    metas, resps = {}, {}
    for i in ids:
        mp = d / f"{i}.meta.json"
        if mp.exists():
            metas[i] = json.loads(mp.read_text(encoding="utf-8"))
            rp = d / f"{i}.json"
            if metas[i].get("status") == 200 and rp.exists():
                resps[i] = json.loads(rp.read_text(encoding="utf-8"))
    ip = d / "run_info.json"
    runs = json.loads(ip.read_text(encoding="utf-8")) if ip.exists() else []
    mon = []
    mp = d / "monitor.csv"
    if mp.exists():
        with open(mp, encoding="utf-8") as fh:
            mon = list(csv.DictReader(fh))
    label = next((r["label"] for r in reversed(runs) if r.get("label")), d.name)
    return {"dir": d, "label": label, "metas": metas, "resps": resps, "runs": runs, "mon": mon}


def runtime_stats(run, common):
    lat = [run["metas"][i]["client_ms"] for i in common]
    srv = [float(run["metas"][i]["server_ms"]) for i in common if run["metas"][i].get("server_ms")]
    st = {"n": len(lat), "mean": statistics.mean(lat) if lat else None,
          "p50": pctl(lat, 0.5), "p90": pctl(lat, 0.9), "p95": pctl(lat, 0.95), "max": max(lat, default=None),
          "srv_p50": pctl(srv, 0.5)}
    per_page = [run["metas"][i]["client_ms"] / max(1, run["resps"][i].get("pages_used") or 1) for i in common]
    st["per_page_p50"] = pctl(per_page, 0.5)
    wall = sum(r.get("wall_s") or 0 for r in run["runs"])
    done = sum(r.get("n_done") or 0 for r in run["runs"])
    st["rate"] = done / wall * 60 if wall else None
    st["conc"] = sorted({r.get("concurrency") for r in run["runs"]} - {None})
    st["model"] = next((r["llm"]["model_path"] for r in reversed(run["runs"]) if r.get("llm")), "—")
    util = [float(x["gpu_util"]) for x in run["mon"] if x.get("gpu_util")]
    mem = [float(x["gpu_mem_mib"]) for x in run["mon"] if x.get("gpu_mem_mib")]
    busy = [float(x["slots_busy"]) for x in run["mon"] if x.get("slots_busy")]
    st["gpu_util"] = statistics.mean(util) if util else None
    st["gpu_mem"] = max(mem) if mem else None
    st["slots"] = statistics.mean(busy) if busy else None
    return st


def buckets(run, common):
    """медиана задержки по группам писем → {группа: (n, мс)}"""
    groups = collections.defaultdict(list)
    for i in common:
        r, ms = run["resps"][i], run["metas"][i]["client_ms"]
        p = r.get("pages_used") or 0
        groups["стр. 1" if p <= 1 else "стр. 2–3" if p <= 3 else "стр. 4+"].append(ms)
        groups["OCR" if r.get("ocr_used") else "текстовый слой"].append(ms)
    return {g: (len(v), pctl(v, 0.5)) for g, v in groups.items()}


def accuracy_rows(run, common):
    ae.use_resp_dir(run["dir"])
    return {r["id"]: r for r in (ae.analyze_doc(i) for i in common)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", nargs="+", help="папки ответов (--out run_eval.py), по одной на модель")
    ap.add_argument("--ids", help="список id; по умолчанию — все id из первой папки")
    ap.add_argument("--md", help="записать таблицы в markdown-файл")
    ap.add_argument("--no-accuracy", action="store_true", help="только скорость")
    args = ap.parse_args()

    dirs = [(HERE / d).resolve() for d in args.dirs]
    if args.ids:
        ids = (HERE / args.ids).read_text(encoding="utf-8").split()
    else:
        ids = sorted(p.name[:-len(".meta.json")] for p in dirs[0].glob("*.meta.json"))
    runs = [load_run(d, ids) for d in dirs]
    common = sorted(set(ids).intersection(*(r["resps"] for r in runs)))
    out = []

    def p(line=""):
        out.append(line)
        print(line)

    p(f"# Сравнение моделей: {', '.join(r['label'] for r in runs)}")
    p()
    p(f"Писем в списке: {len(ids)}; общих (у всех моделей статус 200): {len(common)}.")
    conc = {r["label"]: runtime_stats(r, common)["conc"] for r in runs}
    if len({tuple(c) for c in conc.values()}) > 1:
        p(f"**Внимание:** параллельность прогонов разная ({conc}) — задержки несравнимы.")
    p()

    # --- статусы ---
    p("## Статусы (все письма списка)")
    p()
    p("| Модель | " + " | ".join(["200", "ошибки", "нет ответа", "503 (повторы)"]) + " |")
    p("|---|---|---|---|---|")
    for r in runs:
        ms = r["metas"].values()
        ok = sum(m.get("status") == 200 for m in ms)
        p(f"| {r['label']} | {ok} | {len(ms) - ok} | {len(ids) - len(ms)} | "
          f"{sum(m.get('n_503') or 0 for m in ms)} |")
    p()

    # --- скорость ---
    sts = [runtime_stats(r, common) for r in runs]
    p(f"## Скорость (общие письма, n={len(common)}; задержка client_ms, с)")
    p()
    rows = [
        ("Модель LLM", lambda s: Path(s["model"]).name if s["model"] != "—" else "—"),
        ("Параллельность", lambda s: ", ".join(map(str, s["conc"])) or "—"),
        ("Среднее, с", lambda s: sec(s["mean"])),
        ("Медиана, с", lambda s: sec(s["p50"])),
        ("p90, с", lambda s: sec(s["p90"])),
        ("p95, с", lambda s: sec(s["p95"])),
        ("Макс, с", lambda s: sec(s["max"])),
        ("Медиана server_ms, с", lambda s: sec(s["srv_p50"])),
        ("Медиана на страницу, с", lambda s: sec(s["per_page_p50"])),
        ("Писем/мин (весь прогон)", lambda s: f"{s['rate']:.1f}" if s["rate"] else "—"),
        ("GPU загрузка, ср. %", lambda s: f"{s['gpu_util']:.0f}" if s["gpu_util"] is not None else "—"),
        ("GPU память, макс MiB", lambda s: f"{s['gpu_mem']:.0f}" if s["gpu_mem"] is not None else "—"),
        ("Занятых слотов LLM, ср.", lambda s: f"{s['slots']:.1f}" if s["slots"] is not None else "—"),
    ]
    p("| Метрика | " + " | ".join(r["label"] for r in runs) + " |")
    p("|---" * (len(runs) + 1) + "|")
    for name, f in rows:
        p(f"| {name} | " + " | ".join(f(s) for s in sts) + " |")
    p()
    bks = [buckets(r, common) for r in runs]
    groups = sorted(set().union(*bks))
    p("Медиана задержки по группам писем, с (n):")
    p()
    p("| Группа | " + " | ".join(r["label"] for r in runs) + " |")
    p("|---" * (len(runs) + 1) + "|")
    for g in groups:
        p(f"| {g} | " + " | ".join(f"{sec(b[g][1])} ({b[g][0]})" if g in b else "—" for b in bks) + " |")
    p()
    if len(runs) == 2 and common:
        a, b = runs
        ratio = [b["metas"][i]["client_ms"] / a["metas"][i]["client_ms"] for i in common]
        faster = sum(x < 1 for x in ratio)
        p(f"По письмам: {b['label']} / {a['label']} — медиана отношения задержек {pctl(ratio, 0.5):.2f}; "
          f"{b['label']} быстрее на {faster} из {len(ratio)} писем.")
        p()

    # --- точность ---
    if not args.no_accuracy and common:
        if not (ae.DIR_DATA / "index.parquet").exists():
            print(f"Внимание: нет справочника {ae.DIR_DATA} — причины «нет в справочнике» не определяются "
                  "(на точность не влияет).", file=sys.stderr)
            ae.in_directory = lambda ref_org: (False, "", 0.0)
        acc = [accuracy_rows(r, common) for r in runs]
        p(f"## Точность (общие письма, n={len(common)}; строго / с учётом «формат»)")
        p()
        p("| Поле | " + " | ".join(r["label"] for r in runs) + " |")
        p("|---" * (len(runs) + 1) + "|")
        for f in FIELDS:
            cells = []
            for rows_ in acc:
                ok, fmt, tot = accuracy(list(rows_.values()), f)
                cells.append(f"{pct(ok, tot)} / {pct(fmt, tot)} (n={tot})")
            p(f"| {FIELD_TITLES[f]} | " + " | ".join(cells) + " |")
        p()
        if len(runs) == 2:
            a, b = acc
            la, lb = runs[0]["label"], runs[1]["label"]
            p(f"Расхождения по письмам (строго): «только {la} верно» / «только {lb} верно»:")
            p()
            p(f"| Поле | только {la} | только {lb} |")
            p("|---|---|---|")
            for f in FIELDS:
                only_a = only_b = 0
                for i in common:
                    oa, ob = a[i]["fields"][f]["outcome"], b[i]["fields"][f]["outcome"]
                    if oa in ae.EXCLUDED or ob in ae.EXCLUDED:
                        continue
                    only_a += oa in ae.CORRECT and ob not in ae.CORRECT
                    only_b += ob in ae.CORRECT and oa not in ae.CORRECT
                p(f"| {FIELD_TITLES[f]} | {only_a} | {only_b} |")
            p()

    if args.md:
        (HERE / args.md).write_text("\n".join(out) + "\n", encoding="utf-8")
        print(f"→ {args.md}")


if __name__ == "__main__":
    main()
