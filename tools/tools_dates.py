"""Проверка гипотезы: в эталоне дата документа = дата регистрации (kirish_sana)."""
import collections
import json

from analyze_eval import CORRECT, EXCLUDED, HERE, load_ref, parse_ref_date

rows = [json.loads(l) for l in open(HERE / "results" / "results.jsonl", encoding="utf-8")]
c = collections.Counter()
deltas = collections.Counter()
ex = collections.defaultdict(list)
for r in rows:
    f = r["fields"]["date"]
    if f["outcome"] in EXCLUDED:
        continue
    ref, _ = load_ref(r["id"])
    same = ref.get("hujjat_sana") == ref.get("kirish_sana")
    ok = f["outcome"] in CORRECT
    key = ("верно" if ok else f["reason"].split(" (")[0] or f["outcome"], "дата=регистрации" if same else "дата≠регистрации")
    c[key] += 1
    if not ok and f["resp"]:
        kir = parse_ref_date(ref.get("kirish_sana"))
        srv = f["resp"][:10]
        import datetime as dt
        try:
            d = (dt.date.fromisoformat(kir) - dt.date.fromisoformat(srv)).days
            deltas["сервис раньше регистрации" if d >= 0 else "сервис ПОЗЖЕ регистрации"] += 1
            if d < 0:
                ex["later"].append((r["id"], ref.get("hujjat_sana"), ref.get("kirish_sana"), srv))
        except ValueError:
            pass
for k, v in sorted(c.items()):
    print(k, v)
print(deltas)
print("сервис позже регистрации (невозможно для даты документа):", ex["later"][:10])
