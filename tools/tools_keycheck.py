"""Проверка, что ключ из .env не попал ни в один файл eval_summarize (ключ не печатается)."""
from pathlib import Path

from run_eval import REF_DIR, load_key

key = load_key(REF_DIR / ".env").encode()
here = Path(__file__).resolve().parent.parent   # корень eval_summarize
hits = [p.name for p in here.rglob("*") if p.is_file() and key in p.read_bytes()]
print("файлов проверено:", sum(1 for p in here.rglob("*") if p.is_file()), "| файлов с ключом:", len(hits), hits)
