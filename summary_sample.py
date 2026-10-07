"""Шаг 4: выборка 40 писем для ручной проверки summary.
python summary_sample.py pick      → summary_sample_ids.txt (seed фиксирован)
python summary_sample.py dump N M  → для писем N..M выборки: тема эталона, summary, текст письма (начало)
"""
import json
import random
import re
import sys

import fitz

from analyze_eval import HERE, RESP_DIR, load_ref

SEED = 404
IDS_FILE = HERE / "summary_sample_ids.txt"

if sys.argv[1] == "pick":
    from analyze_eval import REF_DIR
    ids = sorted(d.name[4:] for d in REF_DIR.glob("DOC_*") if any(d.glob("*.pdf")))
    sample = sorted(random.Random(SEED).sample(ids, 40))
    IDS_FILE.write_text("\n".join(sample) + "\n", encoding="utf-8")
    print(len(ids), "писем с PDF; выбрано", len(sample))
else:
    a, b = int(sys.argv[2]), int(sys.argv[3])
    ids = IDS_FILE.read_text(encoding="utf-8").split()
    for i in ids[a:b]:
        ref, pdf = load_ref(i)
        if not (RESP_DIR / f"{i}.json").exists():
            print(f"=== {i}: ответа пока нет\n")
            continue
        resp = json.loads((RESP_DIR / f"{i}.json").read_text(encoding="utf-8"))
        with fitz.open(pdf) as d:
            layer = "\n".join(p.get_text() for p in d)
        text = layer if len(layer.strip()) > 300 else (resp.get("ocr_text") or "")
        text = re.sub(r"\s+", " ", text)
        print(f"=== {i}  pages {resp.get('pages_used')}/{resp.get('page_count')}  ocr_used={resp.get('ocr_used')}  "
              f"источник текста: {'PDF' if text is layer or len(layer.strip()) > 300 else 'ocr_text'}")
        print("ТЕМА (эталон):", ref.get("hujjatning_qisqacha_mazmuni"))
        print("SUMMARY:", resp.get("summary"))
        print("ТЕКСТ:", text[:1800])
        print()
