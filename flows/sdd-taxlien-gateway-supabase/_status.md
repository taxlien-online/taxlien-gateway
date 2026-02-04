# Status: sdd-taxlien-gateway-supabase

## Current Phase

REQUIREMENTS ✅ | **SPECIFICATIONS** | PLAN | IMPLEMENTATION

## Phase Status

SPECIFICATIONS DRAFTED — на ревью

## Last Updated

2026-02-04

## Blockers

- None

## Progress

- [x] Requirements drafted (01-requirements.md)
- [ ] Requirements approved
- [x] Specifications drafted (02-specifications.md)
- [ ] Specifications approved
- [ ] Plan drafted
- [ ] Plan approved
- [ ] Implementation started
- [ ] Implementation complete

## Context Notes

**Decision (2026-02-01):** Supabase как primary backend.

**Supabase заменяет:**
- Storage → Supabase Storage (+ Image Transforms)
- Firebase Auth → Supabase Auth
- Custom CRUD / Liens API → PostgREST (views, RPC)

**Gateway (sdd-taxlien-gateway v3.0):** только Worker API :8081 (work, results, heartbeat, raw-files, tasks). Подключается к той же Supabase PostgreSQL и к Redis.

**Related SDDs:**
- `sdd-taxlien-gateway` — v3.0 Minimal (Worker API)
- `sdd-miw-gift` — FR-12 (foreclosure/OTC/search/export) через Supabase views + PostgREST

## Next Actions

1. Ревью 02-specifications.md
2. Утвердить требования и спеки
3. Написать план (03-plan): порядок деплоя схемы, RLS, Storage, Edge Functions
