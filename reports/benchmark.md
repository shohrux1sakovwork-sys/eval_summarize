# Benchmark: gemma-4-12B va gemma-4-26B-A4B (`doc_summarizer`, `POST /summarize`)

Sana: 2026-10-08. To'plam: 4-to'plam (`db_test_kirimXat_500_4`), 492 ta kiruvchi xat.

## Xulosa

**gemma-4-26B-A4B ham tezroq, ham aniqroq.**

- **Tezlik:** mediana kechikish 35,4 s → **23,3 s** (−34%). O'tkazuvchanlik daqiqasiga 11,9 → **17,8 xat** (+50%). 492 ta xatning 408 tasida 26B tezroq bo'ldi.
- **Aniqlik:** Jo'natuvchi **+18,6** punkt (48,0% → 66,6%), Jurnal **+21,6** punkt (52,6% → 74,2%). Raqam va Sana bo'yicha farq ~1 punkt, bu shovqin chegarasida. Imzolagan bo'yicha 26B biroz yomonroq (−2,4 punkt).
- **Narxi:** GPU xotirasi ko'proq kerak, taxminan 14,5 GB o'rniga 23,5 GB.

## Sinov sharoiti

| | gemma-4-12B | gemma-4-26B-A4B |
|---|---|---|
| Model fayli | `gemma-4-12b-it-Q4_K_M.gguf` | `gemma-4-26B-A4B-it-UD-Q4_K_M.gguf` (unsloth) |
| Kvantlash | Q4_K_M | Q4_K_M (UD) |
| Spekulyativ dekodlash | MTP draft | MTP draft (`mtp-gemma-4-26B-A4B-it.gguf`) |
| Server | llama.cpp b11243, 12 slot × 16384 kontekst | xuddi shunday |
| Ishga tushirilgan vaqt | 2026-10-08 13:44 – 14:21 | 2026-10-08 16:28 – 16:56 |

Umumiy sharoit:
- **GPU:** NVIDIA A100-SXM4-40GB, bitta.
- **Yuklama:** mijoz bir vaqtda 8 ta so'rov yuboradi (`run_eval.py`, ikkala model uchun bir xil).
- **Xatlar:** `ids/set4_ok_ids.txt` ro'yxatidagi 492 ta xat, ikkala model uchun bir xil. To'plamdagi 500 ta xatning 8 tasi chiqarib tashlandi, chunki ularning PDF fayllari buzuq (`ids/set4_bad_pdf_ids.txt`).
- **Natija:** ikkala model ham 492 ta xatning hammasiga 200 statusi bilan javob berdi. Xato, 503 yoki takroriy urinish bo'lmadi.

## Tezlik

Kechikish: so'rov yuborilgandan javob kelgunicha bo'lgan to'liq vaqt (OCR + LLM + ma'lumotnoma), mijoz tomonida o'lchangan.

| Ko'rsatkich | 12B | 26B-A4B |
|---|---|---|
| O'rtacha | 38,7 s | **26,5 s** |
| Mediana | 35,4 s | **23,3 s** |
| p90 | 62,9 s | **46,2 s** |
| p95 | 73,1 s | **58,5 s** |
| Maksimum | 124,4 s | **103,8 s** |
| Bir sahifaga (mediana) | 15,4 s | **10,7 s** |
| Daqiqasiga xatlar | 11,9 | **17,8** |
| GPU yuklanishi (o'rtacha) | 78% | 84% |
| GPU xotirasi (model, taxminan) | ~14,5 GB | ~23,5 GB |
| Band LLM slotlari (o'rtacha) | 6,2 | 5,4 |

Xat turi bo'yicha mediana kechikish (qavs ichida xatlar soni):

| Guruh | 12B | 26B-A4B |
|---|---|---|
| 1 sahifa (151) | 29,7 s | **21,5 s** |
| 2–3 sahifa (200) | 37,0 s | **24,4 s** |
| 4+ sahifa (141) | 39,5 s | **25,2 s** |
| Matn qatlami (324) | 32,2 s | **20,5 s** |
| OCR (168) | 43,0 s | **32,6 s** |

Xatma-xat solishtirganda 26B kechikishining 12B kechikishiga nisbati (mediana) 0,71 ga teng.

## Aniqlik

Operator kiritgan etalon bilan solishtirildi (`analyze_eval.py`). Ikki qiymat berilgan: qat'iy / formatni hisobga olgan holda. Etalon bo'sh bo'lgan va operator qarori bilan bog'liq holatlar maxrajga kirmaydi.

| Maydon | n | 12B | 26B-A4B | Farq |
|---|---|---|---|---|
| Raqam | 478 | 64,4% / 69,9% | 65,7% / 71,1% | +1,3 |
| Sana | 492 | 70,3% | 71,3% | +1,0 |
| Imzolagan | 491 | **80,2%** | 77,8% | −2,4 |
| Jo'natuvchi | 485 | 48,0% / 55,5% | **66,6% / 75,1%** | **+18,6** |
| Jurnal | 492 | 52,6% | **74,2%** | **+21,6** |
| XDFU | 492 | 98,4% | 98,4% | 0 |
| Shoshilinch | 460 | 100% | 100% | 0 |

Har bir maydon bo'yicha nechta xatda faqat bitta model to'g'ri javob berdi (qat'iy):

| Maydon | Faqat 12B to'g'ri | Faqat 26B to'g'ri |
|---|---|---|
| Raqam | 7 | 13 |
| Sana | 15 | 20 |
| Imzolagan | 22 | 10 |
| Jo'natuvchi | 7 | **97** |
| Jurnal | 0 | **106** |
| XDFU | 0 | 0 |
| Shoshilinch | 0 | 0 |

Jo'natuvchi va Jurnal bo'yicha ustunlik bir tomonlama, demak bu tasodifiy farq emas. Jurnal jo'natuvchiga bog'liq, shuning uchun jo'natuvchi to'g'ri topilsa, jurnal ham to'g'ri chiqadi. Raqam, Sana va Imzolagan bo'yicha farqlar kichik va ikki tomonlama. Model temperatura 0.1 da ishlaydi, shuning uchun bu farqlarning bir qismi takroriy ishga tushirishdagi shovqin bo'lishi mumkin.

## Cheklovlar

- **GPU'da boshqa jarayon bor edi.** Ikkala o'lchov paytida ham shu GPU'da vLLM jarayoni (~15 GB) ishlab turgan. Model xotirasi umumiy band xotiradan shu 15 GB ni ayirib hisoblandi. GPU yuklanishiga ham vLLM ta'sir qilgan bo'lishi mumkin.
- **26B uchun xotira zaxirasi kam.** 26B bilan GPU 40,9 GB dan 38,5 GB gacha to'ldi. vLLM bilan birga ishlatilsa, zaxira juda kam qoladi.
- **Token darajasidagi ko'rsatkichlar yo'q.** Sekundiga tokenlar va birinchi tokengacha vaqt (TTFT) o'lchanmadi, chunki llama.cpp `--metrics` siz ishlagan.
- **12B ishga tushirilishi ikki qismda bo'ldi.** Avval 57 ta xat ishlandi, keyin qolgan 435 tasi. Ikkala qism ham bir vaqtda 8 ta so'rov bilan ishlagan. Ikki jarayon bir vaqtda ishlagan qisqa oraliqdagi natijalar o'chirilib, qaytadan bajarildi. Daqiqasiga xatlar soni 435 ta xatli asosiy qism bo'yicha hisoblangan.
- **Har bir model bir marta ishga tushirildi.** Shovqinni baholash uchun takroriy ishga tushirishlar qilinmadi.
- **Xatolar sababi tahlil qilinmagan.** Tashkilotlar ma'lumotnomasi (`../doc_summarizer/data`) bo'lmagani uchun "ma'lumotnomada yo'q" sabablari aniqlanmadi. Bu aniqlik raqamlariga ta'sir qilmaydi.

## Takrorlash

```
# har bir model uchun (llama.cpp'da model almashtirilgandan keyin)
python run_eval.py --ids ids/set4_ok_ids.txt --ref-dir test_docs/db_test_kirimXat_500_4 \
    --out runs/set4_<model> --label <model> --url http://localhost:8091/summarize --env <.env>
# solishtirish
python -m tools.tools_compare runs/set4_gemma4-12b runs/set4_gemma4-26b-a4b \
    --ids ids/set4_ok_ids.txt --md reports/compare_set4.md
```

Ishchi jadvallar (rus tilida): `reports/compare_set4.md`.
