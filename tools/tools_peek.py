"""Просмотр: текстовый слой PDF и ocr_text одного письма, поиск строки.
python -m tools.tools_peek <id> <искомое> [<искомое> ...]"""
import json
import sys

import fitz

from analyze_eval import RESP_DIR, load_ref, norm, skel

doc_id, needles = sys.argv[1], sys.argv[2:]
ref, pdf = load_ref(doc_id)
resp = json.loads((RESP_DIR / f"{doc_id}.json").read_text(encoding="utf-8"))
ocr = resp.get("ocr_text") or ""
with fitz.open(pdf) as d:
    pages = [p.get_text() for p in d]
print(f"pages={len(pages)} ocr_used={resp.get('ocr_used')} pages_used={resp.get('pages_used')} "
      f"ocr_len={len(ocr)} layer_len={[len(p.strip()) for p in pages]}")
print("--- layer p1 head:", pages[0][:300].replace("\n", " | ") if pages else "")
print("--- ocr head:", ocr[:500].replace("\n", " | "))
print("--- ocr tail:", ocr[-400:].replace("\n", " | "))
for n in needles:
    sk = skel(n)
    for name, text in (("ocr", ocr), ("layer", "\n".join(pages))):
        s = skel(text)
        i = s.find(sk)
        print(f"[{n}] in {name}: {i >= 0}", s[max(0, i - 60): i + 60] if i >= 0 else "")
