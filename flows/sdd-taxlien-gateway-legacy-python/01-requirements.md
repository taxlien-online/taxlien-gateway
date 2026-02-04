# Requirements: API Gateway - Unified Entry Point (Legacy Python)

**Version:** 1.0 (Legacy reference)
**Status:** REQUIREMENTS
**Last Updated:** 2026-02-04
**Goal:** Описание legacy Python Gateway и границ ответственности.

**Уточнение по прокси:** Управление прокси не входит в Gateway. Воркеры сами подключаются к tor-socks-proxy (переменные окружения). Endpoints `/internal/proxy/*` в Gateway не реализуются. См. `sdd-taxlien-gateway` (v3.0) и 02-specifications (раздел "tor-socks-proxy: NOT Gateway's Responsibility").

---

## Problem Statement

### Current State

API Gateway упоминается во всех SDDs, но нигде не специфицирован:
- Flutter app предполагает Gateway существует
- SSR site предполагает Gateway существует
- ML service ожидает X-Service-Token от Gateway
- Parser service ожидает X-Service-Token от Gateway

**Проблемы без формальной спецификации:**
1. Неясно кто отвечает за auth/rate limiting
2. Нет единого формата ошибок
3. Нет версионирования API
4. Нет документации endpoint'ов
5. Каждый SDD описывает свою часть взаимодействия

### Why Gateway?

```
БЕЗ GATEWAY (плохо):
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Flutter App │────▶│ Parser API  │     │  ML API     │
└─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │
       │            (auth? limits?)      (auth? limits?)
       │                   │                   │
       └───────────────────┴───────────────────┘
                    Дублирование логики

С GATEWAY (хорошо):
┌─────────────┐
│ Flutter App │──┐
└─────────────┘  │     ┌─────────────┐     ┌─────────────┐
                 ├────▶│   GATEWAY   │────▶│ Internal    │
┌─────────────┐  │     │ (auth,rate) │     │ Services    │
│  SSR Site   │──┘     └─────────────┘     └─────────────┘
└─────────────┘              │
                    Единая точка контроля
```

---

## Scope & Architecture

### Gateway = Tri-Port Architecture (One Service, Three Entry Points)

**Архитектурное решение:** Единый сервис с тремя портами для полной изоляции публичного, внутреннего "по-участкам" (Parcel) и внутреннего "по-лицам" (Party) трафика.

| Port | App | Purpose | Authentication |
|------|-----|---------|----------------|
| **:8080** | Public API | Flutter, SSR Site, B2B clients | Firebase/API Key |
| **:8081** | Internal Parcel API | Parcel Workers only | X-Worker-Token |
| **:8082** | Internal Party API | Party Workers only | X-Worker-Token |

**Преимущества разделения Parcel и Party на уровне портов:**
- **QoS (Quality of Service):** Парсинг миллионов участков не блокирует приоритетный сбор документов по владельцам (Parties).
- **Изоляция очередей:** Разные воркеры тянут задачи из разных очередей через разные порты.
- **Масштабирование:** Возможность выставить разные лимиты (Rate Limits) для Parcel (bulk) и Party (deep dive).

**Почему dual-port, а не отдельные сервисы:**
- Shared codebase (меньше дублирования)
- Shared dependencies (database, redis, storage)
- Единый deploy, но изолированные сети
- Best practice: Netflix BFF pattern, Kubernetes sidecar pattern

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              EXTERNAL (Public)                               │
│                                                                             │
│   ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐      │
│   │  Flutter App    │     │   SSR Site      │     │   B2B Client    │      │
│   │  (Mobile/Web)   │     │   (Next.js)     │     │   (API Key)     │      │
│   └────────┬────────┘     └────────┬────────┘     └────────┬────────┘      │
│            │ User Token            │ SSR Token             │ API Key       │
│            └───────────────────────┼───────────────────────┘               │
│                                    ▼                                        │
│            ┌───────────────────────────────────────────────────────────┐   │
│            │              PUBLIC API APP (:8080)                        │   │
│            │              api.taxlien.online                            │   │
│            │                                                            │   │
│            │   ┌──────────────────────────────────────────────────┐    │   │
│            │   │  1. SSL Termination (Let's Encrypt)              │    │   │
│            │   │  2. Authentication (Firebase/API Key)            │    │   │
│            │   │  3. Authorization (Tier-based access)            │    │   │
│            │   │  4. Rate Limiting (Redis)                        │    │   │
│            │   │  5. Request Validation                           │    │   │
│            │   │  6. Response Caching (Redis)                     │    │   │
│            │   │  7. Logging & Metrics                            │    │   │
│            │   └──────────────────────────────────────────────────┘    │   │
│            │                           │                                │   │
│            └───────────────────────────┼───────────────────────────────┘   │
│                                        │                                    │
└────────────────────────────────────────┼────────────────────────────────────┘
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SHARED SERVICES (Gateway)                          │
│                                                                             │
│   ┌────────────────┐   ┌────────────────┐   ┌────────────────┐             │
│   │   PostgreSQL   │   │     Redis      │   │   /data/raw    │             │
│   │   Connection   │   │   Connection   │   │    Storage     │             │
│   │     Pool       │   │     Pool       │   │                │             │
│   └────────────────┘   └────────────────┘   └────────────────┘             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                         ▲
┌────────────────────────────────────────┼────────────────────────────────────┐
│                        INTERNAL NETWORK (VPN/Private)                        │
│                                        │                                     │
│            ┌───────────────────────────────────────────────────────────┐    │
│            │            INTERNAL API APP (:8081)                        │    │
│            │         internal-api.taxlien.local (VPN only)              │    │
│            │                                                            │    │
│            │   ┌──────────────────────────────────────────────────┐    │    │
│            │   │  1. X-Worker-Token validation                    │    │    │
│            │   │  2. IP whitelist (optional)                      │    │    │
│            │   │  3. No external caching                          │    │    │
│            │   │  4. Direct task queue access                     │    │    │
│            │   │  5. High rate limits (1000 req/min per worker)   │    │    │
│            │   └──────────────────────────────────────────────────┘    │    │
│            │                           ▲                                │    │
│            └───────────────────────────┼───────────────────────────────┘    │
│                                        │                                     │
│   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│   │  Parser Worker  │  │  Parser Worker  │  │  Parser Worker  │            │
│   │  (Machine A)    │  │  (Machine B)    │  │  (Cloud VM)     │            │
│   └─────────────────┘  └─────────────────┘  └─────────────────┘            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Internal Service Architecture

```
taxlien-gateway/
├── gateway/
│   ├── main.py                      # Entry point: runs BOTH apps
│   ├── config.py                    # Shared settings
│   │
├── apps/                        # THREE SEPARATE FASTAPI APPS
│   ├── public.py                # Public API app (:8080)
│   ├── parcel_internal.py       # Internal Parcel API (:8081)
│   └── party_internal.py        # Internal Party API (:8082)
│
├── api/                         # Route handlers
│   ├── public/                  # /v1/* endpoints
│   │   ├── properties.py
│   │   ├── search.py
│   │   ├── predictions.py
│   │   └── usage.py
│   └── internal/                # /internal/* endpoints
│       ├── parcel/              # Parcel-related worker API
│       │   ├── work.py
│       │   ├── results.py
│       │   └── tasks.py
│       └── party/               # Party-related worker API
│           ├── work.py
│           ├── results.py
│           └── documents.py
│       └── heartbeat.py         # Shared heartbeat for all workers
│   │
│   ├── middleware/
│   │   ├── public/                  # Public middleware chain
│   │   │   ├── cors.py
│   │   │   ├── firebase_auth.py
│   │   │   ├── rate_limit.py
│   │   │   └── cache.py
│   │   └── internal/                # Internal middleware chain
│   │       ├── worker_auth.py
│   │       └── ip_whitelist.py
│   │
│   ├── core/                        # SHARED between both apps
│   │   ├── database.py              # AsyncPG pool
│   │   ├── redis.py                 # Redis connection
│   │   └── storage.py               # File storage
│   │
│   └── services/                    # SHARED business logic
│       ├── task_queue.py
│       ├── properties.py
│       └── worker_registry.py
```

### Not In Scope (Gateway)

- Business logic (handled by services)
- Data storage (handled by services)
- ML predictions (handled by ML service)
- Scraping logic (handled by Parser service)
- User management (handled by Firebase)

---

## Functional Requirements

### FR-1: Authentication

**As a** client application
**I want** to authenticate via various methods
**So that** I can access protected endpoints

**Supported Auth Methods:**

| Method | Client Type | Token Format | Validation |
|--------|-------------|--------------|------------|
| Firebase ID Token | Flutter App | JWT | Firebase Admin SDK |
| SSR Service Token | Next.js SSR | Static secret | Environment variable |
| API Key | B2B clients | `X-API-Key` header | Database lookup |
| Anonymous | Public endpoints | None | Rate limit only |

**Acceptance Criteria:**
- [ ] Firebase token validation with 5-minute cache
- [ ] SSR token validation (constant-time comparison)
- [ ] API key lookup with usage tracking
- [ ] Anonymous access for public endpoints only
- [ ] Token refresh handling (401 → client refresh)
- [ ] Invalid token returns 401 with clear message

**Implementation:**

```python
# gateway/auth/authenticator.py
class Authenticator:
    async def authenticate(self, request: Request) -> AuthResult:
        # 1. Check for Firebase token
        if auth_header := request.headers.get("Authorization"):
            if auth_header.startswith("Bearer "):
                token = auth_header[7:]
                return await self._validate_firebase_token(token)

        # 2. Check for SSR service token
        if service_token := request.headers.get("X-SSR-Token"):
            return self._validate_ssr_token(service_token)

        # 3. Check for API key
        if api_key := request.headers.get("X-API-Key"):
            return await self._validate_api_key(api_key)

        # 4. Anonymous
        return AuthResult(authenticated=False, user=None, tier="anonymous")
```

---

### FR-2: Authorization (Tier-Based Access)

**As a** gateway
**I want** to enforce feature access by subscription tier
**So that** premium features are protected

**Tier Matrix:**

| Feature | Anonymous | Free | Starter | Premium | Enterprise |
|---------|-----------|------|---------|---------|------------|
| Property search | 5/day | 10/day | Unlimited | Unlimited | Unlimited |
| Property details | 10/day | 20/day | Unlimited | Unlimited | Unlimited |
| AI predictions | ❌ | 3/month | 10/month | Unlimited | Unlimited |
| Top lists | ❌ | ❌ | Top 10 | Full | Full |
| Bulk export | ❌ | ❌ | ❌ | 1000/day | Unlimited |
| On-demand scrape | ❌ | ❌ | ❌ | 10/day | 100/day |
| API access | ❌ | ❌ | ❌ | ❌ | ✅ |

**Acceptance Criteria:**
- [ ] Tier extracted from auth token or API key
- [ ] Feature limits enforced per endpoint
- [ ] Usage counters in Redis (per user, per day/month)
- [ ] 403 with `X-Upgrade-Required: true` when limit hit
- [ ] Usage stats available via `/v1/usage` endpoint

**Implementation:**

```python
# gateway/auth/authorizer.py
class Authorizer:
    LIMITS = {
        "anonymous": {"search": 5, "details": 10, "predictions": 0},
        "free": {"search": 10, "details": 20, "predictions": 3},
        "starter": {"search": -1, "details": -1, "predictions": 10},  # -1 = unlimited
        "premium": {"search": -1, "details": -1, "predictions": -1},
        "enterprise": {"search": -1, "details": -1, "predictions": -1},
    }

    async def authorize(self, user: User, endpoint: str, action: str) -> AuthzResult:
        limit = self.LIMITS[user.tier].get(action, 0)
        if limit == 0:
            return AuthzResult(allowed=False, reason="tier_restriction")
        if limit == -1:
            return AuthzResult(allowed=True)

        usage = await self.redis.get(f"usage:{user.id}:{action}:{today()}")
        if usage >= limit:
            return AuthzResult(allowed=False, reason="limit_exceeded", upgrade_to="starter")

        return AuthzResult(allowed=True, remaining=limit - usage - 1)
```

---

### FR-3: Rate Limiting

**As a** gateway
**I want** to limit request rates
**So that** services are protected from abuse

**Rate Limit Tiers:**

| Tier | Requests/min | Requests/hour | Burst |
|------|--------------|---------------|-------|
| Anonymous | 10 | 100 | 5 |
| Free | 30 | 500 | 10 |
| Starter | 60 | 2000 | 20 |
| Premium | 120 | 5000 | 50 |
| Enterprise | 600 | 20000 | 100 |

**Acceptance Criteria:**
- [ ] Token bucket algorithm in Redis
- [ ] Per-user rate limits (by user_id or API key)
- [ ] Per-IP rate limits (for anonymous/DDoS)
- [ ] 429 response with `Retry-After` header
- [ ] Rate limit headers in every response:
  - `X-RateLimit-Limit`
  - `X-RateLimit-Remaining`
  - `X-RateLimit-Reset`
- [ ] Bypass for internal health checks

**Implementation:**

```python
# gateway/ratelimit/limiter.py
class RateLimiter:
    async def check(self, identifier: str, tier: str) -> RateLimitResult:
        key = f"ratelimit:{identifier}"
        config = self.LIMITS[tier]

        # Token bucket in Redis
        tokens, last_update = await self.redis.hmget(key, "tokens", "updated")

        # Refill tokens based on time passed
        now = time.time()
        elapsed = now - float(last_update or now)
        tokens = min(config["burst"], float(tokens or config["burst"]) + elapsed * config["rate"])

        if tokens < 1:
            return RateLimitResult(
                allowed=False,
                retry_after=int((1 - tokens) / config["rate"]),
            )

        # Consume token
        await self.redis.hmset(key, {"tokens": tokens - 1, "updated": now})
        await self.redis.expire(key, 3600)

        return RateLimitResult(allowed=True, remaining=int(tokens - 1))
```

---

### FR-4: Request Routing

**As a** gateway
**I want** to route requests to appropriate internal services
**So that** clients have a unified API

**Route Configuration:**

| Public Endpoint | Internal Service | Internal Endpoint |
|-----------------|------------------|-------------------|
| `GET /v1/properties/{id}` | Parser :8080 | `/api/v1/properties/{id}` |
| `GET /v1/properties` | Parser :8080 | `/api/v1/properties` |
| `POST /v1/properties/{id}/refresh` | Parser :8080 | `/api/v1/scrape/parcel` |
| `GET /v1/search/address` | Parser :8080 | `/api/v1/search/address` |
| `GET /v1/search/owner` | Parser :8080 | `/api/v1/search/owner` |
| `POST /v1/predictions/redemption` | ML :8000 | `/api/v1/predict/redemption` |
| `POST /v1/predictions/batch` | ML :8000 | `/api/v1/predict/batch` |
| `GET /v1/top-lists/{strategy}` | ML :8000 | `/api/v1/top-lists/{strategy}` |
| `GET /v1/usage` | Gateway | (internal) |
| `GET /health` | Gateway | (internal) |

**Acceptance Criteria:**
- [ ] Route matching with path parameters
- [ ] Add `X-Service-Token` header to internal requests
- [ ] Add `X-Request-ID` for tracing
- [ ] Add `X-User-ID` and `X-User-Tier` for services
- [ ] Timeout handling (30s default)
- [ ] Circuit breaker for failing services
- [ ] Retry logic (1 retry for 5xx, not for 4xx)

**Implementation:**

```python
# gateway/routing/router.py
class Router:
    ROUTES = [
        Route(
            pattern="/v1/properties/{parcel_id}",
            methods=["GET"],
            service="parser",
            internal_path="/api/v1/properties/{parcel_id}",
            cache_ttl=3600,
        ),
        Route(
            pattern="/v1/predictions/batch",
            methods=["POST"],
            service="ml",
            internal_path="/api/v1/predict/batch",
            cache_ttl=0,  # No cache for POST
        ),
        # ...
    ]

    async def route(self, request: Request, user: User) -> Response:
        route = self._match_route(request.path, request.method)
        if not route:
            raise HTTPException(404, "Endpoint not found")

        # Build internal request
        internal_url = f"{self.services[route.service]}{route.internal_path}"
        headers = {
            "X-Service-Token": self.service_token,
            "X-Request-ID": request.state.request_id,
            "X-User-ID": user.id,
            "X-User-Tier": user.tier,
        }

        # Forward request with circuit breaker
        async with self.circuit_breaker(route.service):
            response = await self.http.request(
                method=request.method,
                url=internal_url,
                headers=headers,
                content=await request.body(),
                timeout=30,
            )

        return response
```

---

### FR-5: Response Caching

**As a** gateway
**I want** to cache responses
**So that** repeated requests are fast and reduce load

**Cache Strategy:**

| Endpoint Pattern | Cache Key | TTL | Invalidation |
|------------------|-----------|-----|--------------|
| `GET /v1/properties/{id}` | `cache:prop:{id}` | 1 hour | On refresh |
| `GET /v1/search/*` | `cache:search:{hash}` | 15 min | - |
| `GET /v1/predictions/*` | `cache:pred:{id}` | 24 hours | On retrain |
| `GET /v1/top-lists/*` | `cache:toplist:{strategy}` | 1 hour | Nightly |
| `POST /*` | No cache | - | - |

**Acceptance Criteria:**
- [ ] Redis-based response cache
- [ ] Cache key includes user tier (different results)
- [ ] `Cache-Control` headers in response
- [ ] `X-Cache: HIT/MISS` header
- [ ] Cache invalidation API (internal only)
- [ ] Stale-while-revalidate for degradation

**Implementation:**

```python
# gateway/cache/manager.py
class CacheManager:
    async def get_or_fetch(
        self,
        cache_key: str,
        ttl: int,
        fetch_fn: Callable,
    ) -> CacheResult:
        # Try cache
        cached = await self.redis.get(cache_key)
        if cached:
            return CacheResult(data=cached, hit=True)

        # Fetch from service
        response = await fetch_fn()

        # Cache if successful
        if response.status_code == 200:
            await self.redis.setex(cache_key, ttl, response.body)

        return CacheResult(data=response.body, hit=False)
```

---

### FR-6: API Versioning

**As a** API consumer
**I want** stable API versions
**So that** my integration doesn't break

**Versioning Strategy:**

- URL path versioning: `/v1/`, `/v2/`
- Current version: `v1`
- Deprecation notice: `Sunset` header
- Version support: N and N-1

**Acceptance Criteria:**
- [ ] Version prefix in all routes
- [ ] Default to latest version if not specified
- [ ] Deprecation headers for old versions
- [ ] Version changelog endpoint `/versions`
- [ ] Breaking changes only in major versions

---

### FR-7: Error Handling

**As a** client
**I want** consistent error responses
**So that** I can handle errors predictably

**Standard Error Format:**

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "You have exceeded your rate limit. Please try again later.",
    "details": {
      "limit": 10,
      "reset_at": "2026-01-18T15:00:00Z",
      "upgrade_to": "starter"
    }
  },
  "request_id": "req_abc123",
  "documentation_url": "https://docs.taxlien.online/errors/RATE_LIMIT_EXCEEDED"
}
```

**Error Codes:**

| HTTP Status | Error Code | Description |
|-------------|------------|-------------|
| 400 | `INVALID_REQUEST` | Malformed request |
| 401 | `UNAUTHORIZED` | Missing or invalid token |
| 403 | `FORBIDDEN` | Tier restriction |
| 403 | `RATE_LIMIT_EXCEEDED` | Too many requests |
| 404 | `NOT_FOUND` | Resource not found |
| 422 | `VALIDATION_ERROR` | Invalid parameters |
| 500 | `INTERNAL_ERROR` | Server error |
| 502 | `SERVICE_UNAVAILABLE` | Backend service down |
| 503 | `MAINTENANCE` | Planned maintenance |

**Acceptance Criteria:**
- [ ] All errors follow standard format
- [ ] Include `request_id` for debugging
- [ ] Include `documentation_url` for help
- [ ] Log all 5xx errors to Sentry
- [ ] Never expose internal stack traces

---

### FR-8: Observability

**As an** operator
**I want** comprehensive observability
**So that** I can monitor and debug the system

**Logging:**

```json
{
  "timestamp": "2026-01-18T14:32:00.123Z",
  "level": "INFO",
  "request_id": "req_abc123",
  "method": "GET",
  "path": "/v1/properties/123",
  "user_id": "user_456",
  "user_tier": "premium",
  "status": 200,
  "latency_ms": 45,
  "cache_hit": true,
  "service": "parser",
  "ip": "1.2.3.4",
  "user_agent": "TaxLienApp/1.0"
}
```

**Metrics (Prometheus):**

| Metric | Type | Labels |
|--------|------|--------|
| `gateway_requests_total` | Counter | method, path, status, tier |
| `gateway_request_duration_seconds` | Histogram | method, path, service |
| `gateway_cache_hits_total` | Counter | endpoint |
| `gateway_cache_misses_total` | Counter | endpoint |
| `gateway_rate_limit_hits_total` | Counter | tier |
| `gateway_circuit_breaker_state` | Gauge | service |
| `gateway_active_connections` | Gauge | - |

**Tracing:**

- OpenTelemetry spans for each request
- Propagate `X-Request-ID` to all services
- Trace: Gateway → Service → Database

**Acceptance Criteria:**
- [ ] Structured JSON logs to stdout
- [ ] Prometheus metrics endpoint `/metrics`
- [ ] Request tracing with correlation IDs
- [ ] Grafana dashboard for gateway
- [ ] Alerting on error rate > 1%

---

### FR-9: Internal API for Parser Workers (Port :8081)

**As a** distributed parser worker
**I want** to communicate only with Gateway's Internal API on a separate port
**So that** I can run on any machine without direct database access, with complete network isolation from public traffic

**Key Architectural Decision: Separate Port (:8081)**

| Aspect | Public API (:8080) | Internal API (:8081) |
|--------|-------------------|---------------------|
| Network | Public internet | VPN/Private network only |
| Authentication | Firebase/API Key | X-Worker-Token |
| Rate Limits | Tier-based | 1000 req/min per worker |
| Caching | Redis response cache | No caching |
| Middleware | CORS, Firebase, Rate Limit | Worker auth, IP whitelist |

**Architecture: Stateless Workers with Isolated Internal Port**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DISTRIBUTED PARSER ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │  Parser Worker  │  │  Parser Worker  │  │  Parser Worker  │             │
│  │  (Machine A)    │  │  (Machine B)    │  │  (Cloud VM)     │             │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘             │
│           │                    │                    │                       │
│           └────────────────────┼────────────────────┘                       │
│                                │                                            │
│                     Only 2 connections:                                     │
│                     1. Gateway Internal API (:8081)                         │
│                     2. External platforms (via tor-socks-proxy)             │
│                                │                                            │
│                                ▼                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                   INTERNAL API APP (:8081)                           │   │
│  │              internal-api.taxlien.local (VPN only)                   │   │
│  │                                                                      │   │
│  │   GET  /internal/work         ← Workers pull tasks                   │   │
│  │   POST /internal/results      ← Workers submit parsed data           │   │
│  │   POST /internal/tasks/{id}/* ← Workers report status                │   │
│  │   POST /internal/raw-files    ← Workers upload raw HTML              │   │
│  │   POST /internal/heartbeat    ← Workers status pulse                 │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│              Gateway manages all storage (SHARED with Public API):          │
│                                    │                                        │
│       ┌────────────────────────────┼────────────────────────────┐          │
│       ▼                            ▼                            ▼          │
│  ┌─────────────┐           ┌─────────────┐           ┌─────────────┐       │
│  │ PostgreSQL  │           │    Redis    │           │  /data/raw  │       │
│  │ (parcels)   │           │(queue/cache)│           │  (storage)  │       │
│  └─────────────┘           └─────────────┘           └─────────────┘       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Internal API Endpoints:**

#### Work Distribution

```python
@app.get("/internal/work")
async def get_work(
    worker_id: str,                    # Unique worker identifier
    capacity: int = 10,                # How many tasks can handle
    platforms: List[str] = None,       # Which platforms worker supports
    max_tier: int = 4,                 # Max scraper tier (1=HTTP, 4=Selenium)
) -> WorkResponse:
    """
    Parser requests work when idle (PULL model).

    Gateway selects tasks based on:
    - Priority (urgent > high > normal > low)
    - Proxy availability for platform
    - Worker capabilities
    - Load balancing across workers

    Returns:
    - tasks: List of work items
    - retry_after: Seconds to wait if no work available
    """
    pass

# Response
class WorkResponse(BaseModel):
    tasks: List[WorkTask]
    retry_after: int = 30

class WorkTask(BaseModel):
    task_id: str
    platform: str           # beacon, qpublic, floridatax
    state: str
    county: str
    parcel_id: str
    priority: int           # 1=urgent, 2=high, 3=normal, 4=low
    url: Optional[str]      # Pre-computed URL if available
    proxy: ProxyInfo        # Assigned proxy for this task
```

#### Data Submission

```python
@app.post("/internal/results")
async def submit_results(
    worker_id: str,
    results: List[ParcelResult],
) -> SubmitResponse:
    """
    Worker submits parsed parcel data.
    Gateway batch-inserts into PostgreSQL.
    """
    pass

class ParcelResult(BaseModel):
    task_id: str
    parcel_id: str
    platform: str
    state: str
    county: str
    data: Dict[str, Any]              # 90+ parsed attributes
    scraped_at: datetime
    parse_duration_ms: int
    raw_html_hash: Optional[str]      # If raw storage enabled

class SubmitResponse(BaseModel):
    inserted: int
    updated: int
    failed: int
    errors: List[str]
```

#### Raw File Upload

```python
@app.post("/internal/raw-files")
async def upload_raw_files(
    worker_id: str,
    files: List[RawFileUpload],
) -> UploadResponse:
    """
    Worker uploads raw HTML files for storage.
    Gateway saves to /data/raw/ or S3.
    """
    pass

class RawFileUpload(BaseModel):
    task_id: str
    parcel_id: str
    platform: str
    content_base64: str               # gzip + base64 encoded HTML
    content_hash: str                 # sha256 for deduplication
    metadata: RawFileMetadata
```

#### Task Status

```python
@app.post("/internal/tasks/{task_id}/complete")
async def complete_task(
    task_id: str,
    worker_id: str,
    metrics: TaskMetrics,
) -> None:
    """Mark task as completed."""
    pass

@app.post("/internal/tasks/{task_id}/fail")
async def fail_task(
    task_id: str,
    worker_id: str,
    error: FailureInfo,
) -> RetryInfo:
    """
    Report task failure.
    Gateway decides: retry, requeue, or dead-letter.
    """
    pass

class FailureInfo(BaseModel):
    reason: FailureReason             # platform_down, blocked, parser_bug, etc.
    message: str
    proxy_port: Optional[int]         # If proxy was banned
    retry_suggested: bool = True

class RetryInfo(BaseModel):
    should_retry: bool
    retry_after: Optional[int]        # Seconds
    new_proxy: Optional[ProxyInfo]    # If proxy was rotated
```

#### Proxy Management

```python
@app.get("/internal/proxy/create")
async def create_proxy(
    worker_id: str,
    platform: str,
) -> ProxyInfo:
    """
    Get a proxy for platform.
    Gateway manages pool and tracks bans per platform.
    """
    pass

@app.post("/internal/proxy/{port}/rotate")
async def rotate_proxy(
    port: int,
    worker_id: str,
    reason: str,                      # banned, slow, error
    platform: str,
) -> ProxyInfo:
    """
    Replace banned/slow proxy.
    Gateway marks old proxy as banned for this platform.
    """
    pass

@app.post("/internal/proxy/{port}/ban")
async def ban_proxy(
    port: int,
    worker_id: str,
    platform: str,
    reason: str,
    duration_minutes: int = 60,
) -> None:
    """Explicitly ban proxy for platform."""
    pass

class ProxyInfo(BaseModel):
    host: str
    port: int
    type: str = "socks5"
    expires_at: Optional[datetime]    # When proxy lease expires
```

#### Worker Heartbeat

```python
@app.post("/internal/heartbeat")
async def worker_heartbeat(
    worker_id: str,
    status: WorkerStatus,
) -> HeartbeatResponse:
    """
    Worker sends periodic heartbeat.
    Gateway tracks active workers for dashboard.
    """
    pass

class WorkerStatus(BaseModel):
    active_tasks: int
    completed_last_minute: int
    failed_last_minute: int
    platforms: List[str]
    cpu_percent: float
    memory_percent: float

class HeartbeatResponse(BaseModel):
    acknowledged: bool
    commands: List[str]               # shutdown, pause, config_update, etc.
```

**Authentication for Internal API:**

| Endpoint | Auth Method | Token |
|----------|-------------|-------|
| `/internal/*` | X-Worker-Token | Per-worker token |
| Rate limit | 1000 req/min per worker | - |
| IP whitelist | Optional | VPN/known IPs |

**Acceptance Criteria:**

- [ ] Workers can pull work without direct DB access
- [ ] Workers submit results via Gateway
- [ ] Gateway batch-writes to PostgreSQL
- [ ] Proxy pool managed centrally by Gateway
- [ ] Worker heartbeats tracked for dashboard
- [ ] Dead workers detected (no heartbeat > 5 min)
- [ ] Tasks from dead workers requeued automatically
- [ ] Raw files uploaded via Gateway (not direct to storage)

---

### FR-10: CI/CD Pipeline

**As a** developer
**I want** automated build and deployment
**So that** changes are safely and reliably delivered to production

**Workflow:**
1. **Pull Request:**
   - Run unit tests
   - Run linting (ruff, mypy)
   - Build Docker image (check for errors)

2. **Push to Main:**
   - Run all tests
   - Build Docker image
   - Push to Container Registry (GHCR)
   - Deploy to Dev/Staging Environment

3. **Release Tag:**
   - Build production image
   - Push to Container Registry
   - Update Kubernetes manifests / Helm chart

**Acceptance Criteria:**
- [ ] GitHub Actions workflow file (`.github/workflows/gateway-ci.yml`)
- [ ] Build and test steps passing
- [ ] Docker image creation and pushing
- [ ] Secrets management for registry/deployment

---

### FR-11: Monitoring Dashboards

**As an** operator
**I want** visual dashboards for the system state
**So that** I can monitor health, workers, and business metrics in real-time

**Dashboard Sections:**
1.  **System Health:** RPS, Error Rates, P95 Latency.
2.  **Worker Fleet:** Active workers per platform, Task throughput.
3.  **Queue State:** Depth by priority, processing lag.
4.  **Proxy Health:** Availability vs Ban rate per platform.
5.  **Business/API:** Usage by Tier, Rate limit hits, Cache efficiency.

**Acceptance Criteria:**
- [ ] Grafana Dashboard JSON files provided in the codebase.
- [ ] Dashboards cover all 5 specified sections.
- [ ] Automated provisioning of dashboards in Grafana.

---

### FR-12: Specialized Investment Endpoints (Miw Gift Flow)

**As an** investment strategist (Miw/Shon)
**I want** specialized endpoints to filter for specific high-value opportunities
**So that** I can execute the "Staircase Strategy" efficiently

**Context:** These endpoints support `flows/sdd-miw-gift/` - investment plan with $1,000 budget for Feb 2026 Arizona auction.

**New Endpoints:**

| Endpoint | Purpose | Criteria |
|----------|---------|----------|
| `GET /api/v1/liens/foreclosure-candidates` | Find liens likely to foreclose | `prior_years >= 2`, `foreclosure_prob > 0.6` |
| `GET /api/v1/liens/otc` | Find Over-The-Counter liens | `is_otc = true`, `state = {state}` |
| `GET /api/v1/liens/search` | Advanced search with multiple criteria | Multiple filters (see below) |
| `GET /api/v1/export/csv` | Bulk export for offline analysis | Returns CSV file |

**Endpoint Details:**

**1. Foreclosure Candidates (`GET /api/v1/liens/foreclosure-candidates`)**

Query Parameters:
- `state` (required): State code (e.g., "AZ", "UT", "SD")
- `prior_years_min` (optional, default=2): Minimum years of delinquency
- `max_amount` (optional): Maximum lien amount (e.g., 500 for Miw's budget)
- `foreclosure_prob_min` (optional, default=0.6): Minimum foreclosure probability
- `redemption_prob_max` (optional): Maximum redemption probability
- `county` (optional): Filter by county
- `limit` (optional, default=100): Max results

Example:
```
GET /api/v1/liens/foreclosure-candidates?state=AZ&prior_years_min=2&max_amount=500&foreclosure_prob_min=0.7
```

Response includes: `parcel_id`, `county`, `address`, `lien_amount`, `market_value`, `prior_years_owed`, `foreclosure_probability`, `redemption_probability`, `miw_score`, `karma_score`, `property_type`, `owner_name`

**2. OTC Liens (`GET /api/v1/liens/otc`)**

Query Parameters:
- `state` (required): State code
- `county` (optional): Filter by county
- `available_now` (optional, default=true): Only liens available for immediate purchase
- `prior_years_min` (optional): Minimum years old
- `max_amount` (optional): Maximum lien amount
- `limit` (optional, default=100): Max results

Example:
```
GET /api/v1/liens/otc?state=AZ&available_now=true&prior_years_min=2&max_amount=500
```

**3. Advanced Search (`GET /api/v1/liens/search`)**

Query Parameters:
- `state` (required): State code
- `county` (optional): County name
- `prior_years_min` (optional): Minimum years of delinquency
- `max_amount` (optional): Maximum lien amount
- `min_market_value` (optional): Minimum property value
- `property_type` (optional): "RESIDENTIAL", "LOT", "COMMERCIAL"
- `foreclosure_prob_min` (optional): Minimum foreclosure probability
- `redemption_prob_max` (optional): Maximum redemption probability
- `serial_payer_score_min` (optional): Minimum serial payer score
- `karma_score_min` (optional): Minimum karma score (ethical filtering)
- `sort_by` (optional): "miw_score", "foreclosure_prob", "lien_amount", "market_value"
- `order` (optional): "asc", "desc" (default="desc")
- `limit` (optional, default=100): Max results
- `offset` (optional, default=0): Pagination offset

Example (Miw's criteria):
```
GET /api/v1/liens/search?state=AZ&prior_years_min=2&max_amount=500&foreclosure_prob_min=0.6&sort_by=miw_score&limit=20
```

**4. CSV Export (`GET /api/v1/export/csv`)**

Query Parameters: Same as `/api/v1/liens/search`

Response: CSV file with headers:
```
parcel_id, county, state, address, lien_amount, market_value,
prior_years_owed, struck_off_date, property_type, owner_name,
assessed_value, auction_date, foreclosure_probability, redemption_probability,
miw_score, karma_score, serial_payer_score, platform, scraped_at
```

**Acceptance Criteria:**
- [ ] Foreclosure candidates endpoint supports all filters above
- [ ] OTC endpoint supports state/county filtering and `available_now` flag
- [ ] Search endpoint supports all Miw criteria filters
- [ ] CSV export includes all required columns (`miw_score`, `karma_score`, `foreclosure_probability`)
- [ ] Rate limit bypass for internal users (Miw/Shon/Admin) via `X-Internal-User` header
- [ ] All endpoints return consistent error format
- [ ] Pagination support for large result sets
- [ ] Response time < 500ms for filtered queries (with indexes)

---

## Non-Functional Requirements

### Performance

| Metric | Target | Acceptable |
|--------|--------|------------|
| P50 latency (cache hit) | < 10ms | < 50ms |
| P50 latency (cache miss) | < 100ms | < 300ms |
| P99 latency | < 500ms | < 1s |
| Throughput | 1000 req/s | 500 req/s |
| Availability | 99.9% | 99.5% |

### Scalability

- Horizontal scaling (stateless design)
- Redis cluster for rate limiting/caching
- Auto-scaling based on CPU/connections

### Security

- [ ] HTTPS only (redirect HTTP → HTTPS)
- [ ] HSTS headers
- [ ] CORS configuration
- [ ] Request size limits (10MB max)
- [ ] SQL injection protection (parameterized)
- [ ] XSS protection headers
- [ ] Rate limiting per IP
- [ ] API key rotation support

---

## Testing Requirements

### Test Coverage Policy

**ВАЖНО: Тесты пишутся ОДНОВРЕМЕННО с кодом, не после.**

| Component | Coverage Target | Test Type |
|-----------|-----------------|-----------|
| Authentication | 100% | Unit + Integration |
| Authorization | 100% | Unit + Integration |
| Rate Limiting | 95%+ | Unit + Load |
| Routing | 100% | Integration |
| Caching | 90%+ | Unit + Integration |
| Error Handling | 100% | Unit |

### Test Examples

```python
# tests/integration/test_auth.py
async def test_firebase_token_valid():
    """Valid Firebase token grants access."""
    token = create_test_firebase_token(user_id="123", tier="premium")
    response = await client.get("/v1/properties/abc", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

async def test_expired_token_returns_401():
    """Expired token returns 401."""
    token = create_expired_token()
    response = await client.get("/v1/properties/abc", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "UNAUTHORIZED"

# tests/integration/test_rate_limit.py
async def test_rate_limit_exceeded():
    """Exceeding rate limit returns 429."""
    for _ in range(11):  # Free tier = 10/min
        await client.get("/v1/properties/abc", headers=free_user_headers)

    response = await client.get("/v1/properties/abc", headers=free_user_headers)
    assert response.status_code == 429
    assert "Retry-After" in response.headers
```

---

## Tech Stack

### Option A: Custom FastAPI Gateway (Recommended for MVP)

**Pros:**
- Full control over logic
- Python ecosystem (matches other services)
- Easy to extend

**Cons:**
- More code to write
- Need to implement patterns manually

```
FastAPI + Starlette
├── uvicorn (ASGI server)
├── httpx (async HTTP client)
├── redis (rate limiting, caching)
├── firebase-admin (token validation)
├── prometheus-client (metrics)
└── opentelemetry (tracing)
```

### Option B: Kong Gateway

**Pros:**
- Battle-tested, production-ready
- Plugins for auth, rate limiting, etc.
- Admin API

**Cons:**
- Learning curve
- May be overkill for our scale
- Less flexibility for custom logic

### Option C: Traefik

**Pros:**
- Docker-native
- Auto-discovery
- Middleware support

**Cons:**
- Less flexible for custom auth
- Configuration complexity

**Recommendation:** Start with **FastAPI** for control and simplicity, migrate to Kong if scale requires.

---

## Dependencies

### Internal Dependencies

| Service | Purpose | Endpoints Used |
|---------|---------|----------------|
| Parser Service | Property data | `/api/v1/properties/*`, `/api/v1/search/*` |
| ML Service | Predictions | `/api/v1/predict/*`, `/api/v1/top-lists/*` |

### External Dependencies

| Service | Purpose |
|---------|---------|
| Firebase Auth | Token validation |
| Redis | Rate limiting, caching |
| Prometheus | Metrics collection |
| Sentry | Error tracking |

---

## Deployment

### Docker Compose (Development) - Dual Port Architecture

```yaml
services:
  gateway:
    build: ./gateway
    ports:
      - "8080:8080"    # Public API (exposed to internet via nginx/cloudflare)
      - "8081:8081"    # Internal API (VPN/private network only)
    environment:
      - GATEWAY_POSTGRES_URL=postgresql://user:pass@postgres:5432/taxlien
      - GATEWAY_REDIS_URL=redis://redis:6379
      - GATEWAY_FIREBASE_PROJECT_ID=taxlien-online
      - GATEWAY_SSR_SERVICE_TOKEN=${SSR_TOKEN}
      - GATEWAY_WORKER_TOKENS=${WORKER_TOKENS}
      - GATEWAY_RAW_STORAGE_PATH=/data/raw
      - GATEWAY_PUBLIC_PORT=8080
      - GATEWAY_INTERNAL_PORT=8081
    volumes:
      - raw_storage:/data/raw
    depends_on:
      - postgres
      - redis
    networks:
      - public      # Port 8080 accessible
      - internal    # Port 8081 accessible

  postgres:
    image: postgres:16-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=taxlien
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - internal

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    networks:
      - internal

  # Parser workers connect only to internal network
  parser-worker:
    build: ./parser-worker
    environment:
      - GATEWAY_INTERNAL_URL=http://gateway:8081
      - WORKER_TOKEN=${WORKER_TOKEN_1}
    networks:
      - internal    # Only internal network access
    deploy:
      replicas: 4

networks:
  public:
    driver: bridge
  internal:
    driver: bridge
    internal: true  # No external access

volumes:
  postgres_data:
  redis_data:
  raw_storage:
```

### Production - Kubernetes with Network Policies

```yaml
# Two separate Services for the same Deployment
apiVersion: v1
kind: Service
metadata:
  name: gateway-public
spec:
  type: LoadBalancer
  ports:
    - port: 80
      targetPort: 8080
  selector:
    app: gateway
---
apiVersion: v1
kind: Service
metadata:
  name: gateway-internal
spec:
  type: ClusterIP  # Internal only
  ports:
    - port: 8081
      targetPort: 8081
  selector:
    app: gateway
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: gateway-internal-only
spec:
  podSelector:
    matchLabels:
      app: gateway
  ingress:
    - from:
        - podSelector:
            matchLabels:
              role: parser-worker
      ports:
        - port: 8081
```

**Key Points:**
- Port 8080 behind Cloudflare/nginx with SSL termination
- Port 8081 accessible only from internal network/VPN
- Kubernetes NetworkPolicy restricts :8081 to parser-worker pods only
- HPA scales based on both ports' metrics

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Uptime | 99.9% | Prometheus + PagerDuty |
| P99 latency | < 500ms | Prometheus histogram |
| Error rate | < 0.1% | Prometheus counter |
| Cache hit rate | > 60% | Prometheus counter |
| Auth success rate | > 99% | Prometheus counter |

---

## Risks & Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Redis failure | High | Low | Redis Sentinel/Cluster |
| Firebase outage | High | Low | Token cache, graceful degradation |
| DDoS attack | High | Medium | Cloudflare, per-IP limits |
| Service cascade failure | High | Medium | Circuit breakers, timeouts |
| Token leakage | Critical | Low | Short TTL, rotation, monitoring |

---

## Next Steps

1. **SPECIFICATIONS Phase:**
   - OpenAPI spec for all endpoints
   - Detailed auth flow diagrams
   - Redis schema design
   - Deployment architecture

2. **PLAN Phase:**
   - Implementation tasks breakdown
   - Integration testing plan
   - Load testing plan
   - Migration strategy (if existing)

3. **IMPLEMENTATION Phase:**
   - Week 1: Core routing, auth, rate limiting
   - Week 2: Caching, error handling
   - Week 3: Observability, testing
   - Week 4: Load testing, deployment

---

**Status:** REQUIREMENTS DRAFT
**Next Phase:** SPECIFICATIONS
**Owner:** Platform Team
