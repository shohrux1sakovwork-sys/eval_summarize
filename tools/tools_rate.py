"""Скорость прогона по meta-файлам: python -m tools.tools_rate"""
import datetime as dt
import json
import os

from analyze_eval import HERE, RESP_DIR

pilot = set((HERE / "ids" / "pilot_ids.txt").read_text().split())
rows = []
for p in RESP_DIR.glob("*.meta.json"):
    m = json.loads(p.read_text(encoding="utf-8"))
    if m["id"] in pilot or m["status"] == "no_pdf":
        continue
    rows.append((os.path.getmtime(p), m))
rows.sort(key=lambda x: x[0])
if rows:
    t0 = dt.datetime.strptime(min(m["started"] for _, m in rows), "%Y-%m-%d %H:%M:%S").timestamp()
    t1 = rows[-1][0]
    n = len(rows)
    rate = n / ((t1 - t0) / 60)
    left = 942 - n
    print(f"готово {n}, за {(t1 - t0) / 60:.1f} мин, {rate:.1f} писем/мин, осталось {left} ≈ {left / rate:.0f} мин")
    sm = sorted(float(m["server_ms"]) for _, m in rows if m.get("server_ms"))
    print(f"server_ms медиана {sm[len(sm) // 2] / 1000:.1f} с")
