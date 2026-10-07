# Данные для отчёта (results.jsonl)

Писем: 1000; статусы: {'200': 990, 'no_pdf': 8, '413': 1, '500': 1}

## Точность

| Поле | Строго | С «формат» | Всего | Строго % | С «формат» % | Под сомнением | Исключено |
|---|---|---|---|---|---|---|---|
| Raqam | 775 | 790 | 969 | 80.0% | 81.5% | 22 | {'пусто в эталоне': 21, 'не обработано': 10} |
| Sana | 807 | 807 | 990 | 81.5% | 81.5% | 77 | {'не обработано': 10} |
| Imzolagan | 868 | 868 | 979 | 88.7% | 88.7% | 4 | {'пусто в эталоне': 11, 'не обработано': 10} |
| Jo‘natuvchi | 370 | 701 | 967 | 38.3% | 72.5% | 7 | {'пусто в эталоне': 23, 'не обработано': 10} |
| Jurnal | 614 | 614 | 990 | 62.0% | 62.0% | 0 | {'не обработано': 10} |
| XDFU | 968 | 968 | 990 | 97.8% | 97.8% | 16 | {'не обработано': 10} |
| Shoshilinch | 945 | 945 | 947 | 99.8% | 99.8% | 1 | {'решение оператора, в тексте отметки нет': 43, 'не обработано': 10} |
| Jurnal без 9/11/16 | 608 | 608 | 926 | 65.7% | 65.7% | 0 | {'не обработано': 1} |
| Jurnal только 9/11/16 | 6 | 6 | 64 | 9.4% | 9.4% | 0 | {'не обработано': 9} |

## Категории итогов по полям
- Raqam: верно 775; пусто у сервиса 106; неверно 73; пусто в эталоне 21; формат 15; не обработано 10
- Sana: верно 807; неверно 130; пусто у сервиса 53; не обработано 10
- Imzolagan: верно 790; верно (транслит) 78; пусто у сервиса 64; неверно 22; инициалы 14; неполные инициалы 11; пусто в эталоне 11; не обработано 10
- Jo‘natuvchi: верно 356; формат / другое написание организации 331; неверно 145; пусто у сервиса 121; пусто в эталоне 23; верно (транслит) 14; не обработано 10
- Jurnal: верно 614; неверно 376; не обработано 10
- XDFU: верно 968; неверно 22; не обработано 10
- Shoshilinch: верно 945; решение оператора, в тексте отметки нет 43; не обработано 10; неверно 2

## Причины (итог не верно/формат, без исключённых)

### Raqam  (всего 194)
- нет в документе: 88
    - 3143764: эталон «TSTB-2599-2» / сервис «» (пусто у сервиса) 
    - 3143767: эталон «TSTB-2906» / сервис «» (пусто у сервиса) 
    - 3143771: эталон «TSTB-2912» / сервис «» (пусто у сервиса) 
- прочитал, но не извлёк: 42
    - 3142452: эталон «4-1001-2504/.118581» / сервис «4-1001-2518/118581» (неверно) похожий номер
    - 3143535: эталон «-5/278» / сервис «5/278» (неверно) часть номера
    - 3146413: эталон «20-6/3374» / сервис «20-6/3374 ox» (неверно) часть номера
- OCR не прочитал: 26
    - 3148596: эталон «31/4-557328/25-1» / сервис «№ 31/4-557328/25-i-» (неверно) похожий номер
    - 3157641: эталон «18/181BL-25» / сервис «№ 18/181BK-25» (неверно) похожий номер
    - 3157959: эталон «16.2/-26-10-6-3» / сервис «16.2/-26-10-h-3» (неверно) похожий номер
- эталон под сомнением: 22
    - 3141685: эталон «33/01-02-4107» / сервис «12/1-3669» (неверно) 
    - 3143365: эталон «4/18033» / сервис «№4/» (неверно) часть номера
    - 3143370: эталон «4/18035» / сервис «21/12-1990» (неверно) 
- —: 15
- за пределами прочитанного: 1
    - 3151761: эталон «4/253» / сервис «» (пусто у сервиса) 

### Sana  (всего 183)
- эталон под сомнением: 77
    - 3141682: эталон «05.01.2026» / сервис «2025-12-30» (неверно) разница -6 дн.; дата эталона = дата регистрации
    - 3141685: эталон «22.12.2025» / сервис «2025-10-24» (неверно) разница -59 дн.
    - 3141700: эталон «05.01.2026» / сервис «2025-12-29» (неверно) разница -7 дн.; дата эталона = дата регистрации
- нет в документе: 44
    - 3142650: эталон «03.01.2026» / сервис «» (пусто у сервиса) 
    - 3144343: эталон «06.01.2026» / сервис «» (пусто у сервиса) 
    - 3148596: эталон «05.01.2026» / сервис «» (пусто у сервиса) 
- прочитал, но не извлёк: 35
    - 3142452: эталон «29.12.2025» / сервис «2025-12-30» (неверно) разница +1 дн.
    - 3143559: эталон «16.12.2025» / сервис «2025-12-30» (неверно) разница +14 дн.
    - 3148844: эталон «06.01.2026» / сервис «2026-01-05» (неверно) разница -1 дн.
- OCR не прочитал: 20
    - 3142793: эталон «05.01.2026» / сервис «» (пусто у сервиса) 
    - 3146765: эталон «06.01.2026» / сервис «2026-01-01» (неверно) разница -5 дн.
    - 3146767: эталон «06.01.2025» / сервис «» (пусто у сервиса) 
- взята другая дата из текста: 5
    - 3153287: эталон «09.01.2026» / сервис «2026-01-15» (неверно) разница +6 дн.; дата сервиса позже регистрации
    - 3184856: эталон «26.01.2026» / сервис «2026-01-27» (неверно) разница +1 дн.; дата сервиса позже регистрации
    - 3186526: эталон «22.01.2026» / сервис «2026-11-22» (неверно) разница +304 дн.; дата сервиса позже регистрации
- за пределами прочитанного: 2
    - 3151761: эталон «09.01.2026» / сервис «» (пусто у сервиса) 
    - 3182537: эталон «19.01.2026» / сервис «2026-01-05» (неверно) разница -14 дн.

### Imzolagan  (всего 111)
- прочитал, но не извлёк: 38
    - 3142544: эталон «J.A.Buriyev» / сервис «A. Buriyev» (инициалы) 
    - 3142673: эталон «N.Suleymanov» / сервис «» (пусто у сервиса) 
    - 3143559: эталон «J.G‘.Sirojev» / сервис «» (пусто у сервиса) 
- нет в документе: 36
    - 3141682: эталон «I.M.Adxamov» / сервис «» (пусто у сервиса) 
    - 3141700: эталон «D.S.Kasimov» / сервис «» (пусто у сервиса) 
    - 3143524: эталон «S.B.Artikova» / сервис «» (пусто у сервиса) 
- OCR не прочитал: 31
    - 3141685: эталон «A.T.Rahmatullayev» / сервис «Rahmatullaev» (неполные инициалы) у сервиса без инициалов
    - 3141856: эталон «Z.B.Djalilov» / сервис «E.B.Djalilov» (инициалы) 
    - 3142452: эталон «B.B.Abduraximov» / сервис «B.Abduraximov» (неполные инициалы) эталон 2, сервис 1
- эталон под сомнением: 4
    - 3172862: эталон «B.Abduraximov» / сервис «B.Abd5fakhimov» (неверно) 
    - 3178587: эталон «N.Abdullaev» / сервис «N.Abdilaxatov» (неверно) 
    - 3182612: эталон «M.M.Abduraxmanov» / сервис «J.Abdusattorov» (неверно) 
- за пределами прочитанного: 2
    - 3156288: эталон «A.Bo‘ronov» / сервис «» (пусто у сервиса) 
    - 3189653: эталон «A.Bo'ronov» / сервис «» (пусто у сервиса) 

### Jo‘natuvchi  (всего 597)
- —: 331
- прочитал, но не извлёк: 72
    - 3142442: эталон «Farg‘ona viloyat sudi iqtisodiy ishlar bo‘yocha sudlov hay'ati» / сервис «Farg'ona viloyat sudining Iqtisodiy ishlar bo'yicha sudlov hay'ati» (неверно) очень похоже (95); query: ФАРҒОНА ВИЛОЯТ СУДИНИНГ ИҚТИСОДИЙ ИШЛАР БЎЙИЧА СУДЛОВ ҲАЙЪАТИ АПЕЛЛЯЦИЯ ИНСТАНЦИЯСИНИНГ АЖРИМИ
    - 3143559: эталон «Toshkent shahar sudi fuqarolik ishlari bo'yicha» / сервис «Ўзбекистон Республикаси Олий суди Верховный суд Республики Узбекистан» (неверно) query: Узбекистон Республикаси Олий суди Верховный суд Республики Узбекистан
    - 3144505: эталон «Oʻzbekiston Respublikasi Oliy sudi» / сервис «» (пусто у сервиса) query: Ijrochi: O.Rajabov
- не та шапка (судебный акт): 70
    - 3142436: эталон «Nurafshon tumanlararo ma'muriy sudi» / сервис «» (пусто у сервиса) query: АЖРИМ (Ариза буйича иш юритишга кабул килиш тугрисида)
    - 3142447: эталон «Toshkent tumanlararo iqtisodiy sudi» / сервис «» (пусто у сервиса) query: АЖРИМ (даъво аризаии uw юритишга цабул ь^илши, иш кузгатиш ва ишии суд мух,окамасига тайёрлаш тугрисида) Тошкент 
    - 3142462: эталон «TOSHKENT TUMANLARARO MA’MURIY SUDI» / сервис «» (пусто у сервиса) query: УЗБЕКИСТОН РЕСПУБЛИКАСИ НОМИДАН ХДЛ к;илув КАРОРИ
- не та шапка (отчёт/таблица): 64
    - 3143767: эталон «O'zbekiston Respublikasi Ichki ishlar vazirligi» / сервис «» (пусто у сервиса) query: Normativ-huquqiy hujjat loyihasining tartibga solish taʻsirini baholash boʻyicha soddalashtirilgan HISOBOT
    - 3143771: эталон «O'zbekiston Respublikasi Ichki ishlar vazirligi» / сервис «» (пусто у сервиса) query: Normativ-huquqiy hujjat loyihasining tartibga solish taʻsirini baholash boʻyicha soddalashtirilgan HISOBOT
    - 3145075: эталон «O'zbekiston Respublikasi Adliya vazirligi» / сервис «» (пусто у сервиса) query: Normativ-huquqiy hujjat loyihasining tartibga solish taʻsirini baholash boʻyicha soddalashtirilgan HISOBOT
- OCR не прочитал: 19
    - 3142452: эталон «Toshkent shahar iqtisodiy ishlar bo'yicha sudlov hay'ati» / сервис «Тошкент шахар иктисодий суди» (неверно) query: ТОШКЕНТ ШАХАР СУДИ ИКТИСОДИЙ ИШЛАР БУЙИЧА СУДЛОВ ХАЙЪАТИ АПЕЛЛЯЦИЯ ИНСТАНЦИЯСИНИНГ АЖРИМИ
    - 3142607: эталон «Toshkent tumanlaro iqtisodiy sudi» / сервис «» (пусто у сервиса) query: A Ж P И M (суд мух,окамасини кейинга цолдириш ва ишга гуво)^ларни жалб этиш тугрисида) Тошкент шах;ар
    - 3144786: эталон «Qoraqalpog‘iston Respublikasi Adliya vazirligi» / сервис «Ozbekstan Respublikasi A'dillik Ministrligi Qaraqalpaqstan Respublikas» (неверно) query: OZBEKSTAN RESPUBLIKASl ADILLIK MINISTRLIGI QARAQALPAQSTAN RESPUBLIKASl ADILLIK MINISTRLIGI
- не та шапка (адресат вместо отправителя): 12
    - 3143764: эталон «O'zbekiston Respublikasi Bosh prokuraturasi» / сервис «ISFT INSTITUTI» (неверно) query: Астрент институти жорий этилиши муносабати билан Узбекистон Республикасининг айрим Конун Хужжатларига узгартириш 
    - 3155104: эталон «Toshkent viloyat iqtisodiy ishlar bo'yicha sudlov hay'ati» / сервис «Toshkent viloyat sudi» (неверно) query: ТОШКЕНТ ВИЛОЯТ СУДИ ИК;ТИСОДИЙ ИШЛАР БУЙИЧА СУДЛОВ ХДЙЪАТИ КАССАЦИЯ ИНСТАНЦИЯСИНИНГ АЖРИМИ (ишни иш юритишга цабу
    - 3179512: эталон «Oʻzbekiston Respublikasi Oliy sudi» / сервис «O'zbekiston Respublikasi Adliya vazirligi» (неверно) query: O‘ZBEKISTON RESPUBLIKASI y Oʻzbekiston Respublikasi OLIY SUDI Adliya vazirligi i Xalqaro-huquqiy hamkorlik va
- выбрана вышестоящая: 11
    - 3148596: эталон «O'zbekiston Respublikasi Bosh prokuraturasi» / сервис «Узбекистон Республикаси Олий суди» (неверно) query: O'ZBEKISTON RESPUBLIKASI Узбекистон Республикаси BOSH PROKURATURASI Олий суди маъмурий ишлар
    - 3166069: эталон «Oʻzbekiston Respublikasi Oliy sudi» / сервис «O‘zbekiston Respublikasi Bosh prokuraturasi» (неверно) query: OʻZBEKISTON RESPUBLIKASI O`zbekiston Respublikasi OLIY SUDI Bosh prokuraturasi
    - 3174114: эталон «OʻZBEKISTON RESPUBLIKASI ICHKI ISHLAR VAZIRLIGI AKADEMIYASI» / сервис «O‘zbekiston Respublikasi ichki ishlar vazirligi» (неверно) query: OʻZBEKISTON RESPUBLIKASI ICHKI ISHLAR VAZIRLIGI
- эталон под сомнением: 7
    - 3146519: эталон «O'zbekiston Respublikasi Mudofaa vazirligi» / сервис «O'zbekiston Respublikasi Adliya vazirligi Farg'ona viloyat adliya bosh» (неверно) query: OʻZBEKISTON RESPUBLIKASI ADLIYA VAZIRLIGI FARGʻONA VILOYAT ADLIYA BOSHQARMASI
    - 3167112: эталон «FIB Mirobod tumanlararo sudi» / сервис «Mirzo Ulug'bek Tumanlararo Sudi» (неверно) query: FUQAROLIK ISHLARI ВО"УТСНА MIRZO ULUG`BEK TUMANLARARO SUDI
    - 3175848: эталон «Toshkent shahar iqtisodiy ishlar bo'yicha sudlov hay'ati» / сервис «Toshkent shaxar sudi» (неверно) query: ишни курган судья Ш.Ш.Джамолов Апелляция инстанцияси судида маърузачи судья Б.Б.Абдурахимов ТОШКЕНТ ШАХАР СУДИ
- неполное название: 6
    - 3156257: эталон «Toshkent shahar sudi iqtisodiy ishlar bo‘yicha sudlov hay’ati» / сервис «Toshkent shahar iqtisodiy sudi» (неверно) query: < ТОШКЕНТ ШАҲАР СУДИ — ИҚТИСОДИЙ ИШЛАР БЎЙИЧА СУДЛОВ ҲАЙЪАТИНИНГ АЖРИМИ (қонуний кучга кирган суд ҳужжатини янги 
    - 3161338: эталон «Toshkent tumanlararo ma'muriy sudi» / сервис «Toshkent tumanlararo sudi» (неверно) query: TOSHKENT TUMANLARARO
    - 3172778: эталон «FIB UCHTEPA TUMANLARARO SUDI» / сервис «fuqarolik sudi» (неверно) query: FUQAROLIK ISHLARI ВО"УТСНА UCHTEPA TUMANLARARO SUDI
- мусорная запись: 5
    - 3155090: эталон «Yangihayot tumani ichki ishlar organlari faoliyatini muvofiqlashtirish» / сервис «O'zbekiston Respublikasi Ichki ishlar vazirligi Toshkent shahar Ichki » (неверно) query: O`ZBEKISTON RESPUBLIKASI ICHKI ISHLAR VAZIRLIGI TOSHKENT SHAHAR ICHKI ISHLAR BOSH BOSHQARMASI YANGIHAYOT TUMANI I
    - 3178587: эталон «Asaka tuman davlat arxivi» / сервис «O'zbekiston Respublikasi Adliya vazirligi huzuridagi "O'zarxiv" agentl» (неверно) query: OʻZBEKISTON RESPUBLIKASI ADLIYA VAZIRLIGI HUZURIDAGI “OʻZARXIV” AGENTLIGI ANDIJON VILOYATI ARXIV ISHI HUDUDIY BOS
    - 3204106: эталон «O‘zbekiston Respublikasi Ichki ishlar vazirligi» / сервис «NNT faoliyati to'g'risidagi hisobot» (неверно) query: HISOBOT 1 Loyiha turi Qonun 2 Loyiha nomi Узбекистон Республикасининг Куриклаш фаолияти тўғрисидаги қонунига ўзга

### Jurnal  (всего 376)
- отправитель верный, журнал по таблице другой: 175
    - 3141689: эталон «5/ Adliya organlari va muassasalaridan kelib tushgan hujjatlar» / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=1
    - 3141698: эталон «2/ Sud, prokuratura, ichki ishlar va davlat xavfsizlik xizmati tizimi » / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=1
    - 3141758: эталон «5/ Adliya organlari va muassasalaridan kelib tushgan hujjatlar» / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=1
- из-за неверного отправителя: 143
    - 3142436: эталон «2/ Sud, prokuratura, ichki ishlar va davlat xavfsizlik xizmati tizimi » / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=0
    - 3142447: эталон «2/ Sud, prokuratura, ichki ishlar va davlat xavfsizlik xizmati tizimi » / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=0
    - 3142462: эталон «2/ Sud, prokuratura, ichki ishlar va davlat xavfsizlik xizmati tizimi » / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=0
- журнал по содержанию: 58
    - 3142673: эталон «9/Vazirlik markaziy apparati xodimlarining ichki ariza va bildirgi, sh» / сервис «5/ ADLIYA ORGANLARI VA MUASSASALARIDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=0
    - 3143227: эталон «9/Vazirlik markaziy apparati xodimlarining ichki ariza va bildirgi, sh» / сервис «6/ TURLI VAZIRLIKLAR, IDORA VA TASHKILOTLARDAN KELIB TUSHGAN HUJJATLAR» (неверно) journal_exact=0
    - 3143400: эталон «9/Vazirlik markaziy apparati xodimlarining ichki ariza va bildirgi, sh» / сервис «2/ SUD, PROKURATURA, ICHKI ISHLAR VA DAVLAT XAVFSIZLIK XIZMATI TIZIMI » (неверно) journal_exact=0

### XDFU  (всего 22)
- эталон под сомнением: 16
    - 3150845: эталон «0» / сервис «1» (неверно) в тексте: …rining 2025-yil 22-yanvardagi 20-um-son xdfu buyrug'i bilan tasdiqlangan “adliya org…, эталон 0
    - 3154084: эталон «0» / сервис «1» (неверно) в тексте: …istratsiyasining 2025 yil 7 iyundagi 03-1181xdfu/37-son topshirig'ining ijrosini ta'minl…, эталон 0
    - 3158017: эталон «0» / сервис «1» (неверно) в тексте: …opshirig'iga asosan (24.05.2018 yildagi 4152-xdfu-son) bosh prokuratura tomonidan o'zbeki…, эталон 0
- пометки в документе нет: 5
    - 3172067: эталон «1» / сервис «0» (неверно) 
    - 3173238: эталон «1» / сервис «0» (неверно) 
    - 3174213: эталон «1» / сервис «0» (неверно) 
- ложная метка: 1
    - 3162925: эталон «0» / сервис «1» (неверно) 

### Shoshilinch  (всего 2)
- эталон под сомнением: 1
    - 3178662: эталон «0» / сервис «1» (неверно) в тексте: …26-yil «21» 01 ref.: 8056/per3/ff/54/25 shoshilinch! o'zbekiston respublikasi adliya vazirl…, эталон 0
- прочитал, но не извлёк: 1
    - 3207742: эталон «1» / сервис «0» (неверно) в тексте: … 02 2026 goda ref.: 4862/per3/cf2/41/25 srochno departament gosudarstvennix uslug pri m…

## «Не та шапка» по видам
- судебный акт: 70 — пример: 3142436 (query «АЖРИМ (Ариза буйича иш юритишга кабул килиш тугрисида)»), 3142447 (query «АЖРИМ (даъво аризаии uw юритишга цабул ь^илши, иш кузгатиш в»)
- отчёт/таблица: 64 — пример: 3143767 (query «Normativ-huquqiy hujjat loyihasining tartibga solish taʻsiri»), 3143771 (query «Normativ-huquqiy hujjat loyihasining tartibga solish taʻsiri»)
- адресат вместо отправителя: 12 — пример: 3143764 (query «Астрент институти жорий этилиши муносабати билан Узбекистон »), 3155104 (query «ТОШКЕНТ ВИЛОЯТ СУДИ ИК;ТИСОДИЙ ИШЛАР БУЙИЧА СУДЛОВ ХДЙЪАТИ К»)

## Журнал: отправитель верный, журнал другой
Всего 175; (ожидаемый, сервис, journal_exact): {('5', '6', 1): 158, ('2', '6', 1): 10, ('2', '6', 0): 7}
- Adliya vazirligi huzuridagi "O‘zarxiv" agentligi (id 213), journal_exact=1: ожидается 5, сервис 6 — 64 писем
- O'zbekiston Respublikasi Adliya vazirligi Jizzax viloyat adliya boshqarmasi (id 39011), journal_exact=1: ожидается 5, сервис 6 — 34 писем
- O‘zbekiston Respublikasi Adliya vazirligi huzuridagi yuridik kadrlarni qayta tayyorlash va malakasini oshirish instituti (id 38846), journal_exact=1: ожидается 5, сервис 6 — 29 писем
- O'zbekiston Respublikasi Adliya vazirligi huzuridagi X.Sulaymonova nomidagi Respublika sud ekspertiza markazi (id 38326), journal_exact=1: ожидается 5, сервис 6 — 17 писем
- Аdliya vazirligi huzuridagi "Intellektual mulk markazi" davlat muassasasi (id 281), journal_exact=1: ожидается 5, сервис 6 — 8 писем
- O‘zbekiston Respublikasi Adliya vazirligi huzuridagi Personallashtirish agentligi (id 211), journal_exact=1: ожидается 5, сервис 6 — 4 писем
- Узбекистон Республикаси Олий суди (id 55128), journal_exact=0: ожидается 2, сервис 6 — 4 писем
- O'zbekiston Respublikasi Ichki ishlar vazirligi Migratsiya va fuqarolikni rasmiylashtirish bosh boshqarmasi (id 1434), journal_exact=1: ожидается 2, сервис 6 — 3 писем
- Ўзбекистон Республикаси Олий суди Верховный суд Республики Узбекистан (id 41677), journal_exact=0: ожидается 2, сервис 6 — 3 писем
- O,ZBEKISTON RESPUBLIKASI DAVLAT XAVFSIZLIK XIZMATI (id 49735), journal_exact=1: ожидается 2, сервис 6 — 2 писем
- O'zbekiston Respublikasi Ichki ishlar vazirligi, Interpol Milliy Markaziy byurosi (id 1445), journal_exact=1: ожидается 2, сервис 6 — 2 писем
- X.Sulaymonova nomidagi Respublika sud ekspertiza markazi (id 31575), journal_exact=1: ожидается 5, сервис 6 — 1 писем
- O‘zbekiston Respublikasi suv xo‘jaligi vazirligi (id 42), journal_exact=1: ожидается 5, сервис 6 — 1 писем
- O'zbekiston Respublikasi Ichki ishlar vazirligi Jamoat xavfsizligi departamenti (id 37650), journal_exact=1: ожидается 2, сервис 6 — 1 писем
- O‘zbekiston Respublikasi huquqni muhofaza qilish akademiyasi (id 552), journal_exact=1: ожидается 2, сервис 6 — 1 писем
- O’zbekiston Respublikasi Ichki ishlar vazirligi Tezkor-qidiruv departamenti kiberxavfsizlik markazi (id 3108), journal_exact=1: ожидается 2, сервис 6 — 1 писем

## Журнал: ошибки по причинам и по парам
[(('отправитель верный, журнал по таблице другой', '5', '6'), 158), (('из-за неверного отправителя', '2', '6'), 120), (('журнал по содержанию (9/11/16)', '9', '6'), 24), (('отправитель верный, журнал по таблице другой', '2', '6'), 17), (('журнал по содержанию (9/11/16)', '11', '6'), 13), (('из-за неверного отправителя', '2', '1'), 10), (('журнал по содержанию (9/11/16)', '9', '1'), 9), (('из-за неверного отправителя', '5', '6'), 6), (('журнал по содержанию (9/11/16)', '9', '5'), 5), (('из-за неверного отправителя', '2', '9'), 5), (('журнал по содержанию (9/11/16)', '16', '6'), 3), (('журнал по содержанию (9/11/16)', '11', '9'), 2), (('журнал по содержанию (9/11/16)', '9', '2'), 1), (('из-за неверного отправителя', '2', '10'), 1), (('журнал по содержанию (9/11/16)', '16', '9'), 1), (('из-за неверного отправителя', '5', '9'), 1)]
journal_exact у верных/неверных (без 9/11/16): Counter({(True, 1): 547, (False, 1): 191, (False, 0): 127, (True, 0): 61})

## ЭЦП и подписант
{'esign': 150, 'esign_no_surname': 30, 'esign_no_surname_ok': 0, 'esign_no_surname_empty': 29, 'no_esign': 840, 'no_esign_no_surname': 36}

## Отправители с наибольшим числом ошибок (строгих: неверно/пусто/инициалы)
- O'zbekiston Respublikasi Bosh prokuraturasi: 67 писем, ошибок 120: Sana 27, Imzolagan 26, Raqam 25, Jo‘natuvchi 18, Jurnal 18, XDFU 6
- O'zbekiston Respublikasi Ichki ishlar vazirligi: 77 писем, ошибок 105: Raqam 35, Jurnal 23, Jo‘natuvchi 21, Sana 18, XDFU 4, Imzolagan 4
- O’zbekiston Respublikasi Adliya vazirligi: 29 писем, ошибок 101: Raqam 29, Jo‘natuvchi 28, Jurnal 28, Sana 12, Imzolagan 3, XDFU 1
- O'zbekiston Respublikasi Adliya vazirligi huzuridagi "O'zarxiv" agentligi: 64 писем, ошибок 79: Jurnal 64, Sana 11, Raqam 2, XDFU 2
- Oʻzbekiston Respublikasi Oliy sudi: 47 писем, ошибок 56: Jurnal 21, Jo‘natuvchi 16, Imzolagan 7, Raqam 7, Sana 5
- O`zbekiston Respublikasi Davlat xavfsizlik xizmati: 33 писем, ошибок 56: Raqam 23, Sana 23, Jurnal 4, Jo‘natuvchi 2, XDFU 2, Imzolagan 2
- Toshkent tumanlararo ma'muriy sudi: 28 писем, ошибок 44: Jo‘natuvchi 20, Jurnal 19, Imzolagan 2, Raqam 2, Sana 1
- O‘zbekiston Respublikasi Adliya vazirligi huzuridagi Yuridik kadrlarni qayta tayyorlash va malakasini oshirish instituti: 29 писем, ошибок 38: Jurnal 29, Sana 7, XDFU 1, Raqam 1
- Toshkent tumanlararo iqtisodiy sudi: 20 писем, ошибок 33: Jo‘natuvchi 14, Jurnal 13, Raqam 3, Sana 3
- Toshkent shahar ma`muriy sudi: 18 писем, ошибок 32: Jo‘natuvchi 12, Jurnal 11, Raqam 3, Sana 3, Imzolagan 3
- Jizzax viloyat adliya boshqarmasi: 22 писем, ошибок 24: Jurnal 22, Raqam 2
- Qoraqalpog‘iston Respublikasi Adliya vazirligi: 20 писем, ошибок 24: Jo‘natuvchi 20, Sana 2, Imzolagan 1, Raqam 1
- O'zbekiston Respublikasi Adliya vazirligi huzuridagi X.Sulaymonova nomidagi Respublika sud ekspertiza markazi: 16 писем, ошибок 19: Jurnal 16, Raqam 1, Sana 1, Imzolagan 1
- Namangan viloyat ma`muriy sudi: 9 писем, ошибок 17: Imzolagan 5, Jo‘natuvchi 4, Jurnal 4, Raqam 4
- Toshkent shahar iqtisodiy ishlar bo'yicha sudlov hay'ati: 7 писем, ошибок 15: Jo‘natuvchi 7, Sana 4, Raqam 2, Imzolagan 1, Jurnal 1

## Скорость и коды
server_ms: n=990 медиана 32.7 с, p90 64.0 с, p99 97.6 с, макс 148.0 с
client_ms: медиана 32.9 с, p90 64.4 с
503 всего: 0; писем с повтором: 0
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
pages_used < page_count: 33 писем; ocr_used: Counter({True: 611, False: 379, None: 10})

## Кириллица в summary
ответов 990; пустых summary 0; summary с кириллицей: 91; в основном (>50% букв) на кириллице: 59
summary не заканчивается концом предложения (вероятно, оборван): 29; примеры: ['3142436', '3146579', '3148851', '3153630', '3155170', '3156288', '3160600', '3165977']
в основном кириллица, примеры: ['3142447', '3142452', '3142462', '3142469', '3142611', '3155148', '3155170', '3157733']
и оборван, и в основном кириллица: 4

## Дополнительные разрезы
Номер «нет в документе»: 88; из них эталон TSTB-…: 65; ЭЦП-документ: 4
Всего писем с номером эталона TSTB-…: 65; верно у сервиса: 0
Дата под сомнением: 77; из них дата эталона = дата регистрации: 43
Дата сервиса позже регистрации (точно ошибка сервиса): 11
Подписант «нет в документе»: 36; из них ЭЦП-документ: 29
Отправитель неверно, но «очень похоже» (ratio≥90) — для ручной проверки: 17: 3142442, 3149320, 3154717, 3156288, 3157733, 3162684, 3173075, 3179391, 3180337, 3181548, 3189171, 3193371, 3195348, 3195364, 3195841, 3201448, 3210133
Ошибки журнала из-за «не та шапка» у отправителя: 110
Отправитель пусто у сервиса: 121; причины: {'не та шапка (судебный акт)': 64, 'OCR не прочитал': 1, 'не та шапка (отчёт/таблица)': 42, 'прочитал, но не извлёк': 14}
ХДФУ: сервис 1, эталон 0, в тексте есть «xdfu»: 16
Источник текста: {'текстовый слой': 379, 'скан/OCR': 611}
- Raqam по источнику: {'OCR': '522/603 (86.6%), с форматом 89.1%', 'текст': '253/366 (69.1%), с форматом 69.1%'}
- Sana по источнику: {'OCR': '519/611 (84.9%), с форматом 84.9%', 'текст': '288/379 (76.0%), с форматом 76.0%'}
- Imzolagan по источнику: {'OCR': '578/603 (95.9%), с форматом 95.9%', 'текст': '290/376 (77.1%), с форматом 77.1%'}
- Jo‘natuvchi по источнику: {'OCR': '234/598 (39.1%), с форматом 87.0%', 'текст': '136/369 (36.9%), с форматом 49.1%'}