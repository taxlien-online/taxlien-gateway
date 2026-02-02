# Plan: Координация SDD Flows для Miw

**Version:** 6.0
**Status:** DRAFT
**Last Updated:** 2026-01-27

---

## Цель плана

Этот план описывает **КАК МОДИФИЦИРОВАТЬ ОСТАЛЬНЫЕ SDD FLOWS** чтобы:
1. Разработать функционал для Miw в кратчайшие сроки
2. Подготовить сырые данные и тестовые артефакты ДО запуска платформы
3. Дать Miw конкурентное преимущество первого пользователя

> **НЕ ВКЛЮЧЕНО:** Личные action items для Miw/Shon/Denis.
> Они разберутся сами. Здесь только технические задачи.

---

## Приоритизация SDD Flows

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  TIER 1: КРИТИЧЕСКИЙ ПУТЬ (нужно для первой покупки Feb 2026)              │
├─────────────────────────────────────────────────────────────────────────────┤
│  sdd-taxlien-parser         → Данные Arizona/South Dakota                  │
│  sdd-taxlien-gateway        → API для доступа к данным                     │
│  sdd-taxlien-ml             → Foreclosure Score, Serial Payer detection    │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  TIER 2: УСКОРИТЕЛИ (делают поиск быстрее и точнее)                        │
├─────────────────────────────────────────────────────────────────────────────┤
│  sdd-taxlien-swipe-app      → FVI/ИПП, Expert Annotations                  │
│  sdd-taxlien-enrichment     → Property photos, owner data                  │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  TIER 3: УДОБСТВА (можно после первой покупки)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  sdd-taxlien-ssr-site       → Web UI + печать документов                   │
│  sdd-taxlien-flutter-app    → Mobile UI (основное приложение)              │
│  sdd-taxlien-content        → Guides, статьи                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## TIER 1: Критический путь

### 1.1 sdd-taxlien-parser

**Цель:** Собрать данные по Arizona и South Dakota ДО Feb 2026.

| Модификация | Приоритет | Описание |
|-------------|-----------|----------|
| Arizona counties FIRST | P0 | Pinal, Yavapai, Cochise, Maricopa - auction Feb 10-26 |
| OTC liens endpoint | P0 | Парсить Over-The-Counter списки (не только аукционы) |
| Prior years liens | P0 | Liens 2+ лет - высокий foreclosure potential |
| South Dakota Lawrence County | P1 | Для Dec 2026 auction |
| Owner history | P1 | Payment history для Serial Payer detection |

**Сырые данные для Miw:**
```
/data/raw/
├── arizona/
│   ├── pinal_otc_liens.csv          # OTC available NOW
│   ├── pinal_auction_feb2026.csv    # Upcoming auction
│   ├── pinal_prior_years.csv        # Liens 2+ years old
│   └── ...
└── south_dakota/
    └── lawrence_upcoming.csv         # For Dec 2026
```

**Тестовые артефакты:**
- [ ] CSV export для offline анализа
- [ ] JSON dump для тестирования ML
- [ ] Sample parcels с полными данными (10-20 штук)

---

### 1.2 sdd-taxlien-gateway

**Цель:** API endpoints для быстрого доступа к данным.

| Модификация | Приоритет | Описание |
|-------------|-----------|----------|
| `/api/v1/liens/otc` | P0 | Список OTC liens по штату/county |
| `/api/v1/liens/foreclosure-candidates` | P0 | Liens с high foreclosure probability |
| `/api/v1/liens/search` | P1 | Поиск по критериям Miw |
| `/api/v1/export/csv` | P1 | Export для offline |

**Endpoint для Miw:**
```
GET /api/v1/liens/foreclosure-candidates?
    state=AZ&
    max_amount=500&
    prior_years_min=2&
    redemption_prob_max=0.3
```

**Тестовые артефакты:**
- [ ] Postman collection с примерами запросов
- [ ] Mock responses для offline тестирования
- [ ] Rate limiting bypass для internal users

---

### 1.3 sdd-taxlien-ml

**Цель:** ML модели для идентификации лучших opportunities.

| Модификация | Приоритет | Описание |
|-------------|-----------|----------|
| Foreclosure Score | P0 | Вероятность что lien НЕ будет redeemed |
| Serial Payer Detection | P0 | Chronic non-payers (но не bankrupt) |
| Owner Portfolio Analysis | P1 | Cross-county owner search |
| Karma Score | P2 | Ethical filtering (blighted properties) |

**ML Pipeline для Miw:**
```python
# Priority scoring для Miw's criteria
def score_for_miw(lien):
    return (
        foreclosure_probability * 0.4 +      # Хотим foreclosure
        (1 - redemption_probability) * 0.3 + # Не хотим redemption
        value_to_lien_ratio * 0.2 +          # Хороший value
        karma_score * 0.1                    # Этичная покупка
    )
```

**Тестовые артефакты:**
- [ ] Pre-trained model на исторических данных
- [ ] Batch predictions для Arizona liens
- [ ] CSV с scored liens для offline review

---

## TIER 2: Ускорители

### 2.1 sdd-taxlien-swipe-app

**Цель:** Быстрый просмотр и разметка properties.

| Модификация | Приоритет | Описание |
|-------------|-----------|----------|
| FVI/ИПП display | P1 | Показывать Family Value Index |
| Expert annotations | P1 | Khun Pho, Denis могут размечать |
| Foreclosure filter | P1 | Показывать только high foreclosure candidates |
| Offline mode | P2 | Работать без интернета |

**Интеграция с ML:**
```
Swipe App → Gateway → ML predictions →
→ Filter: foreclosure_prob > 0.7 →
→ Sort by: miw_score DESC →
→ Show to Miw
```

---

### 2.2 sdd-taxlien-enrichment

**Цель:** Дополнительные данные для принятия решений.

| Модификация | Приоритет | Описание |
|-------------|-----------|----------|
| Google Street View | P1 | Historical photos (condition change) |
| Owner obituary search | P2 | No heirs = guaranteed foreclosure |
| Property photos | P1 | Assessor photos |
| Satellite view | P2 | Lot condition |

**Сырые данные:**
```
/data/enriched/
├── photos/
│   ├── {parcel_id}_streetview_2024.jpg
│   ├── {parcel_id}_streetview_2020.jpg
│   └── {parcel_id}_satellite.jpg
└── owners/
    └── {owner_name}_portfolio.json
```

---

## TIER 3: Удобства (после первой покупки)

### 3.1 sdd-taxlien-ssr-site

| Модификация | Приоритет | Описание |
|-------------|-----------|----------|
| Property cards print | P2 | PDF для offline |
| Comparison matrix | P2 | Сравнение нескольких properties |
| Portfolio tracker | P3 | Tracking purchased liens |

### 3.2 sdd-taxlien-flutter-app

| Модификация | Приоритет | Описание |
|-------------|-----------|----------|
| Notifications | P3 | Alerts при изменении статуса |
| Auction calendar | P2 | Reminder для Feb auctions |

### 3.3 sdd-taxlien-content

| Модификация | Приоритет | Описание |
|-------------|-----------|----------|
| OTC Guide | P2 | Как покупать OTC liens |
| Arizona process | P2 | Специфика Arizona |

---

## Сырые данные для Miw (до запуска платформы)

### Что подготовить:

```
/data/miw-preview/
│
├── arizona_otc_foreclosures.csv
│   # Columns: parcel_id, county, address, lien_amount, market_value,
│   #          prior_years, foreclosure_score, miw_score, karma_score
│
├── arizona_top_20.csv
│   # Top 20 по miw_score (уже отфильтрованы)
│
├── south_dakota_lawrence_upcoming.csv
│   # Для Dec 2026 auction
│
├── photos/
│   └── {parcel_id}/*.jpg
│
└── property_cards/
    └── {parcel_id}.pdf
```

### Критерии отбора для Miw:

```sql
SELECT *
FROM liens
WHERE
    state = 'AZ'
    AND lien_amount <= 500
    AND prior_years >= 2
    AND foreclosure_probability >= 0.6
    AND karma_score >= 0
    AND (
        property_type = 'LOT'
        OR (property_type = 'RESIDENTIAL' AND market_value >= 20000)
    )
ORDER BY miw_score DESC
LIMIT 20
```

---

## Timeline разработки

### Week 1-2 (Jan 27 - Feb 9)

| SDD | Task | Deliverable |
|-----|------|-------------|
| sdd-taxlien-parser | Arizona counties scrape | `arizona_*.csv` files |
| sdd-taxlien-parser | OTC liens extraction | `*_otc_liens.csv` |
| sdd-taxlien-ml | Foreclosure Score training | Trained model |

**Deliverable для Miw:** CSV с 50+ Arizona OTC foreclosures, scored

### Week 3-4 (Feb 10-23)

| SDD | Task | Deliverable |
|-----|------|-------------|
| sdd-taxlien-gateway | API endpoints | Working API |
| sdd-taxlien-ml | Batch predictions | All Arizona liens scored |
| sdd-taxlien-enrichment | Photos for top 20 | Street View images |

**Deliverable для Miw:** Top 20 properties с фото и scores

### Week 5-8 (Feb 24 - Mar 23)

| SDD | Task | Deliverable |
|-----|------|-------------|
| sdd-taxlien-swipe-app | Basic swipe UI | Working app |
| sdd-taxlien-swipe-app | FVI/ИПП display | Scores visible |
| sdd-taxlien-ssr-site | Property cards | PDF export |

**Deliverable для Miw:** Swipe app для быстрого просмотра

### Week 9+ (Mar 24+)

| SDD | Task | Deliverable |
|-----|------|-------------|
| sdd-taxlien-swipe-app | Expert annotations | Family can annotate |
| sdd-taxlien-ml | Owner Portfolio Analysis | Cross-county search |
| All | Integration | Full platform |

---

## Тестовые артефакты

### Для каждого SDD подготовить:

| Артефакт | Цель |
|----------|------|
| Sample data (10-20 parcels) | Тестирование без полного scrape |
| Mock API responses | Offline development |
| Exported CSV | Manual review |
| Screenshot/PDF | Documentation |

### Для Miw специально:

| Артефакт | Когда готово |
|----------|--------------|
| `arizona_otc_top20.csv` | Week 2 |
| `arizona_otc_top20_photos/` | Week 3 |
| `arizona_property_cards.pdf` | Week 4 |
| Working swipe app | Week 5 |

---

## Dependencies между SDD

```
sdd-taxlien-parser
    │
    ├──► sdd-taxlien-gateway ──► sdd-taxlien-swipe-app
    │         │
    │         └──► sdd-taxlien-ssr-site
    │
    └──► sdd-taxlien-ml
              │
              ├──► sdd-taxlien-gateway (predictions endpoint)
              │
              └──► sdd-taxlien-swipe-app (scores display)

sdd-taxlien-enrichment
    │
    └──► sdd-taxlien-swipe-app (photos)
    └──► sdd-taxlien-ssr-site (property cards)
```

---

## Модификации в других SDD

### sdd-taxlien-parser/01-requirements.md

**Добавить:**
- [ ] Arizona counties priority (Feb 2026 auction)
- [ ] OTC liens scraping (not just auction)
- [ ] Prior years liens (foreclosure candidates)
- [ ] Export to CSV for offline analysis

### sdd-taxlien-gateway/01-requirements.md

**Добавить:**
- [ ] `/api/v1/liens/foreclosure-candidates` endpoint
- [ ] `/api/v1/liens/otc` endpoint
- [ ] CSV export endpoint
- [ ] Internal user bypass for rate limiting

### sdd-taxlien-ml/01-requirements.md

**Добавить:**
- [x] Ethical principle (ЦЕННОСТЬ ≠ ЦЕНА) - DONE
- [ ] `miw_score` composite metric
- [ ] Batch prediction job
- [ ] CSV export with predictions

### sdd-taxlien-swipe-app/01-requirements.md

**Добавить:**
- [x] FVI/ИПП display - DONE (in requirements)
- [ ] Foreclosure filter mode
- [ ] Offline cached properties
- [ ] Export to PDF

### sdd-taxlien-enrichment/01-requirements.md

**Добавить:**
- [ ] Street View historical photos
- [ ] Batch photo download
- [ ] Owner portfolio aggregation

---

## Success Criteria

| Metric | Target | Deadline |
|--------|--------|----------|
| Arizona liens scraped | 10,000+ | Feb 5 |
| Foreclosure candidates identified | 100+ | Feb 7 |
| Top 20 for Miw with scores | Ready | Feb 9 |
| Photos for top 20 | Ready | Feb 12 |
| Working swipe app | MVP | Feb 28 |

---

## Approval

```
☐ Plan v6.0 approved
```

**Changes from v5.0:**
- Removed all personal action items for Miw/Shon/Denis
- Focus purely on SDD modifications
- Added raw data preparation
- Added test artifacts
- Added specific deliverables timeline
