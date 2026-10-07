"""Контекст вокруг совпадений regex в тексте письма (текстовый слой PDF или ocr_text).
python tools_ctx.py <id> <regex> [ширина]"""
import json
import re
import sys

import fitz

from analyze_eval import RESP_DIR, load_ref

doc_id, pat = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 300
ref, pdf = load_ref(doc_id)
with fitz.open(pdf) as d:
    text = "\n".join(p.get_text() for p in d)
if len(text.strip()) < 300:
    text = json.loads((RESP_DIR / f"{doc_id}.json").read_text(encoding="utf-8")).get("ocr_text") or ""
text = re.sub(r"\s+", " ", text)
for m in list(re.finditer(pat, text, re.I))[:4]:
    print("…", text[max(0, m.start() - w): m.end() + w], "…\n")
