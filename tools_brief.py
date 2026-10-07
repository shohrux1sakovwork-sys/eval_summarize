"""Краткая сводка results*.jsonl в markdown: python tools_brief.py results_pilot.jsonl"""
import collections
import json
import re
import statistics
import sys

from analyze_eval import (CONTENT_JOURNALS, CORRECT, EMPTY_REF, FIELD_TITLES, FIELDS,
                          NOT_PROCESSED, RESP_DIR, accuracy, pct)

rows = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8")]
print(f"Писем: {len(rows)}; статусы: {dict(collections.Counter(str(r['status']) for r in rows))}\n")
print("| Поле | Верно | Всего | Точность | +формат/сомн. | Категории |")
print("|---|---|---|---|---|---|")
for f in FIELDS + ["journal*"]:
    pred = (lambda r: r["ref_journal"] not in CONTENT_JOURNALS) if f == "journal*" else (lambda r: True)
    fld = "journal" if f == "journal*" else f
    ok, len_, tot = accuracy(rows, fld, pred)
    c = collections.Counter(r["fields"][fld]["outcome"] for r in rows if pred(r))
    cats = ", ".join(f"{k} {v}" for k, v in c.most_common())
    title = "Журнал без 9/11/16" if f == "journal*" else FIELD_TITLES[f]
    print(f"| {title} | {ok} | {tot} | {pct(ok, tot)} | {pct(len_, tot)} | {cats} |")

print("\nПричины ошибок (не верно, не пусто в эталоне):")
for f in FIELDS:
    c = collections.Counter(r["fields"][f]["reason"].split(" (")[0] or "—" for r in rows
                            if r["fields"][f]["outcome"] not in CORRECT | {EMPTY_REF, NOT_PROCESSED})
    if c:
        print(f"- {FIELD_TITLES[f]}: " + "; ".join(f"{k} {v}" for k, v in c.most_common()))

ms = sorted(r["server_ms"] for r in rows if r["server_ms"])
if ms:
    print(f"\nВремя сервера: медиана {statistics.median(ms) / 1000:.1f} с, p90 {ms[int(0.9 * (len(ms) - 1))] / 1000:.1f} с, "
          f"макс {ms[-1] / 1000:.1f} с; 503: {sum(r['n_503'] or 0 for r in rows)}")
cyr = 0
n = 0
for r in rows:
    p = RESP_DIR / f"{r['id']}.json"
    if p.exists():
        n += 1
        cyr += bool(re.search("[Ѐ-ӿ]", json.loads(p.read_text(encoding="utf-8")).get("summary") or ""))
print(f"summary с кириллицей: {cyr}/{n}")
