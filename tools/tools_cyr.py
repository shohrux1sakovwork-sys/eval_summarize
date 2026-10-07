"""Фрагменты кириллицы в summary: python -m tools.tools_cyr [ids-файл]"""
import json
import re
import sys
from pathlib import Path

from analyze_eval import RESP_DIR

ids = Path(sys.argv[1]).read_text().split() if len(sys.argv) > 1 else [p.stem for p in RESP_DIR.glob("*[0-9].json")]
for i in ids:
    p = RESP_DIR / f"{i}.json"
    if not p.exists():
        continue
    s = json.loads(p.read_text(encoding="utf-8")).get("summary") or ""
    words = re.findall(r"\S*[Ѐ-ӿ]\S*", s)
    if words:
        print(i, len(words), "слов:", " ".join(words[:12]))
