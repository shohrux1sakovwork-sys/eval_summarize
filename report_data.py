"""Все измеренные цифры для hisobot.md из results.jsonl → report_data.md (рабочий файл).
python report_data.py [results/results.jsonl] [reports/report_data.md]"""
import collections
import json
import re
import statistics
import sys

from analyze_eval import (CONTENT_JOURNALS, CORRECT, EMPTY_REF, EMPTY_RESP, EXCLUDED, FIELD_TITLES,
                          FIELDS, HERE, NOT_PROCESSED, OPERATOR, ORG_VARIANT, R_DOUBT, R_WRONG_HEADER,
                          WITH_FORMAT, accuracy, esign_stats, journal_table_cases, norm_org,
                          pct, reason_key, resp_path, wrong_header_cases, ERRORS)

src = sys.argv[1] if len(sys.argv) > 1 else "results/results.jsonl"
dst = sys.argv[2] if len(sys.argv) > 2 else "reports/report_data.md"
rows = [json.loads(l) for l in open(HERE / src, encoding="utf-8")]
out = []
p = out.append

st = collections.Counter(str(r["status"]) for r in rows)
p(f"# Данные для отчёта ({src})\n\nПисем: {len(rows)}; статусы: {dict(st)}\n")

p("## Точность\n\n| Поле | Строго | С «формат» | Всего | Строго % | С «формат» % | Под сомнением | Исключено |")
p("|---|---|---|---|---|---|---|---|")
for key, title, pred in [(f, FIELD_TITLES[f], None) for f in FIELDS] + [
        ("journal", "Jurnal без 9/11/16", lambda r: r["ref_journal"] not in CONTENT_JOURNALS),
        ("journal", "Jurnal только 9/11/16", lambda r: r["ref_journal"] in CONTENT_JOURNALS)]:
    pr = pred or (lambda r: True)
    ok, fmt, tot = accuracy(rows, key, pr)
    doubt = sum(r["fields"][key]["reason"] == R_DOUBT for r in rows if pr(r))
    excl = collections.Counter(r["fields"][key]["outcome"] for r in rows
                               if pr(r) and r["fields"][key]["outcome"] in EXCLUDED)
    p(f"| {title} | {ok} | {fmt} | {tot} | {pct(ok, tot)} | {pct(fmt, tot)} | {doubt} | {dict(excl)} |")

sets = sorted({r.get("set", "1") for r in rows})
if len(sets) > 1:
    p("\n## Точность по наборам (строго / с «формат», всего)\n")
    p("| Поле | " + " | ".join(f"Набор {s}" for s in sets) + " | Вместе |")
    p("|---|" + "---|" * (len(sets) + 1))
    for key, title, pred in [(f, FIELD_TITLES[f], None) for f in FIELDS] + [
            ("journal", "Jurnal без 9/11/16", lambda r: r["ref_journal"] not in CONTENT_JOURNALS)]:
        pr = pred or (lambda r: True)
        cells = []
        for s in sets + [None]:
            ok, fmt, tot = accuracy(rows, key, lambda r, s=s: pr(r) and s in (None, r.get("set", "1")))
            cells.append(f"{pct(ok, tot)} / {pct(fmt, tot)}, {tot}")
        p(f"| {title} | " + " | ".join(cells) + " |")

p("\n## Категории итогов по полям")
for f in FIELDS:
    c = collections.Counter(r["fields"][f]["outcome"] for r in rows)
    p(f"- {FIELD_TITLES[f]}: " + "; ".join(f"{k} {v}" for k, v in c.most_common()))

p("\n## Причины (итог не верно/формат, без исключённых)")
for f in FIELDS:
    c = collections.Counter(reason_key(r["fields"][f]["reason"]) or "—" for r in rows
                            if r["fields"][f]["outcome"] not in CORRECT | EXCLUDED)
    p(f"\n### {FIELD_TITLES[f]}  (всего {sum(c.values())})")
    for k, v in c.most_common():
        ex = [r for r in rows if reason_key(r["fields"][f]["reason"]) == k
              and r["fields"][f]["outcome"] not in CORRECT | EXCLUDED][:3]
        p(f"- {k}: {v}")
        for r in ex:
            fv = r["fields"][f]
            p(f"    - {r['id']}: эталон «{fv['ref'][:70]}» / сервис «{fv['resp'][:70]}» ({fv['outcome']}) {fv.get('note', '')[:120]}")

p("\n## «Не та шапка» по видам")
kinds = collections.defaultdict(list)
for kind, r in wrong_header_cases(rows):
    kinds[kind].append(r)
for k, rs in kinds.items():
    p(f"- {k}: {len(rs)} — пример: " + ", ".join(f"{r['id']} (query «{(r['org_resp']['query'] or '')[:60]}»)" for r in rs[:2]))

p("\n## Журнал: отправитель верный, журнал другой")
jt = journal_table_cases(rows)
pairs = collections.Counter((r["ref_journal"], r["journal_resp"], r["journal_exact"]) for r in jt)
p(f"Всего {len(jt)}; (ожидаемый, сервис, journal_exact): {dict(pairs)}")
by_org = collections.Counter((r["org_resp"]["name"], r["org_resp"]["id"], r["journal_exact"], r["ref_journal"],
                              r["journal_resp"]) for r in jt)
for (n, i, ex, rj, sj), v in by_org.most_common():
    p(f"- {n} (id {i}), journal_exact={ex}: ожидается {rj}, сервис {sj} — {v} писем")

p("\n## Журнал: ошибки по причинам и по парам")
jw = [r for r in rows if r["fields"]["journal"]["outcome"] not in CORRECT | EXCLUDED]
p(str(collections.Counter((r["fields"]["journal"]["reason"], r["ref_journal"], r["journal_resp"]) for r in jw).most_common(20)))
p("journal_exact у верных/неверных (без 9/11/16): " + str(collections.Counter(
    (r["fields"]["journal"]["outcome"] in CORRECT, r.get("journal_exact")) for r in rows
    if r["ref_journal"] not in CONTENT_JOURNALS and r["fields"]["journal"]["outcome"] not in EXCLUDED)))

p("\n## ЭЦП и подписант")
p(str(esign_stats(rows)))

p("\n## Отправители с наибольшим числом ошибок (строгих: неверно/пусто/инициалы)")
groups = collections.defaultdict(list)
spell = collections.defaultdict(collections.Counter)
for r in rows:
    k = norm_org(r["ref_org"])
    groups[k].append(r)
    spell[k][r["ref_org"]] += 1
lines = []
for k, rs in groups.items():
    errs = collections.Counter(f for r in rs for f in FIELDS if r["fields"][f]["outcome"] in ERRORS)
    lines.append((sum(errs.values()), len(rs), spell[k].most_common(1)[0][0], errs))
for e, n, name, errs in sorted(lines, key=lambda x: (-x[0], -x[1]))[:15]:
    p(f"- {name}: {n} писем, ошибок {e}: " + ", ".join(f"{FIELD_TITLES[f]} {v}" for f, v in errs.most_common()))

p("\n## Скорость и коды")
ms = sorted(r["server_ms"] for r in rows if r["server_ms"])
cl = sorted(r["client_ms"] for r in rows if r["client_ms"] and str(r["status"]) == "200")
if ms:
    q = lambda a, x: a[int(x * (len(a) - 1))]
    p(f"server_ms: n={len(ms)} медиана {statistics.median(ms) / 1000:.1f} с, p90 {q(ms, .9) / 1000:.1f} с, "
      f"p99 {q(ms, .99) / 1000:.1f} с, макс {ms[-1] / 1000:.1f} с")
    p(f"client_ms: медиана {statistics.median(cl) / 1000:.1f} с, p90 {q(cl, .9) / 1000:.1f} с")
p(f"503 всего: {sum(r['n_503'] or 0 for r in rows)}; писем с повтором: {sum(1 for r in rows if (r['attempts'] or 0) > 1)}")
for r in rows:
    if str(r["status"]) not in ("200",):
        mp = resp_path(r["id"], ".meta.json")
        meta = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {"error": "ещё не отправлено"}
        p(f"- {r['id']}: {r['status']} {str(meta.get('error'))[:150]}")
pg = collections.Counter((r["pages_used"] or 0) < (r["page_count"] or 0) for r in rows if r["page_count"])
p(f"pages_used < page_count: {pg.get(True, 0)} писем; ocr_used: {collections.Counter(r['ocr_used'] for r in rows)}")

p("\n## Кириллица в summary")
n = cyr = mostly = cut = empty = 0
cut_ids, mostly_ids = [], []
for r in rows:
    pth = resp_path(r["id"])
    if pth.exists():
        s = (json.loads(pth.read_text(encoding="utf-8")).get("summary") or "").strip()
        n += 1
        if not s:
            empty += 1
            continue
        letters = re.findall(r"[^\W\d_]", s)
        c = sum(1 for ch in letters if "Ѐ" <= ch <= "ӿ")
        cyr += c > 0
        if letters and c / len(letters) > 0.5:
            mostly += 1
            mostly_ids.append(r["id"])
        if not re.search(r"[.!?…»\"”)]$", s):
            cut += 1
            cut_ids.append(r["id"])
p(f"ответов {n}; пустых summary {empty}; summary с кириллицей: {cyr}; в основном (>50% букв) на кириллице: {mostly}")
p(f"summary не заканчивается концом предложения (вероятно, оборван): {cut}; примеры: {cut_ids[:8]}")
p(f"в основном кириллица, примеры: {mostly_ids[:8]}")
both = len(set(cut_ids) & set(mostly_ids))
p(f"и оборван, и в основном кириллица: {both}")

p("\n## Дополнительные разрезы")
F = lambda f, pred: [r for r in rows if pred(r["fields"][f], r)]
nid = F("number", lambda v, r: v["reason"].startswith("нет в документе"))
p(f"Номер «нет в документе»: {len(nid)}; из них эталон TSTB-…: {sum(v['fields']['number']['ref'].upper().startswith('TSTB') for v in nid)}; "
  f"ЭЦП-документ: {sum('ЭЦП' in v['fields']['number']['reason'] for v in nid)}")
tstb_all = [r for r in rows if r["fields"]["number"]["ref"].upper().startswith("TSTB")]
p(f"Всего писем с номером эталона TSTB-…: {len(tstb_all)}; верно у сервиса: {sum(r['fields']['number']['outcome'] in CORRECT for r in tstb_all)}")
dd = F("date", lambda v, r: v["reason"] == R_DOUBT)
p(f"Дата под сомнением: {len(dd)}; из них дата эталона = дата регистрации: {sum('= дата регистрации' in r['fields']['date']['note'] for r in dd)}")
p(f"Дата сервиса позже регистрации (точно ошибка сервиса): {len(F('date', lambda v, r: 'позже регистрации' in v['note']))}")
sd = F("signer", lambda v, r: v["reason"].startswith("нет в документе"))
p(f"Подписант «нет в документе»: {len(sd)}; из них ЭЦП-документ: {sum('ЭЦП' in r['fields']['signer']['reason'] for r in sd)}")
sim = F("org", lambda v, r: v["outcome"] == "неверно" and "очень похоже" in v["note"])
p(f"Отправитель неверно, но «очень похоже» (ratio≥90) — для ручной проверки: {len(sim)}: " + ", ".join(r["id"] for r in sim))
wh_j = F("journal", lambda v, r: v["reason"] == "из-за неверного отправителя"
         and r["fields"]["org"]["reason"].startswith(R_WRONG_HEADER))
p(f"Ошибки журнала из-за «не та шапка» у отправителя: {len(wh_j)}")
emp_org = F("org", lambda v, r: v["outcome"] == EMPTY_RESP)
p(f"Отправитель пусто у сервиса: {len(emp_org)}; причины: {dict(collections.Counter(reason_key(r['fields']['org']['reason']) for r in emp_org))}")
xd = F("xdfu", lambda v, r: v["reason"] == R_DOUBT)
p(f"ХДФУ: сервис 1, эталон 0, в тексте есть «xdfu»: {len(xd)}")
ocr_pages = collections.Counter(("скан/OCR" if r["ocr_used"] else "текстовый слой") for r in rows if r["ocr_used"] is not None)
p(f"Источник текста: {dict(ocr_pages)}")
for f in ["number", "date", "signer", "org"]:
    acc = {}
    for kind in (True, False):
        ok, fmt, tot = accuracy(rows, f, lambda r, k=kind: r["ocr_used"] is k)
        acc["OCR" if kind else "текст"] = f"{ok}/{tot} ({pct(ok, tot)}), с форматом {pct(fmt, tot)}"
    p(f"- {FIELD_TITLES[f]} по источнику: {acc}")

(HERE / dst).write_text("\n".join(out), encoding="utf-8")
print("\n".join(out))
