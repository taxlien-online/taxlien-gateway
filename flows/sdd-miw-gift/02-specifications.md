# Specifications: Miw's Property Acquisition Plan

**Version:** 3.1 (NO PAID APIs constraint)
**Status:** ✅ APPROVED
**Last Updated:** 2026-01-27
**Approved:** 2026-01-27
**Primary Goal:** Приобретение недвижимости для Miw

---

## Бюджетное ограничение

| Сторона | Вклад | Примечание |
|---------|-------|------------|
| **Российско-Тайская** | **$1,000 MAX** | Больше накопить не смогут |
| Американская (Denis) | TBD | Возможен дополнительный вклад |

**Вывод:** Стратегия должна работать с $1,000. Варианты дороже $1,000 показаны для понимания картины.

---

## ⚠️ Техническое ограничение: NO PAID APIs

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  СИСТЕМНОЕ ОГРАНИЧЕНИЕ                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. НЕТ БЮДЖЕТА на оплату внешних сервисов                                 │
│  2. Качество внешних сервисов МОЖЕТ МЕНЯТЬСЯ                               │
│  3. Нельзя полагаться на внешние зависимости                               │
│                                                                             │
│  ЗАПРЕЩЕНО:                        РАЗРЕШЕНО:                               │
│  ✗ OpenAI API                      ✓ Self-hosted LLM (Llama, etc.)         │
│  ✗ Google Vision API               ✓ Tesseract / TrOCR (local)             │
│  ✗ Google Places API               ✓ OpenStreetMap (free)                  │
│  ✗ WalkScore API                   ✓ Census Bureau (free)                  │
│  ✗ Любые платные API               ✓ County GIS portals (free)             │
│                                    ✓ FEMA data (free)                       │
│                                    ✓ FBI UCR (free)                         │
│                                                                             │
│  Принцип: Если данные не бесплатны и не self-hosted — не используем.       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ДВА ИНВЕСТОРА: Miw vs Shon (v4.0)

### Разные цели — разные стратегии

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  INVESTOR 1: MIW                         INVESTOR 2: SHON                   │
│  ══════════════════                      ═══════════════                    │
│                                                                             │
│  Цель: FORECLOSURE → PROPERTY            Цель: GUARANTEED INTEREST          │
│  Риск: АГРЕССИВНЫЙ                       Риск: КОНСЕРВАТИВНЫЙ               │
│  Бюджет: $1,000 total                    Бюджет: $200-$2,000 × 3 liens      │
│                                                                             │
│  Распределение:                          Что нужно:                         │
│  • $150 = 1 lien (опыт)             • СПИСОК из 10-15 вариантов        │
│  • $850 = foreclosures                   • Сам выберет 3 лучших            │
│                                          • Prefer OTC (без аукциона)        │
│                                                                             │
│  Метрика успеха:                         Метрика успеха:                    │
│  • Множитель при перепродаже            • Гарантированный % (16-18%)        │
│  • Скорость продажи                      • Минимальный риск                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## MIW: Стратегия Foreclosures ($850)

### Вопрос: Сколько объектов можно купить за $850?

| Тип property | Цена range | Сколько за $850 | Множитель | Ликвидность |
|--------------|------------|-----------------|-----------|-------------|
| **OTC Tax Deed (rural lot)** | $100-$500 | 1-8 шт | 5-20x | LOW |
| **OTC Tax Deed (cheap house)** | $500-$2,000 | 0-1 шт | 3-10x | MEDIUM |
| **Auction Tax Deed (lot)** | $200-$1,000 | 1-4 шт | 3-15x | LOW-MEDIUM |
| **Auction Tax Deed (house)** | $1,000-$5,000 | 0-1 шт | 2-5x | MEDIUM-HIGH |

### Рекомендация для Miw: Фокус на OTC Tax Deeds

**Почему OTC лучше для $850:**
- Нет конкуренции на аукционе
- Фиксированная цена (можно планировать)
- Часто дешевле (никто не набивает цену)
- Можно купить НЕСКОЛЬКО cheap lots

### Сценарий A: Максимум объектов (diversification)

```
$850 бюджет
├── $200 - OTC lot #1 (Arizona) → Value $2,000 = 10x
├── $200 - OTC lot #2 (Arizona) → Value $1,500 = 7.5x
├── $200 - OTC lot #3 (Utah)    → Value $3,000 = 15x
└── $250 - OTC lot #4 (Texas)   → Value $1,800 = 7.2x
                                 ─────────────────────
Total invested: $850            → Total value: $8,300
                                → Average multiplier: 9.8x
```

**Плюсы:** Diversification, если один не продастся — остальные компенсируют
**Минусы:** Много мелких сделок, low liquidity (rural lots)

### Сценарий B: Один качественный объект

```
$850 бюджет
└── $850 - OTC house (needs work) → ARV $15,000 = 17.6x
                                   → After $2,000 reno = $12,150 profit
```

**Плюсы:** Один объект проще управлять, house = выше ликвидность
**Минусы:** Всё в одном месте, нужен дополнительный бюджет на ремонт

### Сценарий C: РЕКОМЕНДУЕМЫЙ (баланс)

```
$850 бюджет
├── $350 - OTC lot (good location)  → Value $3,500 = 10x
└── $500 - OTC cheap structure      → Value $8,000 = 16x
                                     ─────────────────────
Total invested: $850               → Total value: $11,500
                                   → Blended multiplier: 13.5x
```

**Почему лучший:**
- 2 объекта = diversification
- Один lot (easy sell) + один structure (higher value)
- Manageable количество

### Где искать OTC Foreclosures для Miw

| Штат | OTC Available? | Минимум | Где смотреть |
|------|----------------|---------|--------------|
| **Arizona** | ✅ Yes | $50+ | County Treasurer websites |
| **Texas** | ✅ Yes (Struck-off) | $100+ | County Tax Office |
| **Florida** | ⚠️ Limited | $200+ | County Tax Collector |
| **Utah** | ❌ No OTC | N/A | Auction only |
| **South Dakota** | ❌ No OTC | N/A | Auction only (Dec) |

### Критерии отбора для Miw (Foreclosures)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              MIW'S FORECLOSURE SELECTION CRITERIA                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  MUST HAVE:                                                                 │
│  ✓ Price ≤ $500 (чтобы купить 2+)                                          │
│  ✓ Clear title (no other liens)                                            │
│  ✓ Road access (paved or maintained dirt)                                  │
│  ✓ Not in flood zone                                                       │
│                                                                             │
│  NICE TO HAVE (higher multiplier):                                         │
│  ○ Near growing area (appreciation)                                        │
│  ○ Utilities available (or nearby)                                         │
│  ○ Buildable lot (not landlocked)                                          │
│  ○ Recent comparable sales (proves demand)                                 │
│                                                                             │
│  AVOID:                                                                     │
│  ✗ Landlocked parcels                                                      │
│  ✗ No road access                                                          │
│  ✗ Environmental issues                                                    │
│  ✗ HOA with back dues                                                      │
│  ✗ IRS liens                                                               │
│                                                                             │
│  TARGET MULTIPLIER: 10x or higher                                          │
│  TARGET TIMELINE: Sell within 6-12 months                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## MIW: Обучающий Lien ($150)

**Цель:** Только опыт, не ROI

| Параметр | Значение |
|----------|----------|
| Бюджет | $150 max |
| Количество | 1 lien |
| Штат | Arizona (16%) или Florida (18%) |
| Тип | OTC (проще) |
| Ожидание | Скорее всего redemption → $150 + 16-18% = $174-177 |

**Почему только один:**
- Liens = медленный путь (3+ года до foreclosure)
- Не приближает к цели (property ownership)
- Только для понимания процесса

---

## SHON: Консервативная стратегия (3 liens)

### Профиль Shon

| Параметр | Значение |
|----------|----------|
| Бюджет per lien | $200 - $2,000 |
| Количество | 3 liens |
| Общий бюджет | $600 - $6,000 |
| Цель | Гарантированный процент |
| Риск | КОНСЕРВАТИВНЫЙ |
| Предпочтение | OTC (без аукциона) |

### Вопрос: Сколько вариантов показать Shon?

**Рекомендация: 10-15 вариантов**

| Показать | Почему |
|----------|--------|
| < 5 | Слишком мало выбора |
| 5-9 | Минимум, но ограничивает |
| **10-15** | ✅ Оптимально (3x-5x от нужного количества) |
| > 15 | Overwhelm, сложно выбрать |

### Критерии для Shon (КОНСЕРВАТИВНЫЕ)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              SHON'S CONSERVATIVE LIEN CRITERIA                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  MUST HAVE (гарантия redemption):                                          │
│  ✓ Redemption probability > 85%                                            │
│  ✓ Property with STRUCTURE (not vacant lot)                                │
│  ✓ Owner-occupied OR active rental                                         │
│  ✓ Homestead exemption = GOOD (owner will pay!)                            │
│  ✓ Prior payment history = consistent                                      │
│  ✓ Lien amount $200-$2,000                                                 │
│                                                                             │
│  NICE TO HAVE:                                                              │
│  ○ High assessed value (owner has equity to protect)                       │
│  ○ Low lien-to-value ratio (< 5%)                                          │
│  ○ First-time delinquency (temporary hardship)                             │
│  ○ Urban/suburban location (stable area)                                   │
│                                                                             │
│  AVOID (too risky for conservative):                                        │
│  ✗ Vacant land (may not redeem)                                            │
│  ✗ Abandoned properties                                                    │
│  ✗ Serial non-payers (multiple years delinquent)                           │
│  ✗ Dissolved LLC owners                                                    │
│  ✗ Low-value properties (not worth redeeming)                              │
│                                                                             │
│  EXPECTED OUTCOME:                                                          │
│  • 90%+ probability: Redemption with 16-18% interest                       │
│  • 10% probability: Foreclosure (bonus!)                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### OTC Sweet Spots для Shon

**Почему OTC лучше для Shon:**
- Не нужно торговаться на аукционе
- Фиксированная цена = предсказуемый ROI
- Меньше работы (buy and wait)
- Можно выбирать в своём темпе

| Штат | OTC Liens | Interest | Типичный range | Redemption Rate |
|------|-----------|----------|----------------|-----------------|
| **Arizona** | ✅ Yes | 16% | $100-$5,000 | 95%+ |
| **Florida** | ✅ Yes | 18% | $200-$10,000 | 90%+ |
| **Illinois** | ⚠️ Limited | 18-36% | $500-$20,000 | 85%+ |

### Шаблон списка для Shon (10-15 вариантов)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SHON'S SELECTION LIST (Example)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  #  │ Parcel        │ County    │ Lien $   │ Value    │ Ratio │ Redeem %  │
│  ───┼───────────────┼───────────┼──────────┼──────────┼───────┼───────────│
│  1  │ 123-45-678    │ Maricopa  │ $450     │ $125,000 │ 0.4%  │ 96%  ⭐   │
│  2  │ 234-56-789    │ Pinal     │ $380     │ $89,000  │ 0.4%  │ 94%  ⭐   │
│  3  │ 345-67-890    │ Maricopa  │ $1,200   │ $245,000 │ 0.5%  │ 97%  ⭐   │
│  4  │ 456-78-901    │ Yavapai   │ $620     │ $156,000 │ 0.4%  │ 93%       │
│  5  │ 567-89-012    │ Pima      │ $890     │ $178,000 │ 0.5%  │ 95%  ⭐   │
│  6  │ 678-90-123    │ Coconino  │ $1,450   │ $312,000 │ 0.5%  │ 96%  ⭐   │
│  7  │ 789-01-234    │ Maricopa  │ $280     │ $92,000  │ 0.3%  │ 94%       │
│  8  │ 890-12-345    │ Pinal     │ $1,890   │ $267,000 │ 0.7%  │ 92%       │
│  9  │ 901-23-456    │ Yavapai   │ $540     │ $134,000 │ 0.4%  │ 95%  ⭐   │
│  10 │ 012-34-567    │ Pima      │ $720     │ $189,000 │ 0.4%  │ 94%       │
│  11 │ 123-45-678B   │ Maricopa  │ $1,100   │ $198,000 │ 0.6%  │ 93%       │
│  12 │ 234-56-789B   │ Cochise   │ $350     │ $78,000  │ 0.4%  │ 91%       │
│                                                                             │
│  ⭐ = Recommended (highest redemption probability + good ratio)            │
│                                                                             │
│  Shon's task: Choose 3 from this list                                      │
│  Expected return: 16% per year (Arizona)                                   │
│  Expected timeline: Redemption within 6-18 months                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Ожидаемый результат для Shon

| Если вложит | После 1 года (16%) | Риск |
|-------------|-------------------|------|
| $600 (3 × $200) | $696 (+$96) | Very Low |
| $1,500 (3 × $500) | $1,740 (+$240) | Very Low |
| $3,000 (3 × $1,000) | $3,480 (+$480) | Very Low |
| $6,000 (3 × $2,000) | $6,960 (+$960) | Very Low |

---

## Сравнение: Miw vs Shon

| | **Miw** | **Shon** |
|---|---|---|
| **Цель** | Property ownership | Passive income |
| **Риск** | High (foreclosure hunting) | Low (redemption expected) |
| **Бюджет** | $1,000 total | $600-$6,000 total |
| **Тип покупки** | Tax DEEDS (foreclosures) | Tax LIENS (interest) |
| **Количество** | 2-4 cheap properties | 3 liens |
| **Ожидаемый ROI** | 500-2000% (if sells) | 16-18% guaranteed |
| **Timeline** | 6-12 months (sell) | 6-18 months (redemption) |
| **Работа** | Active (find buyers, manage) | Passive (wait for payment) |
| **Karma Score** | Важен (ethical) | Не важен |

---

## Важное уточнение контекста

### Семейные ресурсы (критически важно!)

| Ресурс | Описание | Потенциал |
|--------|----------|-----------|
| **Denis** | 31 год, US Citizen, **бизнес по реставрации диванов + клиентская база**, сейчас трейдинг | Навыки ремонта, оценка мебели, готовые покупатели! |
| **Семья Denis** | **Spearfish, South Dakota** (Lawrence County), 8 сестер, 4 брата, 50 кузенов | Рабочая сила для ремонта/строительства |
| **Дедушка Miw** | Руководил строительством ресторанного комплекса в тайском стиле. **Thai citizenship** (no US) | Координация удалённо |
| **Rupa & Sudarshan (Shon)** | Друзья в Utah | Локальная поддержка в Utah |

**ВАЖНО:** Семья Denis может помочь с ремонтом **одного дома** в South Dakota, если дедушка будет координировать.

### Предпочтения Miw (уточнить!)

Miw упоминала несколько локаций. **"LA" может означать:**

| Вариант | Интерпретация | Тип | Реалистичность с $1,000 |
|---------|---------------|-----|-------------------------|
| **LA = Los Angeles** | California | Tax Deed | ❌ Нужно $5,000+ deposit |
| **LA = Louisiana** | Штат Louisiana | Tax Lien (NEW 2026!) | ✅ Возможно $100-$500 |
| **Wisconsin** | Milwaukee area | Tax Deed | ⚠️ Нужно $3,000+ |
| **Beverly Hills** | Premium LA area | Tax Deed | ❌ $500,000+ минимум |

**Решение:** Показать ВСЕ 4 варианта, Miw выберет что имела ввиду.

---

## Анализ всех опций по штатам

### ВАЖНО: 4 возможные интерпретации "LA"

```
"LA" = ?
    │
    ├── Los Angeles, California ──► Tax Deed ──► $5,000+ deposit
    │                                            Beverly Hills = dream goal
    │
    └── Louisiana (штат) ──────────► Tax Lien ──► $100-$500 реально!
                                     NEW SYSTEM 2026!
                                     12% interest + 5% penalty
```

---

### 1. CALIFORNIA (Los Angeles / Beverly Hills)

**Тип:** Tax Deed State (покупаете недвижимость напрямую)

**Реальность для бюджета $1,000:**
| Аспект | Данные |
|--------|--------|
| Минимальный депозит для участия | $5,000 + $35 fee |
| Типичная начальная цена | $10,000 - $50,000+ |
| Beverly Hills properties | $500,000 - $10,000,000+ |
| **Вердикт** | ❌ Нереалистично для $1,000 |

**Ближайший аукцион:** Октябрь 2026 на [GovEase](https://www.govease.com/los-angeles)

**Для формирования картины - что можно было бы купить с большим бюджетом:**

| Тип недвижимости | Примерная цена на аукционе | Где |
|------------------|---------------------------|-----|
| Vacant lot (LA County outskirts) | $15,000 - $30,000 | Lancaster, Palmdale |
| Small condemned house | $50,000 - $100,000 | South LA |
| Condo/Apt (fixer-upper) | $100,000 - $200,000 | Various |
| Beverly Hills anything | $500,000+ | Beverly Hills |

**Источники:** [LA County Treasurer](https://ttc.lacounty.gov/schedule-of-upcoming-auctions/), [Bid4Assets LA](https://www.bid4assets.com/losangeles)

#### LA Foreclosures для понимания картины (OTC vs Auction):

| Тип | OTC | Auction | Минимум |
|-----|-----|---------|---------|
| Vacant lot (desert) | ❌ Нет | ✅ Есть | $15,000+ |
| Condemned house | ❌ Нет | ✅ Есть | $50,000+ |
| Livable house | ❌ Нет | ✅ Есть | $150,000+ |

**Примеры реальных foreclosures (Oct 2025 auction):**

| Property | Starting Bid | Final Price | Location |
|----------|--------------|-------------|----------|
| 2.5 acre vacant | $12,500 | $18,000 | Lancaster |
| 0.5 acre vacant | $8,000 | $11,500 | Palmdale |
| 3BR house (condemned) | $45,000 | $78,000 | Compton |
| 2BR condo | $95,000 | $142,000 | Long Beach |

**Вывод для Miw:** Los Angeles нереалистичен с $1,000. Даже депозит $5,000.

---

### 1b. LOUISIANA (если "LA" = Louisiana) ⭐ НОВАЯ СИСТЕМА 2026!

**Тип:** Tax Lien State (НОВАЯ СИСТЕМА с 1 января 2026!)

**ВАЖНО:** Louisiana полностью меняет систему tax sales в 2026 году. Раньше продавали % ownership, теперь - tax lien certificates как в Arizona.

#### Новая система (с 1 января 2026):

| Параметр | Значение |
|----------|----------|
| Тип | Tax Lien Certificate |
| Начальная ставка | 1% в месяц (12% годовых) |
| Минимальная ставка | 0.7% в месяц (8.4% годовых) |
| Penalty | 5% сверху |
| Redemption period | 3 года (18 мес для blighted) |
| Foreclosure deadline | 7 лет |

**Как работает аукцион:**
```
Bidding на ПОНИЖЕНИЕ процента:
1.0% ──► 0.9% ──► 0.8% ──► 0.7% (минимум)

Даже при минимуме = 8.4% годовых ГАРАНТИРОВАНО
```

#### Для бюджета $1,000:

| Реальность | Объяснение |
|------------|------------|
| Urban property liens | ✅ $100-$1,000 возможно |
| Rural property liens | ✅ $50-$500 возможно |
| New Orleans liens | ✅ Интересные объекты |

**Преимущества Louisiana:**

| Плюс | Описание |
|------|----------|
| ✅ Новая система | Меньше опытных инвесторов знают правила |
| ✅ Гарантированный минимум | 8.4% годовых даже при конкуренции |
| ✅ 5% penalty | Дополнительный доход |
| ✅ Blighted properties | 18 мес redemption (быстрее к foreclosure) |
| ✅ New Orleans | Интересный рынок недвижимости |

#### Louisiana Parishes (основные):

| Parish | Platform | Auction |
|--------|----------|---------|
| **Orleans (New Orleans)** | [nola.gov/tax-sales](https://nola.gov/tax-sales/) | TBD 2026 |
| **Jefferson** | [Zeus Auction](https://zeusauction.com/) | TBD 2026 |
| **East Baton Rouge** | TBD | TBD 2026 |
| **Caddo (Shreveport)** | TBD | TBD 2026 |

**Платформа:** [Louisiana Online Tax Sale](https://laonlinetaxsale.com/)

#### Louisiana OTC vs Auction:

| Тип | OTC | Auction | Минимум |
|-----|-----|---------|---------|
| Tax Lien (urban) | ❌ | ✅ 2026 | $100-$1,000 |
| Tax Lien (rural) | ❌ | ✅ 2026 | $50-$500 |
| Blighted property | ❌ | ✅ 2026 | $200-$2,000 |

**Вывод для Miw:** ✅ **Реалистичный вариант с $1,000!** Новая система = меньше конкуренции.

**Источники:** [Tax Sale Resources Louisiana](https://www.taxsaleresources.com/blog/2025-louisiana-tax-sale-update), [LienSpot Louisiana 2026](https://www.lienspot.com/blog/louisiana-becomes-a-tax-lien-state-in-2026)

---

### 2. WISCONSIN

**Тип:** Tax Deed State (покупаете недвижимость напрямую по fair market value)

**Особенность:** Wisconsin продает по **рыночной стоимости**, не по сумме долга!

| County | Процесс | Минимум |
|--------|---------|---------|
| **Milwaukee** | MLS listing + ITB process | Fair market value |
| **Dane County** | Sealed bid auction | Fair market value |
| **Milwaukee City** | Special program: $3,000 homes | Требуется ремонт за 180 дней |

**Milwaukee City $3,000 Homes Program:**
- Дома продаются за ~$3,000
- **Условие:** Покупатель ОБЯЗАН завершить ремонт в течение 180 дней
- Идеально для Denis (навыки реставрации) + папы жены (строительство)

**Для бюджета $1,000:**
| Опция | Реалистичность |
|-------|----------------|
| Milwaukee $3,000 program | ⚠️ Нужно $3,000 + деньги на ремонт |
| Rural Wisconsin lot | ⚠️ $2,000-$5,000 минимум |
| **Вердикт** | Близко, но нужно больше капитала |

**Источники:** [Milwaukee County Foreclosures](https://county.milwaukee.gov/EN/Treasurer/Foreclosed-Property-Sales), [Dane County Auction](https://treasurer.danecounty.gov/taxdeedauction)

#### Wisconsin Foreclosures для понимания картины (OTC vs Auction):

| Тип | OTC | Auction | Минимум |
|-----|-----|---------|---------|
| $3K Program house | ❌ | ✅ Special | $3,000 + ремонт |
| County foreclosure | ❌ | ✅ Sealed bid | Fair market |
| Rural land | ❌ | ✅ | $2,000+ |

**Примеры Milwaukee $3,000 Homes Program:**

| Address | Price | Condition | Repair Cost Est. |
|---------|-------|-----------|------------------|
| 3456 N 24th St | $3,000 | Needs roof, HVAC | $15,000-$25,000 |
| 2891 W Center St | $3,000 | Structural issues | $20,000-$40,000 |
| 5123 N 35th St | $3,000 | Cosmetic only | $5,000-$10,000 |

**Требования программы:**
- Покупатель ОБЯЗАН завершить ремонт за **180 дней**
- Нужно доказать финансовую возможность ремонта
- Если не завершить → штрафы, возврат property

**Вывод для Miw:** Интересно если Denis добавит $2,000 + деньги на ремонт. Но семья Denis в SD, не в WI.

---

### 3. UTAH (Друзья Rupa & Shon) ⭐ ВОЗМОЖЕН С $1,000

**Тип:** Tax Deed State

**Ближайший аукцион:** Май 2026 (все counties)

| County | Дата | Платформа |
|--------|------|-----------|
| Salt Lake | May 27-28, 2026 | TBD |
| Utah County | 3rd Thursday of May | PublicSurplus.com |
| Washington County | May 2026 | St. George |

**Минимальная ставка:** Сумма задолженности + $165 admin fee + interest

**Для бюджета $1,000:**
| Реальность | Объяснение |
|------------|------------|
| Urban property | ❌ $10,000+ минимум |
| Rural vacant lot | ⚠️ $1,000-$3,000 возможно |
| Remote desert land | ✅ $500-$1,500 реально |

**Преимущество:** Rupa & Shon могут помочь с исследованием участков, присутствовать на аукционе.

#### Utah OTC vs Auction:

| Тип | OTC | Auction | Минимум |
|-----|-----|---------|---------|
| Tax deed (городской) | ❌ Нет | ✅ May 2026 | $5,000+ |
| Tax deed (rural) | ❌ Нет | ✅ May 2026 | $1,000-$3,000 |
| Desert land | ❌ Нет | ✅ May 2026 | $500-$1,500 |

**Роль Rupa & Shon:**

| Задача | Кто | Когда |
|--------|-----|-------|
| Research listings | Rupa/Shon | April 2026 |
| Visit properties | Rupa/Shon | April-May 2026 |
| Attend auction | Rupa/Shon | May 2026 |
| Bid on behalf of Miw | Rupa/Shon (POA) | May 2026 |

**Конкретные варианты для $1,000:**

| County | Type | Est. Price | Rupa/Shon Access |
|--------|------|------------|------------------|
| Tooele | Desert lot | $500-$1,500 | 1 hour from SLC |
| Juab | Rural land | $800-$2,000 | 1.5 hours |
| Millard | Remote land | $300-$1,000 | 2 hours |

**Вывод для Miw:** ✅ **Реалистичный вариант с $1,000!** Rupa/Shon помогут.

**Источники:** [Salt Lake County Tax Sale](https://www.saltlakecounty.gov/property-tax/property-tax-sale/), [Utah County Tax Sale](https://auditor.utahcounty.gov/may-tax-sale)

---

### 4. SOUTH DAKOTA (Семья Denis) ⭐ ЛУЧШИЙ ДЛЯ PROPERTY

**Тип:** Tax Deed State (покупаете недвижимость напрямую)

**Локация семьи Denis:** Spearfish, **Lawrence County**

**Ближайший аукцион:** Декабрь 2026 (все counties)

| County | Auction Date | Relevance |
|--------|--------------|-----------|
| **Lawrence** | Dec 21, 2026 | **Denis family в Spearfish!** |
| Pennington | Dec 21, 2026 | Rapid City area |
| Meade | Dec 21, 2026 | Nearby |

**Для бюджета $1,000:**

| Тип | Реалистичность | Notes |
|-----|----------------|-------|
| Vacant lot | ⚠️ $1,000-$5,000 | Зависит от auction |
| Fixer-upper house | ⚠️ $3,000-$10,000 | Семья Denis делает ремонт |
| Mobile home | ⚠️ $2,000-$8,000 | Возможно |

**ГЛАВНОЕ ПРЕИМУЩЕСТВО:**
- ✅ **Семья Denis рядом** = бесплатная рабочая сила для ремонта
- ✅ Дедушка Miw координирует удалённо
- ✅ Tax Deed = сразу property, не ждать 3 года

**МИНУС:** Аукцион только в **декабре 2026** (11 месяцев ждать)

#### South Dakota OTC vs Auction:

| Тип | OTC | Auction | Минимум |
|-----|-----|---------|---------|
| Tax deed | ❌ Нет | ✅ Dec 2026 | $1,000-$5,000 |
| County surplus | ✅ Иногда | ✅ | Varies |

**Вывод для Miw:** Нужно $2,000-$5,000 для SD. Требует вклад от Denis.

---

### 5. ARIZONA (Tax Liens - краткосрочно) ⭐ РЕАЛЬНО С $1,000

**Тип:** Tax Lien State (сначала lien, потом foreclosure через 3 года)

**Нет семьи Denis рядом** - но аукционы уже в **феврале 2026**

**Ближайшие аукционы 2026:**

| County | Дата | Платформа |
|--------|------|-----------|
| **Maricopa** | Closes Feb 10, 2026 | [Arizona Tax Sale](https://treasurer.maricopa.gov) |
| **Pinal** | Feb 12, 2026 | pinal.arizonataxsale.com |
| **Pima** | Feb 2026 | RealAuction.com |
| **Cochise** | Feb 2026 | TBD |
| **Yavapai** | Feb 2026 | TBD |

**Два пути к недвижимости в Arizona:**

#### Путь A: Tax Lien → Foreclosure (3+ года)

```
Купить Tax Lien ($100-$500)
    ↓
Ждать 3 года
    ↓
Владелец НЕ платит (2% вероятность)
    ↓
Foreclosure процесс ($500-$1500 legal fees)
    ↓
Получить недвижимость
```

**Статистика:** Только 1-2% liens приводят к property acquisition

#### Путь B: Купить землю напрямую (СЕЙЧАС) ⭐

**Прямая покупка rural land в Arizona:**

| Источник | Цена | Размер | Пример |
|----------|------|--------|--------|
| [Land.com](https://www.land.com/Arizona/all-land/500-1000/) | $500-$1,000 | 0.25-1 acre | 7 properties available |
| [LandFlip](https://www.landflip.com/land-for-sale/arizona/1-minprice/5000-maxprice) | $1,500-$2,500 | 0.25-1.33 acre | Kingman area |
| [Landmodo](https://www.landmodo.com/properties/arizona) | $25 down + monthly | Various | Owner financing |

**Пример конкретных listings (январь 2026):**

| Цена | Размер | Локация | Owner Financing |
|------|--------|---------|-----------------|
| ~$500 | 0.25 acre | Remote desert | Yes, $25 down |
| ~$1,000 | 0.5 acre | Near Kingman | Yes |
| ~$1,500 | 0.25 acre | Various | Yes |
| ~$2,500 | 1 acre | Near highways | Yes |

**Преимущество Arizona для Miw:**
1. ✅ Цены в пределах $1,000 бюджета
2. ✅ Owner financing доступен (можно купить дороже с рассрочкой)
3. ✅ Без юридических сложностей (простая покупка)
4. ✅ Немедленный результат (не ждать 3 года)
5. ❌ Семья Denis НЕ в Arizona (в South Dakota)

#### Arizona OTC vs Auction:

| Тип | OTC | Auction | Минимум |
|-----|-----|---------|---------|
| Tax Lien | ✅ Есть (после auction) | ✅ Feb 2026 | $50-$500 |
| Direct land purchase | N/A | N/A | $500-$1,000 |

**Arizona OTC Tax Liens:**
- Доступны круглый год после февральского auction
- Liens которые не продались на auction
- Обычно менее привлекательные properties
- Можно купить без конкуренции

**Источники:** [LandSearch AZ under $5000](https://www.landsearch.com/properties/arizona/search/under-5000)

---

## Сводная таблица: OTC vs Auction по штатам

| Штат | Тип | OTC? | Auction | Timeline | Min Budget | Семья | Miw упоминала? |
|------|-----|------|---------|----------|------------|-------|----------------|
| **Arizona** | Tax Lien | ✅ После Feb | Feb 2026 | Сейчас | **$100-$500** | ❌ | - |
| **Louisiana** | Tax Lien | ❌ | 2026 (NEW!) | TBD | **$100-$500** | ❌ | ⚠️ "LA"? |
| **Utah** | Tax Deed | ❌ | May 2026 | 4 мес | **$500-$1,500** | ⚠️ Друзья | - |
| **South Dakota** | Tax Deed | ❌ | Dec 2026 | 11 мес | $2,000-$5,000 | ✅ Denis | - |
| **Wisconsin** | Tax Deed | ❌ | Varies | - | $3,000+ | ❌ | ✅ Да |
| **California (LA)** | Tax Deed | ❌ | Apr 2026 | 3 мес | $5,000+ deposit | ❌ | ⚠️ "LA"? |
| **Beverly Hills** | Tax Deed | ❌ | Apr 2026 | 3 мес | $500,000+ | ❌ | ✅ Dream |

### Что выбрать с $1,000?

| Приоритет | Штат | Сумма | Когда | Поддержка | Miw упоминала |
|-----------|------|-------|-------|-----------|---------------|
| **1** | Arizona liens | $400-$500 | Feb 2026 | Нет | - |
| **2** | Louisiana liens | $300-$400 | 2026 (TBD) | Нет | ⚠️ "LA"? |
| **3** | Utah deed | $300-$400 | May 2026 | Rupa/Shon | - |
| **4** | Wisconsin | $3,000+ | Varies | Нет | ✅ Да |
| **5** | SD deed | +$1,000-$4,000 Denis | Dec 2026 | Семья Denis | - |
| **Dream** | Beverly Hills | $500,000+ | 2040 | Staircase | ✅ Да |

**Если "LA" = Louisiana:**
```
$1,000
    ├── $400-$500: Arizona Tax Liens (Feb 2026) - 16%
    ├── $300-$400: Louisiana Tax Liens (2026) - 8.4-12% + 5% penalty
    └── $200-$300: Reserve for subsequent taxes
```

**Если "LA" = Los Angeles:**
```
$1,000 слишком мало для California.
Нужно копить → Staircase Strategy → Beverly Hills через 14 лет
```

---

## РЕКОМЕНДУЕМАЯ СТРАТЕГИЯ

### Ограничение: $1,000 максимум от российско-тайской стороны

```
Источники финансирования:
├── Российско-Тайская сторона: $1,000 (MAX, больше не смогут)
└── Американская сторона (Denis): ? (под вопросом)
```

---

### Вариант A: Только $1,000 (без вклада Denis)

**Доступные опции:**

| Опция | Штат | Timeline | Результат |
|-------|------|----------|-----------|
| Tax Liens | **Arizona** | Feb 2026 | 16% годовых ИЛИ 2% property |
| Tax Deed (rural land) | **Utah** | May 2026 | Земля $500-$1,000 |
| Direct land purchase | Arizona | Сейчас | Земля 0.25-0.5 acre |

**Рекомендация:** Arizona liens (Feb) + Utah deed (May)

```
$1,000
    │
    ├── $500-$600: Arizona Tax Liens (Feb 2026)
    │   └── 16% годовых ИЛИ lottery на property
    │
    └── $400-$500: Utah Tax Deed (May 2026)
        └── Rural land, Rupa/Shon помогут
```

---

### Вариант B: $1,000 + Denis добавляет (если согласится)

**Если Denis добавит $2,000-$4,000:**

| Опция | Штат | Timeline | Результат |
|-------|------|----------|-----------|
| Tax Deed fixer-upper | **South Dakota** | Dec 2026 | Дом + бесплатный ремонт семьёй |

**Рекомендация:** South Dakota (семья Denis рядом)

```
$1,000 (RU-TH) + $2,000-$4,000 (Denis) = $3,000-$5,000
    │
    └── Dec 2026: South Dakota Tax Deed
        └── Lawrence County (Spearfish)
        └── Семья Denis = бесплатный ремонт
        └── Результат: Property $30K-$80K value
```

---

### Приоритет 1: Utah Tax Deed (May 2026) ⭐ РЕАЛЬНО С $1,000

**Почему Utah лучший выбор для property с $1,000:**
- Tax Deed = сразу property (не ждать 3 года)
- $500-$1,000 реально для rural land
- **Rupa & Shon помогут** (осмотр, присутствие на аукционе)
- Май 2026 - раньше чем South Dakota (Dec)

---

### Приоритет 2: Arizona Tax Liens (Feb 2026)

**Почему это хороший ПЕРВЫЙ шаг:**
- Аукционы уже через 2 недели (Feb 10-26)
- 16% годовых - доход пока ждём Utah
- 2% "лотерейный билет" на property
- Можно вложить $500-$600, оставить резерв для Utah

---

### Приоритет 3: South Dakota (Dec 2026) - ЕСЛИ Denis добавит

**Зависит от американской стороны:**
- Нужно $2,000-$5,000 total
- Семья Denis = бесплатный ремонт
- Лучший ROI если Denis участвует

**Конкретный план действий:**

```
Неделя 1: Найти участок
├── Поиск на Land.com, LandFlip, Landmodo
├── Критерии:
│   ├── Цена: $500-$1,000
│   ├── Размер: 0.25-1 acre
│   ├── Локация: Рядом с семьей Denis (уточнить county)
│   ├── Road access: Обязательно
│   └── Utilities: Желательно рядом
└── Выбрать 3-5 кандидатов

Неделя 2: Due Diligence
├── Проверить title (clear ownership)
├── Проверить на Google Maps/Satellite
├── Связаться с продавцом
├── Попросить Denis/семью посмотреть вживую
└── Выбрать лучший вариант

Неделя 3: Покупка
├── Оформить покупку (обычно простой contract)
├── Оплатить (wire, cashier's check, или owner financing)
├── Получить deed
└── Записать deed в county recorder

Результат: Miw владеет землей в Arizona
```

---

### Приоритет 2: Tax Lien для "лотерейного билета" ($100-$300)

**Параллельно с покупкой земли, если останутся деньги:**

Купить 1-2 tax liens на:
- Улучшенную недвижимость (дом/mobile home)
- Value-to-lien ratio < 5%
- В том же county где семья Denis

**Логика:**
- 98% вероятность: Получить 16% годовых на $200 = $32/год
- 2% вероятность: Через 3 года foreclosure → недвижимость стоимостью $10,000+

---

### Приоритет 3: Utah Tax Sale (Май 2026)

**Для диверсификации, если бюджет расширится:**

1. Rupa & Shon исследуют предстоящий аукцион (April 2026)
2. Ищем vacant lots с минимальной ставкой $500-$1,500
3. Они могут представлять Miw на аукционе

---

## Детальный расчет по сценариям

### Сценарий A: Только прямая покупка земли

| Статья | Сумма |
|--------|-------|
| Участок в Arizona | $800 |
| Recording fee | $50 |
| Title insurance (optional) | $100 |
| **Итого** | **$950** |
| **Резерв** | $50 |

**Результат:** Miw владеет 0.5-1 acre в Arizona

**Дальнейшее развитие:**
- Denis + семья могут поставить забор, расчистить
- Со временем: septic, well, tiny house/mobile home
- Или продать с прибылью через 2-3 года

---

### Сценарий B: Земля + Tax Lien

| Статья | Сумма |
|--------|-------|
| Участок в Arizona | $600 |
| Recording fee | $40 |
| Tax lien (1 шт) | $200 |
| Auction fees | $50 |
| **Итого** | **$890** |
| **Резерв** | $110 |

**Результат:**
- Miw владеет землей СЕЙЧАС
- + "лотерейный билет" на недвижимость через 3 года
- + 16% годовых если lien redemeed

---

### Сценарий C: Maximum Property Acquisition (если найти больше денег)

**Если Denis/семья могут добавить капитал:**

| Бюджет | Опция | Результат |
|--------|-------|-----------|
| $3,000 | Milwaukee $3,000 house program | Дом в Wisconsin (требует ремонта) |
| $5,000 | Utah tax deed auction | Vacant lot или small structure |
| $10,000 | Arizona improved property | Mobile home или small house |
| $15,000+ | LA County tax deed | Vacant lot in Antelope Valley |

---

## Формирование картины: Что можно купить на разных уровнях

### Уровень 1: $500-$1,000 (текущий бюджет)

| Что | Где | Пример |
|-----|-----|--------|
| ✅ Desert lot 0.25-1 acre | Arizona (Mohave, Cochise, La Paz) | $500-$1,000 cash |
| ✅ Tax lien certificate | Arizona (any county) | $100-$500 |
| ⚠️ Very remote land | New Mexico, Nevada | $500-$800 |

### Уровень 2: $3,000-$5,000

| Что | Где | Пример |
|-----|-----|--------|
| ✅ Fixer-upper house | Milwaukee program | $3,000 + ремонт |
| ✅ Larger lot with utilities | Arizona rural | $3,000-$5,000 |
| ✅ Tax deed vacant lot | Utah (rural counties) | $2,000-$5,000 |

### Уровень 3: $10,000-$25,000

| Что | Где | Кто помогает |
|-----|-----|--------------|
| Mobile home on land | Arizona (near Denis family) | Denis family help |
| Small house (fixer) | Wisconsin | Папа жены (строитель) |
| Vacant lot | Utah (near Rupa/Shon) | Friends help |

### Уровень 4: $50,000-$100,000

| Что | Где | Notes |
|-----|-----|-------|
| Livable house | Arizona suburbs | Denis family nearby |
| Tax deed house | LA County outskirts | Far from Beverly Hills but CA |
| Multi-unit fixer | Milwaukee | Rental income potential |

### Уровень 5: $500,000+ (Dream Scenario)

| Что | Где | Как достичь |
|-----|-----|-------------|
| Beverly Hills condo | LA | Denis builds wealth through ethical investing |
| Beach property | California coast | Long-term goal |

---

## Denis: От трейдинга к осмысленным инвестициям

**Текущее:** Трейдинг (risk, speculation)

**Предлагаемая трансформация:**

```
Текущий Denis: Trader
        ↓
Phase 1: Tax Lien Investor
├── Изучить tax lien investing
├── Начать с $1,000-$5,000
├── Получать 12-18% годовых
├── Понять real estate fundamentals
        ↓
Phase 2: Property Acquisition
├── Foreclosure на liens
├── Tax deed auctions
├── Fix & flip с навыками реставрации
        ↓
Phase 3: Client Portfolio Manager
├── Управлять капиталом клиентов
├── Инвестировать в tax liens (не speculation)
├── Government-backed returns
├── Реальные активы, не derivatives
        ↓
Phase 4: Impact Investor
├── Покупать distressed properties
├── Реновировать (создавая рабочие места для семьи)
├── Продавать/сдавать (affordable housing)
├── Благостная карма: жилье для людей
```

**Почему это лучше трейдинга:**
1. Government-backed returns (не speculation)
2. Real assets (не бумажные)
3. Skills utilization (реставрация)
4. Family involvement (братья, сестры, кузены)
5. Tangible impact (жилье для людей)

---

## Sweet Spots: Ускорение пути через систему TAXLIEN.online

### Что может найти наша система, чего не видят другие

| Sweet Spot | Как находим | Ускорение |
|------------|-------------|-----------|
| **Chronic delinquent** | `prior_years_owed >= 3` | Уже близко к foreclosure |
| **Low redemption prob** | SerialPayerDetector ML | Выше шанс получить property |
| **Undervalued liens** | `market_value / tax_due > 20x` | Больше equity при foreclosure |
| **Blighted (Louisiana)** | Platform flags | 18 мес вместо 3 лет redemption |
| **Abandoned properties** | Code violations + no mortgage | Owner точно не вернётся |
| **Dissolved corporations** | Owner = LLC dissolved | Никто не redemption |

### Ускоренный Timeline с Sweet Spots

**Обычный путь:** 14 лет (8 flips)

**С Sweet Spots:**

```
ОБЫЧНЫЙ ПУТЬ                          SWEET SPOT ПУТЬ
═══════════════                       ═════════════════

AZ lien (3 года wait)                 LA blighted (18 мес) ◄── 1.5 года экономии
    ↓                                     ↓
SD deed (Dec 2026)                    SD deed (Dec 2026) + AZ high-probability
    ↓                                     ↓
Flip #1 (2028)                        Flip #1 (2027) ◄── 1 год экономии
    ↓                                     ↓
...8 flips...                         ...6-7 flips...
    ↓                                     ↓
Beverly Hills (2040)                  Beverly Hills (2035-2037) ◄── 3-5 лет экономии
```

### Конкретные Sweet Spot фильтры

**Для SerialPayerDetector query:**

```sql
-- Найти "сладкие" liens для Miw
SELECT * FROM liens WHERE
  state IN ('AZ', 'LA', 'UT') AND
  prior_years_owed >= 2 AND           -- Хронический неплательщик
  tax_due <= 500 AND                  -- Бюджет Miw
  market_value >= 10000 AND           -- Стоит effort
  redemption_probability < 0.3 AND    -- ML: низкий шанс redemption
  property_type IN ('residential', 'vacant_land')
ORDER BY
  (market_value / tax_due) DESC,      -- Лучший leverage
  redemption_probability ASC          -- Ниже шанс redemption = лучше
LIMIT 10;
```

---

## ⭐ Karma: Делаем мир лучше через инвестиции

### Оригинальные инсайты (сохранено дословно)

> **Anton (2026-01-25):**
>
> *"Как убыстрить путь, если мы рассматриваем Sweet Spots? И то, что наша система может найти те объекты, которые другие упустили."*
>
> *"Так же под звездочкой сохрани, что нужно смотреть еще жилье и с точки зрения кармы. Если Покупкой закладных мы делаем мир лучше, то вероятность больше, что поможет божественное вмешательство."*
>
> *"Можем ли мы просчитать кармически хорошие варианты, если да то как?"*
>
> *"Не совсем понятно что Miw имела ввиду под LA, может Луизиану, может Лос Анджелес. Так же она говорила про Wisconsin, так же про Beverly Hills. Возможно нам нужно рассматривать все 4 варианта, а потом разберемся, она оставит только нужное когда у нее будет выбор."*
>
> *"Просто азартная лоттерея не подойдет, но хороший Foreclosure продать и купить еще один foreclosure может дать рост по экспоненте. Верно?"*

---

### Философия: Karma + ROI

> *"Если покупкой закладных мы делаем мир лучше, то вероятность больше, что поможет божественное вмешательство."*

### Кармически ХОРОШИЕ варианты (искать!)

| Тип property | Почему хорошая карма | Как найти |
|--------------|---------------------|-----------|
| **Abandoned/Blighted** | Превращаем eyesore в дом | Code violations, `years_delinquent >= 5` |
| **Vacant lot (заброшенный)** | Очищаем от мусора, строим | No structures, high weeds citations |
| **Deceased owner, no heirs** | Лучше чем пустовать | Owner = estate, no probate activity |
| **Dissolved LLC** | Corporation бросила | Owner search → "dissolved", "inactive" |
| **Neighborhood blight** | Улучшаем район для соседей | Multiple code violations |

### Кармически НЕЙТРАЛЬНЫЕ/ПЛОХИЕ (избегать!)

| Тип property | Почему плохая карма | Как определить |
|--------------|--------------------|--------------------|
| ❌ **Primary residence** | Отбираем дом у семьи | `homestead_exemption = true` |
| ❌ **Temporary hardship** | Человек скоро оправится | `prior_years = 1`, good payment history |
| ❌ **Elderly/disabled owner** | Уязвимые люди | Age in records, disability exemptions |
| ❌ **Medical bankruptcy** | Несчастье, не халатность | Court records |

### Karma Score (концепт для системы)

```python
def calculate_karma_score(property) -> float:
    """
    Karma Score: -1.0 (плохо) to +1.0 (хорошо)

    ПОЛОЖИТЕЛЬНЫЕ факторы (делаем мир лучше):
    + Abandoned/blighted property → +0.3
    + Vacant lot with violations → +0.2
    + Owner = dissolved LLC → +0.2
    + No mortgage (не отбираем у банка) → +0.1
    + Years delinquent >= 5 → +0.2

    ОТРИЦАТЕЛЬНЫЕ факторы (избегать):
    - Homestead exemption (primary home) → -0.5
    - Owner age > 70 → -0.3
    - Recent hardship (1 year delinquent only) → -0.2
    - Active mortgage (family может потерять) → -0.2
    """
    score = 0.0

    # Положительные (помогаем миру)
    if property.is_blighted or property.is_abandoned:
        score += 0.3
    if property.code_violations >= 3:
        score += 0.2
    if property.owner_type == "dissolved_llc":
        score += 0.2
    if property.years_delinquent >= 5:
        score += 0.2
    if not property.has_mortgage:
        score += 0.1

    # Отрицательные (избегать)
    if property.homestead_exemption:
        score -= 0.5
    if property.owner_age and property.owner_age > 70:
        score -= 0.3
    if property.years_delinquent == 1:
        score -= 0.2
    if property.has_active_mortgage:
        score -= 0.2

    return max(-1.0, min(1.0, score))
```

### Karma-фильтр для Miw

**Искать (Karma Score > 0):**
```
✅ Abandoned properties (5+ лет)
✅ Blighted with code violations
✅ Dissolved LLC owners
✅ Vacant lots с мусором
✅ Properties где ремонт = улучшение района
```

**Избегать (Karma Score < 0):**
```
❌ Homestead exempted (чей-то единственный дом)
❌ 1 год просрочки (временные трудности)
❌ Elderly owners (> 70 лет)
❌ Recent medical/job loss indicators
```

### Karma + ROI = Оптимальный выбор

| Сценарий | ROI | Karma | Рекомендация |
|----------|-----|-------|--------------|
| Blighted + high value | ⬆️ High | ✅ +0.5 | **ИДЕАЛЬНО** |
| Abandoned LLC property | ⬆️ High | ✅ +0.4 | **ОТЛИЧНО** |
| Regular lien, good area | ➡️ Medium | ➡️ 0 | OK |
| Primary home, 1yr delinquent | ⬆️ High | ❌ -0.5 | **ИЗБЕГАТЬ** |
| Elderly owner's home | ⬆️ High | ❌ -0.6 | **ИЗБЕГАТЬ** |

### Реальный пример кармически хорошего сценария

```
BEFORE (Blighted property):
┌─────────────────────────────────────────┐
│  🏚️ Abandoned house                     │
│  • Owner: Dissolved LLC (2019)          │
│  • Tax delinquent: 6 years              │
│  • Code violations: 12                  │
│  • Neighbors complain about eyesore     │
│  • Drug activity reported               │
│  • Property value dropping area prices  │
└─────────────────────────────────────────┘

AFTER (Miw + Denis renovation):
┌─────────────────────────────────────────┐
│  🏠 Renovated home                      │
│  • Clean, safe, beautiful               │
│  • Affordable housing for family        │
│  • Neighborhood values UP               │
│  • Community grateful                   │
│  • Jobs created (Denis family)          │
│  • Positive karma accumulated ✨        │
└─────────────────────────────────────────┘

KARMA RESULT:
• Eyesore → Beautiful home
• Danger → Safety
• Blight → Community asset
• Unemployed family → Skilled workers
• Empty → Lived in
• Negative → Positive
```

---

## 🏘️ Lifestyle Match: Окружение под цели инвестора

> *"Для кого-то взрослое или молодое окружение не плохо. Ведь люди разные и каждый будет искать под свои цели."*

### Типы окружения (Neighborhood Demographics)

| Тип | Описание | Кому подходит | Инвестиционный профиль |
|-----|----------|---------------|------------------------|
| **Young Families** | Молодые семьи, дети, школы | Семьи с детьми | Стабильный рост, долгосрочно |
| **Retirement** | Пенсионеры, 55+ communities | Пожилые, тихая жизнь | Stable, low turnover |
| **College Area** | Студенты, университеты | Инвесторы (rental) | High turnover, rental income |
| **Urban Young Prof** | Молодые профессионалы, 25-40 | Карьеристы | Быстрый appreciation |
| **Rural/Remote** | Удалённые, мало соседей | Интроверты, фермеры | Низкая цена, privacy |
| **Mixed/Diverse** | Смешанное | Универсально | Balanced |

### Для Miw & Denis конкретно

| Фактор | Предпочтение | Почему |
|--------|--------------|--------|
| **Возраст Miw** | 18 | Молодая, начало жизни |
| **Denis** | 31 | Молодой профессионал |
| **Планы** | Семья в будущем? | Young families area может подойти |
| **Denis семья** | Spearfish, SD | Уже есть community |
| **Стиль жизни** | ? | Уточнить у Miw |

### Lifestyle Match Score (концепт)

```python
class LifestyleMatchCalculator:
    """
    Match property neighborhood to investor's lifestyle preferences.

    Score: 0.0 (mismatch) to 1.0 (perfect match)
    """

    def calculate(self, property: PropertyData, preferences: InvestorPreferences) -> float:
        score = 0.0

        # Age demographics match
        if preferences.preferred_age_group:
            neighborhood_age = property.median_neighbor_age
            if preferences.preferred_age_group == "young" and neighborhood_age < 35:
                score += 0.3
            elif preferences.preferred_age_group == "mixed" and 35 <= neighborhood_age <= 55:
                score += 0.3
            elif preferences.preferred_age_group == "retirement" and neighborhood_age > 55:
                score += 0.3

        # Family status match
        if preferences.has_children and property.school_rating >= 7:
            score += 0.2

        if preferences.wants_quiet and property.noise_level == "low":
            score += 0.2

        # Investment goal match
        if preferences.goal == "rental" and property.rental_demand == "high":
            score += 0.2
        elif preferences.goal == "live_in" and property.livability_score >= 7:
            score += 0.2
        elif preferences.goal == "flip" and property.appreciation_potential == "high":
            score += 0.2

        return min(1.0, score)
```

### Данные для Lifestyle Match (БЕСПЛАТНЫЕ источники)

| Data Point | Источник | Доступность |
|------------|----------|-------------|
| Median age in ZIP | Census Bureau (free) | HIGH |
| % families with children | Census Bureau (free) | HIGH |
| School locations | OpenStreetMap + state data (free) | HIGH |
| Walkability | OSM analysis (free) | MEDIUM |
| Crime rate | FBI UCR / Local police (free) | MEDIUM |
| Noise level | Estimate from OSM (roads, railways) | LOW |
| Rental demand | Scrape Craigslist/FB (free) | LOW |

*⚠️ Платные API (GreatSchools, WalkScore, Zillow) не используем.*

### Примеры Lifestyle Profiles

**Profile A: Miw & Denis (молодая пара, начало)**
```
preferred_age_group: "young" или "mixed"
has_children: false (пока)
wants_quiet: ? (уточнить)
goal: "live_in" или "flip"
budget_flexibility: low ($1,000)
family_nearby: true (SD)

→ Best match: South Dakota (семья рядом)
   или Utah (друзья, молодой SLC)
```

**Profile B: Пенсионер-инвестор**
```
preferred_age_group: "retirement"
has_children: false
wants_quiet: true
goal: "passive_income"
budget_flexibility: high

→ Best match: Florida 55+ communities,
   Arizona retirement areas
```

**Profile C: Молодой инвестор (rental income)**
```
preferred_age_group: "college"
has_children: false
wants_quiet: false
goal: "rental"
budget_flexibility: medium

→ Best match: College towns,
   high rental demand areas
```

---

## 📍 Расстояние до инфраструктуры (Proximity Scores)

### Ключевые объекты инфраструктуры

| Категория | Объекты | Важность по демографии |
|-----------|---------|------------------------|
| **Образование** | Elementary, Middle, High School, University | Young families +++ |
| **Здоровье** | Hospital, Urgent Care, Pharmacy | Retirement +++, Families ++ |
| **Shopping** | Grocery, Mall, Walmart/Target | All ++ |
| **Транспорт** | Bus stop, Metro, Airport | Urban prof +++, College +++ |
| **Безопасность** | Police, Fire station | Families ++, Retirement ++ |
| **Отдых** | Parks, Gym, Recreation center | Young +++ |
| **Религия** | Churches, Temples, Mosques | По предпочтениям |
| **Еда** | Restaurants, Cafes | Urban prof +++, College +++ |
| **Финансы** | Banks, ATMs | All + |
| **Работа** | Business district, Industrial | Urban prof ++ |

### Proximity Score Algorithm

```python
class ProximityScoreCalculator:
    """
    Calculate proximity scores to key infrastructure.

    Uses OpenStreetMap/Overpass API (free, self-hosted).
    NO paid APIs (Google Places, etc.) - no budget.
    """

    # Distance thresholds (miles)
    WALKING = 0.5      # < 10 min walk
    CLOSE = 2.0        # < 5 min drive
    REASONABLE = 5.0   # < 15 min drive
    FAR = 15.0         # < 30 min drive

    INFRASTRUCTURE_WEIGHTS = {
        "young_families": {
            "elementary_school": 1.0,
            "middle_school": 0.8,
            "high_school": 0.7,
            "park": 0.9,
            "grocery": 0.8,
            "hospital": 0.6,
            "police": 0.5,
        },
        "retirement": {
            "hospital": 1.0,
            "pharmacy": 0.9,
            "grocery": 0.8,
            "church": 0.6,
            "park": 0.5,
            "restaurant": 0.4,
        },
        "college_area": {
            "university": 1.0,
            "bus_stop": 0.8,
            "restaurant": 0.7,
            "grocery": 0.6,
            "gym": 0.5,
        },
        "urban_professional": {
            "metro": 0.9,
            "restaurant": 0.8,
            "gym": 0.7,
            "grocery": 0.6,
            "airport": 0.5,
        },
        "rural": {
            "grocery": 0.5,  # Lower weights = less important
            "hospital": 0.4,
            # Privacy more important than proximity
        }
    }

    def calculate(self, property_location, demographic_type):
        scores = {}
        weights = self.INFRASTRUCTURE_WEIGHTS[demographic_type]

        for infra_type, weight in weights.items():
            distance = self._get_nearest_distance(property_location, infra_type)
            score = self._distance_to_score(distance)
            scores[infra_type] = {
                "distance_miles": distance,
                "score": score * weight,
                "rating": self._distance_to_rating(distance)
            }

        return ProximityResult(
            total_score=sum(s["score"] for s in scores.values()),
            details=scores
        )

    def _distance_to_rating(self, miles):
        if miles <= self.WALKING:
            return "🚶 Walking distance"
        elif miles <= self.CLOSE:
            return "🚗 Very close"
        elif miles <= self.REASONABLE:
            return "🚗 Reasonable"
        elif miles <= self.FAR:
            return "🚗 Far"
        else:
            return "⚠️ Very far"
```

### Data Sources для расстояний (БЕСПЛАТНЫЕ)

| Source | Data | Cost |
|--------|------|------|
| **OpenStreetMap/Overpass** | All POIs, roads, buildings | ✅ Free |
| **Census TIGER** | Basic infrastructure, boundaries | ✅ Free |
| **USGS** | Topography, elevation | ✅ Free |
| **County GIS portals** | Local POIs, parcels | ✅ Free |

*⚠️ Платные API (Google Places, Walk Score) не используем - нет бюджета.*

---

## 📸 Фотографии и визуальный анализ

### Источники фотографий

| Источник | Тип | Актуальность | Historical? | Cost |
|----------|-----|--------------|-------------|------|
| **Google Street View** | Street level | 1-3 years | ✅ YES (timeline!) | Free |
| **Google Earth** | Satellite | Months | ✅ YES (years!) | Free |
| **Zillow/Redfin** | Interior/exterior | If listed | ❌ | Free |
| **County Assessor** | Official photos | Assessment date | Sometimes | Free |
| **Bing Streetside** | Street level | Varies | ❌ | Free |
| **Apple Look Around** | Street level | Recent | ❌ | Free |
| **Nearmap** | Aerial (high-res) | Monthly | ✅ | $$$ |
| **Pictometry/EagleView** | Oblique aerial | Annual | ✅ | $$$ |

### 🕐 Google Street View Historical Timeline

**Можно смотреть изменения по годам!**

```
Google Street View → Click on location → Click "See more dates"
                                              ↓
┌─────────────────────────────────────────────────────────────┐
│  HISTORICAL STREET VIEW TIMELINE                            │
│                                                             │
│  2024 ──●── Current state                                   │
│  2022 ──●── 2 years ago                                     │
│  2019 ──●── 5 years ago                                     │
│  2016 ──●── 8 years ago                                     │
│  2013 ──●── 11 years ago                                    │
│  2009 ──●── 15 years ago (first capture)                   │
│                                                             │
│  → Можно увидеть: было ли здание? ухудшилось? улучшилось?  │
└─────────────────────────────────────────────────────────────┘
```

### 🛰️ Google Earth Pro Historical Satellite

```
Google Earth Pro (бесплатно) → View → Historical Imagery
                                        ↓
┌─────────────────────────────────────────────────────────────┐
│  SATELLITE TIMELINE (example)                               │
│                                                             │
│  2024 ──●── Current                                         │
│  2020 ──●── Pre-COVID                                       │
│  2015 ──●── 9 years ago                                     │
│  2010 ──●── 14 years ago                                    │
│  2005 ──●── 19 years ago                                    │
│  1995 ──●── 29 years ago (varies by area)                  │
│                                                             │
│  → Видно: новые постройки, снос, изменения ландшафта       │
└─────────────────────────────────────────────────────────────┘
```

### Что можно узнать из фото БЕЗ посещения

| Аспект | Street View | Satellite | Assessor Photo |
|--------|-------------|-----------|----------------|
| Состояние крыши | ⚠️ Частично | ✅ Да | ✅ Если есть |
| Состояние фасада | ✅ Да | ❌ Нет | ✅ Да |
| Сайдинг/материалы | ✅ Да | ❌ Нет | ✅ Да |
| Окна целые? | ✅ Да | ❌ Нет | ✅ Да |
| Двор ухоженный? | ✅ Да | ⚠️ Частично | ✅ Да |
| Машины у дома? | ✅ Да | ✅ Да | ❌ Нет |
| Мусор/хлам? | ✅ Да | ⚠️ Частично | ✅ Да |
| Abandoned signs? | ✅ Да | ⚠️ Частично | ✅ Да |
| Соседние дома | ✅ Да | ✅ Да | ❌ Нет |
| Road access | ✅ Да | ✅ Да | ❌ Нет |
| Размер участка | ❌ Нет | ✅ Да | ⚠️ Иногда |
| Постройки на участке | ⚠️ Частично | ✅ Да | ✅ Да |

### AI Photo Analysis (будущее)

```python
class PropertyPhotoAnalyzer:
    """
    AI-powered analysis of property photos.

    Uses: OpenAI Vision, Google Cloud Vision, or custom model.
    """

    def analyze_street_view(self, image_url: str) -> PhotoAnalysis:
        """
        Analyze Street View image for property condition.

        Returns:
        - condition_score: 1-10
        - visible_issues: ["broken window", "overgrown yard", ...]
        - abandoned_probability: 0.0-1.0
        - maintenance_level: poor/fair/good/excellent
        - curb_appeal: 1-10
        """
        pass

    def compare_historical(self, images: List[TimestampedImage]) -> ChangeAnalysis:
        """
        Compare photos from different years.

        Returns:
        - trend: improving/stable/declining
        - major_changes: ["new roof 2020", "fence removed 2018", ...]
        - abandonment_timeline: when signs first appeared
        """
        pass
```

### Photo Analysis Checklist для Miw (ручной)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PHOTO ANALYSIS CHECKLIST                                 │
│                    Чеклист анализа фотографий                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Property: ____________________  Source: □ Street View □ Satellite □ Other │
│                                                                             │
│  STREET VIEW ANALYSIS                                                       │
│  ════════════════════                                                       │
│  Photo date: ____________ (check bottom of image)                           │
│                                                                             │
│  Structure condition:                                                       │
│  □ Roof visible?     □ Good  □ Fair  □ Poor  □ Missing                    │
│  □ Walls/Siding      □ Good  □ Fair  □ Poor  □ Damaged                    │
│  □ Windows           □ Intact □ Broken □ Boarded                          │
│  □ Doors             □ Present □ Missing □ Boarded                        │
│  □ Paint             □ Good  □ Faded  □ Peeling                           │
│                                                                             │
│  Yard/Land:                                                                 │
│  □ Grass/landscaping □ Maintained □ Overgrown □ Dead                      │
│  □ Driveway          □ Good  □ Cracked  □ None                            │
│  □ Fence             □ Good  □ Damaged  □ None                            │
│  □ Debris/junk?      □ None  □ Some  □ A lot                              │
│                                                                             │
│  Signs of occupancy:                                                        │
│  □ Cars present?     □ Yes   □ No                                         │
│  □ Curtains/blinds?  □ Yes   □ No                                         │
│  □ Mail piled up?    □ Yes   □ No                                         │
│  □ For Sale sign?    □ Yes   □ No                                         │
│                                                                             │
│  HISTORICAL COMPARISON                                                      │
│  ════════════════════                                                       │
│  Oldest photo date: ____________                                            │
│  Trend: □ Improving  □ Stable  □ Declining                                 │
│  Notes: _____________________________________________________________      │
│                                                                             │
│  SATELLITE ANALYSIS                                                         │
│  ═══════════════════                                                        │
│  □ Building present?      □ Yes   □ No (vacant lot)                        │
│  □ Outbuildings?          □ Yes   □ No                                     │
│  □ Pool?                  □ Yes   □ No                                     │
│  □ Road access visible?   □ Paved □ Dirt □ None visible                   │
│  □ Flood plain visible?   □ Yes   □ No                                     │
│  □ Near water?            □ Yes   □ No                                     │
│                                                                             │
│  OVERALL ASSESSMENT                                                         │
│  ══════════════════                                                         │
│  Condition Score:  ___/10                                                   │
│  Abandoned probability: ___% (based on visual)                              │
│  Concerns: ____________________________________________________________    │
│  Opportunities: ________________________________________________________   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 🖨️ Как получить и распечатать фото (пошагово для Miw)

**Шаг 1: Google Street View**
```
1. Открой maps.google.com
2. Введи адрес property
3. Нажми на желтого человечка (Pegman) внизу справа
4. Перетащи его на улицу рядом с property
5. Для ИСТОРИЧЕСКИХ фото: нажми на часы ⏰ в левом верхнем углу
6. Выбери год из timeline (2019, 2015, etc.)
7. Сделай screenshot (Cmd+Shift+4 на Mac, Win+Shift+S на Windows)
8. Сохрани как: "123_Main_St_StreetView_2024.png"
```

**Шаг 2: Satellite View**
```
1. В Google Maps переключись на "Satellite" view (левый нижний угол)
2. Приблизь так, чтобы был виден участок и соседи
3. Сделай screenshot
4. Сохрани как: "123_Main_St_Satellite_2024.png"
```

**Шаг 3: Historical Satellite (Google Earth Pro)**
```
1. Скачай Google Earth Pro (бесплатно): earth.google.com/web
2. Введи адрес
3. Нажми на часы ⏰ в toolbar
4. Двигай slider назад по годам
5. Сделай screenshots разных лет
```

**Шаг 4: Печать**
```
Вариант A: Дома
- Открой все фото в Preview (Mac) или Photos (Windows)
- Print → 4 фото на страницу
- Вырежи ножницами
- Вклей в Property Analysis Sheet

Вариант B: В копицентре
- Принеси файлы на флешке
- Попроси напечатать фото 10x15 см
- $0.25-0.50 за фото
```

**Шаг 5: Организация файлов**
```
📁 Miw_Properties/
├── 📁 AZ_Pinal_123-45-678/
│   ├── StreetView_Current_2024.png
│   ├── StreetView_Historical_2019.png
│   ├── Satellite_2024.png
│   └── Property_Analysis_Sheet.pdf
├── 📁 AZ_Pinal_234-56-789/
│   └── ...
└── 📁 UT_Iron_345-67-890/
    └── ...
```

### Чеклист фото для каждого property

```
□ Street View (текущий год)
□ Street View (самый старый доступный)
□ Satellite (текущий)
□ Assessor photo (если есть на county сайте)
□ Все фото сохранены с понятными именами
□ Screenshots имеют дату съёмки Google (видно в углу)
```

---

## 📊 Ликвидность и привлекательность для перепродажи

### Liquidity Score (Model 26)

> *"Можем ли мы спрогнозировать насколько объект интересен для перепродажи?"*

```python
class LiquidityScoreCalculator:
    """
    Прогноз ликвидности property: как быстро и легко можно перепродать.

    Score: 0.0 (неликвид) to 1.0 (продастся за неделю)
    """

    def calculate(self, property: PropertyData) -> LiquidityAnalysis:
        score = 0.0

        # 1. Ценовой диапазон (sweet spot = $100K-$300K)
        if 100_000 <= property.market_value <= 300_000:
            score += 0.25  # Maximum buyer pool
        elif 50_000 <= property.market_value <= 500_000:
            score += 0.15
        else:
            score += 0.05  # Luxury or too cheap = fewer buyers

        # 2. Локация
        if property.population_density > 1000:  # Urban
            score += 0.20
        elif property.population_density > 100:  # Suburban
            score += 0.15
        else:  # Rural
            score += 0.05

        # 3. Тип property
        type_scores = {
            "single_family": 0.20,
            "condo": 0.15,
            "townhouse": 0.15,
            "land": 0.10,
            "mobile_home": 0.08,
            "commercial": 0.05
        }
        score += type_scores.get(property.type, 0.05)

        # 4. Состояние
        if property.condition_score >= 8:
            score += 0.15  # Move-in ready
        elif property.condition_score >= 5:
            score += 0.10  # Light renovation
        else:
            score += 0.03  # Major work needed

        # 5. Utilities
        utilities_available = sum([
            property.has_water,
            property.has_sewer,
            property.has_electric,
            property.has_gas
        ])
        score += utilities_available * 0.05  # Up to 0.20

        return LiquidityAnalysis(
            score=min(1.0, score),
            estimated_dom=self._estimate_days_on_market(score),
            buyer_pool_size=self._estimate_buyer_pool(property),
            recommended_discount=self._quick_sale_discount(score)
        )

    def _estimate_days_on_market(self, score: float) -> int:
        """Сколько дней на рынке до продажи"""
        if score >= 0.8:
            return 14  # 2 недели
        elif score >= 0.6:
            return 45  # 1.5 месяца
        elif score >= 0.4:
            return 90  # 3 месяца
        else:
            return 180  # 6+ месяцев (или не продастся)
```

### Факторы ликвидности для Miw

| Фактор | High Liquidity ✅ | Low Liquidity ⚠️ |
|--------|------------------|------------------|
| **Цена** | $50K-$300K | >$500K или <$10K |
| **Локация** | В городе, рядом с магазинами | Далеко от всего |
| **Тип** | Дом, таунхаус | Vacant land, commercial |
| **Дорога** | Paved road | Dirt или no access |
| **Utilities** | Все подключены | Нет воды/электричества |
| **Состояние** | Жить можно сразу | Нужен капремонт |
| **Школы** | Хороший рейтинг | Плохие школы |
| **DOM в районе** | <30 дней | >90 дней |

### Flip Potential Score

```
Flip Potential = (ARV - Purchase - Renovation - Costs) / Investment

Где:
- ARV = After Repair Value (цена после ремонта)
- Purchase = Цена покупки на auction
- Renovation = Стоимость ремонта (оценка)
- Costs = Holding costs, closing costs (~10% ARV)

Хороший flip: ROI >= 20% за 6 месяцев
Отличный flip: ROI >= 30% за 6 месяцев
```

### Для стратегии Miw (Staircase)

| Шаг | Liquidity важна? | Почему |
|-----|------------------|--------|
| Шаг 1 ($1K→$10K) | ⚠️ Низкая | Vacant land = дольше продавать |
| Шаг 2 ($10K→$25K) | ➡️ Средняя | Rural houses = меньше покупателей |
| Шаг 3-5 ($25K→$100K) | ✅ Высокая | Входим в sweet spot |
| Шаг 6-8 ($100K→$500K) | ✅ Очень высокая | Maximum buyer pool |

**Вывод:** Первые шаги будут медленнее (6-12 месяцев на продажу), но по мере роста капитала ликвидность увеличивается.

---

## 🗺️ Карты: Геоанализ для property

> *"Отдельно что можешь сказать про карты?"*

### Типы карт и что они показывают

| Тип карты | Что узнаём | Бесплатный источник | Критичность |
|-----------|-----------|---------------------|-------------|
| **Parcel Map** | Границы, размер участка | County GIS Portal | ⭐⭐⭐ MUST |
| **Flood Zone** | Риск затопления | FEMA Flood Map | ⭐⭐⭐ MUST |
| **Zoning Map** | Что можно строить | County Planning | ⭐⭐⭐ MUST |
| **Topographic** | Рельеф, склоны | USGS TopoView | ⭐⭐ Important |
| **Soil Map** | Тип почвы (для septic) | USDA Web Soil Survey | ⭐⭐ Important |
| **Crime Map** | Безопасность района | CrimeMapping.com | ⭐⭐ Important |
| **School District** | Какие школы | GreatSchools.org | ⭐⭐ Important |
| **Utilities Map** | Где проведены коммуникации | County/City utilities | ⭐⭐ Important |
| **Future Development** | Планы застройки | City Planning Dept | ⭐ Nice to have |
| **Historic District** | Ограничения на изменения | County Historic | ⭐ Nice to have |

### FEMA Flood Zones (критично!)

```
Zone X    = Minimal flood risk ✅ SAFE
Zone X500 = 0.2% annual risk (500-year flood) ⚠️ OK
Zone A    = 1% annual risk (100-year flood) ❌ AVOID
Zone AE   = 1% risk + base elevation determined ❌ AVOID
Zone V/VE = Coastal high hazard ❌❌ NEVER BUY
```

**Почему важно:**
- Flood insurance = $500-$3,000/год дополнительно
- Банки требуют страховку для mortgage
- Resale сложнее (меньше покупателей)

### Zoning Codes (основные)

| Code | Значение | Что можно |
|------|----------|-----------|
| R-1 | Residential Single Family | Один дом |
| R-2, R-3 | Residential Multi-Family | Дуплекс, триплекс |
| A, AG | Agricultural | Ферма, животные |
| C-1, C-2 | Commercial | Магазин, офис |
| I-1, I-2 | Industrial | Склад, фабрика |
| PUD | Planned Unit Development | Смешанное по плану |

### Map Analysis Checklist для Miw

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      MAP ANALYSIS CHECKLIST                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Property: ____________________________  Parcel: _________________          │
│                                                                             │
│  PARCEL MAP (County GIS)                                                    │
│  □ Границы участка найдены                                                  │
│  □ Размер участка: _________ acres / sq ft                                 │
│  □ Форма участка: □ Regular □ Irregular □ Flag lot                        │
│  □ Road frontage: _________ feet                                           │
│                                                                             │
│  FLOOD MAP (FEMA)                                                           │
│  □ Flood Zone: _________                                                    │
│  □ Zone X (minimal risk)?  □ Yes ✅  □ No ⚠️                               │
│  □ Требуется flood insurance?  □ Yes  □ No                                 │
│                                                                             │
│  ZONING MAP                                                                 │
│  □ Zoning code: _________                                                   │
│  □ Разрешено жильё?  □ Yes  □ No                                          │
│  □ Можно построить дом?  □ Yes  □ No  □ With variance                     │
│  □ Minimum lot size met?  □ Yes  □ No                                      │
│                                                                             │
│  TOPOGRAPHIC / SOIL                                                         │
│  □ Terrain: □ Flat □ Slope <15% □ Steep >15%                              │
│  □ Soil suitable for septic?  □ Yes  □ No  □ N/A (sewer available)        │
│                                                                             │
│  UTILITIES (from map/county)                                                │
│  □ Water: □ City □ Well needed □ None                                      │
│  □ Sewer: □ City □ Septic needed □ None                                    │
│  □ Electric: □ Available □ Bring to lot ($______)                          │
│  □ Gas: □ Available □ Propane □ None                                       │
│  □ Internet: □ Cable □ DSL □ Satellite only                                │
│                                                                             │
│  NEIGHBORHOOD (Crime, Schools)                                              │
│  □ Crime level: □ Low □ Medium □ High                                      │
│  □ Nearest school: _______________ Rating: ___/10                          │
│  □ School district: _______________                                         │
│                                                                             │
│  RED FLAGS FROM MAPS                                                        │
│  □ In flood zone (A, AE, V)?                                               │
│  □ No road access visible?                                                  │
│  □ Landlocked parcel?                                                       │
│  □ In industrial zone?                                                      │
│  □ Near landfill/power lines/railroad?                                     │
│  □ Steep terrain (>25%)?                                                    │
│                                                                             │
│  OVERALL MAP ASSESSMENT                                                     │
│  □ All clear - proceed ✅                                                   │
│  □ Minor issues - investigate further ⚠️                                   │
│  □ Major red flags - SKIP ❌                                                │
│                                                                             │
│  Notes: ________________________________________________________________   │
│  ______________________________________________________________________    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Как найти карты (пошагово для Miw)

**1. Parcel Map:**
```
Google: "[County name] GIS" или "[County name] parcel map"
Пример: "Pinal County AZ GIS"
→ Ищи Parcel ID или адрес
→ Увидишь границы участка
```

**2. Flood Map:**
```
1. Иди на: msc.fema.gov/portal/search
2. Введи адрес
3. Увидишь зону (X = хорошо, A/AE = плохо)
```

**3. Zoning:**
```
Google: "[County/City name] zoning map"
Или позвони в County Planning: "What is the zoning for parcel [ID]?"
```

**4. Все в одном (если повезёт):**
```
Многие County GIS показывают ВСЁ на одной карте:
- Parcel boundaries
- Flood zones
- Zoning
- Aerial photos
- Owner info
```

### Map Red Flags (сразу отказаться)

| Red Flag | Что это значит | Как увидеть на карте |
|----------|---------------|---------------------|
| 🚫 **Landlocked** | Нет доступа с дороги | Parcel окружён другими |
| 🚫 **Flood Zone A/V** | Затопление каждый год | FEMA map = синий |
| 🚫 **No utilities** | Дорого подключать | Нет линий рядом |
| 🚫 **Steep slope** | Строить сложно/дорого | Contour lines близко |
| 🚫 **Wetlands** | Нельзя строить | Зелёная зона на карте |
| 🚫 **Industrial nearby** | Шум, запах, toxins | Zoning map = I-1, I-2 |

---

## 🧠 Deep Learning: Где применимо

> *"Как можем использовать Deep Learning?"*

### DL Use Cases для Tax Lien системы

| Use Case | Модель | Input | Output | Ценность для Miw |
|----------|--------|-------|--------|------------------|
| **Property Photo Analysis** | CNN (EfficientNet-B4) | Street View фото | condition_score, abandoned_prob | Оценка без поездки |
| **Satellite Change Detection** | U-Net / Siamese CNN | Satellite 2019 vs 2024 | changes: "new building", "demolition" | История изменений |
| **Roof Condition** | CNN + Object Detection | Aerial/satellite | roof_score, damage_detected | Оценка ремонта |
| **Document OCR** | TrOCR / Donut | Сканы tax records | Структурированные данные | Автопарсинг |
| **Legal Description NLP** | BERT fine-tuned | "Lot 5 Block 3 of..." | Parcel boundaries | Понимание описаний |
| **Code Violation Analysis** | BERT / GPT | "Overgrown weeds, trash" | severity_score, karma_impact | Karma Score |
| **Price Prediction** | LSTM / Transformer | История цен в районе | future_price_6mo | ROI прогноз |
| **Personalized Recommendations** | Two-Tower Neural | User preferences + property features | match_score | Персональный поиск |

### 1. Property Photo Analysis (Model 24 Enhanced)

```python
class DeepPropertyAnalyzer:
    """
    CNN-based property condition analysis from photos.

    Architecture: EfficientNet-B4 + Custom head
    Training: Fine-tuned on 50K+ labeled property photos
    """

    def __init__(self):
        self.model = EfficientNetB4(weights="imagenet")
        self.custom_head = nn.Sequential(
            nn.Linear(1792, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Linear(128, 6)  # 6 outputs
        )

    def analyze(self, street_view_url: str) -> PhotoAnalysis:
        """
        Returns:
        - condition_score: 1-10
        - abandoned_probability: 0.0-1.0
        - maintenance_level: poor/fair/good/excellent
        - visible_issues: ["broken_window", "roof_damage", ...]
        - curb_appeal: 1-10
        - estimated_repair_cost: $XXX (rough)
        """
        image = self._fetch_image(street_view_url)
        features = self.model(image)
        outputs = self.custom_head(features)
        return self._decode_outputs(outputs)
```

**Training Data Sources:**
- Zillow property photos (labeled by sale price delta)
- Code violation photos from cities
- Before/after renovation photos
- Manually labeled abandoned properties

### 2. Satellite Change Detection

```python
class SatelliteChangeDetector:
    """
    Siamese CNN for detecting changes between satellite images.

    Use case: "Was there a building in 2019? Is it still there in 2024?"
    """

    def detect_changes(
        self,
        image_old: np.ndarray,  # 2019
        image_new: np.ndarray   # 2024
    ) -> ChangeAnalysis:
        """
        Returns:
        - change_detected: bool
        - change_type: "new_construction", "demolition", "expansion", "no_change"
        - change_area_sqft: estimated
        - confidence: 0.0-1.0
        """
        # Siamese network compares two images
        features_old = self.encoder(image_old)
        features_new = self.encoder(image_new)
        diff = self.comparator(features_old, features_new)
        return self._classify_change(diff)
```

**Для Miw:** Видеть историю участка без посещения. Пример: "В 2019 был дом, в 2024 - пустой участок. Что случилось?"

### 3. Document OCR (для старых records)

```python
class TaxDocumentOCR:
    """
    OCR for scanned tax documents, assessor cards, legal descriptions.

    Model options (ALL self-hosted, NO paid APIs):
    - Tesseract (free, basic)
    - TrOCR (open-source, self-hosted)
    - Donut (open-source, self-hosted)
    """

    def extract(self, document_image: bytes) -> ExtractedData:
        """
        Input: Scanned PDF/image of tax record
        Output: Structured data

        Example output:
        {
            "parcel_id": "123-45-678",
            "owner_name": "John Smith",
            "legal_description": "Lot 5, Block 3, Desert Vista Subdivision",
            "assessed_value": 45000,
            "tax_amount": 892.50,
            "delinquent_years": [2021, 2022, 2023]
        }
        """
```

**Ценность:** Многие rural counties ещё на бумаге. DL позволит автопарсить сканы.

### 4. Code Violation NLP

```python
class CodeViolationAnalyzer:
    """
    BERT-based analysis of code violation text.

    Input: "Property has overgrown weeds, abandoned vehicle,
            broken windows, graffiti on walls"

    Output: Structured severity + karma impact
    """

    def analyze(self, violation_text: str) -> ViolationAnalysis:
        """
        Returns:
        - severity_score: 1-10
        - violation_types: ["vegetation", "vehicle", "structure", "vandalism"]
        - estimated_cleanup_cost: $XXX
        - karma_impact: +0.3 (abandoned = good karma to fix)
        - abandoned_indicator: 0.85 (high probability abandoned)
        """
        embeddings = self.bert.encode(violation_text)
        return self.classifier(embeddings)
```

### 5. Personalized Property Recommendations

```python
class PropertyRecommender:
    """
    Two-Tower Neural Network for matching investors to properties.

    Tower 1: Investor embedding (preferences, history, budget)
    Tower 2: Property embedding (features, location, scores)

    Output: Similarity score (how well property matches investor)
    """

    def __init__(self):
        self.investor_tower = nn.Sequential(...)  # Encodes investor
        self.property_tower = nn.Sequential(...)  # Encodes property

    def recommend(
        self,
        investor: InvestorProfile,
        properties: List[Property],
        top_k: int = 10
    ) -> List[Recommendation]:
        """
        Для Miw:
        - Budget: $1,000
        - Goal: property acquisition (not interest)
        - Risk tolerance: medium
        - Lifestyle: young family
        - Location preference: near Denis family (SD) or warm (AZ)

        → Returns top 10 properties matching her profile
        """
        investor_embedding = self.investor_tower(investor.features)

        scores = []
        for prop in properties:
            prop_embedding = self.property_tower(prop.features)
            similarity = cosine_similarity(investor_embedding, prop_embedding)
            scores.append((prop, similarity))

        return sorted(scores, key=lambda x: x[1], reverse=True)[:top_k]
```

### DL Pipeline для Miw (Simplified)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          DEEP LEARNING PIPELINE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  INPUT: Property Address                                                    │
│         ↓                                                                   │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │  Street View    │  │   Satellite     │  │  Tax Documents  │            │
│  │  Photo          │  │   Images        │  │  (if scanned)   │            │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘            │
│           │                    │                    │                      │
│           ▼                    ▼                    ▼                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │  CNN            │  │  U-Net          │  │  TrOCR          │            │
│  │  (Condition)    │  │  (Changes)      │  │  (OCR)          │            │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘            │
│           │                    │                    │                      │
│           ▼                    ▼                    ▼                      │
│  ┌─────────────────────────────────────────────────────────────┐          │
│  │                    FEATURE FUSION                            │          │
│  │  Combines: visual + change + text + tabular data            │          │
│  └──────────────────────────┬──────────────────────────────────┘          │
│                             │                                              │
│                             ▼                                              │
│  ┌─────────────────────────────────────────────────────────────┐          │
│  │                   FINAL SCORES FOR MIW                       │          │
│  │                                                              │          │
│  │  • Condition Score: 7/10 (from CNN)                         │          │
│  │  • Change History: "Stable since 2018" (from U-Net)         │          │
│  │  • Abandoned Prob: 85% (from CNN + NLP)                     │          │
│  │  • Karma Score: +0.6 (from NLP violations)                  │          │
│  │  • Liquidity Score: 0.4 (rural land)                        │          │
│  │  • RECOMMENDATION: BUY ✅                                    │          │
│  └─────────────────────────────────────────────────────────────┘          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Когда НЕ нужен Deep Learning

| Задача | Лучше использовать | Почему |
|--------|-------------------|--------|
| Redemption prediction | XGBoost/LightGBM | Табличные данные, DL overkill |
| Karma Score | Rule-based + логика | Прозрачность важнее точности |
| Flood zone check | FEMA API lookup | Уже есть данные |
| Liquidity score | Gradient Boosting | Табличные features |

**Правило:** DL нужен когда данные = изображения, текст, последовательности. Для табличных данных XGBoost/LightGBM обычно лучше.

### ⚠️ ОГРАНИЧЕНИЕ: Только self-hosted решения

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ЗАПРЕЩЕНО: Внешние платные API                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Причины:                                                                   │
│  1. НЕТ БЮДЖЕТА на оплату внешних сервисов                                 │
│  2. Качество внешних сервисов МОЖЕТ МЕНЯТЬСЯ                               │
│  3. Нельзя полагаться на внешние зависимости                               │
│                                                                             │
│  ✗ OpenAI Vision API                                                       │
│  ✗ Google Vision API                                                       │
│  ✗ OpenAI GPT-4 API                                                        │
│  ✗ Любые платные API                                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Self-hosted альтернативы

| Компонент | Self-hosted решение | Примечание |
|-----------|---------------------|------------|
| Photo Analysis | **YOLO / Custom CNN** | Локальный inference, GPU optional |
| OCR | **Tesseract / TrOCR (local)** | Open source, self-hosted |
| NLP | **Fine-tuned BERT / Llama** | Local LLM, no API calls |
| Recommendations | **Simple heuristics** | Rule-based, прозрачно |

**Для MVP Miw:** Ручной анализ фото + Tesseract OCR (бесплатно, локально).

---

## 📋 Полный пакет документов на property + владельца

> *"Какие документы дополнительно по объектам можно предоставлять распечатанными?"*

### Уровень 1: Базовый пакет на property (ВСЕГДА)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DOCUMENT PACKAGE: PROPERTY LEVEL                         │
│                    ══════════════════════════════════                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. PROPERTY ANALYSIS SHEET (наш шаблон)           □ Printed               │
│     - Все scores, checklist, решение                                       │
│                                                                             │
│  2. TAX HISTORY (5+ лет)                           □ Printed               │
│     - Год | Assessed Value | Tax Amount | Paid? | Date Paid               │
│     - Источник: County Treasurer website                                   │
│                                                                             │
│  3. PARCEL MAP (County GIS)                        □ Printed               │
│     - Границы участка, размеры                                             │
│     - Соседние parcels                                                     │
│                                                                             │
│  4. FLOOD MAP (FEMA)                               □ Printed               │
│     - Flood zone determination                                             │
│                                                                             │
│  5. ZONING INFO                                    □ Printed               │
│     - Zoning code, что разрешено                                           │
│                                                                             │
│  6. PHOTOS (4 шт)                                  □ Printed               │
│     - Street View (current + historical)                                   │
│     - Satellite                                                            │
│     - Assessor photo (if available)                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Уровень 2: Исторические данные (РЕКОМЕНДУЕТСЯ)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DOCUMENT PACKAGE: HISTORICAL DATA                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  7. ASSESSMENT HISTORY (10+ лет)                   □ Printed               │
│     ┌──────┬────────────┬────────────┬────────────┐                        │
│     │ Year │ Land Value │ Impr Value │ Total      │                        │
│     ├──────┼────────────┼────────────┼────────────┤                        │
│     │ 2024 │ $8,500     │ $0         │ $8,500     │                        │
│     │ 2023 │ $8,200     │ $0         │ $8,200     │                        │
│     │ 2022 │ $7,800     │ $0         │ $7,800     │                        │
│     │ ...  │ ...        │ ...        │ ...        │                        │
│     └──────┴────────────┴────────────┴────────────┘                        │
│     → Тренд: рост/падение/стабильно                                        │
│                                                                             │
│  8. DEED HISTORY (все transfers)                   □ Printed               │
│     ┌────────────┬─────────────────┬─────────────┬───────────┐             │
│     │ Date       │ Grantor (from)  │ Grantee (to)│ Price     │             │
│     ├────────────┼─────────────────┼─────────────┼───────────┤             │
│     │ 2019-03-15 │ ABC Holdings LLC│ XYZ LLC     │ $12,000   │             │
│     │ 2015-08-22 │ John Smith      │ ABC Holdings│ $8,500    │             │
│     │ 2008-01-10 │ County (tax sale)│ John Smith │ $3,200    │             │
│     └────────────┴─────────────────┴─────────────┴───────────┘             │
│     → Источник: County Recorder                                            │
│                                                                             │
│  9. LIEN HISTORY (all liens on property)           □ Printed               │
│     - Tax liens (current + past)                                           │
│     - IRS liens                                                            │
│     - HOA liens                                                            │
│     - Mechanic's liens                                                     │
│     - Judgment liens                                                       │
│     → Источник: County Recorder + Court records                            │
│                                                                             │
│  10. CODE VIOLATIONS HISTORY                       □ Printed               │
│      ┌────────────┬─────────────────────────┬──────────┐                   │
│      │ Date       │ Violation               │ Status   │                   │
│      ├────────────┼─────────────────────────┼──────────┤                   │
│      │ 2023-06-15 │ Overgrown weeds         │ Open     │                   │
│      │ 2022-11-20 │ Abandoned vehicle       │ Resolved │                   │
│      │ 2021-03-08 │ Trash accumulation      │ Resolved │                   │
│      └────────────┴─────────────────────────┴──────────┘                   │
│      → Источник: City Code Enforcement                                     │
│                                                                             │
│  11. PERMIT HISTORY                                □ Printed               │
│      - Building permits (new construction, additions)                      │
│      - Electrical/plumbing permits                                         │
│      - Demolition permits                                                  │
│      → Показывает: были ли улучшения, законные ли                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Уровень 3: OWNER PORTFOLIO (КРИТИЧЕСКИ ВАЖНО!)

> *"Какими другими объектами владеет собственник?"*

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OWNER PORTFOLIO ANALYSIS                                 │
│                    ════════════════════════                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  OWNER: Desert Holdings LLC                                                 │
│  STATUS: ❌ DISSOLVED (2021-03-15)                                          │
│  REGISTERED AGENT: None (expired)                                           │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  OWNER PORTFOLIO SUMMARY                                                    │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  Total Properties Owned: 7                                                  │
│  Total Assessed Value: $89,500                                              │
│  Properties with Tax Liens: 7 (100%) ← RED FLAG FOR OWNER, GREEN FOR US!   │
│  Total Delinquent Amount: $12,340                                           │
│                                                                             │
│  ┌─────┬────────────────────┬──────────┬───────────┬────────────┬─────────┐│
│  │ #   │ Property Address   │ County   │ Value     │ Delinquent │ Years   ││
│  ├─────┼────────────────────┼──────────┼───────────┼────────────┼─────────┤│
│  │ 1   │ 123 Desert View Rd │ Pinal    │ $12,500   │ $1,890     │ 3 yrs   ││
│  │ 2   │ 456 Cactus Ln      │ Pinal    │ $8,200    │ $1,240     │ 3 yrs   ││
│  │ 3   │ 789 Mesa Dr        │ Pinal    │ $15,800   │ $2,150     │ 2 yrs   ││
│  │ 4   │ Parcel 234-56-789  │ Maricopa │ $22,000   │ $3,200     │ 4 yrs   ││
│  │ 5   │ Parcel 345-67-890  │ Yavapai  │ $18,500   │ $2,100     │ 2 yrs   ││
│  │ 6   │ 111 Sand St        │ Cochise  │ $6,500    │ $980       │ 3 yrs   ││
│  │ 7   │ 222 Dust Rd        │ Cochise  │ $6,000    │ $780       │ 2 yrs   ││
│  └─────┴────────────────────┴──────────┴───────────┴────────────┴─────────┘│
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  ANALYSIS                                                                   │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  Pattern: SERIAL NON-PAYER                                                  │
│  - 100% of properties delinquent                                            │
│  - LLC dissolved = no one to redeem                                         │
│  - Average delinquency: 2.7 years                                           │
│                                                                             │
│  REDEMPTION PROBABILITY: 2% (VERY LOW) ✅                                   │
│  FORECLOSURE PROBABILITY: 95% (VERY HIGH) ✅                                │
│                                                                             │
│  RECOMMENDATION: EXCELLENT TARGET FOR MIAW                                  │
│  - Consider buying liens on MULTIPLE properties from this owner            │
│  - Total investment: $12,340 → Potential value: $89,500                    │
│  - If ANY forecloses, ROI is massive                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Если у владельца > 10 properties

> *"А если у собственника более 10 объектов?"*

**Стратегия:** Summary page + детали только на TOP 5 candidates

```
┌─────────────────────────────────────────────────────────────────────────────┐
│           OWNER PORTFOLIO: LARGE PORTFOLIO (10+ PROPERTIES)                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  OWNER: Mega Investments LLC                                                │
│  TOTAL PROPERTIES: 47                                                       │
│  ACROSS COUNTIES: Maricopa, Pinal, Pima, Yavapai, Cochise (5 counties)     │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  PORTFOLIO STATISTICS (SUMMARY)                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  Total Assessed Value:      $1,245,000                                      │
│  Total Delinquent:          $187,500 (across 32 properties)                │
│  Properties Current:        15 (32%)                                        │
│  Properties Delinquent:     32 (68%)                                        │
│  Average Delinquency:       2.1 years                                       │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  DELINQUENCY BY COUNTY                                              │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │  County     │ Total │ Delinquent │ % │ Total Owed │               │   │
│  │  Maricopa   │ 18    │ 12         │ 67% │ $45,200  │               │   │
│  │  Pinal      │ 15    │ 11         │ 73% │ $38,100  │               │   │
│  │  Pima       │ 8     │ 5          │ 63% │ $52,300  │               │   │
│  │  Yavapai    │ 4     │ 3          │ 75% │ $31,400  │               │   │
│  │  Cochise    │ 2     │ 1          │ 50% │ $20,500  │               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  TOP 5 CANDIDATES (sorted by Value/Lien ratio)                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  #1: Parcel 123-45-678 (Pinal)                                             │
│      Value: $45,000 | Lien: $2,100 | Ratio: 21x | Years: 4 ⭐ BEST         │
│      → Full analysis sheet attached (Page 5)                               │
│                                                                             │
│  #2: Parcel 234-56-789 (Maricopa)                                          │
│      Value: $38,000 | Lien: $1,850 | Ratio: 20x | Years: 3                 │
│      → Full analysis sheet attached (Page 8)                               │
│                                                                             │
│  #3: 456 Desert Rd (Yavapai)                                               │
│      Value: $28,500 | Lien: $1,520 | Ratio: 19x | Years: 3                 │
│      → Full analysis sheet attached (Page 11)                              │
│                                                                             │
│  #4: 789 Cactus Way (Pinal)                                                │
│      Value: $22,000 | Lien: $1,200 | Ratio: 18x | Years: 2                 │
│      → Full analysis sheet attached (Page 14)                              │
│                                                                             │
│  #5: Parcel 567-89-012 (Cochise)                                           │
│      Value: $18,000 | Lien: $980 | Ratio: 18x | Years: 3                   │
│      → Full analysis sheet attached (Page 17)                              │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  REMAINING 27 PROPERTIES (SUMMARY ONLY)                                    │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  See Appendix A for full list with:                                        │
│  - Parcel ID, Address, County                                              │
│  - Assessed Value, Lien Amount                                             │
│  - Years Delinquent                                                        │
│  (No detailed analysis - request if interested)                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Уровень 4: Owner Deep Dive (для крупных владельцев)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OWNER DEEP DIVE: ENTITY RESEARCH                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ENTITY INFORMATION                                                         │
│  ═══════════════════                                                        │
│                                                                             │
│  Legal Name: Desert Holdings LLC                                            │
│  Entity Type: Limited Liability Company                                     │
│  State of Formation: Arizona                                                │
│  Formation Date: 2015-06-22                                                 │
│  Status: ❌ ADMINISTRATIVELY DISSOLVED (2021-03-15)                         │
│  Reason: Failure to file annual report                                      │
│                                                                             │
│  Registered Agent: John Smith (EXPIRED)                                     │
│  Principal Address: 123 Main St, Phoenix, AZ 85001 (may be outdated)       │
│                                                                             │
│  OFFICERS/MEMBERS (at dissolution)                                          │
│  ═══════════════════════════════════                                        │
│  - John Smith (Manager) - Last known: 123 Main St, Phoenix                 │
│  - Jane Doe (Member) - Last known: 456 Oak Ave, Tempe                      │
│                                                                             │
│  RELATED ENTITIES (same officers)                                           │
│  ═════════════════════════════════                                          │
│  - Desert Investments Inc (DISSOLVED 2020)                                  │
│  - Sunshine Properties LLC (DISSOLVED 2019)                                 │
│  - Cactus Land Holdings (ACTIVE) ← May have transferred assets!            │
│                                                                             │
│  COURT RECORDS                                                              │
│  ════════════════                                                           │
│  - 2020-CV-12345: Judgment vs Desert Holdings ($45,000) - Unpaid           │
│  - 2019-CV-98765: Foreclosure action by Bank of AZ - Completed             │
│                                                                             │
│  BANKRUPTCY                                                                 │
│  ═══════════════                                                            │
│  No bankruptcy filings found for entity or known officers.                 │
│                                                                             │
│  ANALYSIS                                                                   │
│  ═════════                                                                  │
│  This appears to be a "zombie" LLC - dissolved with no active management.  │
│  Properties are effectively abandoned. No one will redeem.                  │
│  EXCELLENT foreclosure candidates.                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Структура полного пакета документов

```
📁 Property_Package_123-45-678/
│
├── 📄 00_SUMMARY.pdf                    ← 1-page executive summary
│
├── 📁 01_Property_Analysis/
│   ├── Property_Analysis_Sheet.pdf      ← Наш шаблон с решением
│   ├── Photos_Collage.pdf               ← 4 фото на странице
│   └── Map_Analysis_Checklist.pdf
│
├── 📁 02_Property_History/
│   ├── Tax_History_10yr.pdf
│   ├── Assessment_History.pdf
│   ├── Deed_History.pdf
│   ├── Lien_History.pdf
│   ├── Code_Violations.pdf
│   └── Permit_History.pdf
│
├── 📁 03_Maps/
│   ├── Parcel_Map.pdf
│   ├── Flood_Zone_FEMA.pdf
│   ├── Zoning_Map.pdf
│   └── Satellite_Images.pdf
│
├── 📁 04_Owner_Analysis/                ← НОВОЕ!
│   ├── Owner_Portfolio_Summary.pdf
│   ├── Owner_Entity_Info.pdf            ← (if LLC)
│   ├── Related_Entities.pdf             ← (if any)
│   └── Owner_Other_Properties/
│       ├── Property_2_Summary.pdf
│       ├── Property_3_Summary.pdf
│       └── ... (только если <= 10)
│
└── 📁 05_Appendices/
    ├── County_Tax_Records_Screenshots.pdf
    ├── Legal_Description.pdf
    └── Source_URLs.txt                  ← Где взяли данные
```

### Правила для разных размеров портфеля

| Owner Portfolio Size | Документы | Почему |
|---------------------|-----------|--------|
| **1 property** | Полный пакет на property + owner info | Единственный объект |
| **2-5 properties** | Полный пакет на target + summary на остальные | Видим паттерн |
| **6-10 properties** | Полный пакет на target + 1-page summary на каждый | Контекст |
| **11-50 properties** | Полный на target + TOP 5 detailed + list остальных | Фокус на лучших |
| **50+ properties** | Summary only + TOP 10 detailed | Это investor/fund |

### Источники данных для Owner Research

| Данные | Источник | Бесплатно? |
|--------|----------|-----------|
| Properties owned in county | County Assessor/GIS | ✅ Yes |
| Properties in other counties | Multi-county search | ⚠️ Manual |
| LLC info | State Secretary of State | ✅ Yes |
| Court records | County Court website | ✅ Usually |
| Bankruptcy | PACER | ⚠️ $0.10/page |
| Skip tracing (contact info) | BeenVerified, Spokeo | ❌ $1-5 |

### Автоматизация через систему

```python
class OwnerPortfolioAnalyzer:
    """
    Finds all properties owned by same owner across counties.
    """

    def analyze_owner(self, owner_name: str, counties: List[str]) -> OwnerPortfolio:
        """
        1. Search owner name in each county's assessor database
        2. Match by exact name + fuzzy matching
        3. Aggregate all properties
        4. Calculate portfolio statistics
        5. Score redemption probability
        """

        all_properties = []
        for county in counties:
            props = self.search_county(county, owner_name)
            all_properties.extend(props)

        # Deduplicate (same property listed differently)
        unique_properties = self.deduplicate(all_properties)

        return OwnerPortfolio(
            owner_name=owner_name,
            total_properties=len(unique_properties),
            properties=unique_properties,
            total_value=sum(p.assessed_value for p in unique_properties),
            total_delinquent=sum(p.delinquent_amount for p in unique_properties),
            delinquency_rate=self._calc_delinquency_rate(unique_properties),
            serial_payer_score=self._calc_serial_payer_score(unique_properties),
            redemption_probability=self._predict_redemption(unique_properties)
        )
```

---

## 👀 Физический осмотр: Преимущество семьи Denis

> *"Фишка семьи Дениса в том, что они могут посмотреть недвижку до покупки. Как понять что объект фундаментально хорош?"*

### Стратегическое преимущество

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  ДРУГИЕ ИНВЕСТОРЫ                    СЕМЬЯ DENIS                            │
│  ══════════════════                  ══════════════                         │
│                                                                             │
│  Покупают по фото/данным             Физический осмотр ДО покупки          │
│         ↓                                     ↓                             │
│  Риск: неизвестное состояние         Видят реальное состояние              │
│         ↓                                     ↓                             │
│  Часто переплачивают или             Покупают только то, что               │
│  получают проблемы                   ДЕЙСТВИТЕЛЬНО хорошо                  │
│                                                                             │
│  РЕЗУЛЬТАТ: Их конкурентное преимущество = informed decisions              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Dual Purpose: Flip ИЛИ Keep

```
Семья Denis смотрит property
        │
        ├── "Хорошо для flip" → Покупаем, быстро продаём
        │
        └── "Отлично для жизни!" → Оставляем себе (Miw & Denis)
```

---

### КРАСИВО ≠ ХОРОШО (ловушки)

| Что видите | Что может скрывать | Как проверить |
|------------|-------------------|---------------|
| 🎨 **Свежая краска везде** | Трещины, плесень, пятна воды | Простучать стены, понюхать |
| 🌳 **Идеальный двор** | Проблемы с drainage, foundation | Смотреть после дождя |
| ✨ **Новая кухня/ванная** | Старая проводка, гнилые трубы | Открыть под раковиной |
| 🚪 **Новые двери/окна** | Неровный foundation (settling) | Проверить закрываются ли ровно |
| 🏠 **"Недавний ремонт"** | Flip gone wrong, дешёвые материалы | Смотреть качество работ |

### СТРАШНО ≠ ПЛОХО (возможности!)

| Что видите | Что на самом деле | Потенциал |
|------------|-------------------|-----------|
| 😱 **Облезлая краска** | Просто косметика, $500-2000 fix | ✅ HIGH |
| 🌿 **Заросший двор** | 1 день работы, $200 | ✅ HIGH |
| 📦 **Мусор внутри** | Убрать за $500, структура OK | ✅ HIGH |
| 👴 **"Бабушкин" интерьер** | Дома 60-70х = solid bones | ✅ VERY HIGH |
| 🪟 **Грязные окна** | Просто помыть | ✅ HIGH |

---

### ФУНДАМЕНТАЛЬНЫЕ ПРОВЕРКИ (Denis Family Checklist)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│          DENIS FAMILY PHYSICAL INSPECTION CHECKLIST                         │
│          ══════════════════════════════════════════                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ⚠️ ВНИМАНИЕ: Это НЕ замена профессиональной инспекции!                    │
│  Но для ПЕРВИЧНОЙ оценки "стоит ли вообще рассматривать"                   │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  LEVEL 1: СНАРУЖИ (5-10 минут) - можно без входа                           │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  FOUNDATION (смотреть по периметру):                                        │
│  □ Видимые трещины?          □ Нет  □ Hairline (<1/8")  □ Major (>1/4")   │
│  □ Foundation ровный?        □ Да   □ Небольшой наклон  □ Явный наклон    │
│  □ Вода собирается у дома?   □ Нет  □ Немного           □ Лужи/эрозия     │
│  □ Vegetation у foundation?  □ Нет  □ Немного           □ Вплотную к дому │
│                                                                             │
│  🚨 RED FLAG: Трещины >1/4", ступенчатые трещины в кирпиче, дом "уходит"   │
│  💡 TIP: Принести уровень (level) - положить на foundation                 │
│                                                                             │
│  ROOF (смотреть издалека + бинокль):                                        │
│  □ Линия крыши ровная?       □ Да   □ Небольшой провис  □ Явный провис    │
│  □ Shingles на месте?        □ Да   □ Несколько нет     □ Много нет       │
│  □ Видны пятна/мох?          □ Нет  □ Немного           □ Много           │
│  □ Gutters целые?            □ Да   □ Провисают         □ Отсутствуют     │
│                                                                             │
│  🚨 RED FLAG: Провисшая линия крыши = structural problem, не просто крыша  │
│  💡 TIP: Спросить возраст крыши у соседей                                  │
│                                                                             │
│  СТЕНЫ СНАРУЖИ:                                                             │
│  □ Трещины в siding/stucco?  □ Нет  □ Косметические     □ Структурные     │
│  □ Гниль видна?              □ Нет  □ Локально          □ Обширно         │
│  □ Paint peeling?            □ Нет  □ Немного           □ Везде           │
│  □ Наклон стен?              □ Нет  □ Чуть-чуть         □ Заметно         │
│                                                                             │
│  💡 TIP: Ткнуть отвёрткой в дерево у земли - гниль = мягкое                │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  LEVEL 2: ВНУТРИ (15-20 минут) - если есть доступ                          │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  ЗАПАХ (первое впечатление):                                                │
│  □ Затхлый/сырой запах?      □ Нет  □ Слабый            □ Сильный         │
│  □ Запах плесени?            □ Нет  □ Где-то            □ Везде           │
│  □ Запах канализации?        □ Нет  □ В ванной          □ Везде           │
│  □ Химический запах?         □ Нет  □ Слабый            □ Сильный         │
│                                                                             │
│  🚨 RED FLAG: Сильный запах плесени = проблема в стенах/под полом          │
│  🚨 RED FLAG: Химический запах = возможно meth lab (AVOID!)                │
│                                                                             │
│  ПОЛЫ:                                                                      │
│  □ Ровные?                   □ Да   □ Небольшой уклон   □ Явный уклон     │
│  □ Скрипят?                  □ Нет  □ Немного           □ Сильно          │
│  □ Мягкие места?             □ Нет  □ 1-2 места         □ Много           │
│                                                                             │
│  💡 TIP: Положить шарик/мячик - куда катится? Сильный уклон = foundation   │
│  💡 TIP: Попрыгать в разных местах - пол не должен сильно прогибаться      │
│                                                                             │
│  СТЕНЫ/ПОТОЛОК ВНУТРИ:                                                      │
│  □ Трещины?                  □ Нет  □ Hairline          □ Большие         │
│  □ Пятна воды на потолке?    □ Нет  □ Старые            □ Свежие          │
│  □ Пятна воды на стенах?     □ Нет  □ Старые            □ Свежие          │
│  □ Bubbling/peeling paint?   □ Нет  □ Локально          □ Обширно         │
│                                                                             │
│  🚨 RED FLAG: Свежие пятна воды = активная протечка!                       │
│  💡 TIP: Пятна в углах комнат = крыша, пятна внизу стен = foundation       │
│                                                                             │
│  ДВЕРИ И ОКНА:                                                              │
│  □ Двери закрываются ровно?  □ Да   □ Чуть заедают      □ Не закрываются  │
│  □ Окна открываются?         □ Да   □ С трудом          □ Застряли        │
│  □ Щели вокруг рам?          □ Нет  □ Небольшие         □ Большие         │
│                                                                             │
│  🚨 RED FLAG: Двери/окна не закрываются = дом "уходит" (settling)          │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  LEVEL 3: СИСТЕМЫ (10-15 минут) - если можно включить                      │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  ЭЛЕКТРИКА:                                                                 │
│  □ Тип панели?               □ Breakers ✓ □ Fuses ⚠️   □ Неизвестно      │
│  □ Размер панели?            □ 200A ✓    □ 100A OK     □ 60A или меньше  │
│  □ Розетки работают?         □ Да        □ Частично    □ Нет             │
│  □ Розетки 3-prong?          □ Да (grounded) □ 2-prong (old)             │
│                                                                             │
│  💡 TIP: Принести простой тестер розеток ($15)                             │
│  🚨 RED FLAG: Fuse box + 60A = полная замена $5,000-15,000                  │
│                                                                             │
│  САНТЕХНИКА:                                                                │
│  □ Вода течёт?               □ Да, хорошо □ Слабый напор □ Нет воды       │
│  □ Цвет воды?                □ Чистая    □ Ржавая       □ Коричневая      │
│  □ Под раковинами сухо?      □ Да        □ Влажно       □ Течёт           │
│  □ Унитаз смывает?           □ Да        □ Плохо        □ Нет             │
│                                                                             │
│  💡 TIP: Открыть все краны одновременно - давление не должно падать сильно │
│  💡 TIP: Смотреть трубы под раковиной: медь/PEX = ✓, galvanized = ⚠️      │
│                                                                             │
│  HVAC:                                                                      │
│  □ Система включается?       □ Да        □ Шумит        □ Нет             │
│  □ Возраст системы?          □ <10 лет   □ 10-20 лет    □ >20 лет         │
│  □ Воздух из вентиляции?     □ Да        □ Слабый       □ Нет             │
│                                                                             │
│  💡 TIP: Наклейка с датой на furnace/AC unit показывает возраст            │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  LEVEL 4: BASEMENT/CRAWLSPACE/ATTIC (если есть доступ)                     │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  BASEMENT/CRAWLSPACE:                                                       │
│  □ Сухо?                     □ Да        □ Влажно       □ Вода стоит      │
│  □ Запах плесени?            □ Нет       □ Слабый       □ Сильный         │
│  □ Трещины в стенах?         □ Нет       □ Есть         □ Много           │
│  □ Белые отложения (efflo)?  □ Нет       □ Немного      □ Много           │
│                                                                             │
│  🚨 RED FLAG: Стоячая вода = серьёзная проблема с drainage/foundation      │
│  💡 TIP: Белые отложения = вода была/есть                                  │
│                                                                             │
│  ATTIC:                                                                     │
│  □ Свет пробивается?         □ Нет       □ Немного      □ Много           │
│  □ Следы воды?               □ Нет       □ Старые       □ Свежие          │
│  □ Insulation есть?          □ Да, много □ Немного      □ Нет             │
│  □ Вентиляция?               □ Да        □ Частично     □ Нет             │
│                                                                             │
│  🚨 RED FLAG: Свет через крышу = дыры, нужна замена                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### SCORING: Фундаментально хорош или нет?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FUNDAMENTAL SOUNDNESS SCORE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Подсчитать RED FLAGS из чеклиста выше:                                    │
│                                                                             │
│  FOUNDATION RED FLAGS:    _____ (трещины >1/4", наклон, вода)              │
│  ROOF RED FLAGS:          _____ (провис, много shingles нет)               │
│  WATER/MOISTURE FLAGS:    _____ (плесень, протечки, вода в basement)       │
│  STRUCTURAL FLAGS:        _____ (наклон стен, двери не закрываются)        │
│  SYSTEMS FLAGS:           _____ (fuse box, galvanized pipes, no HVAC)      │
│                                                                             │
│  TOTAL RED FLAGS:         _____                                             │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  INTERPRETATION:                                                            │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  0-1 RED FLAGS:   ✅ FUNDAMENTALLY SOUND                                   │
│                   Можно покупать! Косметика = бонус для низкой цены        │
│                                                                             │
│  2-3 RED FLAGS:   ⚠️ NEEDS INVESTIGATION                                   │
│                   Заказать professional inspection перед покупкой          │
│                   Или: снизить max bid значительно                         │
│                                                                             │
│  4-5 RED FLAGS:   ❌ STRUCTURAL CONCERNS                                   │
│                   Только если ОЧЕНЬ дёшево И семья готова к major work     │
│                   Скорее всего = Class D property                          │
│                                                                             │
│  6+ RED FLAGS:    ❌❌ WALK AWAY                                            │
│                   Даже бесплатно не брать (кроме land value)               │
│                   Это Class F = tear-down                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### ЧТО БРАТЬ НА ОСМОТР (Denis Family Kit)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INSPECTION KIT ($50-100)                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  MUST HAVE:                                                                 │
│  □ Фонарик (яркий)                           $15                           │
│  □ Телефон с камерой (фото всего!)           (уже есть)                    │
│  □ Блокнот + ручка                           $2                            │
│  □ Printed checklist (этот документ!)        $1                            │
│                                                                             │
│  NICE TO HAVE:                                                              │
│  □ Outlet tester (тестер розеток)            $15                           │
│  □ Small level (уровень)                     $10                           │
│  □ Moisture meter                            $25                           │
│  □ Tape measure (рулетка)                    $8                            │
│  □ Биноколь (для крыши)                      $20                           │
│  □ Мячик/шарик (для проверки уклона)         $1                            │
│  □ Отвёртка (тыкать в дерево)                $5                            │
│                                                                             │
│  PRO TIP: Взять старую одежду - возможно придётся лезть в crawlspace       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

---

## 🔍 Удалённая оценка фундамента (без физического осмотра)

> *"Можно ли без физического осмотра спрогнозировать качество фундамента?"*

### Да! Вот методы:

### 1. Historical Street View (главный метод)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  STREET VIEW TIMELINE ANALYSIS                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  2015 ────────── 2018 ────────── 2021 ────────── 2024                      │
│    │               │               │               │                        │
│    ▼               ▼               ▼               ▼                        │
│  ┌─────┐        ┌─────┐        ┌─────┐        ┌─────┐                      │
│  │ === │        │ === │        │ ==─ │        │ =── │  ← Линия крыши       │
│  │     │        │     │        │    \│        │   \\│    "поехала"         │
│  │     │        │     │        │     │        │     │                       │
│  └─────┘        └─────┘        └─────┘        └─────┘                      │
│  ✅ Ровно       ✅ Ровно       ⚠️ Наклон     ❌ Хуже                       │
│                                                                             │
│  ВЫВОД: Foundation settling прогрессирует → AVOID                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Что искать на исторических фото:**

| Признак | 2015 vs 2024 | Что значит |
|---------|--------------|-----------|
| Линия крыши | Была ровная → стала кривая | Foundation settling |
| Трещины в brick/stucco | Появились новые | Active movement |
| Окна/двери | Были прямые → перекосились | Structure shifting |
| Пристройки | Отделяются от main house | Differential settling |
| Ступеньки крыльца | Отошли от дома | Foundation movement |

### 2. Satellite Imagery (drainage patterns)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SATELLITE: ЧТО ИСКАТЬ                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  BAD SIGNS (риск foundation problems):                                      │
│                                                                             │
│  □ Вода стоит у дома после дождя (тёмные пятна)                            │
│  □ Дом в низине относительно соседей                                       │
│  □ Drainage направлен К дому, не ОТ дома                                   │
│  □ Нет gutters/downspouts видимых                                          │
│  □ Большие деревья очень близко к дому                                     │
│                                                                             │
│  GOOD SIGNS:                                                                │
│                                                                             │
│  □ Дом на возвышении                                                       │
│  □ Видимый slope AWAY от дома                                              │
│  □ Gutters и downspouts видны                                              │
│  □ Деревья на расстоянии от foundation                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3. Soil Data (USDA Web Soil Survey)

**Бесплатно:** websoilsurvey.nrcs.usda.gov

| Тип почвы | Foundation риск | Почему |
|-----------|----------------|--------|
| **Expansive clay** | ❌ HIGH | Расширяется/сжимается с влагой |
| **Sandy soil** | ⚠️ MEDIUM | Может быть erosion |
| **Rocky/gravel** | ✅ LOW | Стабильно |
| **Loam** | ✅ LOW | Хороший drainage |

**South Dakota (Spearfish area):** В основном стабильные почвы, но проверять конкретный участок.

### 4. Topography (USGS)

| Рельеф | Foundation риск |
|--------|----------------|
| Flat | ✅ Usually OK |
| Gentle slope away from house | ✅ GOOD (drainage) |
| Slope toward house | ❌ BAD (water collects) |
| Hillside | ⚠️ Sliding risk |
| Bottom of hill | ❌ Water collects |

### 5. Permit History (County Records)

**Искать:**
```
□ "Foundation repair" permits → Была проблема!
□ "Underpinning" permits → Серьёзная проблема была
□ "French drain" permits → Проблема с водой
□ "Sump pump" permits → Вода в basement
□ "Structural repair" permits → Что-то было не так
```

**Где искать:** County Building Department website или позвонить.

### 6. Building Age + Construction Type

| Эпоха | Типичные проблемы | Foundation риск |
|-------|-------------------|----------------|
| **Pre-1950** | Старые методы, возможно без rebar | ⚠️ MEDIUM-HIGH |
| **1950-1970** | Solid construction era | ✅ Often GOOD |
| **1970-1990** | Varies, some cost-cutting | ⚠️ MEDIUM |
| **1990-2005** | Often good, but check builder | ✅ Usually OK |
| **2005-2010** | Boom era = rushed construction | ⚠️ CHECK CAREFULLY |
| **Post-2010** | Modern codes, usually OK | ✅ Usually GOOD |

### 7. Price History Anomalies

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PRICE HISTORY RED FLAGS                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Timeline:    2018 ──── 2020 ──── 2021 ──── 2022 ──── Now                  │
│  Price:       $150K     Listed    Delisted  Listed    Tax Sale             │
│                         $145K     (failed)  $120K     $??                  │
│                                                                             │
│  🚨 RED FLAG: Цена ПАДАЕТ + multiple failed sales = hidden problem         │
│                                                                             │
│  Также подозрительно:                                                       │
│  • Продажа значительно ниже рынка                                          │
│  • Много продаж за короткий период (flippers отказываются)                 │
│  • "As-is" в листинге = seller знает о проблемах                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 8. Neighborhood Pattern Analysis

```
Если у соседей проблемы с foundation → вероятно и здесь тоже!

Как узнать:
□ Google "foundation problems [neighborhood name]"
□ Google "[subdivision name] settlement issues"
□ Look at Street View других домов на улице
□ Zillow/Redfin comments on nearby sold homes
□ Local Facebook groups
```

### 9. Insurance/Claims Data (сложно получить)

| Источник | Доступность | Что узнать |
|----------|------------|------------|
| CLUE report | Только для owner/buyer | Past insurance claims |
| FEMA claims | Public (flood only) | Flood history |
| Local news | Public | "Foundation problems in [area]" |

### 10. Assessor Photos Over Time

Некоторые counties хранят assessor photos за разные годы:
- Сравнить фото 2015 vs 2020 vs 2024
- Искать изменения в структуре

---

### Remote Foundation Assessment Score (Model 35?)

```python
class RemoteFoundationAssessor:
    """
    Прогноз состояния foundation БЕЗ физического осмотра.

    Confidence: 60-75% (не замена осмотру, но хороший фильтр)
    """

    def assess(self, property: PropertyData) -> FoundationRisk:
        risk_score = 0.0

        # Historical Street View changes
        if self.detect_roofline_change(property.street_view_history):
            risk_score += 0.3  # Major red flag

        # Soil type
        soil = self.get_soil_type(property.location)
        if soil == "expansive_clay":
            risk_score += 0.2

        # Topography
        if self.is_in_low_spot(property.location):
            risk_score += 0.15

        # Building age
        if property.year_built < 1950:
            risk_score += 0.1

        # Permit history
        if self.has_foundation_repair_permits(property.parcel_id):
            risk_score += 0.25  # Confirms past problems

        # Price anomalies
        if self.has_suspicious_price_drops(property.price_history):
            risk_score += 0.15

        # Neighborhood pattern
        if self.neighborhood_has_foundation_issues(property.location):
            risk_score += 0.2

        return FoundationRisk(
            risk_score=min(1.0, risk_score),
            risk_level=self._categorize(risk_score),
            confidence=0.65,  # Remote assessment = 65% confidence
            factors_found=self._list_factors(),
            recommendation=self._recommend(risk_score)
        )

    def _categorize(self, score: float) -> str:
        if score < 0.2:
            return "LOW_RISK"
        elif score < 0.4:
            return "MEDIUM_RISK"
        elif score < 0.6:
            return "HIGH_RISK"
        else:
            return "VERY_HIGH_RISK"
```

---

### Чеклист удалённой оценки foundation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│          REMOTE FOUNDATION ASSESSMENT CHECKLIST                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Property: _________________________  Parcel: _______________               │
│                                                                             │
│  STREET VIEW HISTORICAL (maps.google.com → clock icon):                    │
│  □ Oldest available year: _______                                          │
│  □ Roofline changed over time?        □ No  □ Slight  □ Major             │
│  □ Visible cracks appeared?           □ No  □ Some    □ Many              │
│  □ Windows/doors look skewed?         □ No  □ Slight  □ Major             │
│  □ Porch/steps separated from house?  □ No  □ Slight  □ Major             │
│                                                                             │
│  SATELLITE ANALYSIS:                                                        │
│  □ House in low spot?                 □ No  □ Yes                         │
│  □ Drainage toward house?             □ No  □ Yes                         │
│  □ Large trees near foundation?       □ No  □ Yes (<10ft)                 │
│  □ Standing water visible?            □ No  □ Sometimes  □ Often          │
│                                                                             │
│  SOIL DATA (websoilsurvey.nrcs.usda.gov):                                  │
│  □ Soil type: _______________________                                      │
│  □ Expansive clay?                    □ No  □ Yes                         │
│  □ Good drainage?                     □ Yes □ No                          │
│                                                                             │
│  PERMIT HISTORY (county website):                                           │
│  □ Any foundation repair permits?     □ No  □ Yes (year: ______)          │
│  □ French drain/sump pump permits?    □ No  □ Yes                         │
│  □ Structural repair permits?         □ No  □ Yes                         │
│                                                                             │
│  BUILDING INFO:                                                             │
│  □ Year built: _______  (pre-1950 = higher risk)                          │
│  □ Foundation type: □ Slab □ Crawlspace □ Basement □ Unknown              │
│                                                                             │
│  PRICE HISTORY:                                                             │
│  □ Multiple failed sales?             □ No  □ Yes                         │
│  □ Price dropped significantly?       □ No  □ Yes                         │
│  □ "As-is" sale?                      □ No  □ Yes                         │
│                                                                             │
│  NEIGHBORHOOD:                                                              │
│  □ Known foundation issues in area?   □ No  □ Yes  □ Unknown              │
│  □ Similar homes have problems?       □ No  □ Yes  □ Unknown              │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  REMOTE ASSESSMENT RESULT                                                   │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  Red flags found: _____                                                     │
│                                                                             │
│  0-1: ✅ LOW RISK - Likely OK, physical inspection recommended             │
│  2-3: ⚠️ MEDIUM RISK - Proceed with caution, inspection REQUIRED           │
│  4-5: ❌ HIGH RISK - Major concerns, probably skip                         │
│  6+:  ❌❌ VERY HIGH - Do not pursue                                        │
│                                                                             │
│  Confidence level: ~65% (remote assessment не заменяет осмотр!)            │
│                                                                             │
│  Notes: _______________________________________________________________   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Когда достаточно remote assessment?

| Ситуация | Remote OK? | Почему |
|----------|-----------|--------|
| **OTC lot (no structure)** | ✅ YES | Нет foundation у vacant land |
| **Дешёвый объект (<$500)** | ✅ Mostly | Риск потери низкий |
| **Объект для flip** | ⚠️ Partial | Remote + quick physical look |
| **Объект для live-in** | ❌ NO | ОБЯЗАТЕЛЬНО physical inspection |
| **Denis family рядом** | ✅ Remote first → Physical confirm | Best of both |

### Workflow для Miw

```
1. Система находит candidates
        ↓
2. Remote Foundation Assessment (этот чеклист)
        ↓
3. Filter: только LOW/MEDIUM risk
        ↓
4. Denis family физически смотрит TOP 3-5
        ↓
5. Покупаем только подтверждённые
```

---

---

## 💎 Скрытая ценность: "Бабушкины дома" (Bonus Value)

> *"Можно ли в бабушкиных вариантах найти антиквариат? Клад? Переходит ли к новому собственнику?"*

### Что может быть внутри

| Категория | Примеры | Потенциальная ценность |
|-----------|---------|----------------------|
| **Антикварная мебель** | Victorian, Mid-century modern | $500 - $50,000+ |
| **Vintage коллекции** | Монеты, марки, карты | $100 - $100,000+ |
| **Ювелирные изделия** | Спрятаны в необычных местах | $100 - $50,000+ |
| **Наличные** | Под матрасом, в стенах, в книгах | $100 - $500,000+ |
| **Искусство** | Картины, скульптуры | $100 - $1,000,000+ |
| **Документы** | Старые акции, облигации | $0 - $100,000+ |
| **Vintage техника** | Радио, часы, инструменты | $50 - $5,000 |
| **Книги** | Первые издания, редкие | $10 - $50,000+ |

### Юридический аспект: Переходит ли к новому владельцу?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  TAX DEED SALE: Personal Property Rules                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ОБЩЕЕ ПРАВИЛО:                                                             │
│  Tax Deed = покупка "as-is, where-is, with all faults AND contents"        │
│                                                                             │
│  ЧТО ПЕРЕХОДИТ:                                                             │
│  ✅ Структура (дом, гараж, сарай)                                           │
│  ✅ Fixtures (встроенные шкафы, сантехника, люстры)                         │
│  ✅ Abandoned personal property (мебель, вещи оставленные внутри)           │
│  ✅ Всё что "прикреплено" к земле                                           │
│                                                                             │
│  ИСКЛЮЧЕНИЯ (проверять по штату):                                           │
│  ⚠️ Некоторые штаты требуют хранить вещи 30-90 дней                        │
│  ⚠️ Наследники могут заявить права на personal property                    │
│  ⚠️ Ценные предметы (>$500) могут требовать уведомления                    │
│                                                                             │
│  ЛУЧШАЯ ПРАКТИКА:                                                           │
│  1. Сфотографировать ВСЁ при входе (timestamp!)                            │
│  2. Хранить ценные находки 90 дней                                         │
│  3. Если наследники объявились - договариваться                            │
│  4. Документировать abandoned status                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### По штатам (важные для Miw)

| Штат | Personal Property Rule | Срок хранения |
|------|----------------------|---------------|
| **South Dakota** | Переходит с property | 30 дней notice |
| **Arizona** | Abandoned = yours | 30 дней |
| **Utah** | Переходит | 15 дней |
| **Texas** | Переходит | Varies by county |

### Сигналы "бонусной ценности" (что искать)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  INDICATORS OF HIDDEN VALUE                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  OWNER PROFILE:                                                             │
│  □ Elderly owner (80+)?              → Накопления за всю жизнь             │
│  □ Lived there 30+ years?            → Много вещей собралось               │
│  □ Owner deceased?                   → Estate не разобрано                 │
│  □ No heirs / family dispute?        → Никто не забрал вещи                │
│  □ Professional background?          → Качественные вещи                   │
│    (doctor, lawyer, engineer)                                              │
│                                                                             │
│  PROPERTY INDICATORS:                                                       │
│  □ "Contents included" в описании?   → Явно есть вещи                      │
│  □ Photos show full house?           → Не вывезено                         │
│  □ Abandoned suddenly?               → Ушли как есть                       │
│  □ No estate sale held?              → Вещи на месте                       │
│  □ House built 1920-1970?            → Эра качественных вещей              │
│                                                                             │
│  NEIGHBORHOOD:                                                              │
│  □ Wealthy area historically?        → Лучшее качество                     │
│  □ Original owners in neighborhood?  → Долгожители                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Можно ли смоделировать? (Deep Learning - Model 36)

```python
class HiddenValuePredictor:
    """
    Прогноз вероятности скрытой ценности в "бабушкином доме".

    Confidence: LOW (40-60%) - это спекулятивная модель!
    """

    def predict(self, property: PropertyData, owner: OwnerData) -> HiddenValueAnalysis:
        score = 0.0

        # Owner age (elderly = more accumulation)
        if owner.estimated_age and owner.estimated_age >= 75:
            score += 0.2
        if owner.estimated_age and owner.estimated_age >= 85:
            score += 0.1  # Additional

        # Ownership duration
        years_owned = property.calculate_ownership_years()
        if years_owned >= 30:
            score += 0.2
        elif years_owned >= 20:
            score += 0.1

        # Owner status
        if owner.is_deceased:
            score += 0.15
        if owner.no_known_heirs:
            score += 0.1

        # Property characteristics
        if property.year_built <= 1970:
            score += 0.1  # Era of quality furniture

        # Abandonment indicators
        if property.abandoned_suddenly:
            score += 0.2
        if property.no_estate_sale_record:
            score += 0.1

        # Historical wealth indicators
        if self._check_wealthy_profession(owner.name):
            score += 0.15
        if self._check_wealthy_neighborhood(property.location):
            score += 0.1

        # Photo analysis (if interior photos available)
        if property.has_interior_photos:
            furniture_score = self.analyze_furniture_quality(property.photos)
            score += furniture_score * 0.2

        return HiddenValueAnalysis(
            probability=min(1.0, score),
            expected_value_range=self._estimate_range(score),
            confidence="LOW",  # This is speculative!
            indicators_found=self._list_indicators(),
            recommendation=self._recommend(score)
        )

    def _estimate_range(self, score: float) -> Tuple[int, int]:
        """Rough estimate of hidden value"""
        if score >= 0.7:
            return (5000, 50000)  # High potential
        elif score >= 0.5:
            return (1000, 10000)  # Medium potential
        elif score >= 0.3:
            return (100, 2000)   # Low potential
        else:
            return (0, 500)      # Minimal
```

### NLP анализ (что можно извлечь из документов)

| Документ | Что извлечь | Как |
|----------|------------|-----|
| **Obituary** | Профессия, богатство, семья | NLP keyword extraction |
| **Property listing history** | "Contents included", "estate sale" | Text search |
| **Assessor notes** | "Well maintained", "original condition" | NLP sentiment |
| **Permit history** | No recent updates = original interior | Pattern matching |
| **Newspaper archives** | Owner's social status, profession | NLP entity extraction |

### Где прячут ценности (исторические паттерны)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  COMMON HIDING SPOTS (from estate cleanout professionals)                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  💰 CASH:                                                                   │
│  • Под матрасом, между матрасами                                           │
│  • В морозилке (в пакетах, контейнерах)                                    │
│  • В книгах (вырезанные страницы)                                          │
│  • За картинами на стене                                                   │
│  • В одежде (карманы, подкладка)                                           │
│  • В банках с крупой/мукой                                                 │
│  • Под половицами                                                          │
│  • В вентиляционных решётках                                               │
│  • В туалетном бачке (в пакете)                                            │
│                                                                             │
│  💎 ЮВЕЛИРНЫЕ ИЗДЕЛИЯ:                                                      │
│  • Шкатулки (очевидно) + фальшивые шкатулки                               │
│  • В носках в комоде                                                       │
│  • В коробках из-под лекарств                                              │
│  • В старых кошельках                                                      │
│  • В обуви                                                                 │
│                                                                             │
│  📜 ДОКУМЕНТЫ/ЦЕННЫЕ БУМАГИ:                                                │
│  • В Библии (классика)                                                     │
│  • Между страницами книг                                                   │
│  • В старых папках с "неважными" бумагами                                  │
│  • В сейфе (если есть)                                                     │
│  • В банковских ячейках (ключ может быть в доме)                           │
│                                                                             │
│  🖼️ ЦЕННЫЕ ПРЕДМЕТЫ:                                                       │
│  • Чердак (часто забытые коллекции)                                        │
│  • Гараж (инструменты, vintage авто части)                                 │
│  • Подвал (вино, консервация, старые вещи)                                 │
│  • Сарай (антикварный инвентарь)                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 🛋️ Преимущество Denis: Реставрация мебели + Клиентская база

> *"У Дениса был бизнес по продаже реставрированных диванов и сохранилась клиентская база."*

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DENIS FURNITURE ADVANTAGE                                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ЧТО ЕСТЬ:                                                                  │
│  ✅ Опыт реставрации мебели (диваны, кресла)                               │
│  ✅ Клиентская база (готовые покупатели!)                                   │
│  ✅ Понимание рынка vintage/restored furniture                              │
│  ✅ Навыки оценки состояния и потенциала                                    │
│                                                                             │
│  КАК ИСПОЛЬЗОВАТЬ:                                                          │
│                                                                             │
│  "Бабушкин дом" куплен                                                     │
│          ↓                                                                  │
│  Denis оценивает мебель внутри                                             │
│          ↓                                                                  │
│  ┌─────────────────────────────────────────────┐                           │
│  │  Ценное:           │  Обычное:             │                           │
│  │  • Антиквариат     │  • Реставрация        │                           │
│  │  • Mid-century     │  • Продажа через      │                           │
│  │  • Дизайнерское    │    клиентскую базу    │                           │
│  │       ↓            │       ↓               │                           │
│  │  Appraiser/Auction │  Denis restores       │                           │
│  │       ↓            │       ↓               │                           │
│  │  Premium sale      │  Sell to customers    │                           │
│  └─────────────────────────────────────────────┘                           │
│                                                                             │
│  ДОПОЛНИТЕЛЬНЫЙ ДОХОД от каждого "бабушкиного дома":                       │
│  • Мебель внутри = $500 - $10,000+                                         │
│  • Реставрация добавляет 2-5x к цене                                       │
│  • Клиентская база = быстрая продажа                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Синергия: Property + Contents + Denis Skills

```
ОБЫЧНЫЙ ИНВЕСТОР:                    MIW + DENIS:

Покупает property                    Покупает property
       ↓                                    ↓
Выбрасывает "хлам"                   Denis оценивает ВСЁ
       ↓                                    ↓
Продаёт только property              ┌──────────────────────┐
       ↓                             │ Revenue streams:     │
Profit: $X                           │ 1. Property flip     │
                                     │ 2. Furniture sales   │
                                     │ 3. Antiques found    │
                                     │ 4. Hidden valuables  │
                                     └──────────────────────┘
                                            ↓
                                     Profit: $X + $Y + $Z
```

### Что Denis может оценить/реставрировать

| Категория | Denis Skill | Маржа после реставрации |
|-----------|-------------|------------------------|
| **Диваны, кресла** | ✅ Экспертный | 200-500% |
| **Стулья, столы** | ✅ Высокий | 150-300% |
| **Кровати, комоды** | ⚠️ Средний | 100-200% |
| **Антиквариат** | ⚠️ Нужен appraiser | Varies |
| **Mid-century modern** | ✅ Востребовано | 300-1000% |

### Vintage Furniture Sweet Spots (что искать)

| Эра | Стиль | Текущий спрос | Цена после реставрации |
|-----|-------|---------------|----------------------|
| **1950-1970** | Mid-century modern | 🔥 ОЧЕНЬ HIGH | $500-$10,000+ per piece |
| **1920-1940** | Art Deco | 🔥 HIGH | $300-$5,000 |
| **1880-1920** | Victorian | ⚠️ MEDIUM | $200-$3,000 |
| **1970-1990** | Vintage | 📈 Growing | $100-$1,000 |

### Brands to Look For (Denis должен знать)

```
HIGH VALUE (если найдёте):
□ Herman Miller (Eames chairs = $2,000-$10,000)
□ Knoll
□ Heywood-Wakefield
□ Drexel
□ Thomasville (vintage)
□ Henredon
□ Baker Furniture
□ Ethan Allen (vintage)

LOOK FOR:
□ Любые маркировки/labels на мебели
□ "Made in Denmark" / "Made in Yugoslavia" (часто качество)
□ Solid wood vs veneer
□ Dovetail joints (признак качества)
□ Original hardware
```

### Workflow: Property + Furniture Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  COMBINED ACQUISITION WORKFLOW                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STEP 1: Property Evaluation                                                │
│  □ Remote assessment (foundation, etc.)                                     │
│  □ Check for "contents included"                                           │
│  □ Interior photos → furniture visible?                                    │
│  □ Era of house → likely furniture era                                     │
│                                                                             │
│  STEP 2: Physical Visit (Denis family)                                      │
│  □ Property inspection (structure)                                         │
│  □ Denis: Quick furniture scan                                             │
│  □ Photos of interesting pieces                                            │
│  □ Estimate contents value                                                 │
│                                                                             │
│  STEP 3: Purchase Decision                                                  │
│  □ Property value: $______                                                 │
│  □ + Estimated furniture value: $______                                    │
│  □ + Potential hidden value: $______                                       │
│  □ = TOTAL POTENTIAL: $______                                              │
│  □ Max bid: $______ (based on combined value)                              │
│                                                                             │
│  STEP 4: Post-Purchase                                                      │
│  □ Document everything (photos)                                            │
│  □ Denis sorts furniture:                                                  │
│     - To restore & sell                                                    │
│     - To keep (for Miw's home)                                             │
│     - To donate/discard                                                    │
│  □ Check hiding spots for valuables                                        │
│  □ Property renovation begins                                              │
│                                                                             │
│  STEP 5: Revenue Collection                                                 │
│  □ Furniture sold through customer base                                    │
│  □ Antiques appraised & sold separately                                    │
│  □ Property flipped OR kept                                                │
│  □ Track total ROI                                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Пример расчёта

```
"Бабушкин дом" в South Dakota:

PURCHASE:
  Tax Deed price:                    $3,000

CONTENTS FOUND:
  Mid-century sofa (needs work):     → Denis restores → $1,500
  Dining set (6 chairs + table):     → Denis restores → $2,000
  Vintage armchair:                  → Denis restores → $800
  Random furniture (sold as-is):     → $500
  Old tools in garage:               → $300
  Books (some valuable):             → $200
                                     ─────────────────────
  Contents subtotal:                 $5,300

PROPERTY:
  Renovate (family labor):           -$8,000
  Sell/Value after:                  +$45,000
                                     ─────────────────────
  Property profit:                   $37,000

TOTAL RETURN:
  Invested: $3,000 (purchase) + $8,000 (reno) = $11,000
  Return: $37,000 (property) + $5,300 (contents) = $42,300

  NET PROFIT: $31,300
  ROI: 285%

  WITHOUT Denis furniture skills:
  Would have discarded contents = $0
  NET PROFIT: $26,000

  DENIS ADVANTAGE: +$5,300 (+20% more profit)
```

---

### Real Stories (для контекста)

| Находка | Где | Стоимость |
|---------|-----|-----------|
| Картина под кроватью | Estate sale house | $27 million (обнаружена работа старого мастера) |
| Монеты в стене | Renovation | $200,000 |
| Бейсбольные карточки на чердаке | Foreclosure | $3 million |
| Наличные в книгах | Estate cleanout | $45,000 |
| Vintage Gibson guitar | Closet | $35,000 |
| First edition books | Basement | $50,000 |

### Практический чеклист при входе

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  FIRST ENTRY PROTOCOL (если купили "бабушкин дом")                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. ДОКУМЕНТИРОВАТЬ:                                                        │
│     □ Фото/видео ВСЕГО при входе (timestamp)                               │
│     □ Не выбрасывать НИЧЕГО первые 2 недели                                │
│     □ Записать состояние каждой комнаты                                    │
│                                                                             │
│  2. ПЕРВИЧНЫЙ ОСМОТР (не трогая):                                          │
│     □ Мебель - стиль, состояние, бренды                                    │
│     □ Картины/искусство - подписи художников?                              │
│     □ Книги - первые издания? Старые?                                      │
│     □ Посуда - фарфор, серебро, маркировка                                 │
│     □ Техника - vintage радио, часы                                        │
│                                                                             │
│  3. ОЦЕНКА (до выброса/продажи):                                           │
│     □ Google подозрительные предметы                                       │
│     □ Сфотографировать маркировки                                          │
│     □ При сомнениях - вызвать appraiser                                    │
│     □ Не чистить/не реставрировать до оценки!                              │
│                                                                             │
│  4. ПРОВЕРИТЬ "ТАЙНИКИ":                                                    │
│     □ Книги (пролистать ВСЕ)                                               │
│     □ Морозилка                                                            │
│     □ Чердак полностью                                                     │
│     □ За картинами                                                         │
│     □ Матрасы (между, под)                                                 │
│     □ Одежда (карманы, подкладка)                                          │
│                                                                             │
│  5. ХРАНЕНИЕ:                                                               │
│     □ Ценные находки - документировать, хранить отдельно                   │
│     □ Подозрительные документы - к юристу                                  │
│     □ Ключи/коды найденные - может быть ячейка                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🕸️ Граф родственных связей: Поиск Foreclosure Opportunities

> *"Owner deceased, no heirs. Можно ли по графу родственных связей найти guaranteed foreclosures?"*

### ⚠️ ВАЖНО: Разница между Foreclosure Score и x1000

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ДВЕ РАЗНЫХ КОНЦЕПЦИИ - НЕ ПУТАТЬ!                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FORECLOSURE SCORE (этот раздел)           x1000 SCORE (раздел антиквариата)
│  ════════════════════════════              ══════════════════════════════   │
│  Цель: найти properties БЕЗ наследников    Цель: найти УНИКАЛЬНЫЙ антиквариат
│  Результат: guaranteed foreclosure         Результат: потенциал ×1000 прибыли
│  Фокус: семейное дерево владельца          Фокус: некролог, профессия, эпоха
│  Риск: кто-то redemption сделает           Риск: антиквариата нет/мало       │
│                                                                             │
│  Пример:                                   Пример:                          │
│  Owner умер, нет детей, нет супруги        Owner был "avid art collector"   │
│  → 90% шанс foreclosure                    → 90% шанс найти ценности ×1000  │
│                                                                             │
│  МОЖНО КОМБИНИРОВАТЬ:                                                       │
│  Foreclosure Score HIGH + x1000 Score HIGH = 🦄 UNICORN OPPORTUNITY         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Концепция: Family Graph для Owner

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OWNER FAMILY GRAPH                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                         ┌─────────────┐                                     │
│                         │  PARENTS    │                                     │
│                         │  ├─ Father ─┼── ? (deceased?)                    │
│                         │  └─ Mother ─┼── ? (deceased?)                    │
│                         └──────┬──────┘                                     │
│                                │                                            │
│          ┌─────────────────────┼─────────────────────┐                     │
│          │                     │                     │                     │
│    ┌─────┴─────┐        ┌─────┴─────┐        ┌─────┴─────┐                │
│    │ SIBLING 1 │        │  OWNER    │        │ SIBLING 2 │                │
│    │ (status?) │        │ DECEASED  │        │ (status?) │                │
│    └───────────┘        │ ⚰️ 2023   │        └───────────┘                │
│                         └─────┬─────┘                                      │
│                               │                                            │
│                    ┌──────────┼──────────┐                                 │
│                    │          │          │                                 │
│              ┌─────┴─────┐    │    ┌─────┴─────┐                          │
│              │  SPOUSE   │    │    │ EX-SPOUSE │                          │
│              │ (status?) │    │    │ (status?) │                          │
│              └───────────┘    │    └───────────┘                          │
│                               │                                            │
│                    ┌──────────┼──────────┐                                 │
│                    │          │          │                                 │
│              ┌─────┴────┐ ┌───┴───┐ ┌────┴─────┐                          │
│              │ CHILD 1  │ │CHILD 2│ │ CHILD 3  │                          │
│              │(status?) │ │  ?    │ │    ?     │                          │
│              └──────────┘ └───────┘ └──────────┘                          │
│                                                                             │
│  HEIR PROBABILITY:                                                          │
│  ═════════════════                                                          │
│  • All nodes = deceased/not found → VERY LOW (foreclosure likely)          │
│  • 1+ living heir found → HIGH (will likely redeem)                        │
│  • Unknown status → MEDIUM (investigate further)                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Foreclosure Opportunity Criteria (No Heirs)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FORECLOSURE OPPORTUNITY CHECKLIST                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  OWNER STATUS:                                                              │
│  ☑ Owner deceased                           REQUIRED                       │
│  ☑ Death confirmed (obituary, records)      REQUIRED                       │
│                                                                             │
│  SPOUSE:                                                                    │
│  □ No spouse ever (single)                  +0.3                           │
│  □ Spouse also deceased                     +0.3                           │
│  □ Divorced, ex-spouse not on deed          +0.2                           │
│  □ Spouse alive but abandoned property      +0.1                           │
│  ☐ Spouse alive and active                  STOP - will redeem             │
│                                                                             │
│  CHILDREN:                                                                  │
│  □ No children found (any records)          +0.3                           │
│  □ All children deceased                    +0.3                           │
│  □ Children exist but estranged             +0.1 (risky)                   │
│  ☐ Children alive and in contact            STOP - will likely redeem      │
│                                                                             │
│  SIBLINGS/OTHER HEIRS:                                                      │
│  □ No siblings found                        +0.1                           │
│  □ All siblings deceased                    +0.1                           │
│  □ Only distant relatives (cousins+)        +0.1 (may not know/care)       │
│                                                                             │
│  LEGAL STATUS:                                                              │
│  □ No probate case filed                    +0.2 (no one claiming)         │
│  □ Probate filed but abandoned              +0.2 (heirs gave up)           │
│  ☐ Active probate                           WAIT - outcome uncertain        │
│                                                                             │
│  PROPERTY INDICATORS:                                                       │
│  □ Property vacant 2+ years                 +0.1                           │
│  □ Mail piling up                           +0.1                           │
│  □ No utilities active                      +0.1                           │
│  □ Taxes delinquent 3+ years                +0.1                           │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  SCORE INTERPRETATION:                                                      │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  Score >= 0.8:  ⭐ FORECLOSURE CERTAIN - No heirs, guaranteed win          │
│  Score 0.5-0.8: ✅ FORECLOSURE LIKELY - Probably no redemption             │
│  Score 0.3-0.5: ⚠️ UNCERTAIN - Need more research                          │
│  Score < 0.3:   ❌ REDEMPTION LIKELY - Heirs exist                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Источники данных для графа

| Источник | Что узнаём | Доступность | Метод |
|----------|-----------|-------------|-------|
| **Obituaries** | Surviving family listed | PUBLIC | NLP extraction |
| **Social Security Death Index** | Death confirmed | PUBLIC | API/search |
| **Probate Court Records** | Heirs, estate status | PUBLIC | Court search |
| **Property Records** | Co-owners, transfers | PUBLIC | County records |
| **Voter Registration** | Family at same address | PUBLIC | State records |
| **Marriage/Divorce Records** | Spouse info | PUBLIC | Vital records |
| **Social Media** | Family connections | SEMI-PUBLIC | API/scraping |
| **Ancestry/Genealogy** | Full family tree | PAID | API |
| **LexisNexis/TLO** | Comprehensive | PAID ($) | Skip trace |

### NLP: Extracting Family from Obituaries

```python
class ObituaryFamilyExtractor:
    """
    Extract family graph from obituary text using NLP.

    Example obituary:
    "John Smith, 87, passed away on March 15, 2023. He was preceded
    in death by his wife Mary (2019) and son Michael (2020). He is
    survived by his daughter Susan of Denver and brother Robert of
    Phoenix. No services are planned."
    """

    def extract(self, obituary_text: str) -> FamilyGraph:
        # NLP patterns
        preceded_by = self._extract_preceded_by(obituary_text)  # Deceased relatives
        survived_by = self._extract_survived_by(obituary_text)   # Living relatives

        graph = FamilyGraph(owner=self.owner_name)

        # Add deceased relatives
        for person, relation in preceded_by:
            graph.add_node(person, relation=relation, status="DECEASED")

        # Add living relatives (THESE ARE POTENTIAL HEIRS!)
        for person, relation, location in survived_by:
            graph.add_node(person, relation=relation, status="ALIVE", location=location)

        return graph

    def _extract_survived_by(self, text: str) -> List[Tuple]:
        """
        Patterns:
        - "survived by his/her [relation] [Name]"
        - "leaves behind [relation] [Name]"
        - "is survived by [Name], his/her [relation]"
        """
        # SpaCy/BERT NER + relation extraction
        pass

# Example output:
{
    "owner": "John Smith",
    "owner_status": "DECEASED",
    "death_date": "2023-03-15",
    "family": {
        "spouse": {"name": "Mary Smith", "status": "DECEASED", "death_year": 2019},
        "children": [
            {"name": "Michael Smith", "status": "DECEASED", "death_year": 2020},
            {"name": "Susan Smith", "status": "ALIVE", "location": "Denver"}  # ⚠️ HEIR!
        ],
        "siblings": [
            {"name": "Robert Smith", "status": "ALIVE", "location": "Phoenix"}  # ⚠️ HEIR!
        ]
    },
    "heir_risk": "MEDIUM",  # Living daughter and brother found
    "foreclosure_score": 0.3      # Heirs exist, redemption likely
}
```

### Model 37: HeirGraphAnalyzer

```python
class HeirGraphAnalyzer:
    """
    Builds family graph and calculates probability of redemption.

    Goal: Find foreclosure opportunities (no heirs = guaranteed foreclosure)
    """

    def analyze(self, owner: OwnerData, property: PropertyData) -> HeirAnalysis:
        # Step 1: Confirm owner deceased
        if not self._confirm_death(owner):
            return HeirAnalysis(foreclosure_score=0, reason="Owner may be alive")

        # Step 2: Build family graph from multiple sources
        graph = FamilyGraph()

        # Obituary (primary source)
        if obituary := self._find_obituary(owner):
            graph.merge(self._parse_obituary(obituary))

        # Property records (co-owners often family)
        co_owners = self._get_co_owners(property)
        for co_owner in co_owners:
            graph.add_potential_heir(co_owner, source="property_records")

        # Probate search
        probate = self._search_probate(owner, property.county)
        if probate:
            graph.merge(self._parse_probate(probate))

        # Social media (if names known)
        for node in graph.get_nodes():
            if social := self._find_social_media(node):
                self._update_node_status(node, social)

        # Step 3: Calculate foreclosure score
        score = self._calculate_score(graph)

        return HeirAnalysis(
            owner=owner,
            family_graph=graph,
            total_potential_heirs=graph.count_living_heirs(),
            foreclosure_score=score,
            recommendation=self._recommend(score),
            confidence=self._calculate_confidence(graph)
        )

    def _calculate_score(self, graph: FamilyGraph) -> float:
        score = 0.0

        # No living spouse
        if not graph.has_living_spouse():
            score += 0.3

        # No living children
        if not graph.has_living_children():
            score += 0.3

        # No living siblings
        if not graph.has_living_siblings():
            score += 0.1

        # No probate filed
        if not graph.has_active_probate():
            score += 0.2

        # Property abandoned indicators
        if self._property_abandoned_signals(graph.property):
            score += 0.1

        return min(1.0, score)
```

### Owner Card: Family Graph Section

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OWNER CARD: FAMILY GRAPH                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  OWNER: John Smith                                                          │
│  STATUS: ⚰️ DECEASED (March 15, 2023)                                       │
│  DEATH SOURCE: Obituary (Spearfish Gazette)                                │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  FAMILY GRAPH                                                               │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  SPOUSE:                                                                    │
│  ├── Mary Smith ────────── ⚰️ DECEASED (2019) ✓ No heir risk              │
│                                                                             │
│  CHILDREN:                                                                  │
│  ├── Michael Smith ─────── ⚰️ DECEASED (2020) ✓ No heir risk              │
│  └── Susan Smith ──────── 🔴 ALIVE (Denver, CO) ⚠️ POTENTIAL HEIR         │
│                                                                             │
│  SIBLINGS:                                                                  │
│  └── Robert Smith ──────── 🔴 ALIVE (Phoenix, AZ) ⚠️ POTENTIAL HEIR        │
│                                                                             │
│  OTHER RELATIVES: None found                                                │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  HEIR ANALYSIS                                                              │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  Living heirs found: 2 (daughter, brother)                                 │
│  Probate status: NOT FILED (as of search date)                             │
│  Property status: Vacant 18 months, taxes 3 years delinquent               │
│                                                                             │
│  FORECLOSURE SCORE: 0.35 / 1.00                                            │
│  ASSESSMENT: ⚠️ MEDIUM RISK - Heirs exist but may not claim                │
│                                                                             │
│  RECOMMENDATION:                                                            │
│  NOT a foreclosure opportunity. Living daughter and brother found.         │
│  However: No probate filed in 18 months = heirs may be unaware/uninterested│
│  Consider: Contact heirs directly for pre-foreclosure purchase?            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Foreclosure Example (идеальный случай)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ⭐ FORECLOSURE OPPORTUNITY EXAMPLE ⭐                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  OWNER: Margaret Wilson                                                     │
│  STATUS: ⚰️ DECEASED (January 8, 2022)                                      │
│                                                                             │
│  FAMILY GRAPH:                                                              │
│  ├── Spouse: Harold Wilson ─── ⚰️ DECEASED (2015)                          │
│  ├── Children: None (obituary: "no children")                              │
│  ├── Siblings: None found (only child per records)                         │
│  └── Other: No relatives mentioned in obituary                             │
│                                                                             │
│  LEGAL STATUS:                                                              │
│  ├── Probate: NOT FILED (4 years!)                                         │
│  ├── Estate: No executor appointed                                         │
│  └── Property: Title still in Margaret's name                              │
│                                                                             │
│  PROPERTY STATUS:                                                           │
│  ├── Vacant: 4 years                                                       │
│  ├── Taxes delinquent: 4 years ($8,500 owed)                               │
│  ├── Utilities: Disconnected 2022                                          │
│  └── Condition: "Бабушкин дом", full of contents                           │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  FORECLOSURE SCORE: 0.95 / 1.00 ⭐⭐⭐                                       │
│                                                                             │
│  ASSESSMENT: EXCELLENT FORECLOSURE OPPORTUNITY                              │
│  • Owner deceased ✓                                                        │
│  • Spouse deceased ✓                                                       │
│  • No children ✓                                                           │
│  • No siblings found ✓                                                     │
│  • No probate = no one claiming ✓                                          │
│  • 4 years vacant = truly abandoned ✓                                      │
│                                                                             │
│  FINANCIALS:                                                                │
│  Tax lien amount: $8,500                                                   │
│  Assessed value: $95,000                                                   │
│  Estimated market: $120,000                                                │
│  Value/Lien ratio: 14x                                                     │
│                                                                             │
│  PROBABILITY OF REDEMPTION: ~1%                                            │
│  PROBABILITY OF FORECLOSURE: ~99%                                          │
│                                                                             │
│  RECOMMENDATION: ⭐ STRONG BUY                                              │
│  Expected outcome: Foreclosure → $120K property for $8.5K investment       │
│                                                                             │
│  BONUS: "Бабушкин дом" full of contents                                    │
│  → Denis furniture opportunity: Est. $2,000-$10,000 additional             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Поиск Foreclosure: Automated Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FORECLOSURE DISCOVERY PIPELINE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STEP 1: Filter tax delinquent properties                                  │
│          WHERE years_delinquent >= 3                                       │
│          AND owner_type = 'individual' (not LLC)                           │
│                ↓                                                            │
│          ~10,000 properties                                                │
│                                                                             │
│  STEP 2: Check owner death records                                         │
│          Social Security Death Index                                        │
│          Obituary search                                                    │
│                ↓                                                            │
│          ~2,000 with deceased owners                                       │
│                                                                             │
│  STEP 3: Build family graphs (NLP on obituaries)                           │
│          Extract: spouse, children, siblings                               │
│                ↓                                                            │
│          Family data for ~1,500 owners                                     │
│                                                                             │
│  STEP 4: Filter by heir status                                             │
│          WHERE living_heirs = 0                                            │
│          OR (living_heirs > 0 AND no_probate AND years_vacant >= 2)        │
│                ↓                                                            │
│          ~200-500 foreclosure candidates                                   │
│                                                                             │
│  STEP 5: Score and rank                                                    │
│          foreclosure_score >= 0.8                                          │
│          ORDER BY value_to_lien_ratio DESC                                 │
│                ↓                                                            │
│          TOP 50 FORECLOSURE OPPORTUNITIES                                  │
│                                                                             │
│  STEP 6: Denis family verification                                         │
│          Physical inspection of top candidates                             │
│                ↓                                                            │
│          FINAL 5-10 to purchase                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏆 Антиквариат мирового уровня: NLP-сигналы из документов

> *"Можно ли из некролога находить антиквариат мирового уровня? Какие ещё уникальные показатели?"*

### Obituary Keywords → World-Class Potential

```python
class WorldClassAntiquePredictor:
    """
    NLP extraction of high-value antique indicators from obituaries
    and other documents.
    """

    # Keyword patterns with scores
    PROFESSION_INDICATORS = {
        "antique dealer": 0.9,
        "art dealer": 0.9,
        "gallery owner": 0.85,
        "auctioneer": 0.8,
        "museum curator": 0.85,
        "museum director": 0.9,
        "art historian": 0.7,
        "archaeologist": 0.7,
        "interior designer": 0.6,
        "architect": 0.5,
    }

    COLLECTOR_INDICATORS = {
        "avid collector": 0.8,
        "passionate collector": 0.8,
        "lifelong collector": 0.85,
        "renowned collector": 0.95,
        "private collection": 0.8,
        "extensive collection": 0.85,
        "world-class collection": 1.0,
    }

    WEALTH_INDICATORS = {
        "philanthropist": 0.7,
        "benefactor": 0.7,
        "donated to museum": 0.8,
        "endowed": 0.8,
        "estate in": 0.6,
        "summer home": 0.6,
        "country club": 0.5,
        "yacht club": 0.6,
    }

    TRAVEL_INDICATORS = {
        "traveled extensively": 0.5,
        "world traveler": 0.5,
        "lived abroad": 0.6,
        "expatriate": 0.5,
        "diplomat": 0.7,
        "ambassador": 0.8,
    }

    MILITARY_INDICATORS = {
        "WWII veteran": 0.6,          # European/Pacific theater souvenirs
        "served in Germany": 0.7,     # Nazi-era items possible
        "served in Japan": 0.7,       # Japanese antiques
        "served in Korea": 0.5,
        "served in Vietnam": 0.4,
        "intelligence officer": 0.6,
        "military attaché": 0.7,
    }

    HERITAGE_INDICATORS = {
        "third generation": 0.7,
        "fourth generation": 0.8,
        "family home since": 0.7,
        "inherited from": 0.6,
        "founding family": 0.8,
        "old money": 0.8,
        "society": 0.5,
    }

    SPECIFIC_COLLECTIONS = {
        "coin collection": 0.6,
        "stamp collection": 0.5,
        "art collection": 0.8,
        "book collection": 0.6,
        "first editions": 0.7,
        "rare books": 0.8,
        "wine collection": 0.6,
        "car collection": 0.7,
        "gun collection": 0.6,
        "jewelry": 0.7,
        "porcelain": 0.6,
        "silver": 0.5,
        "furniture": 0.6,
        "paintings": 0.8,
        "sculptures": 0.7,
    }
```

### Примеры некрологов → Score

**Example 1: LOW potential**
```
"John Smith, 78, retired factory worker, passed away March 15.
He enjoyed fishing and watching TV. Survived by wife Mary and
three children."

EXTRACTED:
- Profession: factory worker (low wealth indicator)
- Hobbies: fishing, TV (no collector signals)
- Heritage: not mentioned

WORLD-CLASS SCORE: 0.05 (very low)
EXPECTED CONTENTS VALUE: $0-500
```

**Example 2: MEDIUM potential**
```
"Robert Johnson, 85, retired physician, passed away January 10.
He was an avid collector of antique medical instruments and
traveled extensively in Europe. Third generation in the family
home built in 1890."

EXTRACTED:
- Profession: physician (0.5 - educated, some wealth)
- Collector: "avid collector" (0.8)
- Specific: "antique medical instruments" (niche but valuable)
- Travel: "traveled extensively in Europe" (0.5)
- Heritage: "third generation", home since 1890 (0.7)

WORLD-CLASS SCORE: 0.65 (medium-high)
EXPECTED CONTENTS VALUE: $5,000-50,000
```

**Example 3: HIGH potential ⭐**
```
"Eleanor Worthington III, 94, renowned art collector and
philanthropist, passed away peacefully at her estate. A former
museum board member at the Metropolitan Museum of Art, she
amassed a world-class collection of Impressionist paintings
during her decades living in Paris. Fourth generation of the
Worthington family. Predeceased by husband Charles (2018).
No children. In lieu of services, donations may be made to..."

EXTRACTED:
- Collector: "renowned art collector" (0.95)
- Collector: "world-class collection" (1.0)
- Specific: "Impressionist paintings" (⭐ museum-quality)
- Profession: "museum board member, Metropolitan" (0.9)
- Wealth: "philanthropist", "estate" (0.7)
- Travel: "decades living in Paris" (0.7)
- Heritage: "fourth generation" (0.8)
- Heirs: NO CHILDREN + husband deceased = FORECLOSURE CERTAIN!

WORLD-CLASS SCORE: 0.95 ⭐⭐⭐
EXPECTED CONTENTS VALUE: $100,000 - $10,000,000+
FORECLOSURE SCORE: 0.95

🚨 ALERT: This is a UNICORN property!
```

### Другие документы для извлечения сигналов

| Документ | Что извлечь | Где найти | Reliability |
|----------|-------------|-----------|-------------|
| **Obituary** | Profession, hobbies, collections, heritage | Newspapers, Legacy.com | HIGH |
| **Newspaper archives** | Society pages, donations, awards | Newspapers.com | MEDIUM |
| **Museum donor lists** | Confirmed wealth + art interest | Museum websites | HIGH |
| **Auction house records** | Past purchases (!) | Christie's, Sotheby's | HIGH |
| **Court records** | Divorce settlements list assets | Court websites | HIGH |
| **Probate inventory** | Actual list of items! | Court | VERY HIGH |
| **Insurance claims** | High-value items insured | (Hard to get) | VERY HIGH |
| **Social Security records** | Employer history | Limited access | MEDIUM |
| **Military records** | Service location, rank | NARA | HIGH |
| **University alumni** | Education, donations | Alumni magazines | MEDIUM |
| **Professional licenses** | Doctor, lawyer, etc. | State boards | HIGH |
| **Business registrations** | Owned gallery? Shop? | State SOS | HIGH |
| **Import records** | Brought items from abroad | (Very hard) | HIGH |
| **Old phone books** | Long-term residence | Ancestry | LOW |

### NLP Pipeline: Document → Antique Score

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    WORLD-CLASS ANTIQUE DISCOVERY PIPELINE                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STEP 1: Gather documents for deceased owner                               │
│  ├── Obituary (primary)                                                    │
│  ├── Newspaper mentions (archive search)                                   │
│  ├── Professional records                                                  │
│  └── Military records (if applicable)                                      │
│                                                                             │
│  STEP 2: NLP extraction                                                    │
│  ├── Named Entity Recognition (NER)                                        │
│  │   └── Organizations (museums, galleries, clubs)                         │
│  │   └── Locations (travel, lived abroad)                                  │
│  │   └── Dates (era of service, residence)                                 │
│  ├── Keyword matching (collector, dealer, etc.)                            │
│  └── Sentiment analysis (wealth indicators)                                │
│                                                                             │
│  STEP 3: Cross-reference                                                   │
│  ├── Museum donor databases                                                │
│  ├── Auction house buyer records (if available)                            │
│  └── Professional association memberships                                  │
│                                                                             │
│  STEP 4: Score calculation                                                 │
│  ├── Profession score (0-1)                                                │
│  ├── Collector score (0-1)                                                 │
│  ├── Wealth score (0-1)                                                    │
│  ├── Heritage score (0-1)                                                  │
│  └── Specific collection score (0-1)                                       │
│                                                                             │
│  STEP 5: World-Class probability                                           │
│  └── Weighted average → ANTIQUE_SCORE                                      │
│                                                                             │
│  OUTPUT:                                                                    │
│  • antique_score: 0.0-1.0                                                  │
│  • expected_value_range: ($min, $max)                                      │
│  • specific_items_likely: ["paintings", "furniture", ...]                  │
│  • confidence: LOW/MEDIUM/HIGH                                             │
│  • recommended_appraiser: "art", "antiques", "military", etc.              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Уникальные показатели по эпохам владения

| Эпоха покупки | Что могли купить | Сегодняшняя ценность |
|---------------|-----------------|---------------------|
| **1920-1940** | Art Deco, early modernism | $$$$ (if authenticated) |
| **1940-1950** | WWII souvenirs, European refugees' items | $$$ - $$$$ |
| **1950-1970** | Mid-century modern (дёшево тогда!) | $$$$ (сейчас хайп) |
| **1970-1980** | Antiques before boom | $$$ |
| **1980-2000** | Speculative buying era | $$ - $$$$ |

### Specific High-Value Indicators

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RED FLAGS FOR WORLD-CLASS ITEMS                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  🎨 ART (highest potential):                                                │
│  □ "Art collector" + museum connection                                     │
│  □ "Studied in Paris/Florence/Rome"                                        │
│  □ Gallery owner or dealer                                                 │
│  □ Art history professor                                                   │
│  □ "Impressionist", "Old Master", "Modern art"                             │
│                                                                             │
│  🪖 MILITARY (WWII especially):                                             │
│  □ Officer rank (had access to better items)                               │
│  □ "Served in Germany 1945" (liberation period)                            │
│  □ "Served in Japan" (occupation period)                                   │
│  □ Intelligence/diplomatic corps                                           │
│  □ Generals/Admirals (gifts, seized items)                                 │
│                                                                             │
│  📚 BOOKS/DOCUMENTS:                                                        │
│  □ "Professor", "scholar", "bibliophile"                                   │
│  □ "First editions", "rare books"                                          │
│  □ University library donations                                            │
│  □ Historical society member                                               │
│                                                                             │
│  💎 JEWELRY/PRECIOUS:                                                       │
│  □ "Society" mentions (debutante, charity balls)                           │
│  □ Old family wealth indicators                                            │
│  □ European aristocratic connections                                       │
│                                                                             │
│  🏺 SPECIFIC COLLECTIONS:                                                   │
│  □ Asian art + lived/traveled in Asia                                      │
│  □ African art + served/lived in Africa                                    │
│  □ Pre-Columbian + traveled Latin America                                  │
│  □ Native American + lived in Southwest                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Real-World Discoveries (public cases)

| Находка | Где | Backstory | Стоимость |
|---------|-----|-----------|-----------|
| Declaration of Independence copy | Behind painting | Owner was historical society member | $2.4M |
| Fabergé egg | Estate sale | Russian immigrant family | $33M |
| Van Gogh sketch | Attic | Art dealer's estate | $15M |
| Ming vase | Used as umbrella stand | Family from Hong Kong | $22M |
| Baseball cards | Attic | Father collected in 1910s | $3M |
| First edition Shakespeare | Library | Professor's estate | $6M |
| WWII Nazi memorabilia | Basement | Veteran served in Germany | $500K |
| Japanese samurai sword | Closet | Veteran served in Pacific | $100K |

### Model 38: WorldClassAntiquePredictor

```python
class WorldClassAntiquePredictor:
    """
    Predicts probability of world-class antiques in property
    based on owner documentation analysis.

    Combines: obituary NLP + profession lookup + heritage analysis
    """

    def predict(self, owner: OwnerData, documents: List[Document]) -> AntiqueAnalysis:
        scores = {}

        # Analyze obituary
        if obituary := self._find_obituary(owner):
            scores['profession'] = self._extract_profession_score(obituary)
            scores['collector'] = self._extract_collector_score(obituary)
            scores['wealth'] = self._extract_wealth_score(obituary)
            scores['heritage'] = self._extract_heritage_score(obituary)
            scores['travel'] = self._extract_travel_score(obituary)
            scores['military'] = self._extract_military_score(obituary)
            scores['specific'] = self._extract_specific_collection(obituary)

        # Cross-reference with other sources
        if museum_connections := self._check_museum_databases(owner):
            scores['museum'] = 0.9  # Strong signal

        if auction_history := self._check_auction_records(owner):
            scores['auction'] = 0.95  # Very strong signal

        # Calculate weighted score
        world_class_score = self._weighted_average(scores)

        # Estimate value range
        value_range = self._estimate_value_range(world_class_score, scores)

        return AntiqueAnalysis(
            owner=owner,
            world_class_score=world_class_score,
            scores_breakdown=scores,
            expected_value_range=value_range,
            likely_items=self._predict_item_types(scores),
            confidence=self._calculate_confidence(scores),
            recommended_appraisers=self._recommend_appraisers(scores),
            red_flags=self._identify_red_flags(scores),
            is_unicorn=(world_class_score >= 0.8)
        )
```

### Combined Score: Foreclosure + x1000 Antiques

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    🦄 UNICORN PROPERTY SCORE 🦄                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  НАПОМИНАНИЕ:                                                              │
│  • Foreclosure Score = нет наследников → гарантированный foreclosure       │
│  • x1000 Score = потенциал антиквариата × 1000 от стоимости property       │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  Foreclosure Score (no heirs):     _____ / 1.0                             │
│  x1000 Antique Score:              _____ / 1.0  ← World-class antiques!    │
│  Denis Furniture Score:            _____ / 1.0                             │
│  Property Condition Score:         _____ / 1.0                             │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  UNICORN SCORE = (Foreclosure × 0.4) + (x1000 Antique × 0.3) +             │
│                  (Furniture × 0.1) + (Condition × 0.2)                     │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  UNICORN SCORE >= 0.85: 🦄 EXCEPTIONAL OPPORTUNITY                         │
│  • Foreclosure Score HIGH → guaranteed win at auction                      │
│  • x1000 Antique Score HIGH → потенциал найти ценности × 1000              │
│  • Property itself valuable                                                │
│  • IMMEDIATE ACTION REQUIRED                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Data Sources by Reliability

| Источник | Reliability | Cost | Coverage |
|----------|-------------|------|----------|
| **Obituaries (local papers)** | HIGH | Free/Low | 60% of deaths |
| **Social Security Death Index** | HIGH | Free | 95% of deaths |
| **Probate Court Records** | HIGH | Free | If filed |
| **Property Co-owner Records** | HIGH | Free | 100% |
| **Ancestry.com** | MEDIUM | $20/mo | Good for genealogy |
| **LexisNexis/TLO** | HIGH | $1-5/search | Comprehensive |
| **Facebook/Social Media** | LOW-MEDIUM | Free | Varies |

---

### Bonus Value Score (добавить в Property Analysis Sheet?)

```
BONUS VALUE POTENTIAL:

Owner Age:        □ <65  □ 65-75  □ 75-85  □ 85+
Ownership Years:  □ <10  □ 10-20  □ 20-30  □ 30+
Estate Cleared?:  □ Yes  □ Partial □ No    □ Unknown
Interior Photos:  □ Empty □ Some items □ Full of stuff
Era of House:     □ Post-1990 □ 1970-90 □ 1950-70 □ Pre-1950

Estimated Bonus Value: $_______ to $_______
Confidence: LOW (speculative)
```

---

### DECISION MATRIX: Keep vs Flip

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    KEEP FOR MIAW vs FLIP?                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  После осмотра, если property фундаментально хорош (0-1 red flags):        │
│                                                                             │
│  KEEP FOR MIAW & DENIS если:                                               │
│  ✓ Near Spearfish (семья рядом)                                            │
│  ✓ 3+ bedrooms (будущая семья)                                             │
│  ✓ Yard/land (место для детей, собаки)                                     │
│  ✓ Good neighborhood (safe, schools)                                       │
│  ✓ Denis family WANTS to renovate this one                                 │
│  ✓ "Feels like home" gut feeling                                           │
│                                                                             │
│  FLIP IT если:                                                              │
│  ○ Far from Spearfish                                                      │
│  ○ Too small (1-2 bedrooms)                                                │
│  ○ Bad neighborhood                                                        │
│  ○ Quick cosmetic fix = fast profit                                        │
│  ○ Denis family says "not for us"                                          │
│                                                                             │
│  IMPORTANT: Не нужно решать сразу!                                         │
│  Можно купить, начать ремонт, и ПОТОМ решить keep или flip.                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Классификация по типу ремонта: Live-in vs Flip

> *"Где семья Дениса — для себя, не для перепродажи. Ремонт долго, для заработка проще перепродажа."*

### Две стратегии — разные критерии

| Критерий | 🏠 LIVE-IN (South Dakota) | 💰 FLIP (Arizona/Utah) |
|----------|--------------------------|------------------------|
| **Цель** | Жить самим | Быстро продать |
| **Время** | Можно 1-2 года | 3-6 месяцев max |
| **Рабочая сила** | Семья Denis (бесплатно) | Подрядчики (дорого) |
| **Фокус** | Фундамент, крыша, системы | Косметика, curb appeal |
| **Бюджет ремонта** | До $30K (постепенно) | До $10K (быстро) |
| **Риск** | Низкий (для себя) | Средний (рынок может упасть) |

---

### Классификация состояния property

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROPERTY CONDITION CLASSIFICATION                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CLASS A: MOVE-IN READY                                                     │
│  ════════════════════════                                                   │
│  • Всё работает, косметика OK                                              │
│  • Ремонт: $0-2,000 (мелочи)                                               │
│  • Время: 0-2 недели                                                       │
│  • Для: Live-in ✅ | Flip ✅ (но маржа низкая)                             │
│                                                                             │
│  CLASS B: COSMETIC ONLY                                                     │
│  ═══════════════════════                                                    │
│  • Структура OK, нужна косметика                                           │
│  • Paint, flooring, fixtures, landscaping                                  │
│  • Ремонт: $2,000-10,000                                                   │
│  • Время: 2-8 недель                                                       │
│  • Для: Live-in ✅ | Flip ✅✅ (ИДЕАЛЬНО для flip!)                        │
│                                                                             │
│  CLASS C: SYSTEMS UPDATE                                                    │
│  ═══════════════════════                                                    │
│  • Структура OK, но системы старые                                         │
│  • HVAC, electrical, plumbing, roof (частично)                             │
│  • Ремонт: $10,000-30,000                                                  │
│  • Время: 1-3 месяца                                                       │
│  • Для: Live-in ✅✅ (хорошо!) | Flip ⚠️ (долго, дорого)                   │
│                                                                             │
│  CLASS D: STRUCTURAL ISSUES                                                 │
│  ══════════════════════════                                                 │
│  • Проблемы с фундаментом, крышей, стенами                                 │
│  • Foundation cracks, roof replacement, wall damage                        │
│  • Ремонт: $30,000-80,000                                                  │
│  • Время: 3-6 месяцев                                                      │
│  • Для: Live-in ⚠️ (если семья может) | Flip ❌ (слишком дорого)           │
│                                                                             │
│  CLASS F: TEAR-DOWN / LAND VALUE ONLY                                       │
│  ════════════════════════════════════                                       │
│  • Структура не подлежит ремонту                                           │
│  • Снос + новое строительство                                              │
│  • Ценность = только земля                                                 │
│  • Для: Live-in ❌ | Flip ❌ (только если land value высокая)              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Что проверять: Структура vs Косметика

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    STRUCTURAL vs COSMETIC CHECKLIST                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  🔴 STRUCTURAL (дорого, долго, критично)                                   │
│  ════════════════════════════════════════                                   │
│                                                                             │
│  FOUNDATION:                                                                │
│  □ Cracks in foundation?      □ None □ Hairline □ Major (>1/4")           │
│  □ Uneven floors?             □ No   □ Slight   □ Significant             │
│  □ Doors/windows stick?       □ No   □ Some     □ Many                    │
│  □ Water in basement?         □ No   □ Damp     □ Flooding               │
│  → Cost if issues: $5,000 - $50,000+                                       │
│                                                                             │
│  ROOF:                                                                      │
│  □ Age of roof?               _____ years (replace if >20-25)             │
│  □ Missing shingles?          □ No   □ Few      □ Many                    │
│  □ Sagging?                   □ No   □ Slight   □ Major                   │
│  □ Water stains on ceiling?   □ No   □ Old      □ Active leak            │
│  → Cost if replace: $8,000 - $25,000                                       │
│                                                                             │
│  WALLS/STRUCTURE:                                                           │
│  □ Cracks in walls?           □ No   □ Hairline □ Major                   │
│  □ Bowing walls?              □ No   □ Slight   □ Major                   │
│  □ Termite damage?            □ No   □ Old      □ Active                  │
│  □ Rot in wood?               □ No   □ Minor    □ Major                   │
│  → Cost if issues: $2,000 - $30,000                                        │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  🟡 SYSTEMS (medium cost, планируемо)                                      │
│  ════════════════════════════════════                                       │
│                                                                             │
│  ELECTRICAL:                                                                │
│  □ Panel age/type?            _____ (replace if fuse box or <100 amp)     │
│  □ Outlets grounded?          □ Yes  □ No (2-prong = old)                 │
│  □ Knob-and-tube wiring?      □ No   □ Yes (MUST replace)                 │
│  → Cost to update: $3,000 - $15,000                                        │
│                                                                             │
│  PLUMBING:                                                                  │
│  □ Pipe material?             □ Copper ✓ □ PEX ✓ □ Galvanized ⚠️ □ Lead ❌│
│  □ Water pressure OK?         □ Yes  □ Low                                │
│  □ Water heater age?          _____ years (replace if >10-15)             │
│  □ Sewer line condition?      □ Good □ Unknown □ Issues                   │
│  → Cost to update: $2,000 - $20,000                                        │
│                                                                             │
│  HVAC:                                                                      │
│  □ System type?               □ Central □ Window units □ None             │
│  □ Age?                       _____ years (replace if >15-20)             │
│  □ Works properly?            □ Yes  □ Needs repair □ Dead                │
│  → Cost to replace: $5,000 - $15,000                                       │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  🟢 COSMETIC (cheap, fast, high impact)                                    │
│  ═══════════════════════════════════════                                    │
│                                                                             │
│  INTERIOR:                                                                  │
│  □ Paint needed?              □ No   □ Touch-up □ Full repaint            │
│    → Cost: $500-3,000                                                      │
│  □ Flooring condition?        □ Good □ Refinish □ Replace                 │
│    → Cost: $1,000-8,000                                                    │
│  □ Kitchen cabinets?          □ Good □ Paint    □ Replace                 │
│    → Cost: $200-15,000                                                     │
│  □ Countertops?               □ Good □ Replace                            │
│    → Cost: $500-5,000                                                      │
│  □ Bathrooms?                 □ Good □ Update fixtures □ Full reno        │
│    → Cost: $200-10,000                                                     │
│  □ Fixtures/hardware?         □ Good □ Update                             │
│    → Cost: $100-500                                                        │
│                                                                             │
│  EXTERIOR:                                                                  │
│  □ Siding?                    □ Good □ Paint/wash □ Replace               │
│    → Cost: $500-15,000                                                     │
│  □ Windows?                   □ Good □ Repair □ Replace                   │
│    → Cost: $200-10,000                                                     │
│  □ Landscaping?               □ Good □ Cleanup □ Full redo                │
│    → Cost: $200-5,000                                                      │
│  □ Driveway?                  □ Good □ Seal    □ Replace                  │
│    → Cost: $100-5,000                                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Матрица решений: Live-in vs Flip

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DECISION MATRIX: LIVE-IN vs FLIP                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PROPERTY CLASS    │  LIVE-IN (SD)           │  FLIP (AZ/UT)               │
│  ══════════════════╪═════════════════════════╪═════════════════════════════│
│                    │                         │                             │
│  CLASS A           │  ✅ BUY                  │  ⚠️ Low margin              │
│  (Move-in ready)   │  Сразу жить             │  Мало места для profit      │
│                    │                         │                             │
│  CLASS B           │  ✅ BUY                  │  ✅✅ IDEAL FOR FLIP         │
│  (Cosmetic only)   │  Семья сделает красиво  │  Quick fix, high ROI       │
│                    │                         │                             │
│  CLASS C           │  ✅✅ BEST FOR LIVE-IN   │  ⚠️ Risky                   │
│  (Systems update)  │  Denis family = free    │  Contractors expensive     │
│                    │  labor for HVAC etc.    │  Timeline risk             │
│                    │                         │                             │
│  CLASS D           │  ⚠️ Only if cheap       │  ❌ AVOID                   │
│  (Structural)      │  + family has skills    │  Too expensive for flip    │
│                    │  Long-term project      │  Too risky                 │
│                    │                         │                             │
│  CLASS F           │  ❌ AVOID               │  ❌ AVOID                   │
│  (Tear-down)       │  Unless land for build  │  Not worth it              │
│                    │                         │                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Конкретно для Miw & Denis

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MIW'S DUAL STRATEGY                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TRACK 1: SOUTH DAKOTA (Lawrence County / Spearfish)                       │
│  ═══════════════════════════════════════════════════                        │
│                                                                             │
│  Goal: Find HOME for Miw & Denis                                           │
│                                                                             │
│  IDEAL PROPERTY:                                                            │
│  • Class C (systems need update)                                           │
│  • Good foundation ✓                                                       │
│  • Good roof (or budget to replace)                                        │
│  • 3 bed / 2 bath (future family)                                          │
│  • Near Denis family (help with renovation)                                │
│                                                                             │
│  WHY CLASS C IS PERFECT:                                                    │
│  • Cheaper at auction (scared buyers)                                      │
│  • Denis family = FREE skilled labor                                       │
│  • Can renovate over 1-2 years (no rush)                                   │
│  • End result: quality home, low cost                                      │
│                                                                             │
│  BUDGET:                                                                    │
│  • Purchase: $5,000-15,000 (tax deed)                                      │
│  • Renovation: $10,000-30,000 (over time)                                  │
│  • Total: $15,000-45,000                                                   │
│  • Market value after: $80,000-150,000                                     │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  TRACK 2: ARIZONA / UTAH (Flip properties)                                 │
│  ═════════════════════════════════════════                                  │
│                                                                             │
│  Goal: Build capital through quick flips                                   │
│                                                                             │
│  IDEAL PROPERTY:                                                            │
│  • Class B (cosmetic only!)                                                │
│  • Structure MUST be solid                                                 │
│  • Paint + flooring + landscaping = done                                   │
│  • High liquidity area                                                     │
│                                                                             │
│  WHY CLASS B IS PERFECT:                                                    │
│  • Quick turnaround (4-8 weeks)                                            │
│  • Low renovation cost ($2,000-8,000)                                      │
│  • Contractors can do it (don't need Denis)                                │
│  • Predictable timeline and budget                                         │
│                                                                             │
│  AVOID FOR FLIP:                                                            │
│  • Class C (too long, contractors expensive)                               │
│  • Class D (way too risky)                                                 │
│  • Rural areas (hard to sell)                                              │
│                                                                             │
│  BUDGET:                                                                    │
│  • Purchase: $1,000-5,000 (tax lien → foreclosure)                        │
│  • Renovation: $2,000-8,000                                                │
│  • Holding costs: $500-1,000                                               │
│  • Total: $3,500-14,000                                                    │
│  • Sell for: $15,000-40,000                                                │
│  • Profit: $5,000-25,000 per flip                                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Renovation Scope Estimator

```python
class RenovationScopeEstimator:
    """
    Estimates renovation scope and cost based on property condition.

    Used in: Property Analysis Sheet, Document Package
    """

    def estimate(self, property: PropertyData, photos: List[Photo]) -> RenovationEstimate:
        structural_issues = self._assess_structural(property, photos)
        systems_issues = self._assess_systems(property)
        cosmetic_issues = self._assess_cosmetic(property, photos)

        # Classify
        if structural_issues.severity >= 0.7:
            property_class = "D"  # Structural
        elif structural_issues.severity >= 0.3:
            property_class = "D"  # Structural (borderline)
        elif systems_issues.severity >= 0.5:
            property_class = "C"  # Systems update
        elif cosmetic_issues.severity >= 0.3:
            property_class = "B"  # Cosmetic
        else:
            property_class = "A"  # Move-in ready

        return RenovationEstimate(
            property_class=property_class,
            structural_cost=structural_issues.estimated_cost,
            systems_cost=systems_issues.estimated_cost,
            cosmetic_cost=cosmetic_issues.estimated_cost,
            total_cost=sum([
                structural_issues.estimated_cost,
                systems_issues.estimated_cost,
                cosmetic_issues.estimated_cost
            ]),
            timeline_weeks=self._estimate_timeline(property_class),
            suitable_for_flip=property_class in ["A", "B"],
            suitable_for_livein=property_class in ["A", "B", "C"],
            denis_family_can_do=property_class in ["B", "C"],  # Family skills
            requires_contractors=property_class in ["C", "D"]
        )
```

### Printed Document: Renovation Assessment Sheet

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RENOVATION ASSESSMENT SHEET                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Property: _______________________________  Date: ____________              │
│                                                                             │
│  PROPERTY CLASS:  □ A (ready)  □ B (cosmetic)  □ C (systems)  □ D (struct) │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  STRUCTURAL ASSESSMENT                                          COST EST.   │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  Foundation:     □ Good  □ Minor cracks  □ Major issues      $_________    │
│  Roof:           □ Good  □ Repair needed □ Replace           $_________    │
│  Walls/Framing:  □ Good  □ Minor repair  □ Major repair      $_________    │
│  Termite/Rot:    □ None  □ Old damage    □ Active            $_________    │
│                                                                             │
│                                         STRUCTURAL TOTAL:     $_________    │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  SYSTEMS ASSESSMENT                                             COST EST.   │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  Electrical:     □ Good  □ Update panel  □ Rewire            $_________    │
│  Plumbing:       □ Good  □ Repairs       □ Repipe            $_________    │
│  HVAC:           □ Good  □ Repair        □ Replace           $_________    │
│  Water Heater:   □ Good  □ Replace                           $_________    │
│                                                                             │
│                                            SYSTEMS TOTAL:     $_________    │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  COSMETIC ASSESSMENT                                            COST EST.   │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  Interior Paint: □ Good  □ Touch-up  □ Full repaint          $_________    │
│  Flooring:       □ Good  □ Refinish  □ Replace               $_________    │
│  Kitchen:        □ Good  □ Update    □ Remodel               $_________    │
│  Bathrooms:      □ Good  □ Update    □ Remodel               $_________    │
│  Fixtures:       □ Good  □ Update                            $_________    │
│  Ext. Paint:     □ Good  □ Touch-up  □ Full repaint          $_________    │
│  Landscaping:    □ Good  □ Cleanup   □ Full redo             $_________    │
│                                                                             │
│                                           COSMETIC TOTAL:     $_________    │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│                              GRAND TOTAL:                     $_________    │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  RECOMMENDATION                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  Suitable for LIVE-IN (SD)?     □ Yes  □ No   Reason: _______________     │
│  Suitable for FLIP (AZ/UT)?     □ Yes  □ No   Reason: _______________     │
│  Denis family can do?           □ Yes  □ Partial  □ No                     │
│  Timeline estimate:             _______ weeks/months                       │
│                                                                             │
│  DECISION:  □ BUY for live-in   □ BUY for flip   □ PASS                   │
│                                                                             │
│  Notes: _______________________________________________________________   │
│  _____________________________________________________________________    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Quick Reference Card (для Miw)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    QUICK REFERENCE: WHAT TO LOOK FOR                        │
├──────────────────────────────────┬──────────────────────────────────────────┤
│  SOUTH DAKOTA (для жизни)        │  ARIZONA/UTAH (для перепродажи)         │
├──────────────────────────────────┼──────────────────────────────────────────┤
│                                  │                                          │
│  ✅ ХОРОШО:                      │  ✅ ХОРОШО:                              │
│  • Solid foundation              │  • Move-in ready or cosmetic only       │
│  • Good bones (structure)        │  • Paint + carpet = done                │
│  • Needs cosmetic + systems      │  • Good location (sells fast)           │
│  • 3+ bedrooms                   │  • No structural issues                 │
│  • Near Denis family             │  • High liquidity area                  │
│                                  │                                          │
│  ❌ ИЗБЕГАТЬ:                    │  ❌ ИЗБЕГАТЬ:                            │
│  • Foundation cracks             │  • ANY structural issues                │
│  • Severe water damage           │  • Systems need update                  │
│  • Mold problems                 │  • Rural location                       │
│  • Far from Spearfish            │  • Long renovation time                 │
│                                  │                                          │
│  💰 BUDGET:                      │  💰 BUDGET:                              │
│  • Buy: $5K-15K                  │  • Buy: $1K-5K                          │
│  • Reno: $10K-30K (over time)    │  • Reno: $2K-8K (quick)                 │
│  • Total: up to $45K             │  • Total: up to $14K                    │
│                                  │                                          │
│  ⏱️ TIMELINE:                    │  ⏱️ TIMELINE:                            │
│  • 1-2 years (no rush)           │  • 4-8 weeks (fast!)                    │
│                                  │                                          │
└──────────────────────────────────┴──────────────────────────────────────────┘
```

---

## 🤝 Связь с владельцем (Owner Communication)

### Как найти контакт владельца

| Метод | Описание | Cost | Success Rate |
|-------|----------|------|--------------|
| **County Records** | Mailing address в tax records | Free | HIGH |
| **Skip Tracing** | TLOxp, BeenVerified, Spokeo | $1-5/search | MEDIUM |
| **Title Company** | Могут найти контакт | Varies | MEDIUM |
| **Letter to Property** | Отправить письмо на адрес | $1 | LOW (if abandoned) |
| **Neighbors** | Спросить соседей | Free | MEDIUM |
| **Social Media** | Найти по имени | Free | LOW |

### Шаблон письма владельцу

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                          [Your Name]                                        │
│                          [Your Address]                                     │
│                          [Date]                                             │
│                                                                             │
│  To: Property Owner                                                         │
│  Re: Property at [Address], Parcel ID: [XXX-XXX-XXX]                       │
│                                                                             │
│  Dear Property Owner,                                                       │
│                                                                             │
│  I am writing regarding the above property which I understand               │
│  has delinquent property taxes. I am interested in learning                │
│  more about the property and its current condition.                         │
│                                                                             │
│  I would like to ask:                                                       │
│                                                                             │
│  1. Is the property currently occupied?                                     │
│  2. What is the current condition of the property?                         │
│  3. Are there any known issues (roof, plumbing, etc.)?                     │
│  4. Are you interested in selling the property directly?                   │
│  5. Do you plan to pay off the tax debt?                                   │
│                                                                             │
│  I understand you may have personal circumstances and I am                  │
│  approaching this with respect. If you would prefer to sell                │
│  the property rather than lose it to tax foreclosure, I may                │
│  be interested in a fair purchase.                                          │
│                                                                             │
│  Please feel free to contact me at:                                         │
│  Phone: [XXX-XXX-XXXX]                                                      │
│  Email: [your@email.com]                                                    │
│                                                                             │
│  Respectfully,                                                              │
│  [Your Name]                                                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Вопросы для владельца (если удастся связаться)

| Вопрос | Почему важно |
|--------|--------------|
| Жилое ли помещение? | Определить состояние |
| Какие проблемы? | Оценить ремонт |
| Почему не платите налоги? | Понять ситуацию |
| Планируете платить? | Шанс redemption |
| Готовы продать напрямую? | Может быть выгоднее чем auction |
| Есть ли арендаторы? | Юридические сложности |
| Есть ли ценные вещи внутри? | Если abandoned |

---

## ⚠️ Другие факторы (не учтённые ранее)

### Природные риски

| Риск | Источник данных | Важность |
|------|-----------------|----------|
| **Flood Zone** | FEMA flood maps | CRITICAL |
| **Fire Risk** | CAL FIRE, local maps | HIGH (особенно CA) |
| **Earthquake** | USGS fault maps | HIGH (CA, AK) |
| **Tornado** | NOAA storm data | MEDIUM (Midwest) |
| **Hurricane** | NOAA coastal maps | HIGH (FL, Gulf) |
| **Wildfire history** | Historical data | MEDIUM |

### Экологические риски

| Риск | Источник данных | Важность |
|------|-----------------|----------|
| **Superfund site** | EPA Superfund list | CRITICAL (avoid!) |
| **Brownfield** | EPA Brownfields | HIGH |
| **Underground tanks** | State DEQ records | MEDIUM |
| **Contaminated water** | EPA/State records | HIGH |
| **Radon** | EPA radon maps | MEDIUM |
| **Lead paint** | If built before 1978 | MEDIUM |
| **Asbestos** | If built before 1980 | MEDIUM |

### Утилиты (Utilities)

| Utility | Как проверить | Важность |
|---------|---------------|----------|
| **Electricity** | County/utility company | CRITICAL |
| **Water** | Municipal or well? | CRITICAL |
| **Sewer** | Municipal or septic? | CRITICAL |
| **Gas** | Utility company | HIGH |
| **Internet** | BroadbandNow.com | MEDIUM |
| **Cell coverage** | OpenSignal maps | MEDIUM |

### Зонирование и ограничения

| Фактор | Источник | Важность |
|--------|----------|----------|
| **Zoning type** | County planning | CRITICAL |
| **Can build/expand?** | County planning | HIGH |
| **HOA?** | Title search | HIGH |
| **Historic district?** | County records | MEDIUM |
| **Easements?** | Title search | HIGH |
| **Setback requirements** | County planning | MEDIUM |

### Будущее развитие

| Фактор | Источник | Impact |
|--------|----------|--------|
| **New highway planned?** | DOT plans | + or - |
| **Commercial development?** | City plans | + |
| **Industrial nearby?** | Zoning maps | - |
| **New school planned?** | School district | + |
| **Rezoning proposals?** | City council | Varies |

### Сводная таблица: ВСЕ факторы

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                    COMPLETE PROPERTY FACTORS CHECKLIST                          │
├────────────────────────────────────────────────────────────────────────────────┤
│                                                                                │
│  FINANCIAL (from system)              │  PHYSICAL (photos/visit)              │
│  ─────────────────────────            │  ────────────────────────             │
│  □ Tax lien amount                    │  □ Condition score                    │
│  □ Market value                       │  □ Roof condition                     │
│  □ Value-to-lien ratio                │  □ Foundation                         │
│  □ Interest rate                      │  □ Utilities present                  │
│  □ Prior years owed                   │  □ Road access                        │
│  □ Redemption probability             │  □ Lot size/shape                     │
│                                       │                                       │
│  ML SCORES (from system)              │  INFRASTRUCTURE (proximity)           │
│  ───────────────────────              │  ─────────────────────────            │
│  □ Risk score                         │  □ Schools                            │
│  □ ROI prediction                     │  □ Healthcare                         │
│  □ Serial payer score                 │  □ Shopping                           │
│  □ Karma score ⭐                     │  □ Transit                            │
│  □ Lifestyle match ⭐                 │  □ Employment                         │
│                                       │                                       │
│  RISKS (research)                     │  LEGAL (title search)                 │
│  ────────────────                     │  ──────────────────                   │
│  □ Flood zone                         │  □ Title clear                        │
│  □ Fire risk                          │  □ No IRS liens                       │
│  □ Environmental                      │  □ No HOA liens                       │
│  □ Natural disasters                  │  □ Easements known                    │
│  □ Crime rate                         │  □ Zoning verified                    │
│                                       │                                       │
│  OWNER INFO (if found)                │  HISTORICAL (photos)                  │
│  ─────────────────────                │  ────────────────────                 │
│  □ Owner type (individual/LLC)        │  □ Condition trend                    │
│  □ Contact attempted                  │  □ Years abandoned?                   │
│  □ Response received                  │  □ Recent changes                     │
│  □ Reason for delinquency             │  □ Neighborhood trend                 │
│                                       │                                       │
└────────────────────────────────────────────────────────────────────────────────┘
```

---

### Вопросы для Miw (уточнить preferences)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LIFESTYLE PREFERENCES QUESTIONNAIRE                      │
│                    Анкета предпочтений для Miw                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Какое окружение предпочитаешь?                                         │
│     □ Молодые семьи (дети, школы, парки)                                   │
│     □ Молодые профессионалы (городская жизнь, кафе, networking)            │
│     □ Смешанное (разные возрасты)                                          │
│     □ Тихое/пенсионное (спокойствие, природа)                              │
│     □ Удалённое/rural (privacy, простор)                                   │
│     □ Не важно                                                              │
│                                                                             │
│  2. Цель покупки?                                                           │
│     □ Жить самим (live in)                                                  │
│     □ Сдавать в аренду (rental income)                                     │
│     □ Перепродать с прибылью (flip)                                        │
│     □ Долгосрочная инвестиция (hold)                                       │
│     □ Пока не решила                                                        │
│                                                                             │
│  3. Планируете детей в ближайшие 5 лет?                                    │
│     □ Да → школы важны                                                     │
│     □ Нет                                                                   │
│     □ Не уверены                                                            │
│                                                                             │
│  4. Важна ли близость к семье Denis (South Dakota)?                        │
│     □ Очень важно (хотим рядом)                                            │
│     □ Желательно                                                            │
│     □ Не важно (готовы в любом штате)                                      │
│                                                                             │
│  5. Когда "LA" - ты имела ввиду:                                           │
│     □ Los Angeles, California (Beverly Hills мечта)                        │
│     □ Louisiana (штат)                                                      │
│     □ Оба интересны                                                         │
│     □ Не помню / другое                                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Молитва/Намерение перед покупкой (опционально)

> *"Пусть эта покупка принесёт благо:*
> *- Нам: честный доход и дом для семьи*
> *- Соседям: улучшение района*
> *- Обществу: affordable housing*
> *- Бывшему владельцу: освобождение от бремени*
> *Пусть эта инвестиция создаст больше добра, чем было до неё."*

---

## Vision: Path to Beverly Hills (Staircase Strategy)

### Beverly Hills - Цель (The Dream)

**Реальные данные LA County (Jan 2026):**

| Метрика | Значение |
|---------|----------|
| Средняя цена на auction | **$3,914,312** |
| Медианная цена дома | **$5,620,000** |
| Цена за sqft | $1,399 |
| Foreclosures доступно | 2-11 объектов |

**LA County Tax Deed Auctions 2026:**

| Auction | Даты | Регистрация | Платформа |
|---------|------|-------------|-----------|
| **April 2026** | Apr 18-21 | Mar 13 - Apr 14 | [GovEase](https://www.govease.com/los-angeles) |
| **June 2026** | Jun 6-9 | May 1 - Jun 2 | [GovEase](https://www.govease.com/los-angeles) |

**Property list:** Будет доступен в February 2026

**Источники:** [LA County Treasurer](https://ttc.lacounty.gov/schedule-of-upcoming-auctions/)

---

### Staircase Strategy: От $1,000 до Beverly Hills

**Это НЕ лотерея, это бизнес-модель.**

```
ЦЕЛЬ: Beverly Hills ($3-5M)
═══════════════════════════════════════════════════════════════════════════════
                                                              ┌─────────────┐
                                                         ▲    │  2040       │
                                                         │    │  Beverly    │
                                                    $3M+ │    │  Hills      │
                                                         │    └─────────────┘
                                              ┌──────────┴──────────┐
                                              │   Flip #7-8         │
                                              │   LA premium area   │
                                              │   $1M → $2M         │
                                              └──────────┬──────────┘
                                                         │
                                    ┌────────────────────┴────────────────────┐
                                    │   Flip #6: LA area fixer                │
                                    │   $400K → $700K                         │
                                    └────────────────────┬────────────────────┘
                                                         │
                          ┌──────────────────────────────┴──────────────────────────────┐
                          │   Flip #4-5: California starters (Riverside, San Bernardino)│
                          │   $150K → $300K                                             │
                          └──────────────────────────────┬──────────────────────────────┘
                                                         │
                ┌────────────────────────────────────────┴────────────────────────────────────────┐
                │   Flip #2-3: Regional expansion (Utah, Wisconsin, Nevada)                      │
                │   $40K → $100K                                                                 │
                └────────────────────────────────────────┬────────────────────────────────────────┘
                                                         │
      ┌──────────────────────────────────────────────────┴──────────────────────────────────────────────────┐
      │   Flip #1: South Dakota fixer-upper (семья Denis делает ремонт БЕСПЛАТНО)                          │
      │   $5K purchase → $25K after renovation                                                              │
      └──────────────────────────────────────────────────┬──────────────────────────────────────────────────┘
                                                         │
══════════════════════════════════════════════════════════════════════════════════════════════════════════════
СТАРТ: $1,000 → Arizona Tax Lien (Feb 2026) → 16% income while waiting
```

---

### Конкретный расчёт: Обычный путь vs Sweet Spot путь

#### Обычный путь: 8 Flips за 14 лет

| Flip | Год | Штат | Buy | Fix (Denis) | Sell | Profit | Капитал |
|------|-----|------|-----|-------------|------|--------|---------|
| 0 | 2026 | AZ | - | - | - | - | **$1,000** |
| 1 | 2027 | SD | $5K | $3K (free) | $20K | $12K | **$13K** |
| 2 | 2028 | WI/UT | $20K | $8K (family) | $50K | $22K | **$35K** |
| 3 | 2030 | NV/UT | $50K | $15K | $100K | $35K | **$70K** |
| 4 | 2032 | CA (Inland) | $100K | $25K | $180K | $55K | **$125K** |
| 5 | 2034 | CA (suburban) | $180K | $40K | $320K | $100K | **$225K** |
| 6 | 2036 | LA area | $350K | $80K | $600K | $170K | **$395K** |
| 7 | 2038 | LA better | $600K | $120K | $1.1M | $380K | **$775K** |
| 8 | 2040 | **Beverly Hills** | $1.2M | $200K | LIVE | - | **🏠 HOME** |

#### ⚡ Sweet Spot путь: 6 Flips за 9-10 лет (+ Good Karma)

| Flip | Год | Тип Sweet Spot | Buy | Fix | Sell | Karma | Капитал |
|------|-----|----------------|-----|-----|------|-------|---------|
| 0 | 2026 | LA blighted lien (18mo) | $500 | - | - | ✅ +0.5 | **$1,000** |
| 1 | 2027 | SD abandoned + AZ foreclosure | $8K | $4K (free) | $35K | ✅ +0.4 | **$28K** |
| 2 | 2029 | WI $3K program (blighted) | $25K | $12K | $70K | ✅ +0.5 | **$61K** |
| 3 | 2031 | CA blighted inland | $80K | $25K | $160K | ✅ +0.4 | **$116K** |
| 4 | 2033 | LA area fixer (karma+) | $180K | $50K | $380K | ✅ +0.3 | **$266K** |
| 5 | 2035 | LA premium area | $400K | $100K | $750K | ➡️ 0 | **$516K** |
| 6 | **2036** | **Beverly Hills** | $800K | $150K | LIVE | ✅ | **🏠 HOME** |

**Экономия времени:** 4-5 лет быстрее через Sweet Spots + хорошая карма!

#### Почему Sweet Spots ускоряют

| Фактор | Обычный путь | Sweet Spot путь |
|--------|--------------|-----------------|
| Louisiana redemption | N/A | 18 мес (vs 3 года) |
| AZ high-probability | Случайно | Целенаправленно |
| Blighted = ниже цена | Market price | 30-50% дисконт |
| Karma bonus | Нет | ✨ Divine help? |
| Меньше конкуренции | Все видят | Только мы видим |

**Ключевые множители:**

| Фактор | Экономия на flip | За 8 flips |
|--------|------------------|------------|
| Denis (ремонт) | $20K-$100K | **$400K+** |
| Семья Denis (labor) | $10K-$50K | **$200K+** |
| Дедушка (координация) | Оптимизация | **$100K+** |
| **ИТОГО экономия** | | **$700K+** |

**Без семьи Denis** этот путь занял бы 20-25 лет и требовал бы $500K+ на contractors.

---

### Timeline: 2026 → 2040

```
2026 ─────────────────────────────────────────────────────────────────► 2040
  │                                                                      │
  │  Feb: AZ liens ($1K)                                                │
  │  May: UT deed ($500)                                                │
  │  Dec: SD deed ($3K) ◄── Denis joins                                 │
  │                                                                      │
  │  2027: SD renovation (family help)                                  │
  │  2028: Sell SD → Buy WI/UT                                          │
  │  2030: Sell WI → Buy NV/CA inland                                   │
  │  2032: Enter California market                                      │
  │  2034-36: Move up LA suburbs                                        │
  │  2038: LA premium areas                                             │
  │  2040: Beverly Hills purchase ◄────────────────────────────────── 🏠│
  │                                                                      │
```

---

### Почему это работает (не лотерея)

| Фактор | Лотерея | Staircase Strategy |
|--------|---------|-------------------|
| Вероятность успеха | 0.0001% | **60-80%** |
| Контроль | Нет | **Полный** |
| Навыки | Не нужны | **Denis: ремонт** |
| Семья | Не помогает | **Бесплатная рабочая сила** |
| Timeline | Мгновенно | **14 лет (терпение)** |
| Риск потери всего | Высокий | **Низкий (реальные активы)** |

**Математика экспоненты:**
- Каждый flip увеличивает капитал в **1.5-2x**
- 8 flips × 1.7x среднее = **1.7^8 = 69x** рост
- $1,000 × 69 = **$69,000** (минимум)
- С экономией на ремонте: **$500K-$1M+**

---

### Beverly Hills Foreclosure Examples (для вдохновения)

**Что продаётся на LA County auctions:**

| Тип | Price Range | Где | Notes |
|-----|-------------|-----|-------|
| Desert lot | $8K-$20K | Lancaster, Palmdale | Entry point to CA |
| Condemned house | $45K-$80K | South LA, Compton | Needs major work |
| Fixer condo | $95K-$150K | Long Beach | Livable after work |
| Small house | $150K-$300K | Inland Empire | Good flip potential |
| Beverly Hills adjacent | $500K-$800K | West LA | Getting close |
| **Beverly Hills** | **$3M-$10M+** | Beverly Hills | THE GOAL |

**Миссия для Miw:** Смотреть на эти объекты НЕ чтобы купить сейчас, а чтобы **видеть цель** и **понимать путь**.

---

## Диверсификация: Не класть все яйца в одну корзину

### Принцип распределения $1,000

```
$1,000 TOTAL
    │
    ├── 40% ($400) ──► Arizona Tax Liens (Feb 2026)
    │                  2-3 liens по $150-200
    │
    ├── 30% ($300) ──► Louisiana Tax Liens (2026)
    │                  2-3 liens по $100-150
    │                  (НОВАЯ система = меньше конкуренции)
    │
    ├── 20% ($200) ──► Utah Tax Deed (May 2026)
    │                  1 участок с помощью Rupa/Shon
    │
    └── 10% ($100) ──► Reserve
                       Subsequent taxes, fees, emergencies
```

### Диверсификация по измерениям

| Измерение | Как диверсифицировать | Пример для Miw |
|-----------|----------------------|----------------|
| **Штаты** | 2-3 разных штата | AZ + LA + UT |
| **Тип** | Liens + Direct land | 70% liens, 30% deed |
| **Timeline** | Разные auction dates | Feb + May + TBD |
| **Риск** | Conservative + Aggressive | 60% safe, 40% foreclosure-hunting |
| **Karma** | Mix good karma properties | 80% karma+, 20% neutral |

### Матрица диверсификации для $1,000

| # | Штат | Тип | Сумма | Риск | Karma | Auction | Ожидание |
|---|------|-----|-------|------|-------|---------|----------|
| 1 | AZ | Tax Lien | $200 | Low | +0.2 | Feb 10 | 16% interest |
| 2 | AZ | Tax Lien (aggressive) | $200 | Med | +0.5 | Feb 10 | Foreclosure chance |
| 3 | LA | Tax Lien (blighted) | $150 | Med | +0.7 | TBD | 12% + 5% penalty |
| 4 | LA | Tax Lien | $150 | Low | +0.3 | TBD | 8-12% interest |
| 5 | UT | Tax Deed (land) | $200 | Low | +0.4 | May | Ownership |
| - | - | **Reserve** | $100 | - | - | - | Emergency |
| **TOTAL** | | | **$1,000** | | | | |

---

## 📄 Печатные документы для Miw

### Документ 1: PORTFOLIO SUMMARY (Обзор портфеля)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     MIW'S TAX LIEN PORTFOLIO 2026                           │
│                         Общий бюджет: $1,000                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  РАСПРЕДЕЛЕНИЕ ПО ШТАТАМ                    РАСПРЕДЕЛЕНИЕ ПО ТИПУ          │
│  ════════════════════════                   ════════════════════════         │
│                                                                             │
│  Arizona      ████████████  $400 (40%)      Tax Liens  ████████████ $700    │
│  Louisiana    ████████      $300 (30%)      Tax Deeds  ████         $200    │
│  Utah         ████          $200 (20%)      Reserve    ██           $100    │
│  Reserve      ██            $100 (10%)                                      │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  TIMELINE 2026                                                              │
│  ════════════                                                               │
│                                                                             │
│  Jan     Feb        Mar     Apr     May        Jun ... Dec                  │
│   │       │          │       │       │          │       │                   │
│   │    AZ Auction    │       │    UT Auction    │    SD Auction             │
│   │    Feb 10-26     │       │    May 2026      │    Dec 21                 │
│   │    $400 ─────────┼───────┼───► $200 ────────┼────► (if Denis joins)     │
│   │                  │       │                  │                           │
│   └──────────────────┼───────┼──────────────────┼───────────────────────    │
│                      │       │                  │                           │
│                    LA Auction (TBD)             │                           │
│                    $300 ────────────────────────┘                           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  ОЖИДАЕМЫЕ РЕЗУЛЬТАТЫ (3 года)                                              │
│  ═════════════════════════════                                              │
│                                                                             │
│  Сценарий A (90%): Все liens redeemed                                       │
│  ├── AZ: $400 × 16% × 3 года = $192 interest                               │
│  ├── LA: $300 × 12% × 3 года = $108 interest                               │
│  ├── UT: Land ownership (value TBD)                                         │
│  └── ИТОГО: ~$300 interest + land                                          │
│                                                                             │
│  Сценарий B (8%): 1 lien → foreclosure                                      │
│  ├── Property value: $10,000-$50,000                                        │
│  ├── Remaining liens: ~$200 interest                                        │
│  └── ИТОГО: Property + interest                                             │
│                                                                             │
│  Сценарий C (2%): Multiple foreclosures                                     │
│  └── ИТОГО: 2+ properties (exceptional)                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

Дата создания: ____________    Подпись Miw: ____________
```

---

### Документ 2: PROPERTY ANALYSIS SHEET (На каждый объект)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      PROPERTY ANALYSIS SHEET                                │
│                      Лист анализа недвижимости                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ОСНОВНАЯ ИНФОРМАЦИЯ                                                        │
│  ════════════════════                                                       │
│                                                                             │
│  Parcel ID: _______________________    State: ____  County: ______________  │
│                                                                             │
│  Property Address: ____________________________________________________    │
│                                                                             │
│  Property Type:  □ Vacant Land   □ House   □ Mobile Home   □ Commercial    │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  📸 ФОТОГРАФИИ (вклеить или прикрепить распечатки)                         │
│  ══════════════════════════════════════════════════                         │
│                                                                             │
│  ┌─────────────────────────────┐  ┌─────────────────────────────┐          │
│  │                             │  │                             │          │
│  │                             │  │                             │          │
│  │    STREET VIEW (Current)    │  │    SATELLITE VIEW           │          │
│  │                             │  │                             │          │
│  │    Дата съёмки: _________   │  │    Дата съёмки: _________   │          │
│  │                             │  │                             │          │
│  │                             │  │                             │          │
│  └─────────────────────────────┘  └─────────────────────────────┘          │
│                                                                             │
│  ┌─────────────────────────────┐  ┌─────────────────────────────┐          │
│  │                             │  │                             │          │
│  │                             │  │                             │          │
│  │   STREET VIEW (Historical)  │  │   ASSESSOR PHOTO            │          │
│  │                             │  │   (if available)            │          │
│  │   Дата съёмки: _________    │  │                             │          │
│  │   (самое старое доступное)  │  │   Дата: _________           │          │
│  │                             │  │                             │          │
│  └─────────────────────────────┘  └─────────────────────────────┘          │
│                                                                             │
│  Photo URLs (для справки):                                                  │
│  Street View: ___________________________________________________________  │
│  Google Maps: ___________________________________________________________  │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ФИНАНСОВЫЕ ДАННЫЕ                                                          │
│  ═════════════════                                                          │
│                                                                             │
│  Tax Lien Amount:        $__________                                        │
│  Market Value:           $__________                                        │
│  Value-to-Lien Ratio:    __________x  (хорошо если > 10x)                  │
│                                                                             │
│  Interest Rate:          __________%                                        │
│  Prior Years Owed:       __________ лет                                     │
│  Redemption Period:      __________ месяцев                                 │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ML PREDICTIONS (из системы TAXLIEN.online)                                 │
│  ═══════════════════════════════════════════                                │
│                                                                             │
│  Redemption Probability:    [____]%    □ High (>70%)  □ Med  □ Low (<30%)  │
│  Serial Payer Score:        [____]     □ Sweet Spot (>0.8)                 │
│  Expected ROI:              [____]%                                         │
│  Risk Score:                [____]/100                                      │
│                                                                             │
│  ⭐ KARMA SCORE:            [____]     □ Positive (>0.3)  □ Negative       │
│                                                                             │
│  Karma Factors:                                                             │
│  □ Blighted/Abandoned (+0.3)     □ Homestead Exemption (-0.5)              │
│  □ Dissolved LLC (+0.2)          □ Elderly Owner (-0.3)                    │
│  □ 5+ Years Delinquent (+0.2)    □ Recent Hardship (-0.2)                  │
│  □ No Mortgage (+0.1)            □ Active Mortgage (-0.2)                  │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  DUE DILIGENCE CHECKLIST                                                    │
│  ═══════════════════════                                                    │
│                                                                             │
│  □ Google Maps/Satellite viewed        □ Road access confirmed              │
│  □ No environmental hazards            □ Zoning allows building             │
│  □ No IRS/HOA liens                    □ Title clear                        │
│  □ Denis/family can visit              □ Auction rules understood           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  РЕШЕНИЕ                                                                    │
│  ═══════                                                                    │
│                                                                             │
│  □ BUY - Покупать       Max Bid: $__________                               │
│  □ WATCH - Наблюдать    Reason: ________________________________           │
│  □ SKIP - Пропустить    Reason: ________________________________           │
│                                                                             │
│  Notes: ________________________________________________________________   │
│  _______________________________________________________________________   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

Дата анализа: ____________    Подпись: ____________
```

---

### Документ 3: COMPARISON MATRIX (Сравнение вариантов)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              COMPARISON MATRIX - MIW'S OPTIONS                                       │
│                              Матрица сравнения вариантов                                            │
├───────────────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────────────────────┤
│                   │ Option 1 │ Option 2 │ Option 3 │ Option 4 │ Option 5 │ WINNER                   │
├───────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────────────────────┤
│ State             │ AZ       │ AZ       │ LA       │ LA       │ UT       │                          │
│ County            │          │          │          │          │          │                          │
│ Parcel ID         │          │          │          │          │          │                          │
├───────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────────────────────┤
│ COST              │ $        │ $        │ $        │ $        │ $        │ Lowest: Option ___       │
├───────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────────────────────┤
│ Interest Rate     │    %     │    %     │    %     │    %     │ N/A      │ Highest: Option ___      │
├───────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────────────────────┤
│ Market Value      │ $        │ $        │ $        │ $        │ $        │ Best ratio: Option ___   │
├───────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────────────────────┤
│ Value/Lien Ratio  │    x     │    x     │    x     │    x     │    x     │                          │
├───────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────────────────────┤
│ Prior Years Owed  │          │          │          │          │ N/A      │ Most: Option ___         │
├───────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────────────────────┤
│ Redemption Prob   │    %     │    %     │    %     │    %     │ N/A      │ Lowest: Option ___       │
├───────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────────────────────┤
│ ⭐ Karma Score    │          │          │          │          │          │ Best karma: Option ___   │
├───────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────────────────────┤
│ Family Support    │ □ Yes    │ □ Yes    │ □ Yes    │ □ Yes    │ □ Yes    │ Most support: Option ___ │
│                   │ □ No     │ □ No     │ □ No     │ □ No     │ □ No     │                          │
├───────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────────────────────┤
│ Auction Date      │          │          │          │          │          │ Soonest: Option ___      │
├───────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────────────────────┤
│ OVERALL SCORE     │   /10    │   /10    │   /10    │   /10    │   /10    │ BEST: Option ___         │
│ (Miw's rating)    │          │          │          │          │          │                          │
└───────────────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────────────────────┘

Scoring Guide:
- Cost: Lower is better (within budget)
- Interest Rate: Higher is better
- Value/Lien Ratio: Higher is better (>10x ideal)
- Prior Years: More = higher foreclosure chance
- Redemption Prob: Lower = higher property acquisition chance
- Karma: Higher is better (positive impact)
- Family: Yes = support available

Final Selection: Options ___, ___, ___ (diversified portfolio)
Total Investment: $________ (must be ≤ $900, keep $100 reserve)

Дата: ____________    Подпись Miw: ____________
```

---

### Документ 4: DECISION CHECKLIST (Перед покупкой)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      PRE-PURCHASE DECISION CHECKLIST                        │
│                      Чеклист перед покупкой                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Property: ________________________    Amount: $__________                  │
│                                                                             │
│  ФИНАНСОВАЯ ПРОВЕРКА                                                        │
│  ════════════════════                                                       │
│  □ Сумма в пределах бюджета (max $____ для этой покупки)                   │
│  □ Останется резерв минимум $100                                           │
│  □ Value-to-lien ratio проверен (>10x)                                     │
│  □ Interest rate понятен                                                    │
│  □ Все fees учтены (auction fee, recording fee)                            │
│                                                                             │
│  ЮРИДИЧЕСКАЯ ПРОВЕРКА                                                       │
│  ════════════════════                                                       │
│  □ Title clear (нет других liens)                                          │
│  □ Нет IRS liens                                                           │
│  □ Нет HOA liens                                                           │
│  □ Redemption period понятен                                               │
│  □ Foreclosure процесс понятен (если нужно)                                │
│                                                                             │
│  ФИЗИЧЕСКАЯ ПРОВЕРКА                                                        │
│  ════════════════════                                                       │
│  □ Google Maps/Satellite просмотрен                                        │
│  □ Road access есть                                                        │
│  □ Нет flood zone                                                          │
│  □ Нет environmental hazards                                               │
│  □ Denis/family могут осмотреть (если возможно)                            │
│                                                                             │
│  KARMA ПРОВЕРКА ⭐                                                          │
│  ═══════════════                                                            │
│  □ Karma score > 0 (не причиняем вред)                                     │
│  □ НЕ homestead exemption (не чей-то единственный дом)                     │
│  □ НЕ elderly owner (если известно)                                        │
│  □ Property abandoned/blighted = хорошо (улучшаем район)                   │
│                                                                             │
│  ДИВЕРСИФИКАЦИЯ                                                             │
│  ══════════════                                                             │
│  □ Это НЕ единственная покупка (eggs in multiple baskets)                  │
│  □ Другой штат чем предыдущие покупки                                      │
│  □ Другой тип (если есть liens, добавить deed или наоборот)                │
│                                                                             │
│  РЕГИСТРАЦИЯ И ПРОЦЕСС                                                      │
│  ══════════════════════                                                     │
│  □ Зарегистрирована на auction platform                                    │
│  □ Deposit внесен (если требуется)                                         │
│  □ Знаю как bidding работает                                               │
│  □ Знаю deadline для оплаты                                                │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FINAL DECISION                                                             │
│  ══════════════                                                             │
│                                                                             │
│  All boxes checked? □ Yes  □ No (if No, STOP and resolve)                  │
│                                                                             │
│  □ APPROVED - Proceed with purchase                                         │
│  □ REJECTED - Do not purchase                                               │
│  □ WAIT - Need more information: _____________________________________     │
│                                                                             │
│  Max bid amount: $__________                                                │
│                                                                             │
│  Молитва/намерение сделана: □ Yes                                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

Дата: ____________    Подпись Miw: ____________    Подпись Denis: ____________
```

---

### Документ 5: CALENDAR (Календарь действий)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      MIW'S TAX LIEN CALENDAR 2026                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  JANUARY 2026                                                               │
│  ════════════                                                               │
│  □ Week 4: Review this document with Denis                                  │
│  □ Jan 30: Register for Arizona auction platforms                           │
│                                                                             │
│  FEBRUARY 2026 ★ ARIZONA AUCTIONS                                           │
│  ═══════════════════════════════════                                        │
│  □ Feb 1-9: Research Arizona liens (use TAXLIEN.online)                    │
│  □ Feb 9: Print Property Analysis Sheets for top 5 candidates              │
│  □ Feb 9: Complete Comparison Matrix                                        │
│  □ Feb 10: ★ AUCTION - Pinal, Yavapai, Cochise counties                    │
│  □ Feb 12: ★ AUCTION - Maricopa county                                      │
│  □ Feb 15: Complete Decision Checklists for winners                         │
│  □ Feb 20: Pay for won liens                                                │
│  □ Feb 26: ★ AUCTION - Pima county (backup)                                │
│                                                                             │
│  MARCH-APRIL 2026                                                           │
│  ════════════════                                                           │
│  □ Register for Louisiana auction (when dates announced)                    │
│  □ Research Utah counties with Rupa/Shon                                    │
│  □ Register for Utah auction                                                │
│                                                                             │
│  MAY 2026 ★ UTAH AUCTION                                                    │
│  ═══════════════════════════                                                │
│  □ May 1-20: Research Utah properties (Rupa/Shon help)                     │
│  □ May 20: Rupa/Shon visit top candidates                                   │
│  □ May 27-28: ★ AUCTION - Utah counties                                     │
│  □ May 30: Pay for won deed                                                 │
│                                                                             │
│  JUNE-NOVEMBER 2026                                                         │
│  ══════════════════                                                         │
│  □ Louisiana auction (date TBD)                                             │
│  □ Monthly: Check Arizona lien status (redemptions?)                        │
│  □ Save additional funds for South Dakota (if Denis joins)                  │
│  □ November: Research Lawrence County, SD listings                          │
│                                                                             │
│  DECEMBER 2026 ★ SOUTH DAKOTA (if budget allows)                            │
│  ═══════════════════════════════════════════════                            │
│  □ Dec 1-15: Research Lawrence County properties                            │
│  □ Dec 18: Denis family visits candidates                                   │
│  □ Dec 21: ★ AUCTION - Lawrence County tax deed                             │
│  □ Dec 25: 🎄 Celebrate (hopefully with new property!)                      │
│                                                                             │
│  2027 AND BEYOND                                                            │
│  ════════════════                                                           │
│  □ Q1 2027: Any AZ liens redeemed? Collect interest                        │
│  □ Q2-Q4 2027: SD renovation with Denis family (if purchased)              │
│  □ 2028: First flip? Staircase to Beverly Hills begins...                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

EMERGENCY CONTACTS:
- Arizona auction help: _______________
- Louisiana auction help: _______________
- Rupa/Shon (Utah): _______________
- Denis: _______________
- Anton: _______________

Print date: ____________
```

---

## Пример заполненного Property Analysis Sheet

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      PROPERTY ANALYSIS SHEET                                │
│                      ═══════ ПРИМЕР ═══════                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ОСНОВНАЯ ИНФОРМАЦИЯ                                                        │
│  ════════════════════                                                       │
│                                                                             │
│  Parcel ID: 123-45-678A               State: AZ   County: Pinal            │
│                                                                             │
│  Property Address: 1234 Desert View Rd, Casa Grande, AZ 85122              │
│                                                                             │
│  Property Type:  ☑ Vacant Land   □ House   □ Mobile Home   □ Commercial    │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  📸 ФОТОГРАФИИ                                                              │
│  ════════════                                                               │
│                                                                             │
│  ┌─────────────────────────────┐  ┌─────────────────────────────┐          │
│  │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │  │  ░░░░░░░░░░░░░░░░░░░░░░░░░  │          │
│  │  ▓▓    DESERT LOT      ▓▓  │  │  ░░░  SATELLITE VIEW  ░░░  │          │
│  │  ▓▓   [Vacant Land]    ▓▓  │  │  ░░░   [Bird's Eye]   ░░░  │          │
│  │  ▓▓    Flat, Clear     ▓▓  │  │  ░░░   Roads Visible  ░░░  │          │
│  │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │  │  ░░░░░░░░░░░░░░░░░░░░░░░░░  │          │
│  │  STREET VIEW: Jan 2024     │  │  SATELLITE: Dec 2023        │          │
│  └─────────────────────────────┘  └─────────────────────────────┘          │
│                                                                             │
│  ┌─────────────────────────────┐  ┌─────────────────────────────┐          │
│  │  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  │  │  ┌───┐                       │          │
│  │  ▒▒  HISTORICAL VIEW   ▒▒  │  │  │N/A│  No assessor photo   │          │
│  │  ▒▒   [Same as 2019]   ▒▒  │  │  └───┘  available           │          │
│  │  ▒▒   Always vacant    ▒▒  │  │                             │          │
│  │  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  │  │                             │          │
│  │  OLDEST AVAILABLE: 2019    │  │  ASSESSOR PHOTO: N/A        │          │
│  └─────────────────────────────┘  └─────────────────────────────┘          │
│                                                                             │
│  Photo URLs: maps.google.com/?q=1234+Desert+View+Rd+Casa+Grande+AZ         │
│                                                                             │
│  Photo Notes: Земля всегда была пустой (2019-2024). Нет строений.          │
│               Хорошо видна грунтовая дорога. Соседи: пустые участки.        │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ФИНАНСОВЫЕ ДАННЫЕ                                                          │
│  ═════════════════                                                          │
│                                                                             │
│  Tax Lien Amount:        $187                                               │
│  Market Value:           $12,500                                            │
│  Value-to-Lien Ratio:    66.8x  (хорошо если > 10x) ✓                      │
│                                                                             │
│  Interest Rate:          16%                                                │
│  Prior Years Owed:       3 лет  ← SWEET SPOT!                              │
│  Redemption Period:      36 месяцев                                         │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ML PREDICTIONS (из системы TAXLIEN.online)                                 │
│  ═══════════════════════════════════════════                                │
│                                                                             │
│  Redemption Probability:    [28]%     □ High (>70%)  □ Med  ☑ Low (<30%)   │
│  Serial Payer Score:        [0.15]    □ Sweet Spot (>0.8)                  │
│  Expected ROI:              [340]%    ← If foreclosure!                    │
│  Risk Score:                [35]/100                                        │
│                                                                             │
│  ⭐ KARMA SCORE:            [+0.6]    ☑ Positive (>0.3)  □ Negative        │
│                                                                             │
│  Karma Factors:                                                             │
│  □ Blighted/Abandoned (+0.3)     □ Homestead Exemption (-0.5)              │
│  ☑ Dissolved LLC (+0.2)          □ Elderly Owner (-0.3)                    │
│  ☑ 5+ Years Delinquent (+0.2)    □ Recent Hardship (-0.2)                  │
│  ☑ No Mortgage (+0.1)            □ Active Mortgage (-0.2)                  │
│                                                                             │
│  Owner: "Desert Holdings LLC" - DISSOLVED 2021                              │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  DUE DILIGENCE CHECKLIST                                                    │
│  ═══════════════════════                                                    │
│                                                                             │
│  ☑ Google Maps/Satellite viewed        ☑ Road access confirmed             │
│  ☑ No environmental hazards            ☑ Zoning allows building            │
│  ☑ No IRS/HOA liens                    ☑ Title clear                       │
│  □ Denis/family can visit              ☑ Auction rules understood          │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  РЕШЕНИЕ                                                                    │
│  ═══════                                                                    │
│                                                                             │
│  ☑ BUY - Покупать       Max Bid: $200                                      │
│  □ WATCH - Наблюдать    Reason: ________________________________           │
│  □ SKIP - Пропустить    Reason: ________________________________           │
│                                                                             │
│  Notes: High foreclosure potential! Dissolved LLC owner, 3 years           │
│  delinquent. Good karma - vacant land, no one harmed. If foreclosure       │
│  happens, land worth $12,500 for only $187 investment!                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

Дата анализа: Jan 28, 2026    Подпись: Miw ✓
```

---

## Конкретные следующие шаги

### Немедленно (эта неделя):

1. **Уточнить у Denis:** В каком именно county Arizona живет его семья?
2. **Поиск земли:** Открыть Land.com, фильтр Arizona $500-$1,000
3. **Связаться с Rupa/Shon:** Готовы ли помочь с Utah в мае?

### До Feb 10, 2026 (Maricopa Tax Lien Sale):

4. **Если решим участвовать:** Зарегистрироваться на treasurer.maricopa.gov
5. **Исследовать liens:** В county где живет семья Denis

### До покупки земли:

6. **Due diligence checklist:**
   - [ ] Road access verified
   - [ ] No liens on property
   - [ ] Clear title
   - [ ] Denis/family physically visited
   - [ ] Zoning allows future building

---

---

## Интеграция с системой TAXLIEN.online

**См. детальный план:** `04-integration-with-system.md`

### Ключевой инсайт

Properties с `prior_years_owed >= 2` = ускоренный путь к foreclosure (не ждать 3 года с нуля)

### Зависимости от других SDD flows:

| Flow | Статус | Нужно для Miw |
|------|--------|---------------|
| sdd-taxlien-parser | IMPL v5.3 | **UPDATE:** Добавить Arizona scrapers |
| sdd-taxlien-ml | COMPLETE | Готов (SerialPayerDetector) |
| sdd-auction-scraper | COMPLETE | Готов (15 AZ counties) |
| sdd-taxlien-gateway | IMPL v1.2 | **UPDATE:** Endpoint для chronic delinquent |

### Arizona Auction Dates (из системы):

| County | Date | Семья Denis? |
|--------|------|--------------|
| Pinal | Feb 10 | Возможно (rural) |
| Yavapai | Feb 10 | Возможно (rural) |
| Cochise | Feb 10 | Возможно (rural) |
| Maricopa | Feb 12 | Нет (Phoenix) |
| Pima | Feb 26 | Нет (Tucson) |

---

## Источники

### California / Los Angeles
- [LA County Tax Auctions](https://ttc.lacounty.gov/schedule-of-upcoming-auctions/)
- [GovEase LA County](https://www.govease.com/los-angeles)

### Louisiana (NEW 2026 System)
- [Louisiana Online Tax Sale](https://laonlinetaxsale.com/)
- [New Orleans Tax Sales](https://nola.gov/tax-sales/)
- [Jefferson Parish Tax Sale](https://www.jpso.com/442/Register-for-Annual-Tax-Sale)
- [Louisiana 2026 Changes](https://www.taxsaleresources.com/blog/2025-louisiana-tax-sale-update)
- [LienSpot Louisiana](https://www.lienspot.com/blog/louisiana-becomes-a-tax-lien-state-in-2026)

### Wisconsin
- [Milwaukee County Foreclosures](https://county.milwaukee.gov/EN/Treasurer/Foreclosed-Property-Sales)
- [Dane County Tax Deed Auction](https://treasurer.danecounty.gov/taxdeedauction)

### Utah
- [Salt Lake County Tax Sale](https://www.saltlakecounty.gov/property-tax/property-tax-sale/)
- [Utah County Tax Sale](https://auditor.utahcounty.gov/may-tax-sale)

### Arizona
- [Maricopa County Tax Liens](https://treasurer.maricopa.gov/Pages/LoadPage?page=TaxLienTutorial)
- [Pima County Tax Liens](https://www.to.pima.gov/taxLienSale/)
- [Arizona Land $500-$1000](https://www.land.com/Arizona/all-land/500-1000/)
- [LandFlip Arizona](https://www.landflip.com/land-for-sale/arizona/1-minprice/5000-maxprice)
- [LandSearch AZ under $5000](https://www.landsearch.com/properties/arizona/search/under-5000)
