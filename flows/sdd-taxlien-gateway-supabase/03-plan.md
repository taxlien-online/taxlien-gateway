# Implementation Plan: Supabase Backend

> Version: 1.0  
> Status: DRAFT  
> Last Updated: 2026-02-04  
> Specifications: [02-specifications.md](02-specifications.md)

## Summary

Внедрение Supabase как единого backend: схема БД, RLS, Storage и Edge Functions. Порядок деплоя — основа (таблицы, индексы) → RLS → представления и функции → Storage → Edge Functions. Артефакты — SQL-миграции в `supabase/migrations/` и Edge Functions в `supabase/functions/`. Репозиторий taxlien-gateway может хранить миграции для согласованной схемы с Worker API.

## Task Breakdown

### Phase 1: Schema Foundation

#### Task 1.1: Base tables (parcels, auctions, liens)
- **Description**: Миграция с CREATE TABLE для parcels, auctions, liens в правильном порядке (parcels → auctions → liens из-за FK). Индексы по state, county, parcel_id, status, auction_id.
- **Files**:
  - `supabase/migrations/YYYYMMDDHHMMSS_01_base_tables.sql` — Create
- **Dependencies**: None
- **Verification**: Применить миграцию в Supabase; PostgREST показывает `/rest/v1/parcels`, `/rest/v1/auctions`, `/rest/v1/liens`.
- **Complexity**: Medium

#### Task 1.2: User and app tables (user_profiles, favorites, swipes, annotations)
- **Description**: Таблицы, зависящие от auth.users и parcels: user_profiles, favorites, swipes, annotations. Индексы по user_id, parcel_id.
- **Files**:
  - `supabase/migrations/YYYYMMDDHHMMSS_02_user_tables.sql` — Create
- **Dependencies**: Task 1.1
- **Verification**: Таблицы созданы; FK на auth.users и parcels работают.
- **Complexity**: Low

### Phase 2: RLS

#### Task 2.1: RLS on public data (parcels, liens, auctions)
- **Description**: ALTER TABLE ... ENABLE ROW LEVEL SECURITY; политики SELECT для parcels (all), liens/auctions (authenticated/anon по спекам).
- **Files**:
  - `supabase/migrations/YYYYMMDDHHMMSS_03_rls_public.sql` — Create
- **Dependencies**: Task 1.1
- **Verification**: Запросы с anon/authenticated ключами возвращают ожидаемые строки; без ключа — отказ.
- **Complexity**: Medium

#### Task 2.2: RLS on user data (user_profiles, favorites, swipes)
- **Description**: RLS для user_profiles, favorites, swipes: SELECT/INSERT/UPDATE/DELETE только где auth.uid() = user_id или id.
- **Files**:
  - `supabase/migrations/YYYYMMDDHHMMSS_04_rls_user.sql` — Create
- **Dependencies**: Task 1.2
- **Verification**: Пользователь видит только свои favorites/swipes/profile; чужой id — пустой результат.
- **Complexity**: Low

#### Task 2.3: RLS on annotations
- **Description**: RLS для annotations по user_id/parcel_id (владелец).
- **Files**:
  - Включить в миграцию 04 или отдельно `supabase/migrations/YYYYMMDDHHMMSS_05_rls_annotations.sql`
- **Dependencies**: Task 1.2
- **Verification**: Доступ только к своим annotations.
- **Complexity**: Low

### Phase 3: Views and Functions

#### Task 3.1: Views (v_liens_full, v_foreclosure_candidates, v_otc_liens, v_top_picks)
- **Description**: CREATE VIEW по FR-2; v_liens_full как база для остальных.
- **Files**:
  - `supabase/migrations/YYYYMMDDHHMMSS_06_views.sql` — Create
- **Dependencies**: Task 1.1
- **Verification**: GET `/rest/v1/v_liens_full`, `v_foreclosure_candidates`, `v_otc_liens`, `v_top_picks` с фильтрами.
- **Complexity**: Low

#### Task 3.2: Functions and trigger (search_liens, get_top_picks, increment_swipe)
- **Description**: CREATE FUNCTION search_liens, get_top_picks; trigger increment_swipe на swipes.
- **Files**:
  - `supabase/migrations/YYYYMMDDHHMMSS_07_functions.sql` — Create
- **Dependencies**: Task 3.1 (views используют liens/parcels)
- **Verification**: POST `/rest/v1/rpc/search_liens`, `/rest/v1/rpc/get_top_picks` с параметрами; INSERT в swipes увеличивает user_profiles.swipes_today.
- **Complexity**: Medium

### Phase 4: Storage

#### Task 4.1: Buckets and storage policies
- **Description**: Создать buckets images (public), documents (private), exports (private). Политики: images — public read; documents — authenticated read; exports — read by owner (path = uid/...).
- **Files**:
  - `supabase/migrations/YYYYMMDDHHMMSS_08_storage.sql` — Create (storage.buckets + storage.objects policies)
- **Dependencies**: None (можно параллельно с Phase 1–3)
- **Verification**: Загрузка/скачивание через Supabase Storage API; Image Transforms URL для images.
- **Complexity**: Low

### Phase 5: Edge Functions

#### Task 5.1: Edge Function rate-limit
- **Description**: Deno Edge Function: проверка JWT, чтение user_profiles (tier, swipes_today), возврат 429 при превышении лимита по tier.
- **Files**:
  - `supabase/functions/rate-limit/index.ts` — Create
- **Dependencies**: Task 1.2 (user_profiles)
- **Verification**: Вызов с валидным JWT и превышением swipes_today → 429; в пределах лимита → 200.
- **Complexity**: Medium

#### Task 5.2: Edge Function ml-predict (optional)
- **Description**: Прокси POST на ML_SERVICE_URL для predictions. Опционально — только если нужен вызов ML через Edge.
- **Files**:
  - `supabase/functions/ml-predict/index.ts` — Create
- **Dependencies**: None
- **Verification**: POST с телом → ответ от ML service.
- **Complexity**: Low

### Phase 6: Realtime and Replication

#### Task 6.1: Enable Realtime for tables
- **Description**: Включить Realtime для liens, auctions (и при необходимости parcels) через Supabase Dashboard или migration (realtime publication).
- **Files**:
  - Документация или `supabase/migrations/YYYYMMDDHHMMSS_09_realtime.sql` — добавить таблицы в publication supabase_realtime.
- **Dependencies**: Task 1.1
- **Verification**: Подписка из клиента на изменения по таблице возвращает события.
- **Complexity**: Low

### Phase 7: Gateway alignment (this repo)

#### Task 7.1: Document connection and schema contract
- **Description**: Убедиться, что Gateway (Worker API) и миграции используют одну и ту же схему: имена таблиц (parcels, liens и т.д.), типы полей. Добавить в README или docs ссылку на Supabase migrations и переменные (SUPABASE_URL / direct Postgres для воркеров).
- **Files**:
  - `README.md` или `flows/sdd-taxlien-gateway-supabase/04-implementation-log.md` — Modify
- **Dependencies**: Все миграции
- **Verification**: Gateway при записи results не ломает ограничения и типы Supabase.
- **Complexity**: Low

## Dependency Graph

```
1.1 (base tables) ─┬─→ 2.1 (RLS public) ─→ 3.1 (views) ─→ 3.2 (functions)
                   │
1.2 (user tables) ─┼─→ 2.2 (RLS user) ─→ 2.3 (RLS annotations)
                   │
                   └─→ 5.1 (rate-limit)

4.1 (storage) ──── standalone
5.2 (ml-predict) ─ standalone (optional)
6.1 (realtime) ─── after 1.1
7.1 (docs) ─────── after all
```

## File Change Summary

| File | Action | Reason |
|------|--------|--------|
| `supabase/migrations/*_01_base_tables.sql` | Create | FR-1 parcels, auctions, liens |
| `supabase/migrations/*_02_user_tables.sql` | Create | FR-1 user_profiles, favorites, swipes, annotations |
| `supabase/migrations/*_03_rls_public.sql` | Create | FR-3 RLS parcels, liens, auctions |
| `supabase/migrations/*_04_rls_user.sql` | Create | FR-3 RLS user tables |
| `supabase/migrations/*_05_rls_annotations.sql` | Create | FR-3 RLS annotations (или объединить с 04) |
| `supabase/migrations/*_06_views.sql` | Create | FR-2 views |
| `supabase/migrations/*_07_functions.sql` | Create | FR-4 functions + trigger |
| `supabase/migrations/*_08_storage.sql` | Create | FR-5 buckets + policies |
| `supabase/migrations/*_09_realtime.sql` | Create | FR-7 Realtime publication |
| `supabase/functions/rate-limit/index.ts` | Create | FR-6 rate-limit |
| `supabase/functions/ml-predict/index.ts` | Create | FR-6 ml-predict (optional) |
| `README.md` or flow docs | Modify | Schema contract, env vars for Gateway |

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Порядок миграций ломает FK | Low | High | Строгий порядок: parcels → auctions → liens → user tables |
| RLS блокирует легитимный доступ | Medium | Medium | Тесты с anon/authenticated; постепенное включение RLS по таблицам |
| Storage policies слишком строгие | Low | Low | Начать с read-only политик, расширять по необходимости |
| Edge Function cold start | Low | Low | Принять задержку или кэшировать tier в клиенте |

## Rollback Strategy

1. **Миграции**: для каждой миграции при необходимости написать down (DROP POLICY, DROP VIEW, DROP FUNCTION, DROP TABLE в обратном порядке) или восстановить БД из снапшота до применения миграции.
2. **Storage**: удалить объекты из бакетов при откате; бакеты можно оставить.
3. **Edge Functions**: отключить вызовы из клиента; удалить или заменить функции на no-op.
4. **Клиенты**: держать возможность переключения обратно на старый API до полного отключения (feature flag или env).

## Checkpoints

After each phase:

- [ ] Миграции применяются без ошибок в Supabase.
- [ ] PostgREST возвращает ожидаемые данные для типовых запросов.
- [ ] RLS проверен под anon и authenticated.
- [ ] После Phase 7: Gateway (если уже подключён к той же БД) не падает на новых ограничениях.

## Open Implementation Questions

- [ ] Хранить ли миграции в taxlien-gateway или в отдельном repo (e.g. taxlien-supabase)? Решение: оставить в gateway для единого контракта схемы с Worker API.
- [ ] Материализованные представления для v_top_picks: отложить до замера производительности.
- [ ] CSV export (FR-12): реализовать в Edge Function или PostgREST streaming — решить в рамках sdd-miw-gift.

---

## Approval

- [ ] Reviewed by: —
- [ ] Approved on: —
- [ ] Notes: —
