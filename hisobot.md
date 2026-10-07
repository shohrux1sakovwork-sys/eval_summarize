# doc_summarizer servisi aniqligi: 1000 ta kiruvchi xat bo‘yicha tekshiruv

**Nima tekshirildi.** `POST /summarize` servisi (test server A100, versiya 1.2.0) xatdan 7 ta rekvizitni qanchalik to‘g‘ri olishi tekshirildi: raqam, sana, imzolagan shaxs, jo‘natuvchi tashkilot, jurnal, XDFU va shoshilinchlik belgilari. Taqqoslash uchun operatorlar kiritgan va tekshirgan 1000 ta xatdan foydalanildi.

**Hajm.** 1000 ta xatdan 8 tasida PDF yo‘q edi. Servisga 992 ta xat yuborildi va 990 tasiga javob olindi. 1 ta fayl 40 MB limitidan katta, 1 tasida server xatosi (500) chiqdi.

---

## 1. Asosiy xulosalar

1. **Raqam, sana va imzolovchi yaxshi aniqlanadi.** Raqam 80,0%, sana 81,5%, imzolagan shaxs 88,7% to‘g‘ri. XDFU (97,8%) va shoshilinchlik (99,8%) deyarli xatosiz.
2. **Jo‘natuvchida qat’iy hisobda faqat 38,3% to‘g‘ri.** Ammo yana 331 ta xatda servis to‘g‘ri tashkilotni topgan, faqat ma’lumotnomadagi boshqa yozilishda bergan. Masalan, "Adliya vazirligi **Navoiy viloyat adliya boshqarmasi**", operatorda esa "Navoiy viloyat adliya boshqarmasi". Bularni hisobga olsak, aniqlik **72,5%**.
3. **Jurnal 62,0% to‘g‘ri** (9/11/16-jurnallarsiz 65,7%). Eng katta muammo — jurnallar jadvali. 175 ta xatda jo‘natuvchi to‘g‘ri topilgan, lekin jadval boshqa jurnal bergan. Ularning 158 tasida 5-jurnal o‘rniga 6-jurnal: O‘zarxiv, Yuridik kadrlar instituti, Sud ekspertiza markazi va boshqalar. Jadvalni tuzatish ko‘p mehnat talab qilmaydi va jurnal aniqligini **84,6%** gacha ko‘taradi.
4. **Jo‘natuvchining asosiy xatosi — noto‘g‘ri sarlavha.** 146 ta xatda servis tashkilotni xat shapkasidan emas, boshqa joydan qidirgan:
   - 70 ta sud hujjatida "AJRIM", "HAL QILUV QARORI" kabi sarlavhadan;
   - 64 ta hisobotda "HISOBOT", "Loyiha turi" jadvalidan;
   - 12 tasida adresatdan.
5. **Ayrim rekvizitlar xat matnida umuman yo‘q.**
   - 65 ta hisobotda operator raqam sifatida tizimdagi `TSTB-…` raqamini kiritgan. Servis ulardan birortasini topa olmadi.
   - ERI bilan imzolangan 30 ta xatda imzolovchining familiyasi faqat elektron imzoda (QR) bor. Servis bulardan birortasini topa olmadi.
6. **Qisqacha mazmun mazmunan yaxshi, lekin tilida muammo bor.**
   - 40 ta xat qo‘lda tekshirildi: 39 tasida mohiyat to‘g‘ri berilgan, 36 tasida xatga zid joy yo‘q.
   - Barcha 990 ta javobdan 91 tasida kirill harflari bor, 59 tasi asosan kirillda.
   - 29 ta summary jumla o‘rtasida uzilgan.
7. **Etalonning o‘zi ham shubhali.** 77 ta sanada servis bergan sana matnda aniq turibdi, etalondagi sana esa matnda yo‘q. Ulardan 43 tasida etalon sanasi xatni ro‘yxatga olish sanasi bilan bir xil. Ehtimol, operator ro‘yxatga olish sanasini kiritgan. Bunday holatlar xato deb hisoblangan, lekin alohida belgilangan.

---

## 2. Maydonlar bo‘yicha aniqlik

"Jami" — javob olingan va etalonda qiymati bor xatlar. **Qat’iy** — faqat to‘liq mos kelganlar. **Format bilan** — boshqa yozilish ham to‘g‘ri deb hisoblangan:
- jo‘natuvchida: tashkilot nomi yuqori turuvchi organ bilan yoki bo‘linma sifatida yozilgan;
- raqamda: `VMQ-` prefiksi yoki etalondagi tarkibli raqamning bir qismi.

| Maydon | To‘g‘ri / jami | Qat’iy | Format bilan | Etalon shubhali |
|---|---|---|---|---|
| Hujjat raqami | 775 / 969 | 80,0% | 81,5% | 22 |
| Hujjat sanasi | 807 / 990 | 81,5% | 81,5% | 77 |
| Imzolagan shaxs | 868 / 979 | 88,7% | 88,7% | 4 |
| Jo‘natuvchi tashkilot | 370 / 967 | **38,3%** | **72,5%** | 7 |
| Jurnal (hammasi) | 614 / 990 | 62,0% | 62,0% | — |
| Jurnal (9/11/16 dan tashqari) | 608 / 926 | 65,7% | 65,7% | — |
| Jurnal (faqat 9/11/16) | 6 / 64 | 9,4% | 9,4% | — |
| XDFU belgisi | 968 / 990 | 97,8% | 97,8% | 16 |
| Shoshilinch belgisi | 945 / 947 | 99,8% | 99,8% | 1 |

**Hisobdan chiqarilganlar:**
- **Shoshilinch**: 43 ta xatda etalonda "shoshilinch" bor, lekin xat matnida bunday belgi yo‘q. Bu operator qarori, servis xatosi emas.
- **Jo‘natuvchi**: 23 ta xatda etalonda tashkilot o‘rniga shaxs yozilgan, masalan "N.Suleymanov", "Patent vakili".
- **Raqam**: 21 ta xatda etalon bo‘sh yoki raqam emas.
- **Imzolovchi**: 11 ta xatda etalon bo‘sh.

**Imzolovchi** to‘g‘rilariga transliteratsiya farqlari ham kiritilgan (78 ta): x/h, y/i, a/o farqi, masalan Abdullaxanov / Abdullaxonov.

**9, 11, 16-jurnallar** xat mazmuniga qarab tanlanadi, servis esa jurnalni faqat jo‘natuvchiga qarab tanlaydi. Shuning uchun ular alohida ko‘rsatilgan.

---

## 3. Xatolar sabablari

Har bir xato uchun xat matni (OCR) va PDF matn qatlami tekshirildi: to‘g‘ri qiymat matnda bormi yoki yo‘qmi.

| Maydon | Asosiy sabablar (soni) |
|---|---|
| Raqam (194) | matnda yo‘q — 88 (shundan `TSTB-…` 65); o‘qilgan, lekin olinmagan — 42; OCR buzib o‘qigan — 26; etalon shubhali — 22 |
| Sana (183) | etalon shubhali — 77; matnda yo‘q — 44; o‘qilgan, lekin olinmagan — 35; OCR o‘qimagan — 20; matndagi boshqa sana olingan — 5 |
| Imzolovchi (111) | o‘qilgan, lekin olinmagan — 38; matnda yo‘q — 36 (shundan ERI hujjati 29); OCR o‘qimagan — 31 |
| Jo‘natuvchi (266, formatdan tashqari) | noto‘g‘ri sarlavha — 146; o‘qilgan, lekin olinmagan — 72; OCR o‘qimagan — 19; yuqori turuvchi tanlangan — 11 |
| Jurnal (376) | jo‘natuvchi to‘g‘ri, jadval boshqa jurnal bergan — 175; jo‘natuvchi xato — 143; mazmunga ko‘ra jurnal (9/11/16) — 58 |

**Misollar** (ID — etalon / servis — sabab):

- **Jurnal jadvali.** "O‘zarxiv" agentligi (ma’lumotnomadagi id 213) jadvalda 6-jurnalga bog‘langan, `journal_exact=1`. Etalonda 64 ta xatning hammasi 5-jurnalda.
- **Noto‘g‘ri sarlavha, sud hujjati.**
  - 3142436 — "Nurafshon tumanlararo ma'muriy sudi" / bo‘sh. Servis "АЖРИМ (Ариза бўйича иш юритишга қабул қилиш…)" sarlavhasidan qidirgan.
- **Noto‘g‘ri sarlavha, hisobot.**
  - 3143767 — "Ichki ishlar vazirligi" / bo‘sh. Servis "…soddalashtirilgan HISOBOT" sarlavhasidan qidirgan.
- **Noto‘g‘ri sarlavha, adresat.**
  - 3179512 — "Oliy sudi" / "Adliya vazirligi". Adresat jo‘natuvchi deb olingan.
- **Raqam matnda yo‘q.**
  - 3143767 — "TSTB-2906" / bo‘sh. Bu tizim raqami, xat matnida u yo‘q.
- **Imzo faqat ERIda.**
  - 3141682 — "I.M.Adxamov" / bo‘sh. Xat elektron imzo bilan tasdiqlangan, familiya matnda yo‘q.
- **Sana, etalon shubhali.**
  - 3141682 — 05.01.2026 / 2025-12-30. Servis sanasi matnda bor, etalon sanasi esa ro‘yxatga olish sanasi bilan bir xil.
- **Sana, aniq servis xatosi.**
  - 3186526 — 22.01.2026 / 2026-11-22. Bunday sana ro‘yxatga olishdan keyin bo‘lishi mumkin emas. Shunday holatlar 11 ta.

**Matn manbai bo‘yicha farq.** Elektron (matn qatlamli) PDFlarda natija skanlardan yomonroq: raqam 69,1% va 86,6%, imzolovchi 77,1% va 95,9%. Sababi elektron xatlar orasida `TSTB` hisobotlari va ERI bilan imzolangan xatlar ko‘p.

---

## 4. Eng ko‘p xato chiqqan jo‘natuvchilar

| Jo‘natuvchi | Xatlar | Xatolar | Asosan qaysi maydonda |
|---|---|---|---|
| Bosh prokuratura | 67 | 120 | sana 27, imzolovchi 26, raqam 25, jo‘natuvchi 18, jurnal 18 |
| Ichki ishlar vazirligi | 77 | 105 | raqam 35, jurnal 23, jo‘natuvchi 21, sana 18 |
| Adliya vazirligi (29 tadan 25 tasi TTB hisobotlari) | 29 | 101 | raqam 29, jo‘natuvchi 28, jurnal 28 |
| "O‘zarxiv" agentligi | 64 | 79 | jurnal 64 |
| Oliy sud | 47 | 56 | jurnal 21, jo‘natuvchi 16 |
| Davlat xavfsizlik xizmati | 33 | 56 | raqam 23, sana 23 |
| Toshkent tumanlararo ma'muriy sudi | 28 | 44 | jo‘natuvchi 20, jurnal 19 |
| Yuridik kadrlar instituti | 29 | 38 | jurnal 29 |
| Toshkent tumanlararo iqtisodiy sudi | 20 | 33 | jo‘natuvchi 14, jurnal 13 |
| Qoraqalpog‘iston Respublikasi Adliya vazirligi | 20 | 24 | jo‘natuvchi 20 — pastdagi izohga qarang |

**Qoraqalpog‘iston Adliya vazirligi.** Bu xatlarning shapkasi qoraqalpoq tilida. 20 ta xatdan 19 tasida servis ma’lumotnomadagi tuman bo‘linmasini tanlagan: "…Qaraqalpaqstan Respublikasi A'dillik ministrligi Kegeyli rayoni FHDY bo‘limi". Faqat 1 tasida (3185889) vazirlikning qoraqalpoqcha nomi to‘g‘ri berilgan, lekin hisobda u ham xato deb olingan.

To‘liq ro‘yxat `natijalar.xlsx` faylining "Jo‘natuvchilar" varag‘ida.

---

## 5. Tezlik va barqarorlik

- **Server vaqti (bitta xat):** median 32,7 s, p90 64,0 s, p99 97,6 s, eng ko‘p 148,0 s. Mijoz tomonidagi vaqt deyarli bir xil (median 32,9 s).
- **Parallel ishlash:** 8 ta so‘rov bir vaqtda yuborildi, minutiga taxminan 13–14 xat ishlandi.
- **503 (band):** 0 ta.
- **413 (juda katta fayl):** 1 ta (3169938, 64,9 MB). Serverdagi limit **40 MB**; API hujjatida 100 MB deb yozilgan.
- **500 (server xatosi):** 1 ta (3172127). Ikki marta takrorlandi, natija bir xil (request_id: 75c2f141b2fb, b507ac085ad6). Fayl — bitta sahifali skan, sahifa o‘lchami juda katta (2782×3929 pt, taxminan 98×139 sm). Ehtimoliy sabab: rasmni OCR uchun kattalashtirganda xotira yoki o‘lcham limiti. Server logida tekshirish kerak.
- **Tarmoq uzilishi:** 2 ta, faqat sinov bosqichida, qayta yuborilganda ishladi.

---

## 6. Nimani tuzatish kerak

Ta’sir — tuzatilsa nechta xato yo‘qolishi mumkin (o‘lchangan xatolar soni bo‘yicha, eng yuqori chegara).

| # | Nima qilish kerak | Ta’sir | Qiyinchilik |
|---|---|---|---|
| 1 | **Jurnallar jadvalini tuzatish.** Adliya vazirligi tizimidagi tashkilotlarni (O‘zarxiv, Yuridik kadrlar instituti, Sud ekspertiza markazi, Intellektual mulk markazi, Personallashtirish agentligi, Jizzax viloyat adliya boshqarmasi) 5-jurnalga bog‘lash. IIV, DXX va Oliy sud bo‘linmalarini 2-jurnalga bog‘lash. Ro‘yxat "Jurnal jadvali" varag‘ida. | jurnal: 175 ta (65,7% → 84,6%) | past |
| 2 | **Sud hujjatlari va TTB hisobotlarida jo‘natuvchini boshqacha topish.** Sud hujjatlarida sud nomini matndan olish ("… sudining sudyasi"). Hisobotlarda jadvaldagi "Ishlab chiqaruvchi" qatoridan olish. Adresatni jo‘natuvchi deb olmaslik. | jo‘natuvchi: 146 ta; jurnal: 110 ta | o‘rta |
| 3 | **Tashkilot nomini operatorlar yozadigan qisqa shaklda berish.** Ma’lumotnomada nom yuqori turuvchi organ bilan yozilgan; uni yuqori turuvchisiz qaytarish yoki moslik jadvali tuzish. | jo‘natuvchi qat’iy: 331 ta (38,3% → 72,5%) | past–o‘rta |
| 3a | **Qoraqalpoqcha shapkalarda tuman bo‘linmasi tanlanishini tuzatish.** "Kegeyli rayoni FHDY bo‘limi" yozuvi o‘rniga vazirlikning o‘zi tanlanishi kerak. | jo‘natuvchi: 19 ta | past |
| 4 | **Summary faqat lotinda va to‘liq bo‘lishi.** Kirillni lotinga o‘girish yoki qayta so‘rash; javob uzunligi limitini tekshirish. | kirill: 91 ta, uzilgan: 29 ta | past |
| 5 | **Mazmunga ko‘ra jurnallar (9, 11, 16).** Masalan, Apellyatsiya kengashiga ariza → 11, NNT ro‘yxatdan o‘tkazish → 16, xodimning ichki arizasi → 9. | jurnal: 58 ta | o‘rta |
| 6 | **ERI bilan imzolangan xatlarda imzolovchini elektron imzo ma’lumotidan olish** (QR yoki IJRO tizimi). | imzolovchi: 29–30 ta | o‘rta (tizimga kirishga bog‘liq) |
| 7 | **`TSTB-…` raqamlari bo‘yicha qoida kelishish.** Bu raqam xat matnida yo‘q: uni tizimdan olish yoki tekshiruvdan chiqarish kerak. | raqam: 65 ta | tashkiliy |
| 8 | **Juda katta rasmlarni OCRdan oldin kichraytirish;** 40 MB limitni hujjat bilan moslashtirish. | 2 ta xat | past |

---

## 7. Cheklovlar

- **Etalonni odamlar kiritgan.** Unda ham xatolar bor: masalan, "boshqaimasi" kabi imlo xatolari, raqam o‘rniga tashkilot nomi, sanada ro‘yxatga olish sanasi. Shubhali holatlar alohida belgilangan, lekin etalon tuzatilmagan va ular xato sifatida hisobga kirgan.
- **To‘plamda faqat xatlar (`Xat`) bor.** Farmon, qaror va boshqa hujjat turlari tekshirilmagan.
- **Xato sabablari avtomatik aniqlangan** (matnda qidirish orqali), ular taxminiy. 17 ta jo‘natuvchi "juda o‘xshash" (o‘xshashlik ≥ 90) deb belgilangan, ularni qo‘lda ko‘rish kerak. Ro‘yxat Excel faylida.
- **"Ma’lumotnomada yo‘q" tekshiruvi mahalliy nusxada qilingan.** `index.parquet` faylida 66 598 ta nom bor, server esa 64 541 ta yozuv yuklagan. Ular farq qilishi mumkin.
- **Qisqacha mazmun qo‘lda faqat 40 ta xatda tekshirilgan.** Kirill va uzilish esa barcha 990 ta javobda avtomatik sanalgan.
- **Har bir xat bir marta yuborilgan.** Bir xil xatga servis har safar bir xil javob beradimi — bu tekshirilmagan.
- **Ishlanmagan xatlar:** 8 ta xatda PDF yo‘q, 2 tasi ishlanmadi (413 va 500). Ular aniqlik hisobiga kirmagan.

---

*Fayllar: `natijalar.xlsx` (har bir xat bo‘yicha natija, xulosa, xato turlari, jo‘natuvchilar, jurnal jadvali, noto‘g‘ri sarlavhalar, qisqacha mazmun tekshiruvi), `responses/` (servisning to‘liq javoblari), `run_eval.py`, `analyze_eval.py`.*
