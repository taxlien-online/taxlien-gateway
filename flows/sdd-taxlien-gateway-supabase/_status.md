# Status: sdd-taxlien-supabase

## Current Phase

**REQUIREMENTS** | SPECIFICATIONS | PLAN | IMPLEMENTATION

## Phase Status

DRAFTING

## Last Updated

2026-02-01

## Blockers

- None

## Progress

- [x] Requirements drafted
- [ ] Requirements approved
- [ ] Specifications drafted
- [ ] Specifications approved
- [ ] Plan drafted
- [ ] Plan approved
- [ ] Implementation started
- [ ] Implementation complete

## Context Notes

**Decision (2026-02-01):** Использовать Supabase как primary backend вместо custom microservices.

**Supabase заменяет:**
- `sdd-taxlien-storage` → Supabase Storage
- `sdd-taxlien-imgproxy` → Supabase Image Transforms
- Firebase Auth → Supabase Auth
- Custom CRUD API → PostgREST auto-API

**Остаётся custom Go service для:**
- Worker Internal API (task queue)
- ML predictions proxy (optional)
- Complex rate limiting (optional)

**Related SDDs:**
- `sdd-taxlien-gateway` - упрощённый до Worker API only
- `sdd-taxlien-ml` - ML service (отдельный)

## Next Actions

1. Review requirements draft
2. Approve Supabase approach
3. Define database schema
4. Define RLS policies
