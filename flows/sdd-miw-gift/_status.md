# Status: sdd-miw-gift

## ⚠️ Как работает этот SDD

**sdd-miw-gift = КОМПАС для других SDD (НЕ код!)**

Работает через выстраивание пути **В ОСТАЛЬНЫХ SDD**, ориентируясь на sdd-miw-gift:

**PRIMARY (критический путь):**
- sdd-taxlien-parser → Arizona counties first (Feb 2026 auction)
- sdd-taxlien-gateway → foreclosure endpoint priority
- sdd-taxlien-ml → Foreclosure Score, x1000 Antique Score models

**SECONDARY (задел на будущее):**
- sdd-taxlien-ssr-site → web UI + печать
- sdd-taxlien-flutter-app → mobile UI
- *Пригодится после первичной закупки: расширенный поиск, другие штаты*

**TERTIARY (обобщение и sharing):**
- sdd-taxlien-content → статьи, guides
- *Обобщить знания, поделиться путём, помочь другим людям*

## Current Phase

~~REQUIREMENTS~~ ✅ | ~~SPECIFICATIONS~~ ✅ | ~~PLAN~~ ✅ | **IMPLEMENTATION**

## Phase Status

- Requirements v4.0: **APPROVED** (2026-01-27)
- Specifications: **APPROVED** (2026-01-27)
- Plan v5.0: SUPERSEDED by v6.0
- Plan v6.0: **APPROVED** (2026-01-27)

## Last Updated

2026-01-27

## ✅ ЗАВЕРШЕНО: sdd-taxlien-swipe-app создан

**Документы созданы:**
- [x] `sdd-taxlien-swipe-app/01-requirements.md` - FVI/ИПП, Expert Annotations
- [x] `sdd-taxlien-swipe-app/02-specifications.md` - Architecture, Data Models, API
- [x] `sdd-taxlien-swipe-app/03-plan.md` - 5-phase transfer plan
- [x] `sdd-taxlien-swipe-app/_status.md` - Status tracking

**Также обновлено:**
- [x] `sdd-taxlien-ml/01-requirements.md` - Added ethical principle "ЦЕННОСТЬ ≠ ЦЕНА"

## Beneficiary

**Miw Dodonova** (18 years old)
- Partner: Denis (31, US Citizen, **Spearfish, South Dakota** family, renovation skills)
- Preference: Beverly Hills, но реалистично - **South Dakota** (семья рядом)
- Primary Goal: **Купить недвижимость** (не заработок на процентах)
- **Дедушка Miw:** Thai citizenship (координирует ремонт удалённо)

---

## Summary: Что изменилось в v3.0

| Аспект | v1.0 | v2.0 | v3.0 (текущий) |
|--------|------|------|----------------|
| Цель | Заработок на % | Покупка property | **Tax Deed + ремонт** |
| Фокус | Tax liens | Arizona | **South Dakota** |
| Timeline | 3-5 лет | Немедленно | **Feb 2026 + Dec 2026** |
| Family | Не учтено | Arizona (ошибка) | **Spearfish, SD** |
| Strategy | Single | Single | **Dual: AZ liens + SD deed** |

---

## Рекомендованная стратегия (v4.0) - UPDATED

### ДВА ИНВЕСТОРА с разными целями

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  INVESTOR 1: MIW                      │  INVESTOR 2: SHON                   │
│  ══════════════════                   │  ═══════════════                    │
│  Goal: FORECLOSURE → PROPERTY         │  Goal: GUARANTEED INTEREST          │
│  Risk: Aggressive                     │  Risk: Conservative                 │
│  Budget: $1,000 total                 │  Budget: $200-$2,000 × 3 liens      │
│                                       │                                     │
│  $150 = 1 lien (опыт)            │  Needs: LIST of 10-15 options       │
│  $850 = foreclosures (max ROI)        │  Will choose: 3 liens himself       │
│                                       │  Prefer: OTC (no auction hassle)    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### MIW: Фокус на FORECLOSURES ($1,000)

```
$1,000 бюджет Miw
    │
    ├── $150: 1 Tax Lien (ОБУЧЕНИЕ)
    │   └── Просто для опыта, не цель
    │
    └── $850: FORECLOSURES (ГЛАВНАЯ ЦЕЛЬ)
        └── Tax Deed auctions
        └── OTC foreclosed properties
        └── Максимум 1-3 cheap properties
        └── Цель: быстрая перепродажа с множителем
```

### SHON: Консервативный портфель (3 liens)

```
Shon Budget: $200-$2,000 per lien × 3 = $600-$6,000 total
    │
    ├── Нужен СПИСОК из 10-15 вариантов
    │   └── Shon САМ выбирает 3
    │
    ├── Критерии для Shon:
    │   └── HIGH redemption probability (>80%)
    │   └── Guaranteed interest (16% AZ, 18% FL, etc.)
    │   └── Safe properties (homestead, good payment history)
    │
    └── Prefer: OTC (Over The Counter)
        └── No auction competition
        └── Fixed price
        └── Less hassle
```

### Приоритет 1: South Dakota (Dec 2026) - MIW ⭐

**Бюджет:** $850 от Miw + вклад Denis
**Результат:** Дом + бесплатный ремонт семьёй Denis
**Timeline:** Dec 21, 2026
**Класс property:** C (systems update) - идеально для DIY

### Приоритет 2: Arizona/Utah Foreclosures - MIW

**Бюджет:** $850 (после $150 на опыт)
**Результат:** 1-3 cheap foreclosed properties
**Timeline:** Feb-May 2026
**Цель:** Quick flip с максимальным множителем

---

## Анализ по штатам

| Штат | Тип | Timeline | OTC | Auction | Min $ | Family | Verdict |
|------|-----|----------|-----|---------|-------|--------|---------|
| **Arizona** | Tax Lien | Feb 2026 | ✅ | ✅ | $100 | ❌ | **С $1,000** |
| **Utah** | Tax Deed | May 2026 | ❌ | ✅ | $500 | ⚠️ Rupa/Shon | **С $1,000** |
| South Dakota | Tax Deed | Dec 2026 | ❌ | ✅ | $2,000 | ✅ Denis | **Denis нужен** |
| Wisconsin | Tax Deed | Varies | ❌ | ✅ | $3,000 | ❌ | За бюджетом |
| California | Tax Deed | Oct 2026 | ❌ | ✅ | $5,000 | ❌ | За бюджетом |

---

## Ключевые ресурсы семьи

| Ресурс | Локация | Роль |
|--------|---------|------|
| **Denis** | Spearfish, SD | СТАРШИЙ из 12 siblings, хочет помочь им найти дома |
| **11 siblings Denis** | Spearfish, SD | БЕНЕФИЦИАРЫ (не рабочая сила!) - ищем им дома |
| **Khun Pho** | Thailand (remote) | Консультация по строительству |
| Rupa | Utah | Backup для UT auction |
| **Shon** | Utah | **Отдельный инвестор** (консервативный) |

---

## Два инвестора

| | **Miw** | **Shon** |
|---|---|---|
| **Цель** | FORECLOSURE → Property | Гарантированный % |
| **Риск** | Агрессивный | Консервативный |
| **Бюджет** | $1,000 total | $200-$2,000 × 3 liens |
| **Тип** | Tax DEEDS | Tax LIENS |
| **Обучение** | 1 lien за $150 | — |
| **Основной фокус** | $850 на foreclosures | Список 10-15 вариантов |
| **Выбор** | Система рекомендует | Сам выбирает 3 из списка |
| **OTC** | Да (дешевле) | Да (проще) |

---

## Blockers

- [x] ~~Уточнить county семьи Denis~~ → **Lawrence County, SD (Spearfish)**
- **$1,000 = максимум** от российско-тайской стороны (больше накопить не смогут)
- SD Tax Deed ($2,000-$5,000) требует вклада от американской стороны (Denis)

---

## Progress

- [x] Requirements drafted (v1.0)
- [x] Requirements updated (v2.0 - property focus)
- [x] Requirements updated (v3.0 - компас для других SDD)
- [x] **Requirements APPROVED (2026-01-27)**
- [x] Specifications drafted (v2.0 - full analysis)
- [x] Coordination plan created (04-integration-with-system.md)
- [x] Plan updated (v3.0 - dual strategy AZ + SD)
- [x] Family location corrected: **Spearfish, South Dakota**
- [x] **sdd-taxlien-parser updated** with Arizona/Utah priority (Jan 25)
- [x] **Vision: Path to Beverly Hills** added to specifications (Staircase Strategy)
- [x] **Louisiana added** ("LA" может быть Louisiana, не Los Angeles)
- [x] **4 варианта Miw** уточнены: LA (California), Louisiana, Wisconsin, Beverly Hills
- [x] **Sweet Spots section** - ускорение через систему (14 лет → 9-10 лет)
- [x] **⭐ Karma section** - кармически хорошие варианты (blighted → beautiful home)
- [x] **Karma Score concept** - алгоритм для фильтрации по карме
- [x] **Karma Score added to sdd-taxlien-ml** (Phase 4, Model 21)
- [x] **User insights saved** - оригинальные цитаты сохранены в спецификации
- [x] **Diversification strategy** - не класть все яйца в одну корзину
- [x] **5 печатных документов** для Miw:
  - Portfolio Summary
  - Property Analysis Sheet (+ пример)
  - Comparison Matrix
  - Decision Checklist
  - Calendar 2026
- [x] **Lifestyle Match** - окружение под цели инвестора (Model 22 в ML)
- [x] **Lifestyle Questionnaire** - анкета предпочтений для Miw
- [x] **Proximity Scores** - расстояние до школ, больниц и др. (Model 23)
- [x] **Photo Analysis** - Google Street View historical, satellite (Model 24)
- [x] **Owner Communication** - шаблон письма, skip tracing
- [x] **Risk Factors** - flood, fire, environmental, utilities (Model 25)
- [x] **Complete Factors Checklist** - все факторы в одном чеклисте
- [x] **Photo Guide for Miw** - пошаговая инструкция по захвату и печати фото
- [x] **Photo section in Example** - добавлены фото в пример Property Analysis Sheet
- [x] **Liquidity Score** - прогноз ликвидности и привлекательности для перепродажи (Model 26)
- [x] **Map Analysis** - FEMA flood zones, zoning, terrain, utilities (Model 27)
- [x] **Map Analysis Checklist** - чеклист для Miw по картам
- [x] **Flip Potential Score** - ROI калькулятор для fix-and-flip
- [x] **Deep Learning section** - CNN для фото, OCR, NLP, рекомендации
- [x] **Phase 5 added to ML** - Models 28-32 (DL models)
- [x] **Owner Portfolio Analysis** - полный пакет документов на владельца
- [x] **Document Package Structure** - 4 уровня документов (basic → deep dive)
- [x] **Large Portfolio Rules** - стратегия для владельцев с 10+ properties
- [x] **Model 33: OwnerPortfolioAnalyzer** - cross-county owner search
- [x] **Dual Strategy: Live-in vs Flip** - разные критерии для SD и AZ/UT
- [x] **Property Classification A-F** - по типу ремонта (cosmetic → structural)
- [x] **Structural vs Cosmetic Checklist** - детальный чеклист
- [x] **Renovation Assessment Sheet** - новый печатный документ
- [x] **Model 34: RenovationScopeEstimator** - оценка объёма ремонта
- [x] **v4.0: Miw vs Shon split** - два разных инвестора
- [x] **Miw: $150 lien (опыт) + $850 foreclosures**
- [x] **Shon: Conservative strategy** - 3 liens, список 10-15 вариантов
- [x] **OTC focus** - для обоих инвесторов (проще, дешевле)
- [x] **Foreclosure scenarios** - A (много дешёвых), B (один хороший), C (баланс)
- [x] **Physical Inspection Advantage** - семья Denis смотрит ДО покупки
- [x] **"Красиво ≠ Хорошо" guide** - ловушки косметического ремонта
- [x] **"Страшно ≠ Плохо" guide** - скрытые возможности
- [x] **Denis Family Inspection Checklist** - 4 уровня проверки
- [x] **Fundamental Soundness Score** - подсчёт red flags
- [x] **Inspection Kit list** - что брать на осмотр ($50-100)
- [x] **Keep vs Flip decision matrix** - когда оставить себе
- [x] **"Опыт" вместо "обучение"** - точная формулировка для $150 lien
- [x] **Remote Foundation Assessment** - 10 методов без физического осмотра:
  - Historical Street View (roofline changes)
  - Satellite drainage patterns
  - USDA Soil Data (expansive clay)
  - Topography (low spots)
  - Permit history (foundation repair)
  - Building age + construction type
  - Price history anomalies
  - Neighborhood pattern analysis
  - Assessor photos over time
- [x] **Remote Foundation Checklist** - печатный документ
- [x] **Model 35 concept: RemoteFoundationAssessor**
- [x] **Workflow: Remote filter → Physical confirm**
- [x] **Hidden Value ("Бабушкин дом")** - антиквариат, наличные, коллекции
- [x] **Legal: Personal Property Transfer** - что переходит к покупателю
- [x] **Hidden Value Indicators** - сигналы скрытой ценности
- [x] **Model 36 concept: HiddenValuePredictor** - Deep Learning на документах
- [x] **Common Hiding Spots** - где прячут ценности
- [x] **First Entry Protocol** - чеклист при входе в купленный дом
- [x] **Bonus Value Score** - добавить в Property Analysis Sheet
- [x] **Denis Furniture Advantage** - реставрация + клиентская база
- [x] **Synergy: Property + Contents + Denis Skills** - комбинированный доход
- [x] **Furniture Pipeline Workflow** - от покупки до продажи
- [x] **ROI пример** - Denis advantage = +20% profit
- [x] **Owner Family Graph** - граф родственных связей для карточки владельца
- [x] **Foreclosure Opportunity Criteria** - чеклист для поиска гарантированных foreclosures (no heirs)
- [x] **NLP Obituary Parser** - извлечение семьи из некрологов
- [x] **Model 37: HeirGraphAnalyzer** - анализ вероятности redemption по графу (Foreclosure Score)
- [x] **Foreclosure Discovery Pipeline** - автоматический поиск opportunities
- [x] **Foreclosure Example** - идеальный случай (Margaret Wilson)
- [x] **World-Class Antique NLP** - извлечение сигналов из некрологов:
  - Profession indicators (art dealer, museum curator)
  - Collector indicators ("avid collector", "world-class collection")
  - Wealth indicators (philanthropist, museum board)
  - Travel indicators (lived in Paris, traveled extensively)
  - Military indicators (WWII Germany/Japan = souvenirs)
  - Heritage indicators (third generation, family home since 1890)
- [x] **Model 38: WorldClassAntiquePredictor**
- [x] **Unicorn Property Score** - Foreclosure + x1000 Antiques + Furniture + Condition
- [x] **ВАЖНО: x1000 = world-class antiques** (не "no heirs" - это Foreclosure Score)
- [x] **ОГРАНИЧЕНИЕ: NO PAID APIs** - только self-hosted и бесплатные источники
- [x] **Real-world discoveries** - Van Gogh $15M, Fabergé $33M examples
- [ ] **Уточнить у Miw:** Что она имела ввиду под "LA"?
- [ ] **Заполнить Lifestyle Questionnaire** с Miw
- [x] **Specifications APPROVED (2026-01-27)**
- [x] **Plan v6.0 APPROVED (2026-01-27)**
- [x] **SDD Flows Updated (2026-01-28):**
  - [x] sdd-taxlien-parser: Arizona priority, OTC liens, prior years, payment history
  - [x] sdd-taxlien-gateway: Foreclosure candidates, OTC, search endpoints
  - [x] sdd-taxlien-ml: miw_score composite metric, batch predictions
  - [x] sdd-taxlien-enrichment: Street View photos, owner obituary search
  - [x] sdd-taxlien-swipe-app: Foreclosure filter, offline mode, PDF export
  - [x] sdd-taxlien-ssr-site: Property cards print
  - [x] sdd-taxlien-content: OTC Guide, Arizona process guide
- [ ] **Для Miw:** Найти 5-10 OTC foreclosures < $500
- [ ] **Для Shon:** Сгенерировать список 10-15 conservative liens
- [ ] Parser scrapes Arizona counties (deadline: Feb 9)
- [ ] Miw registered for AZ auction
- [ ] Miw: 1 lien за $150 (опыт)
- [ ] Miw: 2-4 foreclosures за $850
- [ ] Shon: 3 liens выбраны из списка
- [ ] **Dec 21:** South Dakota deed purchased

## Integration Note (Gateway / Supabase)

**Endpoints для Miw (foreclosure-candidates, OTC, search, CSV export):** реализуются через **sdd-taxlien-gateway-supabase** (PostgREST, views, RPC), а не через Go Gateway. Go Gateway (sdd-taxlien-gateway v3.0) — только Worker API :8081. См. 04-integration-with-system.md.

## Next Actions

### Feb 2026:
1. Register for Arizona auction platform
2. Bid on 2-3 Arizona liens ($500-$700)

### Feb-Nov 2026:
3. Accumulate additional savings (+$1,000-$4,000)
4. Research Lawrence County, SD tax deed listings

### Dec 2026:
5. **Denis family visits properties** in Lawrence County
6. **Bid at Lawrence County Tax Deed Auction** (Dec 21)
7. If won → Renovation planning with дедушка Miw

---

## Vision: Denis как старший брат

```
Denis (31, старший из 12) → Находит хорошие дома через Tax Liens →
→ Помогает siblings найти доступное жильё для их будущих семей

Timeline: 2026+
Result: Доступные дома для семьи Denis
```

---

## Новая метрика: FVI / ИПП

**FVI** = Family Value Index (English)
**ИПП** = Индекс Полной Пользы (Russian)

```
FVI = (Financial Value + Personal Value) / Cost

Personal Value = Σ отметок от ВСЕХ экспертов:
  • Khun Pho: строительство
  • Denis: мебель для реставрации
  • Miw: дизайн, эстетика
  • Anton: ретро авто, наука, живопись
  • Vasilisa: антикварные игрушки

Результат: Максимизируем НЕ ТОЛЬКО ROI, но полную семейную ценность
```
