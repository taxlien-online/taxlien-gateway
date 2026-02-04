# Specifications: Supabase Backend

**Version:** 1.0
**Status:** DRAFT
**Last Updated:** 2026-02-04
**Requirements:** [01-requirements.md](01-requirements.md)

---

## Overview

Supabase выступает единым backend для TAXLIEN.online: БД, Auth, Storage, auto-generated REST (PostgREST). Спека уточняет схему, RLS, хранилище и интеграцию с минимальным Gateway (Worker API).

## Affected Systems

| System | Impact | Notes |
|--------|--------|-------|
| Supabase Project | Create/Modify | PostgreSQL, Auth, Storage, Edge Functions |
| taxlien-gateway | Modify | Только Worker API :8081; публичный API не в Gateway |
| Flutter / SSR / Swipe apps | Modify | Переход на Supabase SDK вместо custom API |

## Architecture

```
Clients (Flutter, SSR, Swipe)
    │
    ├── Supabase SDK ──► PostgREST (/rest/v1/*), Auth, Storage, Realtime
    │
    └── Worker API ────► Gateway :8081 (X-Worker-Token) ──► Redis + same PostgreSQL
```

## Data Model (Summary)

- **parcels** — участки (parcel_id, state, county, platform, address, property_type, values, owner, scraped_at, …)
- **liens** — налоговые залоги (parcel_id FK, lien_amount, dates, status, is_otc, prior_years_owed, ML scores: redemption_probability, foreclosure_probability, miw_score, karma_score)
- **auctions** — аукционы (state, county, auction_date, platform, status, …)
- **user_profiles** — расширение auth.users (tier, preferences, swipes_today, …)
- **favorites**, **swipes**, **annotations** — пользовательские данные с RLS

Детальные DDL — в 01-requirements (FR-1).

## Views (FR-2)

- **v_liens_full** — liens + parcel fields + lien_to_value_ratio
- **v_foreclosure_candidates** — prior_years_owed >= 2, foreclosure_probability > 0.6 (для sdd-miw-gift)
- **v_otc_liens** — is_otc = true, status = 'ACTIVE'
- **v_top_picks** — flipper/landlord/beginner scores

## Row-Level Security (FR-3)

- **parcels, liens:** SELECT для authenticated (и при необходимости anon с лимитами через Edge/RLS).
- **favorites, swipes, user_profiles:** только владелец (auth.uid() = user_id / id).
- **storage.objects:** политики по bucket (images — public read; documents — authenticated; exports — owner).

## Database Functions (FR-4)

- **search_liens(...)** — фильтры (state, county, max_amount, foreclosure_prob, prior_years, property_type, is_otc, limit, offset).
- **get_top_picks(state, county, persona, limit)** — топ по флиппер/лендлорд/beginner.
- **increment_swipe()** — trigger на swipes для учёта swipes_today в user_profiles.

Вызов через PostgREST: `POST /rest/v1/rpc/search_liens`, `POST /rest/v1/rpc/get_top_picks`.

## Storage (FR-5)

- **Buckets:** images (public), documents (private), exports (private, owner).
- **Image Transforms:** Supabase Image Transforms (width, height, quality) в URL.
- **Policies:** см. 01-requirements FR-5.

## Edge Functions (FR-6)

- **rate-limit** — проверка tier и swipes_today; возврат 429 при превышении.
- **ml-predict** (опционально) — прокси к ML service для predictions.

## API Surface (PostgREST)

- Таблицы и представления: GET/POST/PATCH/DELETE по `/rest/v1/{table}`.
- RPC: POST `/rest/v1/rpc/search_liens`, `/rest/v1/rpc/get_top_picks`.
- Примеры запросов — в 01-requirements (API Endpoints).

## Integration with Gateway

- **Gateway v3.0** подключается к той же PostgreSQL (Supabase) через pgx для записи результатов воркеров (parcels, сырые данные) и к Redis для очередей.
- Публичные endpoints (liens, foreclosure-candidates, OTC, search, export) обслуживаются через Supabase PostgREST и views/functions, не через Gateway.

## Miw / FR-12 (sdd-miw-gift)

Endpoints для Miw/Shon (foreclosure-candidates, OTC, search, CSV export) реализуются через:

- **Views:** v_foreclosure_candidates, v_otc_liens
- **Function:** search_liens
- **Export:** Edge Function или PostgREST + stream CSV, либо клиентская выборка с лимитами

Rate limit bypass для внутренних пользователей — через tier в user_profiles или отдельный сервисный ключ.

## Migration

- **From Firebase Auth:** миграция пользователей в Supabase Auth (admin API), маппинг firebase_uid в user_metadata.
- **From custom API:** деплой схемы Supabase → перенос данных → переключение клиентов на Supabase SDK → отключение старых endpoints.

## Open Design Questions

- [ ] Материализованные представления для тяжёлых запросов (v_top_picks и т.п.).
- [ ] Точный формат CSV export (Edge Function vs PostgREST streaming).
- [ ] Tier-based limits: только RLS + Edge или отдельная таблица лимитов.

---

**Next Phase:** PLAN (разбивка задач по внедрению схемы, RLS, Storage, Edge Functions).
