# CLAUDE.md

## What this is

An evaluation harness (not an app) for the `doc_summarizer` service's `POST /summarize` endpoint. Incoming letters (PDFs) are sent to the service, and the extracted requisites are compared with operator-entered reference data. Then the error causes are classified and reported. Plain Python scripts, no package, tests or linter. Git tracks code, id lists and reports only; generated data (`runs/`, `results/`, `logs/`) is in `.gitignore`.

Language conventions: code comments, docstrings, console output and `report_data*.md` are in **Russian**. User-facing deliverables (`hisobot.md`, xlsx sheet and column names, `summary_review.json`) are in **Uzbek (Latin)**. Outcome/reason strings (e.g. `"верно"`, `"не та шапка"`) are constants in `analyze_eval.py`. They are matched by exact string elsewhere, so change them only through the constants.

Setup: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt` (`httpx`, `rapidfuzz`, `pymupdf`/`fitz`, `openpyxl`). Run everything from the project root.

## Layout

- Root: the pipeline scripts `run_eval.py`, `analyze_eval.py`, `report_data.py`.
- `tools/`: helper scripts. Run them as modules from the root (`python -m tools.tools_peek …`) so `from analyze_eval import …` resolves.
- `ids/`: id lists (`pilot_ids*.txt`, `retry_ids.txt`, `summary_sample_ids.txt`).
- `runs/`: raw service responses, one folder per set (`responses/`, `responses_2/`).
- `results/`: `results*.jsonl` and `natijalar*.xlsx` from `analyze_eval.py`.
- `reports/`: `hisobot.md`, `report_data*.md`, `summary_review.json`.
- `logs/`: console logs of runs.

Path constants live in `analyze_eval.py` (`HERE`, `RUNS`, `RESULTS`, `REPORTS`, `SETS`) and `run_eval.py` (`REF_DIR`, `RESP_DIR`).

## External paths (siblings of this directory, read-only)

- `../db_test_kirimXat/DOC_<id>/` holds reference set 1: `*.json` with key `rekvizit_document`, plus `*.pdf` (sometimes missing → status `no_pdf`). Its `.env` holds `DOC_API_KEY`.
- `../db_test_kirimXat_1000_2/DOC_<id>/` holds reference set 2.
- `../doc_summarizer/data/` holds the organization directory used to judge "not in directory" cases.

Set → (reference dir, response dir) is defined in `SETS` in `analyze_eval.py`: set 1 → `runs/responses/`, set 2 → `runs/responses_2/`. A new set needs a new `SETS` entry. IDs never overlap between sets. `set_of(id)` finds the set by checking which reference dir contains `DOC_<id>`. If these sibling dirs are absent, the analysis cannot run.

The API key must never be printed or written to any file. `python -m tools.tools_keycheck` verifies that no file contains it.

## Pipeline

1. **Run the service**: `run_eval.py` sends PDFs to `http://localhost:8092/summarize` (header `X-API-Key`).
   ```
   python run_eval.py --pilot 50                 # pick pilot (fixed seed) → ids/pilot_ids.txt, then run
   python run_eval.py --ids ids/pilot_ids.txt    # run a list of ids
   python run_eval.py --all                      # whole set 1
   python run_eval.py --all --ref-dir ../db_test_kirimXat_1000_2 --out runs/responses_2   # set 2
   python run_eval.py --all --url http://<host>:<port>/summarize --out runs/responses_3   # another endpoint
   ```
   It writes `<out>/<id>.json` (the raw response) and `<id>.meta.json` (status, client_ms, server_ms, attempts, n_503, error). It is resumable: ids whose meta status is in `{200, 413, 422, "no_pdf"}` are skipped, and the rest are retried. Concurrency is hard-capped at 8 so the server is not overloaded. The script retries 503s and network errors.

2. **Analyze**: `analyze_eval.py` compares 7 fields (`number, date, signer, org, journal, xdfu, urgent`) for each letter.
   ```
   python analyze_eval.py                                            # set 1 → results/results.jsonl, results/natijalar.xlsx
   python analyze_eval.py --ids ids/pilot_ids.txt --xlsx results/natijalar_pilot.xlsx --jsonl results/results_pilot.jsonl
   python analyze_eval.py --sets 1,2 --xlsx results/natijalar_jami.xlsx --jsonl results/results_jami.jsonl   # combined ("jami")
   ```
   To debug a single letter, call `analyze_eval.analyze_doc("<id>")` from Python.

3. **Report numbers**: `python report_data.py results/results_jami.jsonl reports/report_data_jami.md` collects every figure used in `hisobot.md` into a working markdown file. `hisobot.md` is the hand-written final report. Its numbers must come from `report_data*.md`.

## How `analyze_eval.py` judges a field

- **Normalization** (`norm`): NFKC, unified apostrophes and dashes, Cyrillic→Latin transliteration (Uzbek), collapsed whitespace. Names use `skel()` to absorb transliteration variants (x/h, q/k, o'/u…). Organizations use `norm_org` plus rapidfuzz.
- **Outcome**: each field gets an outcome from a fixed set (`OK`, `FORMAT`, `ORG_VARIANT`, `INITIALS`, `WRONG`, `EMPTY_RESP`, …). These outcomes are grouped as follows:
  - `CORRECT` gives strict accuracy.
  - `WITH_FORMAT` gives accuracy "with format".
  - `EXCLUDED` (empty reference, not processed, operator decision) is left out of the denominator.
  - `ERRORS` and `YELLOW` drive the red and yellow fills in the xlsx.
- **Reason** (`generic_reason`): the script looks for the reference value in the service's `ocr_text`, in unread pages (`pages_used < page_count`), and in the PDF text layer. From that it decides between "OCR did not read it", "read but not extracted", "beyond the pages read", "not in the document" (including e-signature/QR-only docs, detected by `ESIGN_RE`), and "reference doubtful". "Reference doubtful" means the service value is clearly in the text while the reference value is not.
- **Org** has its own reasons: wrong header (e.g. a court-document title or report table picked as the org query), parent org chosen, not in directory, and garbage record.
- **Journal**: an error is attributed to a wrong sender if the org was wrong, and otherwise to the journal table. Journals 9/11/16 are content-based (`CONTENT_JOURNALS`) and are reported separately.
- **Urgent flag**: if the reference says urgent but the text has no mark, the outcome is `OPERATOR` (excluded), not an error.

`report_data.py` and several `tools_*.py` import constants and helpers from `analyze_eval.py`. Keep those names stable.

## Helper scripts

Ad-hoc investigation tools in `tools/`; each one's docstring gives its usage. Run as `python -m tools.<name>`. The most useful are:
- `tools_peek.py <id> <str>…` shows the PDF text layer next to `ocr_text`.
- `tools_ctx.py <id> <regex>` shows regex context in the letter text.
- `tools_dump.py <jsonl> <field> [all]` dumps one field from a results file.
- `tools_brief.py <jsonl>` gives a quick summary.
- `tools_rate.py` reports run throughput.

`summary_sample.py pick|dump N M` handles the 40-letter manual summary review, whose results are in `summary_review.json`.

## Artifacts

In `results/`, set 1 (~1000 letters) produced `results.jsonl` and `natijalar.xlsx`, and the combined sets produced `results_jami.jsonl` and `natijalar_jami.xlsx`. These are generated outputs: regenerate them with the commands above instead of editing them.
