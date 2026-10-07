"""Свойства PDF: python -m tools.tools_pdfinfo <id>"""
import sys

import fitz

from analyze_eval import load_ref

ref, pdf = load_ref(sys.argv[1])
with fitz.open(pdf) as d:
    print("pages", d.page_count, "encrypted", d.is_encrypted, "needs_pass", d.needs_pass,
          "size_MB", round(pdf.stat().st_size / 1e6, 2), "meta", d.metadata)
    for i, p in enumerate(d):
        if i >= 3:
            break
        imgs = p.get_images()
        print(f"p{i + 1}: {p.rect.width:.0f}x{p.rect.height:.0f}pt rot={p.rotation} text={len(p.get_text().strip())} imgs={len(imgs)}",
              [(x[2], x[3]) for x in imgs[:3]])
