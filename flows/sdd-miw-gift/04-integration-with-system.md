# Coordination: sdd-miw-gift Dependencies

**Version:** 1.1
**Purpose:** Определить какие SDD flows нужно обновить и в каком порядке для достижения целей Miw

---

## Цель

**Найти для Miw property в Arizona за $1,000 используя систему TAXLIEN.online**

Ключевой инсайт: Properties с `prior_years_owed >= 2` = ускоренный путь к foreclosure

---

## Порядок выполнения SDD flows

```
┌─────────────────────────────────────────────────────────────┐
│  1. sdd-taxlien-parser                                      │
│     Добавить в requirements: Arizona county scrapers        │
│     Приоритет: Maricopa, Pinal, Yavapai (rural AZ)         │
└─────────────────────────────┬───────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  2. sdd-taxlien-gateway                                     │
│     Добавить в requirements: endpoint для chronic delinquent│
│     Filter: prior_years_owed, max_amount, state            │
└─────────────────────────────┬───────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  3. sdd-miw-gift                                            │
│     Использовать API для поиска liens в Arizona            │
│     Bid на auction Feb 10-26, 2026                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Изменения в существующих SDD flows

### 1. sdd-taxlien-parser (ПЕРВЫЙ)

**Текущий статус:** IMPLEMENTATION v5.3

**✅ ОБНОВЛЕНО (2026-01-25):** Добавлена секция "Arizona/Utah Priority" в `01-requirements.md`:

| Requirement | Description | Status |
|-------------|-------------|--------|
| Arizona scrapers | Maricopa, Pinal, Yavapai, Cochise | ✅ Added |
| Field: prior_years_owed | Parse количество лет просрочки | ✅ Added |
| Priority: Delinquent liens | Focus на liens идущих на auction Feb 2026 | ✅ Added |
| Utah research | Counties для May 2026 auction | ✅ Added |

**Deadline:** Feb 10, 2026 (Arizona Auction)

**Обоснование:** Без данных в базе невозможно найти liens для Miw

---

### 2. sdd-taxlien-gateway (ВТОРОЙ)

**Текущий статус:** IMPLEMENTATION v1.2

**Нужно добавить в requirements:**

| Requirement | Description |
|-------------|-------------|
| Endpoint: chronic delinquent | Filter by prior_years_owed >= N |
| Filter: max_amount | Budget filter (e.g., $500) |
| Include: ML scores | Return SerialPayerDetector score |

**Обоснование:** API нужен для query данных из базы

---

### 3. sdd-taxlien-ml (УЖЕ ГОТОВ)

**Текущий статус:** COMPLETE

**Что уже есть:**
- SerialPayerDetector - идентифицирует хронических неплательщиков
- RiskScorer - оценка риска
- RedemptionPredictor - вероятность redemption

**Для Miw:** Низкий `redemption_probability` = выше шанс foreclosure

---

### 4. sdd-auction-scraper (УЖЕ ГОТОВ)

**Текущий статус:** IMPLEMENTATION COMPLETE

**Что уже есть:**
- `data/historical/2026_az_data.json` - 15 Arizona counties
- Даты аукционов Feb 2026

**Для Miw:** Использовать даты для планирования bid

---

## Timeline

| Date | Action | SDD Flow |
|------|--------|----------|
| Jan 25-31 | Update parser requirements for Arizona | sdd-taxlien-parser |
| Feb 1-7 | Parser scrapes Arizona counties | sdd-taxlien-parser |
| Feb 5-9 | Update gateway with chronic delinquent endpoint | sdd-taxlien-gateway |
| Feb 9 | Query database for candidates | sdd-miw-gift |
| Feb 10 | Pinal, Yavapai, Cochise auctions | sdd-miw-gift |
| Feb 12 | Maricopa auction | sdd-miw-gift |
| Feb 26 | Pima auction | sdd-miw-gift |

---

## Blockers

1. **Уточнить county семьи Denis** - влияет на приоритет scraping
2. **Parser Arizona scrapers** - нет данных = нет поиска

---

## Parallel Path (не зависит от системы)

Пока ждём parser:
- Прямая покупка земли на Land.com ($500-$800)
- Немедленный результат, не требует системы
