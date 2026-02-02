# Requirements: Miw's Property Acquisition Plan

**Version:** 4.0
**Status:** ✅ APPROVED
**Last Updated:** 2026-01-27
**Approved:** 2026-01-27
**Goal:** Приобретение реальной недвижимости для Miw с бюджетом $1,000

---

## ⚠️ Как работает sdd-miw-gift

> **ВАЖНО:** Этот SDD работает НЕ через код, а через управление ДРУГИМИ SDD flows.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  sdd-miw-gift = КОМПАС ДЛЯ ДРУГИХ SDD                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Цель: Достичь цели Miw НАИБЫСТРЕЙШИМ способом                             │
│                                                                             │
│  Метод работы:                                                              │
│  1. Выстраивание пути В ОСТАЛЬНЫХ SDD, ориентируясь на sdd-miw-gift       │
│  2. Изменение приоритетов в sdd-taxlien-parser (какие counties первыми)   │
│  3. Изменение приоритетов в sdd-taxlien-gateway (какие endpoints нужны)   │
│  4. Изменение приоритетов в sdd-taxlien-ml (какие модели важнее)          │
│  5. Добавление фишек и пояснений в спецификации других SDD                │
│  6. Roadmap ВСЕЙ СИСТЕМЫ идёт в соответствии с кратчайшим путём к цели    │
│                                                                             │
│  sdd-miw-gift УПРАВЛЯЕТ:                                                   │
│                                                                             │
│  ═══ PRIMARY (критический путь к цели Miw) ═══                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │ sdd-taxlien-    │  │ sdd-taxlien-    │  │ sdd-taxlien-    │             │
│  │ parser          │→ │ gateway         │→ │ ml              │             │
│  │ (Arizona first!)│  │ (foreclosure    │  │ (Foreclosure    │             │
│  │                 │  │  endpoint)      │  │  Score, x1000)  │             │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘             │
│           │                                                                │
│           └──────────────────┐                                             │
│                              ▼                                             │
│                    ┌─────────────────┐                                     │
│                    │ sdd-taxlien-    │                                     │
│                    │ enrichment      │                                     │
│                    │ (obituaries,    │                                     │
│                    │  photos, graph) │                                     │
│                    └─────────────────┘                                     │
│                                                                             │
│  ═══ SECONDARY (задел на будущее) ═══                                      │
│  ┌─────────────────┐  ┌─────────────────┐                                  │
│  │ sdd-taxlien-    │  │ sdd-taxlien-    │                                  │
│  │ ssr-site        │  │ flutter-app     │                                  │
│  │ (web UI +       │  │ (mobile UI +    │                                  │
│  │  печать)        │  │  on-the-go)     │                                  │
│  └─────────────────┘  └─────────────────┘                                  │
│                                                                             │
│  Почему SECONDARY?                                                          │
│  • Цель Miw достижима БЕЗ них (первичная ручная закупка)                   │
│  • Дадут задел на БУДУЩЕЕ:                                                 │
│    - После первой закупки пройдёт время                                    │
│    - Miw/Denis/Shon захотят что-то проанализировать вручную               │
│    - Или сделать расширенный поиск                                         │
│    - Или обратить внимание на другие штаты/counties                        │
│    - Вдруг там будет что-то интересное                                     │
│                                                                             │
│  ═══ TERTIARY (обобщение и sharing) ═══                                    │
│  ┌─────────────────┐                                                       │
│  │ sdd-taxlien-    │                                                       │
│  │ content         │                                                       │
│  │ (статьи,        │                                                       │
│  │  guides)        │                                                       │
│  └─────────────────┘                                                       │
│                                                                             │
│  Почему TERTIARY?                                                           │
│  • Обобщить накопленные знания                                             │
│  • Поделиться пройденным путём                                             │
│  • Дать другим людям возможность пользоваться проделанным трудом           │
│  • Статьи: "Как мы нашли foreclosure за $500", "x1000 антиквариат" и др.  │
│                                                                             │
│  НЕ включает:                                                               │
│  ✗ Написание кода в sdd-miw-gift                                           │
│  ✗ Создание software в sdd-miw-gift                                        │
│                                                                             │
│  Включает:                                                                  │
│  ✓ Анализ возможностей (какие штаты, какие liens)                         │
│  ✓ Печатные документы для Miw (чеклисты, формы)                           │
│  ✓ Roadmap с конкретными датами и действиями                              │
│  ✓ Приоритизация ДРУГИХ SDD: что делать СЕЙЧАС vs что делать ПОТОМ        │
│  ✓ Requirements injection в другие SDD flows                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Problem Statement

### Context

**Семья Антона:**
- **Anton** - отец семейства
- **Vannisa** (Ванниса) - жена Антона, дочь Khun Pho
- **Miw** (18 лет) - старшая дочь Антона и Ваннисы
- **Vasilisa** (Василиса) - младшая дочь (род. 9 августа 2026)

**Beneficiary:** Miw (Miw Dodonova)
- Age: 18 years old
- Relationship: Дочь Anton и Vannisa
- **Preferences:** Нравится Beverly Hills, LA; открыта к Wisconsin

**Partner Context:** Denis (партнёр Miw)
- Age: 31
- Citizenship: **US Citizen**
- Previous business: Реставрация диванов (навыки ремонта!)
- Current: Трейдинг (хотим переориентировать на более осмысленное)
- Family: Large family in **Spearfish, South Dakota** (Lawrence County)
  - **12 siblings** (включая Denis), рождены 1994-2015
  - Порядок: `bbggbgggggbg` (b=boy, g=girl)
  - **4 мальчика, 8 девочек**
  - **Denis - СТАРШИЙ** (первый 'b', ~1994)

**Мотивация Denis:**
> Denis хочет помочь своим 11 младшим siblings найти хорошие дома для их будущих семей.
> Как старший брат, он чувствует ответственность за их будущее.

**Это меняет цель проекта:**
- НЕ "использовать родственников как рабочую силу"
- А "найти доступное жильё для большой семьи"
- Tax liens = способ получить дома по цене ниже рынка
- 11 siblings = потенциально 11 семей, которым нужны дома

**Дополнительные ресурсы:**
- **Khun Pho (Кхун Пхо):** Папа Ваннисы, дедушка Miw и Василисы. Профессиональный строитель, руководил строительством ресторанного комплекса в тайском стиле. **Гражданство: Тайское** - может консультировать по качеству строений удалённо
- **Друзья в Utah:** Rupa и Sudarshan (Shon) - локальная поддержка

**Расширенная цель (Denis's Vision):**
```
┌─────────────────────────────────────────────────────────────────┐
│  DENIS КАК СТАРШИЙ БРАТ                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  11 младших siblings (возраст ~11-30 лет в 2026)               │
│  = 11 будущих семей, которым нужны дома                        │
│                                                                 │
│  Tax Liens Strategy:                                            │
│  • Находить foreclosure properties по низкой цене              │
│  • Оценивать качество (Khun Pho консультирует)                 │
│  • Предлагать siblings варианты доступного жилья               │
│  • Помочь им начать взрослую жизнь с собственным домом         │
│                                                                 │
│  Это НЕ "рабочая сила" - это ЗАБОТА старшего брата             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Investment Goal:**
- Budget: **$1,000** (one-time gift)
- Horizon: Немедленный результат → долгосрочное развитие
- **Primary objective:** Купить реальную недвижимость (землю или строение)
- Secondary objective: Создать базу для будущей семьи Miw и Denis
- Tertiary objective: Помочь Denis перейти от трейдинга к осмысленным инвестициям

### Why Tax Liens for This Situation?

1. **Arizona Connection:** Denis's family is in Arizona - a prime tax lien state with:
   - Up to 16% annual interest rate
   - 3-year redemption period
   - Strong secondary market

2. **Property Acquisition Potential:** Unlike stocks/bonds, tax liens can convert to real property ownership if not redeemed

3. **Educational Value:** Hands-on learning about US real estate investing for Miw's future

4. **Alignment with TAXLIEN.online:** Real user testing of the platform with genuine investment goals

---

## Investment Strategy

### Strategic Options Analysis

| Strategy | Expected Return | Risk | Property Upside | Complexity |
|----------|----------------|------|-----------------|------------|
| A: Arizona-focused liens | 12-16% interest | Low | Medium | Low |
| B: Florida high-volume OTC | 15-18% interest | Low | Low | Low |
| C: Property acquisition focus | Variable | High | High | Medium |
| D: Hybrid (AZ liens + TX deeds) | 10-14% blended | Medium | High | Medium |

### Recommended Strategy: **D - Hybrid Portfolio**

**Rationale:**
1. Denis's Arizona family connection makes AZ liens personally meaningful
2. Mix of income (liens) and property potential (redeemable deeds)
3. $1,000 budget is small - need concentration for impact
4. 3-year horizon aligns with Arizona redemption period

---

## Portfolio Requirements

### FR-1: Budget Allocation

**Total Budget:** $1,000

| Allocation | Amount | Purpose | Target States |
|------------|--------|---------|---------------|
| Primary Liens | $600 (60%) | Interest income + property option | Arizona |
| Secondary Liens | $300 (30%) | Diversification + higher rates | Florida, Iowa |
| Reserve | $100 (10%) | Subsequent taxes + fees | - |

### FR-2: Target Property Criteria

**Arizona Liens (Primary - $600):**
- County preference: Maricopa, Pinal, Pima, Yavapai (near Denis's family area if known)
- Face value: $100-$400 per lien (2-4 liens)
- Value-to-lien ratio: Under 10%
- Property type: Residential (single family, mobile home) or vacant buildable land
- Risk score: Low to Medium-Low
- Redemption probability: 70-85% (balanced approach)

**Florida/Iowa Liens (Secondary - $300):**
- Type: OTC (over-the-counter) only
- Face value: $100-$200 per lien
- Value-to-lien ratio: Under 5%
- Interest rate: Maximum available (18% FL, 24% IA)
- Risk score: Low
- Redemption probability: 85%+ (income focus)

### FR-3: Risk Management

**Position Limits:**
- Maximum single lien: $300 (30% of portfolio)
- Minimum liens in portfolio: 4
- Maximum liens: 8
- Geographic concentration: Max 70% in one state

**Risk Tolerance:**
- Willing to accept 1 failed/problem lien if others perform
- No speculative vacant land without road access
- Avoid environmental risk areas (flood zones, brownfields)

### FR-4: Timeline Expectations

| Phase | Timeline | Expected Outcome |
|-------|----------|------------------|
| Initial Investment | Month 1 | Deploy $900, hold $100 reserve |
| Monitoring | Months 2-12 | Track redemptions, pay subsequent taxes |
| First Redemptions | Months 6-24 | Some Florida liens redeem |
| Arizona Decision Point | Month 36 | AZ liens: redeemed OR begin foreclosure |
| Final Outcome | Year 3-5 | Interest income OR property acquisition |

### FR-5: Success Metrics

**Minimum Success (base case):**
- All liens redeem within redemption period
- Net return: $100-$150 (10-15% on $900 invested)
- No legal costs incurred

**Target Success:**
- 80% of liens redeem with full interest
- 20% of liens (1-2) held past redemption → foreclosure option
- Net return: $150-$200 including one property option

**Exceptional Success:**
- One or more liens convert to property ownership
- Property value > 5x lien investment
- Net value created: $1,000+ (original capital preserved + property)

---

## Integration with TAXLIEN.online

### Platform Testing Value

This investment serves as a real-world beta test:

1. **Search Functionality:** Test filtering for specific criteria
2. **Risk Scores:** Validate ML predictions against real outcomes
3. **Due Diligence Tools:** Verify satellite/parcel data accuracy
4. **Portfolio Tracking:** Test tracking features with real positions
5. **Redemption Alerts:** Test notification system

### Data Collection

Track and document for product improvement:
- Time to find suitable liens
- Accuracy of risk predictions
- User experience friction points
- Missing features identified
- Real vs. predicted outcomes

---

## Acceptance Criteria

### Portfolio Construction

- [ ] Identify 4-8 liens meeting all criteria above
- [ ] Total investment ≤ $900 (keeping $100 reserve)
- [ ] At least 2 liens in Arizona
- [ ] At least 1 lien in Florida or Iowa
- [ ] All liens have value-to-lien ratio under 10%
- [ ] Risk-weighted portfolio score: Low to Medium-Low

### Due Diligence Per Lien

For each recommended lien:
- [ ] Property satellite image reviewed
- [ ] Road access verified
- [ ] Value-to-lien ratio calculated
- [ ] Redemption probability estimated
- [ ] Risk score assigned with explanation
- [ ] Foreclosure process complexity assessed (for AZ)

### Documentation

- [ ] Each lien documented with:
  - Parcel ID, county, state
  - Face value, interest rate
  - Property description
  - Risk assessment
  - Expected outcome (redeem vs. acquire)
  - Action timeline

---

## Legal & Tax Considerations

**For Miw's Records:**

1. **Ownership:** Liens can be purchased in Miw's name (she's 18+)
2. **Tax Implications:** Interest income is taxable; property acquisition has different treatment
3. **State Requirements:** Each state may have registration/investor requirements
4. **Professional Advice:** Recommend consulting CPA for tax filing

**Note:** This SDD provides investment strategy, not legal/tax advice.

---

## Next Steps

1. **SPECIFICATIONS:** Specific lien recommendations with full analysis
2. **PLAN:** Step-by-step purchase and monitoring process
3. **IMPLEMENTATION:** Execute purchases, set up tracking

---

## User Requests Log (Запросы пользователя)

> Этот раздел фиксирует ключевые запросы и уточнения от пользователя.

### Denis Family Details (2026-01-27)

**Источник:** Denis напрямую

**Информация:**
> "12 of us fairly evenly spaced between 1994 and 2015, although not sure the exact year for most of my siblings"
> "The order was bbggbgggggbg"
> "Lots of girls haha"

**Уточнение от пользователя:**
> "Денис - старший. Не рассматривай родных Дениса как ресурс рабочих. Денису интересно помочь своим siblings дать варианты хороших домов для их будущих семей."

**Интерпретация:**
- 12 siblings total (включая Denis)
- 4 мальчика (b), 8 девочек (g)
- Рождены между 1994-2015 (21 год, равномерно)
- **Denis - СТАРШИЙ** (первый 'b', ~1994)
- **Цель Denis:** Помочь 11 младшим siblings найти хорошие дома для их будущих семей
- Tax liens = инструмент для получения доступного жилья

---

### Этический принцип: Ценность ≠ Цена (2026-01-27)

**Запрос:**
> "Оригинал микроскопа Райфа или дисков Сёрла для Антона бесценны, они уникальны, потому что Антон сам изобретатель. Не нужно их оценивать с точки зрения денег, чтобы в будущем модель ML не ошибалась, чтобы люди не наживались, и было этично. А те кому что-то реально надо могли получить именно для себя, что ценно им, а что другим не ценно. Не поощряем спекуляцию на уникальности."

**Результат:**
- Добавлен этический принцип в FVI/ИПП: ЦЕННОСТЬ ≠ ЦЕНА
- ML должна матчить вещи с людьми по РЕАЛЬНОЙ ценности
- НЕ помогать спекулянтам находить редкости
- Уникальные вещи → тем, кому они РЕАЛЬНО нужны

**Plan v5.0 APPROVED**

---

### Уточнение про ОРИГИНАЛЫ и NO CODING (2026-01-27)

**Запрос:**
> "Не просто катушка Теслы в гараже, а именно ОРИГИНАЛЬНАЯ КАТУШКА ТЕСЛЫ, либо человек должен был быть лично с ним знаком. Просто хлам из современных катушек Теслы и разгребание идей гениев текущего времени Антону не интересно."
>
> "В плане - только доработка других sdd flows - именно требований, спецификаций и приоритезация планов. Никакого кодинга в sdd-miw-gift."

**Результат:**
1. Уточнено: Anton интересуют ТОЛЬКО ОРИГИНАЛЫ изобретений:
   - Приборы, сделанные лично изобретателями
   - Вещи от людей, лично знавших изобретателей
   - Документы с провенансом
   - ❌ НЕ современные реплики

2. Напоминание: sdd-miw-gift = КОМПАС
   - ✅ Доработка requirements ДРУГИХ SDD
   - ✅ Доработка specifications ДРУГИХ SDD
   - ✅ Приоритизация планов ДРУГИХ SDD
   - ❌ НИКАКОГО КОДИНГА в sdd-miw-gift

---

### Expert Annotation для Deal Detective (2026-01-27)

**Запрос:**
> "Knun Pho профессиональный строитель и он может на фотографиях подсказывать ИИ детали. Он может обводить области, ставить точки, линии и кривые, чтобы сфокусировать attention на конкретных деталях - например перекошенная крыша или качественный фундамент. Denis может указывать на интересные предметы мебели для реставрации. Anton может указать на интересный кузов от ретро автомобиля. Так же Антону интересны научные изобретения (Аппарат Райфа, микроскоп Райфа, аппарат Арнольда Лаховского, диск Сёрла, изобретения Теслы)."

**Результат:**
- Добавлен раздел "Expert Network & x1000 Opportunities"
- Профили экспертов: Knun Pho (строительство), Denis (мебель), Anton (авто + science)
- Концепция annotation tools для обучения AI
- Приоритеты для sdd-taxlien-ml моделей x1000 detection

---

### Как работает sdd-miw-gift (2026-01-27)

**Запрос:**
> "sdd-miw-gift работает посредством выстраивания правильной документации и следованию пути для достижения цели Miw наибыстрым способом, добавляя в те спецификации фишки и пояснения и меняя порядок их следования и приоритезацию чтобы их roadmap шел в соответствии с кратчайшим пути для достижения цели Miw."

**Уточнение:**
> "Выстраивание пути именно В ОСТАЛЬНЫХ SDD, ориентируясь на sdd-miw-gift"

**Интерпретация:**
- sdd-miw-gift = **КОМПАС** для других SDD flows
- Цель: кратчайший путь к цели Miw через управление ДРУГИМИ SDD
- Метод: изменение приоритетов в parser, gateway, ML ориентируясь на Miw's goals
- sdd-miw-gift НЕ содержит код, но НАПРАВЛЯЕТ код в других SDD

### Терминология (2026-01-27)

**Запрос:**
> "x1000 - не про no heirs, x1000 - это про уникальный антиквариат мирового уровня"

**Результат:**
- **Foreclosure Score** = no heirs → guaranteed foreclosure
- **x1000 Score** = world-class antique potential (×1000 multiplier)

### Два инвестора (2026-01-25)

**Запрос:**
> "Miw lien расчетом просто на процент с малым бюджетом нужно купить только 1, для опыта не дороже 150$. Shon - отдельный инвестор, консервативный."

**Результат:**
- Miw: $150 (1 lien для опыта) + $850 (foreclosures)
- Shon: $200-$2000 × 3 liens, выбирает сам из списка 10-15

### Denis Family Advantage (2026-01-25)

**Запрос:**
> "Фишка семьи Дениса в том, что они могут посмотреть недвижку до покупки."

**Результат:**
- Physical inspection before buying = competitive advantage
- Denis Family Inspection Checklist добавлен в specifications

---

## Expert Network & x1000 Opportunities (2026-01-27)

### Концепция: Коллаборативная Annotation Платформа

> **Идея:** Эксперты обучают ИИ видеть ценное через аннотации на фотографиях.
> Это развитие Deal Detective: не просто swipe, а **экспертный анализ с разметкой**.

**Инструменты разметки:**
- Обводка областей (области внимания)
- Точки (конкретные детали)
- Линии (указатели, размеры)
- Кривые (контуры, формы)
- Комментарии к каждой разметке

**Цель:** Фокусировать attention ИИ на конкретных деталях, которые видит эксперт.

---

### Expert Profiles & Interests

### Семья

```
┌─────────────────────────────────────────────────────────────────┐
│  СЕМЕЙНОЕ ДРЕВО                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Khun Pho ─┬─ (жена)                                           │
│            │                                                    │
│            └── Vannisa (дочь Khun Pho)                         │
│                    │                                            │
│                    ├─── married to ─── Anton                   │
│                    │                                            │
│                    └── Дети:                                    │
│                        ├── Miw (18 лет)                        │
│                        │   └── Partner: Denis (31, US Citizen) │
│                        │                                        │
│                        └── Vasilisa (род. 9 августа 2026)      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

#### 🏗️ Khun Pho (Папа Ваннисы, дедушка Miw и Василисы)
**Экспертиза:** Профессиональный строитель
**Опыт:** Руководил строительством ресторанного комплекса в тайском стиле
**Гражданство:** Тайское (координация удалённо)

**Может указать на фото:**
- ✅ Качественный фундамент
- ⚠️ Перекошенная крыша
- ⚠️ Трещины в стенах
- ✅ Хорошая кладка
- ⚠️ Проблемы с дренажом
- ✅ Качество окон/дверей
- ⚠️ Признаки затопления
- ✅ Состояние кровли

**x1000 категория:** Редкие архитектурные элементы, handcrafted детали

---

#### 🛋️ Denis (Партнёр Miw)
**Экспертиза:** Реставрация мебели (диваны)
**Опыт:** Бывший бизнес по реставрации диванов
**Гражданство:** US Citizen

**Может указать на фото:**
- Антикварная мебель для реставрации
- Ценные предметы интерьера
- Vintage furniture с потенциалом
- Редкие материалы (дерево, ткани)
- Дизайнерские предметы

**x1000 категория:**
- Mid-century modern furniture
- Victorian era pieces
- Art Deco furniture
- Rare wood types (walnut, mahogany)
- Designer pieces (Eames, Knoll, Herman Miller)

---

#### 🚗 Anton (Папа Miw и Василисы, муж Ваннисы)
**Экспертиза:** Технологии, научные изобретения, ретро автомобили, антикварная живопись
**Интересы:** Редкие технологические артефакты, классическое искусство

**Может указать на фото:**
- Кузова ретро автомобилей для реставрации
- Vintage технологическое оборудование
- Научные приборы
- Редкие механизмы
- Антикварные картины и живопись

**x1000 категории:**

**Ретро автомобили:**
- Кузова классических американских авто (1950s-1970s)
- Muscle cars (Mustang, Camaro, Challenger)
- Classic trucks (Ford F-series, Chevy C10)
- European classics (Porsche, Mercedes, Jaguar)

**Антикварная живопись:**
- 🎨 Картины старых мастеров (Old Masters)
- 🎨 Импрессионисты
- 🎨 Русская живопись XIX века
- 🎨 Иконы
- 🎨 Портреты и пейзажи с провенансом
- 🎨 Работы известных художников в запущенном состоянии (требуют реставрации)

**Научные изобретения (крайне редкие!):**

> ⚠️ **ВАЖНО:** Антону интересны ТОЛЬКО ОРИГИНАЛЫ и личные связи с изобретателями.
> Современные реплики и "разгребание идей гениев текущего времени" НЕ интересны.

- 🔬 **Аппарат Райфа (Rife Machine)** - ОРИГИНАЛ от Royal Rife или его ассистентов
- 🔬 **Микроскоп Райфа (Rife Microscope)** - ОРИГИНАЛ (уникальная оптика)
- ⚡ **Аппарат Арнольда Лаховского (Lakhovsky MWO)** - ОРИГИНАЛ 1920-1940х
- 🛸 **Диск Сёрла (Searl Effect Generator)** - ОРИГИНАЛ от John Searl
- ⚡ **Изобретения Теслы** - ТОЛЬКО ОРИГИНАЛЫ:
  - Приборы, сделанные лично Теслой
  - Приборы от людей, лично знавших Теслу
  - Документы, письма, чертежи с подписью Теслы
  - ❌ НЕ современные реплики катушек Теслы
  - ❌ НЕ "вдохновлённые Теслой" поделки

**Критерий:** Владелец property должен был:
- Лично знать изобретателя, ИЛИ
- Быть наследником изобретателя, ИЛИ
- Быть коллекционером с задокументированным провенансом

**Почему это x1000:**
- Эти устройства практически невозможно найти
- ОРИГИНАЛЫ стоят от $50K до $1M+
- Часто находятся в заброшенных лабораториях, гаражах учёных
- Tax lien на property умершего изобретателя/коллекционера = jackpot
- Картины в заброшенных домах могут оказаться работами известных мастеров

---

#### 🧸 Vasilisa (Дочь Антона и Ваннисы)
**Дата рождения:** 9 августа 2026
**Статус:** Младшая сестра Miw

**Интересы (будущий эксперт):**
- 🧸 Антикварные игрушки

**x1000 категории:**

**Антикварные игрушки:**
- 🧸 Куклы Jumeau, Bru, Kestner (Франция, Германия, XIX век)
- 🧸 Steiff плюшевые игрушки (особенно ранние медведи)
- 🧸 Механические игрушки (автоматоны)
- 🧸 Tin toys (жестяные игрушки, 1900-1960s)
- 🧸 Немецкие ёлочные игрушки (Lauscha glass)
- 🧸 Советские игрушки (редкие серии)
- 🧸 Кукольные домики с мебелью
- 🧸 Игрушечные поезда (Märklin, Lionel)

**Почему это x1000:**
- Редкие куклы XIX века: $10K - $300K+
- Steiff teddy bears первых выпусков: $50K+
- Автоматоны: $100K+
- Часто хранятся на чердаках, в подвалах заброшенных домов
- Владельцы (пожилые люди) не осознают ценность

---

### Как это работает в Deal Detective

```
┌─────────────────────────────────────────────────────────────────┐
│  DEAL DETECTIVE + EXPERT ANNOTATION                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. User swipes property card                                   │
│  2. Видит что-то интересное → нажимает "Annotate"              │
│  3. Открывается режим разметки:                                 │
│     ┌────────────────────────────────┐                          │
│     │  [Photo of property]           │                          │
│     │                                │                          │
│     │    ○ ← точка: "crooked beam"   │                          │
│     │   ╭─╮                          │                          │
│     │   │ │ ← область: "vintage car" │                          │
│     │   ╰─╯                          │                          │
│     │    ─── ← линия: "crack"        │                          │
│     │                                │                          │
│     └────────────────────────────────┘                          │
│  4. Эксперт добавляет комментарии                               │
│  5. AI обучается на аннотациях                                  │
│  6. Со временем AI сам находит такие детали                     │
│                                                                 │
│  РЕЗУЛЬТАТ: Краудсорсинговое обучение x1000 детектора          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### Training Data от экспертов

| Эксперт | Категория | Пример аннотации |
|---------|-----------|------------------|
| Khun Pho | Construction | "Фундамент просел на 2 дюйма справа" |
| Denis | Furniture | "Это Eames Lounge Chair 1956 года!" |
| Anton | Vintage Cars | "Кузов Ford Mustang 1967 Fastback" |
| Anton | Scientific | "Это похоже на катушку Теслы" |
| Anton | Paintings | "Это может быть работа Айвазовского!" |
| Vasilisa | Toys | "Steiff медведь с пуговицей в ухе!" |

**ML Pipeline:**
```
Expert annotation → Labeled training data → YOLO/object detection → Auto-detection
```

---

### Приоритет для sdd-taxlien-ml

Модели для x1000 detection:

| Model | Input | Output | Priority | Эксперт |
|-------|-------|--------|----------|---------|
| Construction Defect Detector | Photo | Defects list + severity | P1 | Khun Pho |
| Antique Furniture Detector | Photo | Furniture type + estimated value | P2 | Denis |
| Vintage Car Detector | Photo | Make/model/year + condition | P2 | Anton |
| Antique Painting Detector | Photo | Style/era/artist hints | P2 | Anton |
| Antique Toy Detector | Photo | Toy type/era/maker | P3 | Vasilisa |
| Scientific Equipment Detector | Photo | Device type + rarity | P3 | Anton |

**Constraint:** Все модели self-hosted (YOLO, не OpenAI Vision)

---

## sdd-taxlien-swipe-app (Планируемый перенос)

> **ВАЖНО:** Это НЕ новый код. Это план ПЕРЕНОСА существующего кода и спецификаций
> из `sdd-taxlien-flutter-app/lib/features/deal_detective/` в отдельное приложение.

### Существующий код для переноса

```
taxlien-flutter-app/lib/features/deal_detective/
├── screens/
│   ├── deal_detective_screen.dart      # Главный экран со стеком карточек
│   └── detective_preferences_screen.dart
├── widgets/
│   ├── swipeable_property_card.dart    # Свайп-карточка с анимацией
│   ├── action_buttons.dart             # Pass/Like/SuperLike/Undo
│   ├── match_notification_modal.dart   # "It's a Match!"
│   ├── share_property_sheet.dart       # Поделиться
│   └── detective_tutorial.dart         # Onboarding
├── services/
│   ├── match_service.dart              # Логика матчинга
│   ├── daily_limit_service.dart        # Free/Paid лимиты
│   └── share_service.dart
├── models/
│   ├── user_preferences.dart
│   └── match.dart
└── constants/
    └── detective_constants.dart        # Все настройки
```

---

### Новая механика свайпа (для обсуждения)

**Текущая (Tinder-style):**
```
← Pass    ↑ SuperLike    → Like
```

**Предлагаемая (Multi-dimensional):**

```
                    ↑
              Следующий вариант
                    │
    ←───────────────┼───────────────→
    Контекст        │           Детали
    (статьи,        │         (интерьер,
    obituaries)     │          фото)
                    │
                    ↓
              Предыдущий вариант
```

**Проблема:** Левый свайп (контекст) не для всех актуален:
- ✅ Anton: газетные статьи про учёных, obituaries
- ❌ Denis: не интересны газеты
- ❌ Miw: не интересны газеты
- ❌ Khun Pho: не интересны газеты

---

### Альтернативная механика: Profile-Based Marking

> **Идея:** Каждый эксперт помечает ТО, ЧТО ИНТЕРЕСНО ЕМУ в своём профиле.
> AI обучается на этих разметках и подбирает варианты всё лучше.

```
┌─────────────────────────────────────────────────────────────────┐
│  PROFILE-BASED LEARNING                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Khun Pho смотрит фото и помечает:                             │
│  • "Хороший фундамент" ✅ / "Плохой фундамент" ❌               │
│  • "Крыша в порядке" ✅ / "Крыша перекошена" ❌                 │
│  → AI учится: что Khun Pho считает хорошим/плохим              │
│                                                                 │
│  Denis смотрит фото интерьера и помечает:                      │
│  • "Интересный диван для реставрации" ⭐                        │
│  • "Ценная мебель" ⭐                                           │
│  → AI учится: что Denis считает ценным                         │
│                                                                 │
│  Miw смотрит общий вид и помечает:                             │
│  • "Нравится дизайн" 💚                                         │
│  • "Красивая лужайка" 💚                                        │
│  • "Хорошие соседи/район" 💚                                    │
│  • "Некрасивый забор" 💔                                        │
│  → AI учится: эстетические предпочтения Miw                    │
│                                                                 │
│  Anton смотрит контекст и помечает:                            │
│  • "Интересная история владельца" 📰                            │
│  • "Возможно редкое оборудование" 🔬                            │
│  → AI учится: что Anton ищет                                   │
│                                                                 │
│  ═══════════════════════════════════════════════════════════   │
│                                                                 │
│  AI КОМБИНИРУЕТ ВСЕ ПРОФИЛИ:                                   │
│  Property Score = f(Khun Pho, Denis, Miw, Anton, ...)          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### Метрика: FVI / ИПП

> **FVI** = Family Value Index (English)
> **ИПП** = Индекс Полной Пользы (Russian)

---

### ⚠️ ЭТИЧЕСКИЙ ПРИНЦИП: Не поощряем спекуляцию

> **Anton - изобретатель.** Оригинал микроскопа Райфа или дисков Сёрла для него БЕСЦЕННЫ.
> Не потому что они дорогие, а потому что они уникальны и важны ему лично.

```
┌─────────────────────────────────────────────────────────────────┐
│  ПРИНЦИП FVI/ИПП: ЦЕННОСТЬ ≠ ЦЕНА                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ❌ НЕ ПООЩРЯЕМ:                                                │
│  • Спекуляцию на уникальности                                   │
│  • Оценку всего в деньгах                                       │
│  • Перепродажу ради наживы                                      │
│                                                                 │
│  ✅ ПООЩРЯЕМ:                                                   │
│  • Вещь попадает к тому, кому она РЕАЛЬНО нужна                │
│  • То, что ценно одному - может быть не ценно другому          │
│  • Этичное распределение уникальных предметов                  │
│                                                                 │
│  ПРИМЕР:                                                        │
│  • Микроскоп Райфа → Anton (изобретатель) = БЕСЦЕННО           │
│  • Микроскоп Райфа → спекулянт = просто $$$, неэтично          │
│                                                                 │
│  ML МОДЕЛЬ ДОЛЖНА:                                              │
│  • Матчить вещи с людьми по РЕАЛЬНОЙ ценности для них          │
│  • НЕ максимизировать денежную оценку                          │
│  • НЕ помогать спекулянтам находить редкости                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Для sdd-taxlien-ml:** Модели должны учитывать профиль пользователя и показывать уникальные предметы тем, кому они реально ценны, а не всем подряд.

---

**Принцип:** Не ограничиваем экспертов одним измерением!
- Anton может заметить и мебель, и машину, и научный прибор, и красивый вид
- Khun Pho может оценить и фундамент, и интересный автомобиль в гараже
- Denis может отметить и диван, и качество постройки
- Miw может увидеть и дизайн, и антикварную куклу

**Каждый размечает ВСЁ, что видит интересного.**

```
FVI/ИПП = (Financial Value + Σ Personal Values) / Cost

Personal Values = всё, что отметили ВСЕ эксперты
                  без ограничения по категориям
```

---

### UX Best Practices для разметки

**Вдохновение от успешных приложений:**

| App | Что делает хорошо | Применяем |
|-----|-------------------|-----------|
| **Pinterest** | Визуальное discovery, сохранение в boards | Коллекции по интересам |
| **Tinder** | Простой бинарный выбор | Базовый swipe |
| **Instagram** | Double-tap = like, долгое нажатие = save | Быстрые жесты |
| **Google Photos** | Учится распознавать лица, места | AI учится на разметке |
| **Spotify** | Учится на поведении (не только лайках) | Implicit learning |
| **Are.na** | Свободная организация контента | Гибкие категории |

---

### UX Принципы для Swipe App

#### 1. Простота входа (Progressive Disclosure)

```
Level 1: Просто свайп (нравится/не нравится)
         ↓
Level 2: Tap на фото → zoom + можно поставить точку
         ↓
Level 3: Long press → меню разметки (область, линия, комментарий)
         ↓
Level 4: Expert mode → полный набор инструментов
```

#### 2. Жесты без категорий

```
┌─────────────────────────────────────────────────────────────────┐
│  НЕ ЗАСТАВЛЯЕМ ВЫБИРАТЬ КАТЕГОРИЮ                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ❌ Плохо: "Выберите тип: Мебель / Авто / Строительство"       │
│                                                                 │
│  ✅ Хорошо: Просто тапни на интересное                         │
│            AI сам поймёт категорию по контексту                │
│            и по истории разметок этого пользователя            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### 3. Implicit Learning (учимся на поведении)

```
Явные сигналы:              Неявные сигналы:
• Tap/mark на объекте       • Время просмотра фото
• Свайп вправо (like)       • Zoom на область
• Комментарий               • Возврат к просмотренному
• Добавление в коллекцию    • Скорость пролистывания
                            • Какие фото открывает в галерее
```

#### 4. Feedback Loop (показываем что AI учится)

```
┌─────────────────────────────────────────────────────────────────┐
│  "Anton, мы заметили что тебе интересны:"                      │
│                                                                 │
│  🚗 Ретро автомобили (12 отметок)                              │
│  🔬 Научное оборудование (8 отметок)                           │
│  🎨 Картины (5 отметок)                                        │
│  🏠 Качество постройки (3 отметки)  ← новое!                   │
│                                                                 │
│  [Показывать больше таких?]  [Да] [Нет] [Настроить]           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### 5. Коллективный просмотр (Family Mode)

```
┌─────────────────────────────────────────────────────────────────┐
│  FAMILY MODE: Все смотрят одно property                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [Photo of property with overlay marks]                        │
│                                                                 │
│     🔵 Khun Pho отметил: "Хороший фундамент"                   │
│     🟢 Denis отметил: "Интересный комод!"                      │
│     🟡 Miw отметила: "Красивый двор"                           │
│     🔴 Anton отметил: "Это же ОРИГИНАЛЬНАЯ катушка Теслы в гараже!"        │
│                                                                 │
│  Combined FVI/ИПП: 9.2 ⭐⭐⭐⭐⭐                                │
│                                                                 │
│  [Обсудить] [Добавить в шорт-лист] [Пропустить]               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### 6. Быстрые действия (Quick Actions)

```
Жест                    Действие
─────────────────────────────────────
Tap                     Отметить интересное (точка)
Double-tap              Quick like ❤️
Long press              Меню (область, комментарий, share)
Pinch zoom              Рассмотреть детали
Swipe up                Следующее property
Swipe down              Предыдущее property
Swipe right             Like + в коллекцию
Swipe left              Pass
Two-finger tap          Переключить фото (экстерьер/интерьер)
```

#### 7. Разметка без трения

```
┌─────────────────────────────────────────────────────────────────┐
│  МИНИМУМ ШАГОВ ДЛЯ РАЗМЕТКИ                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1 tap = отметка "интересно" (AI сам определит что)            │
│                                                                 │
│  Опционально (если хочет уточнить):                            │
│  • Голосовой комментарий (1 кнопка → говори)                   │
│  • Текст (появляется клавиатура)                               │
│  • Emoji реакция (👍 👎 ❤️ 🔥 💎 🏠 🚗 🎨)                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### Пример FVI/ИПП в действии

```
Property: 123 Oak Street, Phoenix, AZ
Lien Amount: $500
Assessed Value: $85,000

═══ FINANCIAL ═══
Expected ROI: 16% ($80)
Foreclosure probability: 35%
Financial Score: 6.5/10

═══ FAMILY MARKS ═══
Khun Pho (3 marks):
  • "Фундамент solid" (+2)
  • "Крыша нужен ремонт" (-1)
  • "Гараж хороший" (+1)
  → Khun Pho Score: 7/10

Denis (2 marks):
  • "Винтажный буфет!" (+3)
  • "Кресло для реставрации" (+2)
  → Denis Score: 9/10

Miw (4 marks):
  • "Симпатичный двор" (+2)
  • "Соседи ок" (+1)
  • "Далеко от центра" (-1)
  • "Нравится цвет дома" (+1)
  → Miw Score: 7.5/10

Anton (1 mark):
  • "В гараже старый Ford Mustang!!!" (+5)
  → Anton Score: 10/10

═══ COMBINED FVI/ИПП ═══

FVI = (Financial + Khun Pho + Denis + Miw + Anton) / 5
    = (6.5 + 7 + 9 + 7.5 + 10) / 5
    = 8.0 ⭐⭐⭐⭐

Recommendation: ВЫСОКИЙ ПРИОРИТЕТ
Причина: Mustang в гараже может стоить больше чем весь lien!
```
