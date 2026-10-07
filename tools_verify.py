"""Проверка утверждений отчёта."""
import collections
import json

from analyze_eval import HERE, norm_org

rows = [json.loads(l) for l in open(HERE / "results.jsonl", encoding="utf-8")]
adl = [r for r in rows if norm_org(r["ref_org"]) == "adliya vazirligi"]
print("Adliya vazirligi писем:", len(adl), "TSTB:", sum(r["fields"]["number"]["ref"].upper().startswith("TSTB") for r in adl),
      "query HISOBOT:", sum("hisobot" in (r.get("org_resp", {}) or {}).get("query", "").lower() for r in adl))
qq = [r for r in rows if "qoraqalpog" in norm_org(r["ref_org"]) and "adliya" in norm_org(r["ref_org"])]
print("Qoraqalpog'iston AV писем:", len(qq), "ответ/query на каракалпакском (adillik/ministrligi):",
      sum(any(w in ((r.get("org_resp") or {}).get("query") or "").lower() for w in ("adillik", "ministrligi", "a'dillik"))
          for r in qq))
print(collections.Counter(((r.get("org_resp") or {}).get("name") or "")[:60] for r in qq).most_common(5))
