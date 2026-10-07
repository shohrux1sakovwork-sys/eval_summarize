# Данные для отчёта (results_jami.jsonl)

Писем: 2500; статусы: {'200': 2480, 'no_pdf': 18, '413': 1, '500': 1}

## Точность

| Поле | Строго | С «формат» | Всего | Строго % | С «формат» % | Под сомнением | Исключено |
|---|---|---|---|---|---|---|---|
| Raqam | 1882 | 1939 | 2439 | 77.2% | 79.5% | 91 | {'пусто в эталоне': 41, 'не обработано': 20} |
| Sana | 2020 | 2020 | 2480 | 81.5% | 81.5% | 161 | {'не обработано': 20} |
| Imzolagan | 2208 | 2208 | 2462 | 89.7% | 89.7% | 12 | {'пусто в эталоне': 18, 'не обработано': 20} |
| Jo‘natuvchi | 999 | 1784 | 2433 | 41.1% | 73.3% | 17 | {'пусто в эталоне': 47, 'не обработано': 20} |
| Jurnal | 1522 | 1522 | 2480 | 61.4% | 61.4% | 0 | {'не обработано': 20} |
| XDFU | 2418 | 2418 | 2480 | 97.5% | 97.5% | 38 | {'не обработано': 20} |
| Shoshilinch | 2359 | 2359 | 2362 | 99.9% | 99.9% | 1 | {'решение оператора, в тексте отметки нет': 118, 'не обработано': 20} |
| Jurnal без 9/11/16 | 1502 | 1502 | 2333 | 64.4% | 64.4% | 0 | {'не обработано': 1} |
| Jurnal только 9/11/16 | 20 | 20 | 147 | 13.6% | 13.6% | 0 | {'не обработано': 19} |

## Точность по наборам (строго / с «формат», всего)

| Поле | Набор 1 | Набор 2 | Вместе |
|---|---|---|---|
| Raqam | 80.0% / 81.5%, 969 | 75.3% / 78.2%, 1470 | 77.2% / 79.5%, 2439 |
| Sana | 81.5% / 81.5%, 990 | 81.4% / 81.4%, 1490 | 81.5% / 81.5%, 2480 |
| Imzolagan | 88.7% / 88.7%, 979 | 90.4% / 90.4%, 1483 | 89.7% / 89.7%, 2462 |
| Jo‘natuvchi | 38.3% / 72.5%, 967 | 42.9% / 73.9%, 1466 | 41.1% / 73.3%, 2433 |
| Jurnal | 62.0% / 62.0%, 990 | 60.9% / 60.9%, 1490 | 61.4% / 61.4%, 2480 |
| XDFU | 97.8% / 97.8%, 990 | 97.3% / 97.3%, 1490 | 97.5% / 97.5%, 2480 |
| Shoshilinch | 99.8% / 99.8%, 947 | 99.9% / 99.9%, 1415 | 99.9% / 99.9%, 2362 |
| Jurnal без 9/11/16 | 65.7% / 65.7%, 926 | 63.5% / 63.5%, 1407 | 64.4% / 64.4%, 2333 |

## Категории итогов по полям
- Raqam: верно 1882; пусто у сервиса 253; неверно 247; формат 57; пусто в эталоне 41; не обработано 20
- Sana: верно 2020; неверно 298; пусто у сервиса 162; не обработано 20
- Imzolagan: верно 1996; верно (транслит) 212; пусто у сервиса 158; неверно 50; инициалы 28; не обработано 20; неполные инициалы 18; пусто в эталоне 18
- Jo‘natuvchi: верно 968; формат / другое написание организации 785; неверно 364; пусто у сервиса 285; пусто в эталоне 47; верно (транслит) 31; не обработано 20
- Jurnal: верно 1522; неверно 958; не обработано 20
- XDFU: верно 2418; неверно 62; не обработано 20
- Shoshilinch: верно 2359; решение оператора, в тексте отметки нет 118; не обработано 20; неверно 3

## Причины (итог не верно/формат, без исключённых)

### Raqam  (всего 557)
- нет в документе: 207
    - 3143764: эталон «TSTB-2599-2» / сервис «» (пусто у сервиса) 
    - 3143767: эталон «TSTB-2906» / сервис «» (пусто у сервиса) 
    - 3143771: эталон «TSTB-2912» / сервис «» (пусто у сервиса) 
- прочитал, но не извлёк: 106
    - 3142452: эталон «4-1001-2504/.118581» / сервис «4-1001-2518/118581» (неверно) похожий номер
    - 3143535: эталон «-5/278» / сервис «5/278» (неверно) часть номера
    - 3146413: эталон «20-6/3374» / сервис «20-6/3374 ox» (неверно) часть номера
- OCR не прочитал: 92
    - 3148596: эталон «31/4-557328/25-1» / сервис «№ 31/4-557328/25-i-» (неверно) похожий номер
    - 3157641: эталон «18/181BL-25» / сервис «№ 18/181BK-25» (неверно) похожий номер
    - 3157959: эталон «16.2/-26-10-6-3» / сервис «16.2/-26-10-h-3» (неверно) похожий номер
- эталон под сомнением: 91
    - 3141685: эталон «33/01-02-4107» / сервис «12/1-3669» (неверно) 
    - 3143365: эталон «4/18033» / сервис «№4/» (неверно) часть номера
    - 3143370: эталон «4/18035» / сервис «21/12-1990» (неверно) 
- —: 57
- за пределами прочитанного: 4
    - 3151761: эталон «4/253» / сервис «» (пусто у сервиса) 
    - 3221156: эталон «TSTB-3350» / сервис «» (пусто у сервиса) 
    - 3251314: эталон «7-867736/26» / сервис «» (пусто у сервиса) 

### Sana  (всего 460)
- эталон под сомнением: 161
    - 3141682: эталон «05.01.2026» / сервис «2025-12-30» (неверно) разница -6 дн.; дата эталона = дата регистрации
    - 3141685: эталон «22.12.2025» / сервис «2025-10-24» (неверно) разница -59 дн.
    - 3141700: эталон «05.01.2026» / сервис «2025-12-29» (неверно) разница -7 дн.; дата эталона = дата регистрации
- нет в документе: 127
    - 3142650: эталон «03.01.2026» / сервис «» (пусто у сервиса) 
    - 3144343: эталон «06.01.2026» / сервис «» (пусто у сервиса) 
    - 3148596: эталон «05.01.2026» / сервис «» (пусто у сервиса) 
- прочитал, но не извлёк: 83
    - 3142452: эталон «29.12.2025» / сервис «2025-12-30» (неверно) разница +1 дн.
    - 3143559: эталон «16.12.2025» / сервис «2025-12-30» (неверно) разница +14 дн.
    - 3148844: эталон «06.01.2026» / сервис «2026-01-05» (неверно) разница -1 дн.
- OCR не прочитал: 63
    - 3142793: эталон «05.01.2026» / сервис «» (пусто у сервиса) 
    - 3146765: эталон «06.01.2026» / сервис «2026-01-01» (неверно) разница -5 дн.
    - 3146767: эталон «06.01.2025» / сервис «» (пусто у сервиса) 
- за пределами прочитанного: 14
    - 3151761: эталон «09.01.2026» / сервис «» (пусто у сервиса) 
    - 3182537: эталон «19.01.2026» / сервис «2026-01-05» (неверно) разница -14 дн.
    - 3226944: эталон «15.02.2026» / сервис «» (пусто у сервиса) 
- взята другая дата из текста: 12
    - 3153287: эталон «09.01.2026» / сервис «2026-01-15» (неверно) разница +6 дн.; дата сервиса позже регистрации
    - 3184856: эталон «26.01.2026» / сервис «2026-01-27» (неверно) разница +1 дн.; дата сервиса позже регистрации
    - 3186526: эталон «22.01.2026» / сервис «2026-11-22» (неверно) разница +304 дн.; дата сервиса позже регистрации

### Imzolagan  (всего 254)
- нет в документе: 101
    - 3141682: эталон «I.M.Adxamov» / сервис «» (пусто у сервиса) 
    - 3141700: эталон «D.S.Kasimov» / сервис «» (пусто у сервиса) 
    - 3143524: эталон «S.B.Artikova» / сервис «» (пусто у сервиса) 
- прочитал, но не извлёк: 83
    - 3142544: эталон «J.A.Buriyev» / сервис «A. Buriyev» (инициалы) 
    - 3142673: эталон «N.Suleymanov» / сервис «» (пусто у сервиса) 
    - 3143559: эталон «J.G‘.Sirojev» / сервис «» (пусто у сервиса) 
- OCR не прочитал: 53
    - 3141685: эталон «A.T.Rahmatullayev» / сервис «Rahmatullaev» (неполные инициалы) у сервиса без инициалов
    - 3141856: эталон «Z.B.Djalilov» / сервис «E.B.Djalilov» (инициалы) 
    - 3142452: эталон «B.B.Abduraximov» / сервис «B.Abduraximov» (неполные инициалы) эталон 2, сервис 1
- эталон под сомнением: 12
    - 3172862: эталон «B.Abduraximov» / сервис «B.Abd5fakhimov» (неверно) 
    - 3178587: эталон «N.Abdullaev» / сервис «N.Abdilaxatov» (неверно) 
    - 3182612: эталон «M.M.Abduraxmanov» / сервис «J.Abdusattorov» (неверно) 
- за пределами прочитанного: 5
    - 3156288: эталон «A.Bo‘ronov» / сервис «» (пусто у сервиса) 
    - 3189653: эталон «A.Bo'ronov» / сервис «» (пусто у сервиса) 
    - 3221156: эталон «B.Islamov» / сервис «» (пусто у сервиса) 

### Jo‘natuvchi  (всего 1434)
- —: 785
- прочитал, но не извлёк: 185
    - 3142442: эталон «Farg‘ona viloyat sudi iqtisodiy ishlar bo‘yocha sudlov hay'ati» / сервис «Farg'ona viloyat sudining Iqtisodiy ishlar bo'yicha sudlov hay'ati» (неверно) очень похоже (95); query: ФАРҒОНА ВИЛОЯТ СУДИНИНГ ИҚТИСОДИЙ ИШЛАР БЎЙИЧА СУДЛОВ ҲАЙЪАТИ АПЕЛЛЯЦИЯ ИНСТАНЦИЯСИНИНГ АЖРИМИ
    - 3143559: эталон «Toshkent shahar sudi fuqarolik ishlari bo'yicha» / сервис «Ўзбекистон Республикаси Олий суди Верховный суд Республики Узбекистан» (неверно) query: Узбекистон Республикаси Олий суди Верховный суд Республики Узбекистан
    - 3144505: эталон «Oʻzbekiston Respublikasi Oliy sudi» / сервис «» (пусто у сервиса) query: Ijrochi: O.Rajabov
- не та шапка (судебный акт): 161
    - 3142436: эталон «Nurafshon tumanlararo ma'muriy sudi» / сервис «» (пусто у сервиса) query: АЖРИМ (Ариза буйича иш юритишга кабул килиш тугрисида)
    - 3142447: эталон «Toshkent tumanlararo iqtisodiy sudi» / сервис «» (пусто у сервиса) query: АЖРИМ (даъво аризаии uw юритишга цабул ь^илши, иш кузгатиш ва ишии суд мух,окамасига тайёрлаш тугрисида) Тошкент 
    - 3142462: эталон «TOSHKENT TUMANLARARO MA’MURIY SUDI» / сервис «» (пусто у сервиса) query: УЗБЕКИСТОН РЕСПУБЛИКАСИ НОМИДАН ХДЛ к;илув КАРОРИ
- не та шапка (отчёт/таблица): 146
    - 3143767: эталон «O'zbekiston Respublikasi Ichki ishlar vazirligi» / сервис «» (пусто у сервиса) query: Normativ-huquqiy hujjat loyihasining tartibga solish taʻsirini baholash boʻyicha soddalashtirilgan HISOBOT
    - 3143771: эталон «O'zbekiston Respublikasi Ichki ishlar vazirligi» / сервис «» (пусто у сервиса) query: Normativ-huquqiy hujjat loyihasining tartibga solish taʻsirini baholash boʻyicha soddalashtirilgan HISOBOT
    - 3145075: эталон «O'zbekiston Respublikasi Adliya vazirligi» / сервис «» (пусто у сервиса) query: Normativ-huquqiy hujjat loyihasining tartibga solish taʻsirini baholash boʻyicha soddalashtirilgan HISOBOT
- выбрана вышестоящая: 41
    - 3148596: эталон «O'zbekiston Respublikasi Bosh prokuraturasi» / сервис «Узбекистон Республикаси Олий суди» (неверно) query: O'ZBEKISTON RESPUBLIKASI Узбекистон Республикаси BOSH PROKURATURASI Олий суди маъмурий ишлар
    - 3166069: эталон «Oʻzbekiston Respublikasi Oliy sudi» / сервис «O‘zbekiston Respublikasi Bosh prokuraturasi» (неверно) query: OʻZBEKISTON RESPUBLIKASI O`zbekiston Respublikasi OLIY SUDI Bosh prokuraturasi
    - 3174114: эталон «OʻZBEKISTON RESPUBLIKASI ICHKI ISHLAR VAZIRLIGI AKADEMIYASI» / сервис «O‘zbekiston Respublikasi ichki ishlar vazirligi» (неверно) query: OʻZBEKISTON RESPUBLIKASI ICHKI ISHLAR VAZIRLIGI
- OCR не прочитал: 38
    - 3142452: эталон «Toshkent shahar iqtisodiy ishlar bo'yicha sudlov hay'ati» / сервис «Тошкент шахар иктисодий суди» (неверно) query: ТОШКЕНТ ШАХАР СУДИ ИКТИСОДИЙ ИШЛАР БУЙИЧА СУДЛОВ ХАЙЪАТИ АПЕЛЛЯЦИЯ ИНСТАНЦИЯСИНИНГ АЖРИМИ
    - 3142607: эталон «Toshkent tumanlaro iqtisodiy sudi» / сервис «» (пусто у сервиса) query: A Ж P И M (суд мух,окамасини кейинга цолдириш ва ишга гуво)^ларни жалб этиш тугрисида) Тошкент шах;ар
    - 3144786: эталон «Qoraqalpog‘iston Respublikasi Adliya vazirligi» / сервис «Ozbekstan Respublikasi A'dillik Ministrligi Qaraqalpaqstan Respublikas» (неверно) query: OZBEKSTAN RESPUBLIKASl ADILLIK MINISTRLIGI QARAQALPAQSTAN RESPUBLIKASl ADILLIK MINISTRLIGI
- не та шапка (адресат вместо отправителя): 26
    - 3143764: эталон «O'zbekiston Respublikasi Bosh prokuraturasi» / сервис «ISFT INSTITUTI» (неверно) query: Астрент институти жорий этилиши муносабати билан Узбекистон Республикасининг айрим Конун Хужжатларига узгартириш 
    - 3155104: эталон «Toshkent viloyat iqtisodiy ishlar bo'yicha sudlov hay'ati» / сервис «Toshkent viloyat sudi» (неверно) query: ТОШКЕНТ ВИЛОЯТ СУДИ ИК;ТИСОДИЙ ИШЛАР БУЙИЧА СУДЛОВ ХДЙЪАТИ КАССАЦИЯ ИНСТАНЦИЯСИНИНГ АЖРИМИ (ишни иш юритишга цабу
    - 3179512: эталон «Oʻzbekiston Respublikasi Oliy sudi» / сервис «O'zbekiston Respublikasi Adliya vazirligi» (неверно) query: O‘ZBEKISTON RESPUBLIKASI y Oʻzbekiston Respublikasi OLIY SUDI Adliya vazirligi i Xalqaro-huquqiy hamkorlik va
- неполное название: 20
    - 3156257: эталон «Toshkent shahar sudi iqtisodiy ishlar bo‘yicha sudlov hay’ati» / сервис «Toshkent shahar iqtisodiy sudi» (неверно) query: < ТОШКЕНТ ШАҲАР СУДИ — ИҚТИСОДИЙ ИШЛАР БЎЙИЧА СУДЛОВ ҲАЙЪАТИНИНГ АЖРИМИ (қонуний кучга кирган суд ҳужжатини янги 
    - 3161338: эталон «Toshkent tumanlararo ma'muriy sudi» / сервис «Toshkent tumanlararo sudi» (неверно) query: TOSHKENT TUMANLARARO
    - 3172778: эталон «FIB UCHTEPA TUMANLARARO SUDI» / сервис «fuqarolik sudi» (неверно) query: FUQAROLIK ISHLARI ВО"УТСНА UCHTEPA TUMANLARARO SUDI
- эталон под сомнением: 17
    - 3146519: эталон «O'zbekiston Respublikasi Mudofaa vazirligi» / сервис «O'zbekiston Respublikasi Adliya vazirligi Farg'ona viloyat adliya bosh» (неверно) query: OʻZBEKISTON RESPUBLIKASI ADLIYA VAZIRLIGI FARGʻONA VILOYAT ADLIYA BOSHQARMASI
    - 3167112: эталон «FIB Mirobod tumanlararo sudi» / сервис «Mirzo Ulug'bek Tumanlararo Sudi» (неверно) query: FUQAROLIK ISHLARI ВО"УТСНА MIRZO ULUG`BEK TUMANLARARO SUDI
    - 3175848: эталон «Toshkent shahar iqtisodiy ishlar bo'yicha sudlov hay'ati» / сервис «Toshkent shaxar sudi» (неверно) query: ишни курган судья Ш.Ш.Джамолов Апелляция инстанцияси судида маърузачи судья Б.Б.Абдурахимов ТОШКЕНТ ШАХАР СУДИ
- мусорная запись: 14
    - 3155090: эталон «Yangihayot tumani ichki ishlar organlari faoliyatini muvofiqlashtirish» / сервис «O'zbekiston Respublikasi Ichki ishlar vazirligi Toshkent shahar Ichki » (неверно) query: O`ZBEKISTON RESPUBLIKASI ICHKI ISHLAR VAZIRLIGI TOSHKENT SHAHAR ICHKI ISHLAR BOSH BOSHQARMASI YANGIHAYOT TUMANI I
    - 3178587: эталон «Asaka tuman davlat arxivi» / сервис «O'zbekiston Respublikasi Adliya vazirligi huzuridagi "O'zarxiv" agentl» (неверно) query: OʻZBEKISTON RESPUBLIKASI ADLIYA VAZIRLIGI HUZURIDAGI “OʻZARXIV” AGENTLIGI ANDIJON VILOYATI ARXIV ISHI HUDUDIY BOS
    - 3204106: эталон «O‘zbekiston Respublikasi Ichki ishlar vazirligi» / сервис «NNT faoliyati to'g'risidagi hisobot» (неверно) query: HISOBOT 1 Loyiha turi Qonun 2 Loyiha nomi Узбекистон Республикасининг Куриклаш фаолияти тўғрисидаги қонунига ўзга
- шапка не найдена: 1
    - 3217548: эталон «O‘zbekiston Respublikasi Oliy sudi ma'muriy ishlar bo‘yicha sudlov hay» / сервис «» (пусто у сервиса) query пуст

### Jurnal  (всего 958)
- отправитель верный, журнал по таблице другой: 472
    - 3141689: эталон «5/ Adliya organlari va muassasalaridan kelib tushgan hujjatlar» / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=1
    - 3141698: эталон «2/ Sud, prokuratura, ichki ishlar va davlat xavfsizlik xizmati tizimi » / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=1
    - 3141758: эталон «5/ Adliya organlari va muassasalaridan kelib tushgan hujjatlar» / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=1
- из-за неверного отправителя: 359
    - 3142436: эталон «2/ Sud, prokuratura, ichki ishlar va davlat xavfsizlik xizmati tizimi » / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=0
    - 3142447: эталон «2/ Sud, prokuratura, ichki ishlar va davlat xavfsizlik xizmati tizimi » / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=0
    - 3142462: эталон «2/ Sud, prokuratura, ichki ishlar va davlat xavfsizlik xizmati tizimi » / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=0
- журнал по содержанию: 127
    - 3142673: эталон «9/Vazirlik markaziy apparati xodimlarining ichki ariza va bildirgi, sh» / сервис «5/ ADLIYA ORGANLARI VA MUASSASALARIDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=0
    - 3143227: эталон «9/Vazirlik markaziy apparati xodimlarining ichki ariza va bildirgi, sh» / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=0
    - 3143400: эталон «9/Vazirlik markaziy apparati xodimlarining ichki ariza va bildirgi, sh» / сервис «2/ SUD, PROKURATURA, ICHKI ISHLAR VA DAVLAT XAVFSIZLIK XIZMATI TIZIMI » (неверно) journal_exact=0

### XDFU  (всего 62)
- эталон под сомнением: 38
    - 3150845: эталон «0» / сервис «1» (неверно) в тексте: …rining 2025-yil 22-yanvardagi 20-um-son xdfu buyrug'i bilan tasdiqlangan “adliya org…, эталон 0
    - 3154084: эталон «0» / сервис «1» (неверно) в тексте: …istratsiyasining 2025 yil 7 iyundagi 03-1181xdfu/37-son topshirig'ining ijrosini ta'minl…, эталон 0
    - 3158017: эталон «0» / сервис «1» (неверно) в тексте: …opshirig'iga asosan (24.05.2018 yildagi 4152-xdfu-son) bosh prokuratura tomonidan o'zbeki…, эталон 0
- пометки в документе нет: 20
    - 3172067: эталон «1» / сервис «0» (неверно) 
    - 3173238: эталон «1» / сервис «0» (неверно) 
    - 3174213: эталон «1» / сервис «0» (неверно) 
- ложная метка: 3
    - 3162925: эталон «0» / сервис «1» (неверно) 
    - 3312201: эталон «0» / сервис «1» (неверно) 
    - 3312537: эталон «0» / сервис «1» (неверно) 
- прочитал, но не извлёк: 1
    - 3297608: эталон «1» / сервис «0» (неверно) в тексте: …@exat.uz 2026-yil 24-mart 3/1-847/8-son xdfu o'zbekiston respublikasi adliya vazirli…

### Shoshilinch  (всего 3)
- прочитал, но не извлёк: 2
    - 3207742: эталон «1» / сервис «0» (неверно) в тексте: … 02 2026 goda ref.: 4862/per3/cf2/41/25 srochno departament gosudarstvennix uslug pri m…
    - 3281313: эталон «1» / сервис «0» (неверно) в тексте: … 03 2026 goda ref.: 4349/per3/ag3/32/09 srochno departament gosudarstvennix uslug pri m…
- эталон под сомнением: 1
    - 3178662: эталон «0» / сервис «1» (неверно) в тексте: …26-yil «21» 01 ref.: 8056/per3/ff/54/25 shoshilinch! o'zbekiston respublikasi adliya vazirl…, эталон 0

## «Не та шапка» по видам
- судебный акт: 161 — пример: 3142436 (query «АЖРИМ (Ариза буйича иш юритишга кабул килиш тугрисида)»), 3142447 (query «АЖРИМ (даъво аризаии uw юритишга цабул ь^илши, иш кузгатиш в»)
- отчёт/таблица: 146 — пример: 3143767 (query «Normativ-huquqiy hujjat loyihasining tartibga solish taʻsiri»), 3143771 (query «Normativ-huquqiy hujjat loyihasining tartibga solish taʻsiri»)
- адресат вместо отправителя: 26 — пример: 3143764 (query «Астрент институти жорий этилиши муносабати билан Узбекистон »), 3155104 (query «ТОШКЕНТ ВИЛОЯТ СУДИ ИК;ТИСОДИЙ ИШЛАР БУЙИЧА СУДЛОВ ХДЙЪАТИ К»)

## Журнал: отправитель верный, журнал другой
Всего 472; (ожидаемый, сервис, journal_exact): {('5', '6', 1): 385, ('5', '6', 0): 1, ('2', '6', 1): 66, ('2', '6', 0): 20}
- Adliya vazirligi huzuridagi "O‘zarxiv" agentligi (id 213), journal_exact=1: ожидается 5, сервис 6 — 167 писем
- O‘zbekiston Respublikasi Adliya vazirligi huzuridagi yuridik kadrlarni qayta tayyorlash va malakasini oshirish instituti (id 38846), journal_exact=1: ожидается 5, сервис 6 — 93 писем
- O'zbekiston Respublikasi Adliya vazirligi Jizzax viloyat adliya boshqarmasi (id 39011), journal_exact=1: ожидается 5, сервис 6 — 69 писем
- O'zbekiston Respublikasi Adliya vazirligi huzuridagi X.Sulaymonova nomidagi Respublika sud ekspertiza markazi (id 38326), journal_exact=1: ожидается 5, сервис 6 — 30 писем
- O‘zbekiston Respublikasi Mudofaa vazirligi (id 46), journal_exact=1: ожидается 2, сервис 6 — 23 писем
- Аdliya vazirligi huzuridagi "Intellektual mulk markazi" davlat muassasasi (id 281), journal_exact=1: ожидается 5, сервис 6 — 17 писем
- Узбекистон Республикаси Олий суди (id 55128), journal_exact=0: ожидается 2, сервис 6 — 15 писем
- O‘zbekiston Respublikasining Milliy Gvardiyasi (id 22), journal_exact=1: ожидается 2, сервис 6 — 11 писем
- O,ZBEKISTON RESPUBLIKASI DAVLAT XAVFSIZLIK XIZMATI (id 49735), journal_exact=1: ожидается 2, сервис 6 — 10 писем
- O'zbekiston Respublikasi Ichki ishlar vazirligi, Interpol Milliy Markaziy byurosi (id 1445), journal_exact=1: ожидается 2, сервис 6 — 10 писем
- O‘zbekiston Respublikasi huquqni muhofaza qilish akademiyasi (id 552), journal_exact=1: ожидается 2, сервис 6 — 6 писем
- O‘zbekiston Respublikasi Adliya vazirligi huzuridagi Personallashtirish agentligi (id 211), journal_exact=1: ожидается 5, сервис 6 — 5 писем
- Ўзбекистон Республикаси Олий суди Верховный суд Республики Узбекистан (id 41677), journal_exact=0: ожидается 2, сервис 6 — 5 писем
- O'zbekiston Respublikasi Ichki ishlar vazirligi Migratsiya va fuqarolikni rasmiylashtirish bosh boshqarmasi (id 1434), journal_exact=1: ожидается 2, сервис 6 — 3 писем
- "Konvension markaz majmuasi direksiyasi” davlat muassasasi (id None), journal_exact=0: ожидается 5, сервис 6 — 1 писем
- X.Sulaymonova nomidagi Respublika sud ekspertiza markazi (id 31575), journal_exact=1: ожидается 5, сервис 6 — 1 писем
- O‘zbekiston Respublikasi suv xo‘jaligi vazirligi (id 42), journal_exact=1: ожидается 5, сервис 6 — 1 писем
- O‘zbekiston Respublikasi notarial palatasi (id 305), journal_exact=1: ожидается 5, сервис 6 — 1 писем
- Toshkent viloyati arxiv ishi hududiy boshqarmasi (id 40673), journal_exact=1: ожидается 5, сервис 6 — 1 писем
- O'zbekiston Respublikasi Ichki ishlar vazirligi Jamoat xavfsizligi departamenti (id 37650), journal_exact=1: ожидается 2, сервис 6 — 1 писем
- O‘zbekiston Respublikasi Ichki ishlar vazirligi “Xavfsiz shahar” tizimlarini rivojlantirish markazi (id 47348), journal_exact=1: ожидается 2, сервис 6 — 1 писем
- O’zbekiston Respublikasi Ichki ishlar vazirligi Tezkor-qidiruv departamenti kiberxavfsizlik markazi (id 3108), journal_exact=1: ожидается 2, сервис 6 — 1 писем

## Журнал: ошибки по причинам и по парам
[(('отправитель верный, журнал по таблице другой', '5', '6'), 386), (('из-за неверного отправителя', '2', '6'), 309), (('отправитель верный, журнал по таблице другой', '2', '6'), 86), (('журнал по содержанию (9/11/16)', '9', '6'), 45), (('из-за неверного отправителя', '2', '1'), 27), (('журнал по содержанию (9/11/16)', '11', '6'), 25), (('журнал по содержанию (9/11/16)', '9', '1'), 19), (('журнал по содержанию (9/11/16)', '9', '5'), 9), (('из-за неверного отправителя', '5', '6'), 9), (('из-за неверного отправителя', '2', '9'), 9), (('журнал по содержанию (9/11/16)', '11', '2'), 9), (('журнал по содержанию (9/11/16)', '16', '6'), 8), (('журнал по содержанию (9/11/16)', '11', '9'), 7), (('журнал по содержанию (9/11/16)', '9', '2'), 2), (('из-за неверного отправителя', '5', '9'), 2), (('из-за неверного отправителя', '2', '10'), 1), (('журнал по содержанию (9/11/16)', '16', '9'), 1), (('из-за неверного отправителя', '5', '2'), 1), (('из-за неверного отправителя', '2', '5'), 1), (('журнал по содержанию (9/11/16)', '11', '12'), 1)]
journal_exact у верных/неверных (без 9/11/16): Counter({(True, 1): 1347, (False, 1): 502, (False, 0): 329, (True, 0): 155})

## ЭЦП и подписант
{'esign': 384, 'esign_no_surname': 85, 'esign_no_surname_ok': 1, 'esign_no_surname_empty': 80, 'no_esign': 2096, 'no_esign_no_surname': 88}

## Отправители с наибольшим числом ошибок (строгих: неверно/пусто/инициалы)
- O'zbekiston Respublikasi Bosh prokuraturasi: 165 писем, ошибок 272: Imzolagan 77, Sana 63, Raqam 59, Jo‘natuvchi 33, Jurnal 30, XDFU 10
- O'zbekiston Respublikasi Ichki ishlar vazirligi: 182 писем, ошибок 249: Raqam 84, Jurnal 54, Jo‘natuvchi 52, Sana 42, XDFU 10, Imzolagan 7
- O'zbekiston Respublikasi Adliya vazirligi: 67 писем, ошибок 219: Raqam 67, Jo‘natuvchi 59, Jurnal 59, Sana 26, Imzolagan 7, XDFU 1
- O'zbekiston Respublikasi Adliya vazirligi huzuridagi "O'zarxiv" agentligi: 167 писем, ошибок 215: Jurnal 167, Sana 33, Raqam 8, XDFU 7
- O`zbekiston Respublikasi Davlat xavfsizlik xizmati: 115 писем, ошибок 199: Raqam 80, Sana 79, Jurnal 16, Imzolagan 10, XDFU 8, Jo‘natuvchi 6
- O‘zbekiston Respublikasi Oliy sudi: 123 писем, ошибок 139: Jurnal 60, Jo‘natuvchi 42, Raqam 15, Imzolagan 11, Sana 10, XDFU 1
- O‘zbekiston Respublikasi Adliya vazirligi huzuridagi Yuridik kadrlarni qayta tayyorlash va malakasini oshirish instituti: 93 писем, ошибок 107: Jurnal 93, Sana 10, XDFU 2, Raqam 2
- Toshkent tumanlararo ma'muriy sudi: 51 писем, ошибок 85: Jo‘natuvchi 36, Jurnal 35, Raqam 6, Sana 5, Imzolagan 3
- Toshkent tumanlararo iqtisodiy sudi: 52 писем, ошибок 84: Jo‘natuvchi 36, Jurnal 33, Raqam 6, Sana 5, Imzolagan 4
- Toshkent shahar ma`muriy sudi: 40 писем, ошибок 66: Jo‘natuvchi 26, Jurnal 24, Raqam 7, Imzolagan 5, Sana 4
- O'zbekiston Respublikasi Mudofaa vazirligi: 29 писем, ошибок 53: Jurnal 28, XDFU 9, Raqam 7, Jo‘natuvchi 6, Sana 3
- Jizzax viloyat adliya boshqarmasi: 46 писем, ошибок 50: Jurnal 46, Raqam 3, XDFU 1
- Toshkent shahar sudi iqtisodiy ishlar bo‘yicha sudlov hay’ati: 14 писем, ошибок 31: Jo‘natuvchi 14, Jurnal 8, Sana 6, Imzolagan 2, Raqam 1
- O'zbekiston Respublikasi Adliya vazirligi huzuridagi X.Sulaymonova nomidagi Respublika sud ekspertiza markazi: 25 писем, ошибок 30: Jurnal 25, Raqam 2, Sana 2, Imzolagan 1
- Qoraqalpog‘iston Respublikasi Adliya vazirligi: 22 писем, ошибок 26: Jo‘natuvchi 22, Sana 2, Imzolagan 1, Raqam 1

## Скорость и коды
server_ms: n=2480 медиана 33.4 с, p90 62.7 с, p99 103.9 с, макс 168.2 с
client_ms: медиана 33.9 с, p90 63.2 с
503 всего: 1; писем с повтором: 1
- 3149242: no_pdf None
- 3152087: no_pdf None
- 3152806: no_pdf None
- 3162821: no_pdf None
- 3169875: no_pdf None
- 3169938: 413 {"detail":"file exceeds the 40 MB limit"}
- 3172127: 500 {"detail":"Internal server error","request_id":"b507ac085ad6"}
- 3175830: no_pdf None
- 3207488: no_pdf None
- 3207499: no_pdf None
- 3227191: no_pdf None
- 3246372: no_pdf None
- 3256693: no_pdf None
- 3267524: no_pdf None
- 3273229: no_pdf None
- 3273443: no_pdf None
- 3274335: no_pdf None
- 3288689: no_pdf None
- 3290762: no_pdf None
- 3310476: no_pdf None
pages_used < page_count: 71 писем; ocr_used: Counter({True: 1506, False: 974, None: 20})

## Кириллица в summary
ответов 2480; пустых summary 0; summary с кириллицей: 243; в основном (>50% букв) на кириллице: 153
summary не заканчивается концом предложения (вероятно, оборван): 70; примеры: ['3142436', '3146579', '3148851', '3153630', '3155170', '3156288', '3160600', '3165977']
в основном кириллица, примеры: ['3142447', '3142452', '3142462', '3142469', '3142611', '3155148', '3155170', '3157733']
и оборван, и в основном кириллица: 12

## Дополнительные разрезы
Номер «нет в документе»: 207; из них эталон TSTB-…: 150; ЭЦП-документ: 9
Всего писем с номером эталона TSTB-…: 151; верно у сервиса: 0
Дата под сомнением: 161; из них дата эталона = дата регистрации: 75
Дата сервиса позже регистрации (точно ошибка сервиса): 34
Подписант «нет в документе»: 101; из них ЭЦП-документ: 79
Отправитель неверно, но «очень похоже» (ratio≥90) — для ручной проверки: 46: 3142442, 3149320, 3154717, 3156288, 3157733, 3162684, 3173075, 3179391, 3180337, 3181548, 3189171, 3193371, 3195348, 3195364, 3195841, 3201448, 3210133, 3212271, 3218491, 3224683, 3229675, 3229718, 3229847, 3229865, 3234195, 3237368, 3237803, 3255230, 3256694, 3257579, 3261898, 3264085, 3265043, 3273251, 3279152, 3282965, 3286848, 3292009, 3294014, 3294897, 3312068, 3312549, 3313477, 3313799, 3314543, 3320191
Ошибки журнала из-за «не та шапка» у отправителя: 251
Отправитель пусто у сервиса: 285; причины: {'не та шапка (судебный акт)': 143, 'OCR не прочитал': 6, 'не та шапка (отчёт/таблица)': 90, 'прочитал, но не извлёк': 44, 'шапка не найдена': 1, 'не та шапка (адресат вместо отправителя)': 1}
ХДФУ: сервис 1, эталон 0, в тексте есть «xdfu»: 38
Источник текста: {'текстовый слой': 974, 'скан/OCR': 1506}
- Raqam по источнику: {'OCR': '1243/1486 (83.6%), с форматом 87.5%', 'текст': '639/953 (67.1%), с форматом 67.1%'}
- Sana по источнику: {'OCR': '1267/1506 (84.1%), с форматом 84.1%', 'текст': '753/974 (77.3%), с форматом 77.3%'}
- Imzolagan по источнику: {'OCR': '1433/1495 (95.9%), с форматом 95.9%', 'текст': '775/967 (80.1%), с форматом 80.1%'}
- Jo‘natuvchi по источнику: {'OCR': '649/1482 (43.8%), с форматом 88.1%', 'текст': '350/951 (36.8%), с форматом 50.4%'}