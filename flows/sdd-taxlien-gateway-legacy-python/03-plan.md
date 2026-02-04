# Plan: API Gateway Implementation (Legacy Python)

**Version:** 1.1 (Legacy reference)
**Status:** PLAN
**Based on:** Specifications v1.0
**Last Updated:** 2026-02-04

**Примечание:** Целевая реализация — v3.0 Minimal в `sdd-taxlien-gateway` (Go, один порт :8081). Задачи ниже описывают legacy Python-реализацию и возможную миграцию; Phase 5 (Tri-Port) не реализовывать — заменён на v3.0.

---

## Phase 0: Unit Test Coverage of Existing Code (PRIORITY 1)

**Goal:** Full unit test coverage of any existing Gateway code to understand what's actually implemented.

### 0.1. Audit Existing Code
- [ ] Check if `gateway/` directory exists with any code
- [ ] List all `.py` files in `gateway/` (if exists)
- [ ] For each file, document: exists? functions? tested?
- [ ] Create coverage report if code exists
- [ ] **Output:** `EXISTING_CODE_AUDIT.md` with real vs documented status

### 0.2. Test Existing Auth (if exists)
- [ ] Test `auth/authenticator.py` - Firebase, Worker, SSR token validation
- [ ] Test `auth/authorizer.py` - tier-based access control
- [ ] Mock Firebase Admin SDK
- [ ] **Verification:** Auth module has ≥80% line coverage

### 0.3. Test Existing Middleware (if exists)
- [ ] Test `middleware/rate_limit.py` - token bucket logic
- [ ] Test `middleware/cors.py` - CORS headers
- [ ] Test with mock Redis
- [ ] **Verification:** Middleware has ≥70% line coverage

### 0.4. Test Existing Services (if exists)
- [ ] Test `services/queue.py` - enqueue, fetch, complete
- [ ] Test `services/proxy_pool.py` - allocate, ban, rotate
- [ ] Test `services/worker_registry.py` - heartbeat, cleanup
- [ ] Mock Redis and PostgreSQL
- [ ] **Verification:** Services have ≥70% line coverage

### 0.5. Document Gaps
- [ ] List files specified in `02-specifications.md` that don't exist
- [ ] List functions that exist but don't match spec
- [ ] Create implementation priority based on findings

**Phase 0 Exit Criteria:**
- [ ] `EXISTING_CODE_AUDIT.md` documents what's real vs planned
- [ ] All existing code has ≥70% test coverage
- [ ] Critical gaps identified for Phase 1

---

## Strategy

Implement the Gateway in 4 phases, prioritizing **Internal API** to unblock Parser workers.

**Testing Strategy:**
- **Unit Tests**: Auth, Rate Limiting, Queue logic
- **Integration Tests**: TestClient with mocked Redis/Postgres
- **E2E Tests**: Real Gateway + Parser Worker integration

---

## Phase 1: Foundation & Core Infrastructure

**Goal**: Functional FastAPI skeleton with Redis, Logging, and basic Middleware.

- [ ] **Task 1.1: Project Skeleton**
    - Create `sdd-taxlien-gateway` directory structure.
    - Setup `pyproject.toml` (poetry/pip).
    - Setup `Dockerfile` and `docker-compose.yml` (w/ Redis).
    - Create `main.py` with basic health check.
    - **Verification**: `curl localhost:8000/health` returns 200.

- [ ] **Task 1.2: Configuration & Logging**
    - Implement `core/config.py` (Pydantic settings).
    - Setup structured logging (`structlog`).
    - **Verification**: Logs output in JSON format.

- [ ] **Task 1.3: Redis & Database Manager**
    - Implement `core/redis.py` (Async client pool).
    - Implement `core/db.py` (SQLAlchemy async engine).
    - **Verification**: Integration test connecting to Redis/DB.

- [ ] **Task 1.4: Rate Limiter (Redis)**
    - Implement Token Bucket logic in Lua.
    - Create `RateLimitMiddleware`.
    - **Verification**: Test hitting limit triggers 429.

---

## Phase 2: Internal API (Worker Support)

**Goal**: Allow distributed workers to pull tasks and push results.

- [ ] **Task 2.1: Auth (Worker Tokens)**
    - Implement `AuthMiddleware` for `X-Worker-Token`.
    - **Verification**: Request without token returns 401.

- [ ] **Task 2.2: Work Queue Logic**
    - Create `services/queue.py`.
    - Implement `pop_work(worker_id, platforms)` logic.
    - **Verification**: Unit test queuing and popping items.

- [ ] **Task 2.3: Endpoint `/internal/work`**
    - Implement GET endpoint.
    - **Verification**: Worker receives tasks from queue.

- [ ] **Task 2.4: Endpoint `/internal/results`**
    - Implement POST endpoint.
    - Schema validation for `ParcelResult`.
    - Mock DB write for now (or basic insert).
    - **Verification**: Valid JSON payload is accepted.

- [ ] **Task 2.5: Endpoint `/internal/heartbeat` & `/internal/proxy`**
    - Implement Heartbeat (update Redis).
    - Implement Proxy endpoints (mock proxy service calls).
    - **Verification**: Redis key updates on heartbeat.

---

## Phase 3: External API (Client Support)

**Goal**: Public API for Apps/Sites with Firebase Auth and Caching.

- [ ] **Task 3.1: Firebase Authentication**
    - Integrate `firebase-admin`.
    - Update `AuthMiddleware` to handle Bearer tokens.
    - Implement `User` extraction and Tier assignment.
    - **Verification**: Valid JWT passes, invalid fails.

- [ ] **Task 3.2: HTTP Client & Circuit Breaker**
    - Implement `services/http_client.py`.
    - Add Circuit Breaker logic (Open/Half-Open/Closed).
    - **Verification**: Simulate 500s and ensure breaker opens.

- [ ] **Task 3.3: Proxy Endpoints (Properties/Search)**
    - Implement `/v1/properties/*`.
    - Forward requests to `PARSER_SERVICE_URL`.
    - **Verification**: Response from Parser Service is relayed.

- [ ] **Task 3.4: Response Caching**
    - Implement `CacheMiddleware` or decorator.
    - Cache keys based on URL + User Tier.
    - **Verification**: Second request hits cache (check headers).

---

## Phase 4: Production Readiness

**Goal**: Metrics, Safety, and Deployment config.

- [x] **Task 4.1: Observability**
    - Add Prometheus middleware.
    - Expose `/metrics` endpoint.
    - **Verification**: `/metrics` shows request counts.

- [x] **Task 4.2: Tier Enforcement**
    - Implement `TierMiddleware` or Dependency.
    - Check usage limits in Redis before routing.
    - **Verification**: Free tier blocked after N requests.

- [x] **Task 4.3: Final Integration Test**
    - End-to-end test flow: Auth -> Gateway -> (Mock) Service -> Cache.

---

## Phase 5: Parcel vs Party Separation (Stateless Support)

**Goal:** Implement Tri-Port architecture to isolate Parcel and Party internal traffic.

### 5.1. Refactor Configuration
- [ ] Update `gateway/config.py` to include `parcel_internal_port` (8081) and `party_internal_port` (8082).
- [ ] Add separate token sets for parcel and party workers if needed.

### 5.2. Create Internal Applications
- [ ] Create `gateway/apps/parcel_internal.py` with routes for parcel workers.
- [ ] Create `gateway/apps/party_internal.py` with routes for party/document workers.
- [ ] Ensure both apps share core services (DB, Redis) but have independent middleware.

### 5.3. Split Route Handlers
- [ ] Move parcel-related internal routes to `gateway/api/internal/parcel/`.
- [ ] Move party-related internal routes to `gateway/api/internal/party/`.
- [ ] Create shared heartbeat router in `gateway/api/internal/heartbeat.py`.

### 5.4. Update Main Entry Point
- [ ] Refactor `gateway/main.py` to launch 3 `uvicorn.Server` instances concurrently using `asyncio.gather`.
- [ ] Implement graceful shutdown for all 3 servers.

### 5.5. Infrastructure & Docker
- [ ] Update `gateway/Dockerfile` to `EXPOSE 8080 8081 8082`.
- [ ] Update `docker-compose.yml` with new ports and environment variables.
- [ ] Update `prometheus.yml` to scrape metrics from all 3 ports.

### 5.6. Verification
- [ ] Test that `:8081` only accepts Parcel-related requests.
- [ ] Test that `:8082` only accepts Party-related requests.
- [ ] Verify metrics isolation in Grafana.

---

## Phase 5: CI/CD Pipeline (New)

**Goal**: Automated testing and Docker image publishing.

- [ ] **Task 5.1: GitHub Actions Workflow**
    - Create `.github/workflows/gateway-ci.yml`.
    - Configure `test` job (lint, type-check, pytest).
    - Configure `build-and-push` job (GHCR).
    - **Verification**: Push to branch triggers tests; push to main triggers build.

---

## Phase 6: Monitoring Dashboards (New)

**Goal**: Visual visibility of system state.

- [ ] **Task 6.1: Grafana Dashboard Generation**
    - Create `gateway/monitoring/grafana/dashboards/gateway_command_center.json`.
    - Implement all 4 rows defined in specs.
    - **Verification**: Dashboard JSON is valid and can be imported into Grafana.

---

## Complexity Estimates

| Phase | Complexity | Est. Files |
|-------|------------|------------|
| 1. Foundation | Low | 5-7 |
| 2. Internal API | Medium | 6-8 |
| 3. External API | High | 8-10 |
| 4. Production | Medium | 3-5 |
| 5. CI/CD | Low | 1 |
| 6. Dashboards | Low | 1 |

## Dependencies

- **Redis**: Critical for all phases (queue, rate limiting, worker registry)
- **PostgreSQL**: Needed for Task 2.4 (parcel results storage)
- **tor-socks-proxy**: For Phase 2.5 proxy endpoints (can be mocked)

---

## Implementation Order

```
Phase 1 (Foundation)     → Phase 2 (Internal API)     → Phase 3 (External API)    → Phase 4 (Production)
       ↓                          ↓                            ↓                          ↓
   Health check              Workers can               Apps/SSR can                Metrics &
   Redis/DB pool            pull & submit              query data                  monitoring
   Rate limiter              tasks                                                  ready
```

---

## Success Criteria

1. **Phase 2 Complete**: Parser workers can run end-to-end against Gateway
2. **Phase 3 Complete**: SSR site can fetch property data via Gateway
3. **Phase 4 Complete**: Prometheus metrics visible in Grafana

---

**Next Step:** User approval, then begin Phase 1 implementation.
