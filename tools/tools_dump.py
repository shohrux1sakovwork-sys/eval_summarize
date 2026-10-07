"""Вспомогательный просмотр results*.jsonl: python -m tools.tools_dump results/results_pilot.jsonl org [all]"""
import json
import sys

path, field = sys.argv[1], sys.argv[2]
show_all = len(sys.argv) > 3
for line in open(path, encoding="utf-8"):
    r = json.loads(line)
    f = r["fields"][field]
    if show_all or f["outcome"] not in ("верно",):
        print(f"{r['id']} | {f['outcome']} | {f['reason']} | pages {r['pages_used']}/{r['page_count']}")
        print("   REF:", f["ref"])
        print("   SRV:", f["resp"])
        if f.get("note"):
            print("   ", f["note"][:250])
