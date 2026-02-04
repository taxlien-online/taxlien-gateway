# Status: sdd-taxlien-gateway

## Current Phase

REQUIREMENTS ✅ | **SPECIFICATIONS** | PLAN | IMPLEMENTATION

## Phase Status

SPECIFICATIONS (v3.0 Minimal) — drafting

## Last Updated

2026-02-04

## Blockers

- None

## Progress

### v1.x (Python/FastAPI) — DEPRECATED / LEGACY
- [x] Requirements drafted
- [x] Requirements approved (v1.0) ✅
- [x] Specifications drafted (v1.0)
- [x] Plan approved ✅
- [x] Implementation (v1.1 Complete); code in `legacy/`

### v2.0 (Go Tri-Port) — SUPERSEDED
- [x] Requirements v2.0 drafted (Go, Tri-Port)
- [ ] Superseded by v3.0 Minimal; preserved in 01-requirements for reference

### v3.0 (Minimal Worker API) — CURRENT TARGET
- [x] Requirements: v3.0 scope documented in 01-requirements (Current target section)
- [x] Specifications: v3.0 section added in 02-specifications
- [x] Plan: v3.0 tasks added in 03-plan
- [ ] Specifications v3.0: User review
- [ ] Plan v3.0: User approval
- [ ] Implementation: Go minimal server (:8081 only)

## Context Notes (v3.0 Minimal)

**Decision (2026-02-01):** Supabase как primary backend.

**v3.0 (Minimal Worker API) — CURRENT:**
- Supabase: Auth, CRUD, Storage, Rate Limiting, Liens/foreclosure endpoints (PostgREST + RLS)
- Gateway: только Worker Internal API
- Один порт: **:8081** (internal only)

**Tech Stack (v3.0):**
- Go 1.22+ (Chi router)
- pgx → PostgreSQL (Supabase DB)
- go-redis → task queue

**Architecture:**
- Single port :8081, X-Worker-Token, no public API, no proxy logic (workers manage tor-socks-proxy themselves).

**Related SDDs:**
- `sdd-taxlien-gateway-supabase` — primary backend (Auth, CRUD, liens, storage)
- `sdd-taxlien-ml` — ML predictions
- `sdd-miw-gift` — FR-12 endpoints (foreclosure/OTC/search/export) реализуются через Supabase views + PostgREST

## Next Actions

1. Review 02-specifications (v3.0 section)
2. Review 03-plan (v3.0 Minimal tasks)
3. Approve specs/plan and start implementation (Go minimal server)