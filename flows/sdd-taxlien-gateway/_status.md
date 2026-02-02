# Status: sdd-taxlien-gateway

## Current Phase

**REQUIREMENTS** | SPECIFICATIONS | PLAN | IMPLEMENTATION

## Phase Status

DRAFTING (Go Rewrite v2.0)

## Last Updated

2026-02-01

## Blockers

- None

## Progress

### v1.x (Python/FastAPI) - DEPRECATED
- [x] Requirements drafted
- [x] Requirements approved (v1.0) ✅
- [x] Requirements update (v1.1 - CI/CD & Dashboards) ✅
- [x] Requirements update (v1.2 - Dual-Port Architecture) ✅
- [x] Specifications drafted (v1.0)
- [x] Specifications approved ✅
- [x] Plan approved ✅
- [x] Implementation (v1.1 Complete)

### v2.0 (Go Rewrite)
- [x] Requirements v2.0: Tech Stack changed to Go (Chi router)
- [x] Requirements v2.0: Code examples converted to Go
- [x] Requirements v2.0: Tri-Port Architecture (Public :8080, Parcel :8081, Party :8082)
- [ ] Requirements v2.0: User approval
- [ ] Specifications v2.0: Update OpenAPI spec
- [ ] Specifications v2.0: Go-specific architecture details
- [ ] Plan v2.0: Go implementation tasks
- [ ] Implementation v2.0: Core server structure
- [ ] Implementation v2.0: Middleware chain
- [ ] Implementation v2.0: Handlers
- [ ] Implementation v2.0: Tests

## Context Notes (v2.0 → v3.0 Minimal)

**Decision (2026-02-01):** Supabase как primary backend.

**v2.0 (Go Full Gateway) - SUPERSEDED:**
- Tri-Port Architecture
- Full CRUD API
- Auth, Rate Limiting, Caching

**v3.0 (Minimal Worker API) - CURRENT:**
- Supabase handles: Auth, CRUD, Storage, Rate Limiting
- Gateway handles ONLY: Worker Internal API
- Single port: :8081 (internal only)

**Tech Stack (Minimal):**
- Go 1.22+ с Chi router
- pgx для PostgreSQL (direct to Supabase DB)
- go-redis для task queue

**Architecture:**
- Single Port: Internal (:8081) for Workers only
- NO public API (handled by Supabase PostgREST)
- NO auth (workers use X-Worker-Token)
- NO rate limiting (handled by Supabase)

**Replaced by Supabase:**
- `sdd-taxlien-imgproxy` → Supabase Image Transforms
- `sdd-taxlien-storage` → Supabase Storage
- Public CRUD API → Supabase PostgREST
- Firebase Auth → Supabase Auth

**Related SDDs:**
- `sdd-taxlien-supabase` - Primary backend (NEW)
- `sdd-taxlien-ml` - ML predictions service

## Next Actions

1. Review Go requirements draft (01-requirements.md)
2. Approve requirements v2.0
3. Review extracted SDDs (imgproxy, storage)
4. Update specifications with Go-specific details
5. Create implementation plan for Go