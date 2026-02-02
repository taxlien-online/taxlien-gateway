# Requirements: API Gateway - Unified Entry Point

**Version:** 2.0 (Go Rewrite)
**Status:** REQUIREMENTS PHASE - DRAFTING
**Last Updated:** 2026-02-01
**Goal:** Single entry point for all external clients to access TAXLIEN.online services
**Tech Stack:** Go 1.22+ (Chi router, pgx, go-redis)

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

### Internal Service Architecture (Go)

```
taxlien-gateway/
├── cmd/
│   └── gateway/
│       └── main.go                  # Entry point: runs TRI-PORT servers
├── internal/
│   ├── config/
│   │   └── config.go                # Viper-based configuration
│   ├── server/
│   │   ├── public.go                # Public API server (:8080)
│   │   ├── parcel.go                # Internal Parcel API (:8081)
│   │   └── party.go                 # Internal Party API (:8082)
│   ├── handler/
│   │   ├── public/                  # /v1/* handlers
│   │   │   ├── properties.go
│   │   │   ├── search.go
│   │   │   ├── predictions.go
│   │   │   ├── usage.go
│   │   │   └── liens.go             # FR-12: Miw endpoints
│   │   └── internal/                # /internal/* handlers
│   │       ├── work.go              # Worker task distribution
│   │       ├── results.go           # Data submission
│   │       ├── tasks.go             # Task status management
│   │       ├── heartbeat.go         # Worker heartbeat
│   │       └── proxy.go             # Proxy management
│   ├── middleware/
│   │   ├── auth.go                  # Firebase/API Key auth
│   │   ├── ratelimit.go             # Token bucket rate limiting
│   │   ├── cache.go                 # Response caching
│   │   ├── cors.go                  # CORS handling
│   │   ├── logging.go               # Structured logging
│   │   ├── requestid.go             # Request ID injection
│   │   └── worker.go                # Worker token validation
│   ├── service/
│   │   ├── auth.go                  # Authentication logic
│   │   ├── authz.go                 # Authorization (tiers)
│   │   ├── queue.go                 # Redis task queue
│   │   ├── properties.go            # Property CRUD
│   │   ├── liens.go                 # FR-12: Lien queries
│   │   └── worker.go                # Worker registry
│   ├── model/
│   │   ├── user.go
│   │   ├── task.go
│   │   ├── parcel.go
│   │   ├── lien.go                  # FR-12: Lien model
│   │   └── error.go                 # Standard error format
│   └── pkg/
│       ├── db/
│       │   └── postgres.go          # pgx connection pool
│       ├── cache/
│       │   └── redis.go             # go-redis client
│       └── metrics/
│           └── prometheus.go        # Metrics collection
├── api/
│   └── openapi.yaml                 # OpenAPI 3.0 specification
├── migrations/
│   └── *.sql                        # SQL migrations
├── Dockerfile
├── docker-compose.yml
├── go.mod
├── go.sum
├── Makefile
└── README.md
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

**Implementation (Go):**

```go
// internal/service/auth.go
type Authenticator struct {
    firebaseApp    *firebase.App
    ssrToken       string
    apiKeyStore    *APIKeyStore
    tokenCache     *cache.Cache
}

func (a *Authenticator) Authenticate(r *http.Request) (*AuthResult, error) {
    // 1. Check for Firebase token
    if authHeader := r.Header.Get("Authorization"); authHeader != "" {
        if strings.HasPrefix(authHeader, "Bearer ") {
            token := authHeader[7:]
            return a.validateFirebaseToken(r.Context(), token)
        }
    }

    // 2. Check for SSR service token
    if ssrToken := r.Header.Get("X-SSR-Token"); ssrToken != "" {
        return a.validateSSRToken(ssrToken)
    }

    // 3. Check for API key
    if apiKey := r.Header.Get("X-API-Key"); apiKey != "" {
        return a.validateAPIKey(r.Context(), apiKey)
    }

    // 4. Anonymous
    return &AuthResult{Authenticated: false, User: nil, Tier: "anonymous"}, nil
}
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

**Implementation (Go):**

```go
// internal/service/authz.go
var TierLimits = map[string]map[string]int{
    "anonymous":  {"search": 5, "details": 10, "predictions": 0},
    "free":       {"search": 10, "details": 20, "predictions": 3},
    "starter":    {"search": -1, "details": -1, "predictions": 10}, // -1 = unlimited
    "premium":    {"search": -1, "details": -1, "predictions": -1},
    "enterprise": {"search": -1, "details": -1, "predictions": -1},
}

type Authorizer struct {
    redis *redis.Client
}

func (a *Authorizer) Authorize(ctx context.Context, user *User, action string) (*AuthzResult, error) {
    tierLimits, ok := TierLimits[user.Tier]
    if !ok {
        return &AuthzResult{Allowed: false, Reason: "unknown_tier"}, nil
    }

    limit, ok := tierLimits[action]
    if !ok || limit == 0 {
        return &AuthzResult{Allowed: false, Reason: "tier_restriction"}, nil
    }
    if limit == -1 {
        return &AuthzResult{Allowed: true}, nil
    }

    key := fmt.Sprintf("usage:%s:%s:%s", user.ID, action, time.Now().Format("2006-01-02"))
    usage, _ := a.redis.Get(ctx, key).Int()

    if usage >= limit {
        return &AuthzResult{Allowed: false, Reason: "limit_exceeded", UpgradeTo: "starter"}, nil
    }

    return &AuthzResult{Allowed: true, Remaining: limit - usage - 1}, nil
}
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

**Implementation (Go):**

```go
// internal/middleware/ratelimit.go
type RateLimiter struct {
    redis  *redis.Client
    limits map[string]RateLimitConfig
}

type RateLimitConfig struct {
    Rate  float64 // tokens per second
    Burst float64 // max tokens
}

func (rl *RateLimiter) Check(ctx context.Context, identifier, tier string) (*RateLimitResult, error) {
    key := fmt.Sprintf("ratelimit:%s", identifier)
    config := rl.limits[tier]

    now := float64(time.Now().Unix())

    // Get current state from Redis
    vals, _ := rl.redis.HMGet(ctx, key, "tokens", "updated").Result()

    var tokens, lastUpdate float64
    if vals[0] != nil {
        tokens, _ = strconv.ParseFloat(vals[0].(string), 64)
    } else {
        tokens = config.Burst
    }
    if vals[1] != nil {
        lastUpdate, _ = strconv.ParseFloat(vals[1].(string), 64)
    } else {
        lastUpdate = now
    }

    // Refill tokens
    elapsed := now - lastUpdate
    tokens = math.Min(config.Burst, tokens+elapsed*config.Rate)

    if tokens < 1 {
        retryAfter := int((1 - tokens) / config.Rate)
        return &RateLimitResult{Allowed: false, RetryAfter: retryAfter}, nil
    }

    // Consume token
    rl.redis.HSet(ctx, key, "tokens", tokens-1, "updated", now)
    rl.redis.Expire(ctx, key, time.Hour)

    return &RateLimitResult{Allowed: true, Remaining: int(tokens - 1)}, nil
}
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

**Implementation (Go):**

```go
// internal/handler/public/router.go
type RouteConfig struct {
    Pattern      string
    Methods      []string
    Service      string
    InternalPath string
    CacheTTL     time.Duration
}

var Routes = []RouteConfig{
    {
        Pattern:      "/v1/properties/{parcelID}",
        Methods:      []string{"GET"},
        Service:      "parser",
        InternalPath: "/api/v1/properties/{parcelID}",
        CacheTTL:     time.Hour,
    },
    {
        Pattern:      "/v1/predictions/batch",
        Methods:      []string{"POST"},
        Service:      "ml",
        InternalPath: "/api/v1/predict/batch",
        CacheTTL:     0, // No cache for POST
    },
}

func (h *Handler) ProxyRequest(w http.ResponseWriter, r *http.Request, route RouteConfig, user *User) {
    // Build internal request
    internalURL := h.services[route.Service] + route.InternalPath

    req, _ := http.NewRequestWithContext(r.Context(), r.Method, internalURL, r.Body)
    req.Header.Set("X-Service-Token", h.serviceToken)
    req.Header.Set("X-Request-ID", middleware.GetReqID(r.Context()))
    req.Header.Set("X-User-ID", user.ID)
    req.Header.Set("X-User-Tier", user.Tier)

    // Forward with circuit breaker
    resp, err := h.circuitBreaker.Execute(route.Service, func() (*http.Response, error) {
        return h.httpClient.Do(req)
    })
    if err != nil {
        http.Error(w, "Service unavailable", http.StatusBadGateway)
        return
    }
    defer resp.Body.Close()

    // Copy response
    for k, v := range resp.Header {
        w.Header()[k] = v
    }
    w.WriteHeader(resp.StatusCode)
    io.Copy(w, resp.Body)
}
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

**Implementation (Go):**

```go
// internal/middleware/cache.go
type CacheManager struct {
    redis *redis.Client
}

type CacheResult struct {
    Data []byte
    Hit  bool
}

func (c *CacheManager) GetOrFetch(ctx context.Context, key string, ttl time.Duration, fetchFn func() ([]byte, int, error)) (*CacheResult, error) {
    // Try cache
    cached, err := c.redis.Get(ctx, key).Bytes()
    if err == nil {
        return &CacheResult{Data: cached, Hit: true}, nil
    }

    // Fetch from service
    data, statusCode, err := fetchFn()
    if err != nil {
        return nil, err
    }

    // Cache if successful
    if statusCode == http.StatusOK {
        c.redis.Set(ctx, key, data, ttl)
    }

    return &CacheResult{Data: data, Hit: false}, nil
}
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

**Internal API Endpoints (Go):**

#### Work Distribution

```go
// internal/handler/internal/work.go

// GET /internal/work
func (h *Handler) GetWork(w http.ResponseWriter, r *http.Request) {
    workerID := r.URL.Query().Get("worker_id")
    capacity, _ := strconv.Atoi(r.URL.Query().Get("capacity"))
    if capacity == 0 {
        capacity = 10
    }
    platforms := r.URL.Query()["platforms"]
    maxTier, _ := strconv.Atoi(r.URL.Query().Get("max_tier"))
    if maxTier == 0 {
        maxTier = 4
    }

    tasks, err := h.queueService.FetchTasks(r.Context(), workerID, capacity, platforms)
    if err != nil {
        respondError(w, http.StatusInternalServerError, err)
        return
    }

    respond(w, http.StatusOK, WorkResponse{
        Tasks:      tasks,
        RetryAfter: 30,
    })
}

// Models
type WorkResponse struct {
    Tasks      []WorkTask `json:"tasks"`
    RetryAfter int        `json:"retry_after"`
}

type WorkTask struct {
    TaskID   string     `json:"task_id"`
    Platform string     `json:"platform"`
    State    string     `json:"state"`
    County   string     `json:"county"`
    ParcelID string     `json:"parcel_id"`
    Priority int        `json:"priority"`
    URL      string     `json:"url,omitempty"`
    Proxy    *ProxyInfo `json:"proxy,omitempty"`
}
```

#### Data Submission

```go
// internal/handler/internal/results.go

// POST /internal/results
func (h *Handler) SubmitResults(w http.ResponseWriter, r *http.Request) {
    var req struct {
        WorkerID string         `json:"worker_id"`
        Results  []ParcelResult `json:"results"`
    }
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
        respondError(w, http.StatusBadRequest, err)
        return
    }

    result, err := h.propertyService.BatchUpsert(r.Context(), req.Results)
    if err != nil {
        respondError(w, http.StatusInternalServerError, err)
        return
    }

    respond(w, http.StatusOK, result)
}

type ParcelResult struct {
    TaskID          string                 `json:"task_id"`
    ParcelID        string                 `json:"parcel_id"`
    Platform        string                 `json:"platform"`
    State           string                 `json:"state"`
    County          string                 `json:"county"`
    Data            map[string]interface{} `json:"data"`
    ScrapedAt       time.Time              `json:"scraped_at"`
    ParseDurationMs int                    `json:"parse_duration_ms"`
    RawHTMLHash     string                 `json:"raw_html_hash,omitempty"`
}

type SubmitResponse struct {
    Inserted int      `json:"inserted"`
    Updated  int      `json:"updated"`
    Failed   int      `json:"failed"`
    Errors   []string `json:"errors"`
}
```

#### Task Status

```go
// internal/handler/internal/tasks.go

// POST /internal/tasks/{taskID}/complete
func (h *Handler) CompleteTask(w http.ResponseWriter, r *http.Request) {
    taskID := chi.URLParam(r, "taskID")

    var req struct {
        WorkerID string      `json:"worker_id"`
        Metrics  TaskMetrics `json:"metrics"`
    }
    json.NewDecoder(r.Body).Decode(&req)

    if err := h.queueService.CompleteTask(r.Context(), taskID, req.WorkerID, req.Metrics); err != nil {
        respondError(w, http.StatusInternalServerError, err)
        return
    }

    respond(w, http.StatusOK, map[string]string{"status": "ok"})
}

// POST /internal/tasks/{taskID}/fail
func (h *Handler) FailTask(w http.ResponseWriter, r *http.Request) {
    taskID := chi.URLParam(r, "taskID")

    var req struct {
        WorkerID string      `json:"worker_id"`
        Error    FailureInfo `json:"error"`
    }
    json.NewDecoder(r.Body).Decode(&req)

    retryInfo, err := h.queueService.HandleFailure(r.Context(), taskID, req.WorkerID, req.Error)
    if err != nil {
        respondError(w, http.StatusInternalServerError, err)
        return
    }

    respond(w, http.StatusOK, retryInfo)
}

type FailureInfo struct {
    Reason         string `json:"reason"`
    Message        string `json:"message"`
    ProxyPort      int    `json:"proxy_port,omitempty"`
    RetrySuggested bool   `json:"retry_suggested"`
}

type RetryInfo struct {
    ShouldRetry bool       `json:"should_retry"`
    RetryAfter  int        `json:"retry_after,omitempty"`
    NewProxy    *ProxyInfo `json:"new_proxy,omitempty"`
    MovedToDLQ  bool       `json:"moved_to_dlq"`
}
```

#### Worker Heartbeat

```go
// internal/handler/internal/heartbeat.go

// POST /internal/heartbeat
func (h *Handler) Heartbeat(w http.ResponseWriter, r *http.Request) {
    var req struct {
        WorkerID string       `json:"worker_id"`
        Status   WorkerStatus `json:"status"`
    }
    json.NewDecoder(r.Body).Decode(&req)

    commands, err := h.workerRegistry.Update(r.Context(), req.WorkerID, req.Status)
    if err != nil {
        respondError(w, http.StatusInternalServerError, err)
        return
    }

    respond(w, http.StatusOK, HeartbeatResponse{
        Acknowledged: true,
        Commands:     commands,
    })
}

type WorkerStatus struct {
    ActiveTasks          int      `json:"active_tasks"`
    CompletedLastMinute  int      `json:"completed_last_minute"`
    FailedLastMinute     int      `json:"failed_last_minute"`
    Platforms            []string `json:"platforms"`
    CPUPercent           float64  `json:"cpu_percent"`
    MemoryPercent        float64  `json:"memory_percent"`
}

type HeartbeatResponse struct {
    Acknowledged bool     `json:"acknowledged"`
    Commands     []string `json:"commands"`
}

type ProxyInfo struct {
    Host      string     `json:"host"`
    Port      int        `json:"port"`
    Type      string     `json:"type"`
    ExpiresAt *time.Time `json:"expires_at,omitempty"`
}
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

### Test Examples (Go)

```go
// internal/handler/public/properties_test.go
func TestFirebaseTokenValid(t *testing.T) {
    // Setup test server
    srv := setupTestServer(t)
    defer srv.Close()

    // Create valid test token
    token := createTestFirebaseToken(t, "123", "premium")

    req, _ := http.NewRequest("GET", srv.URL+"/v1/properties/abc", nil)
    req.Header.Set("Authorization", "Bearer "+token)

    resp, err := http.DefaultClient.Do(req)
    require.NoError(t, err)
    assert.Equal(t, http.StatusOK, resp.StatusCode)
}

func TestExpiredTokenReturns401(t *testing.T) {
    srv := setupTestServer(t)
    defer srv.Close()

    token := createExpiredToken(t)

    req, _ := http.NewRequest("GET", srv.URL+"/v1/properties/abc", nil)
    req.Header.Set("Authorization", "Bearer "+token)

    resp, err := http.DefaultClient.Do(req)
    require.NoError(t, err)
    assert.Equal(t, http.StatusUnauthorized, resp.StatusCode)

    var errResp ErrorResponse
    json.NewDecoder(resp.Body).Decode(&errResp)
    assert.Equal(t, "UNAUTHORIZED", errResp.Error.Code)
}

// internal/middleware/ratelimit_test.go
func TestRateLimitExceeded(t *testing.T) {
    srv := setupTestServer(t)
    defer srv.Close()

    headers := freeUserHeaders(t)

    // Exhaust rate limit (free tier = 10/min)
    for i := 0; i < 11; i++ {
        req, _ := http.NewRequest("GET", srv.URL+"/v1/properties/abc", nil)
        for k, v := range headers {
            req.Header.Set(k, v)
        }
        http.DefaultClient.Do(req)
    }

    // Next request should be rate limited
    req, _ := http.NewRequest("GET", srv.URL+"/v1/properties/abc", nil)
    for k, v := range headers {
        req.Header.Set(k, v)
    }

    resp, err := http.DefaultClient.Do(req)
    require.NoError(t, err)
    assert.Equal(t, http.StatusTooManyRequests, resp.StatusCode)
    assert.NotEmpty(t, resp.Header.Get("Retry-After"))
}
```

### Running Tests

```bash
# Run all tests
go test ./...

# Run with coverage
go test -cover ./...

# Run integration tests only
go test -tags=integration ./...

# Run with race detector
go test -race ./...
```

---

## Tech Stack

### Selected: Go (Chi Router) - Production Grade

**Decision (2026-02-01):** Переход с Python/FastAPI на Go для:
- Лучшая производительность (10x меньше latency)
- Единый бинарник (простой deploy)
- Меньше memory footprint
- Отличная поддержка concurrency (goroutines)

```
Go 1.22+
├── chi (HTTP router)
├── pgx (PostgreSQL driver)
├── go-redis (Redis client)
├── firebase-admin-go (token validation)
├── prometheus/client_golang (metrics)
├── otel (OpenTelemetry tracing)
├── zap (structured logging)
└── viper (configuration)
```

**Project Structure:**
```
taxlien-gateway/
├── cmd/
│   └── gateway/
│       └── main.go           # Entry point: runs tri-port servers
├── internal/
│   ├── config/
│   │   └── config.go         # Viper-based configuration
│   ├── server/
│   │   ├── public.go         # Public API server (:8080)
│   │   ├── parcel.go         # Internal Parcel API (:8081)
│   │   └── party.go          # Internal Party API (:8082)
│   ├── handler/
│   │   ├── public/           # Public API handlers
│   │   │   ├── properties.go
│   │   │   ├── search.go
│   │   │   ├── predictions.go
│   │   │   └── liens.go      # FR-12: Miw endpoints
│   │   └── internal/         # Internal API handlers
│   │       ├── work.go
│   │       ├── results.go
│   │       ├── tasks.go
│   │       └── heartbeat.go
│   ├── middleware/
│   │   ├── auth.go           # Firebase/API Key auth
│   │   ├── ratelimit.go      # Token bucket
│   │   ├── cache.go          # Response caching
│   │   ├── logging.go        # Structured logging
│   │   └── worker.go         # Worker token validation
│   ├── service/
│   │   ├── auth.go           # Authentication logic
│   │   ├── authz.go          # Authorization (tiers)
│   │   ├── queue.go          # Redis task queue
│   │   ├── properties.go     # PostgreSQL queries
│   │   └── worker.go         # Worker registry
│   ├── model/
│   │   ├── user.go
│   │   ├── task.go
│   │   ├── parcel.go
│   │   └── lien.go           # FR-12: Lien model
│   └── pkg/
│       ├── db/
│       │   └── postgres.go   # pgx pool
│       ├── cache/
│       │   └── redis.go      # go-redis
│       └── metrics/
│           └── prometheus.go
├── api/
│   └── openapi.yaml          # OpenAPI 3.0 spec
├── Dockerfile
├── docker-compose.yml
├── go.mod
├── go.sum
└── Makefile
```

**Alternatives Considered:**

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

**Recommendation:** Go with Chi router for performance, simplicity, and full control.

---

## Dependencies

### Related SDDs

| SDD | Purpose | Integration |
|-----|---------|-------------|
| `sdd-taxlien-storage` | MinIO object storage | Raw HTML upload, file storage |
| `sdd-taxlien-imgproxy` | Image resizing | Gateway generates signed URLs |
| `sdd-taxlien-ml` | ML predictions | Proxy requests to ML service |

### Internal Services

| Service | Purpose | Endpoints Used |
|---------|---------|----------------|
| PostgreSQL | Primary database | Direct connection (pgx) |
| Redis | Cache, rate limits, queue | Direct connection (go-redis) |
| MinIO | Object storage | S3 API via `sdd-taxlien-storage` |
| ML Service | Predictions | `/api/v1/predict/*`, `/api/v1/top-lists/*` |

### External Dependencies

| Service | Purpose |
|---------|---------|
| Firebase Auth | Token validation |
| CloudFlare | CDN, DDoS protection |
| Prometheus | Metrics collection |
| Sentry | Error tracking |

### Note on Image Serving

Gateway **НЕ** проксирует изображения. Клиенты обращаются напрямую к imgproxy:

```
Client → CloudFlare CDN → imgproxy → MinIO
```

Gateway только генерирует signed URLs для изображений. См. `sdd-taxlien-imgproxy` для деталей.

---

## Deployment

### Dockerfile (Go - Multi-stage Build)

```dockerfile
# Build stage
FROM golang:1.22-alpine AS builder

WORKDIR /app

# Install dependencies
RUN apk add --no-cache git ca-certificates

# Copy go mod files
COPY go.mod go.sum ./
RUN go mod download

# Copy source
COPY . .

# Build binary
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o /gateway ./cmd/gateway

# Runtime stage
FROM alpine:3.19

RUN apk add --no-cache ca-certificates tzdata

WORKDIR /app

COPY --from=builder /gateway .

# Expose all three ports
EXPOSE 8080 8081 8082

# Health check for all apps
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget -qO- http://localhost:8080/health && \
        wget -qO- http://localhost:8081/health && \
        wget -qO- http://localhost:8082/health || exit 1

ENTRYPOINT ["/app/gateway"]
```

### Docker Compose (Development) - Tri-Port Architecture

```yaml
services:
  gateway:
    build:
      context: ./taxlien-gateway
      dockerfile: Dockerfile
    ports:
      - "8080:8080"    # Public API
      - "8081:8081"    # Internal Parcel API
      - "8082:8082"    # Internal Party API
    environment:
      - GATEWAY_POSTGRES_URL=postgresql://user:pass@postgres:5432/taxlien
      - GATEWAY_REDIS_URL=redis://redis:6379
      - GATEWAY_FIREBASE_PROJECT_ID=taxlien-online
      - GATEWAY_SSR_SERVICE_TOKEN=${SSR_TOKEN}
      - GATEWAY_WORKER_TOKENS=${WORKER_TOKENS}
      - GATEWAY_RAW_STORAGE_PATH=/data/raw
      - GATEWAY_PUBLIC_PORT=8080
      - GATEWAY_PARCEL_PORT=8081
      - GATEWAY_PARTY_PORT=8082
    volumes:
      - raw_storage:/data/raw
    depends_on:
      - postgres
      - redis
    networks:
      - public
      - internal

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
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    networks:
      - internal

  # Parser workers connect only to internal network
  parser-worker:
    build: ./taxlien-parser
    environment:
      - GATEWAY_PARCEL_URL=http://gateway:8081
      - WORKER_TOKEN=${WORKER_TOKEN_1}
    networks:
      - internal
    deploy:
      replicas: 4

networks:
  public:
    driver: bridge
  internal:
    driver: bridge
    internal: true

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

**Status:** REQUIREMENTS v2.0 DRAFT (Go Rewrite)
**Next Phase:** SPECIFICATIONS v2.0
**Owner:** Platform Team
**Changes from v1.x:**
- Tech Stack: Python/FastAPI → Go/Chi
- Architecture: Dual-Port → Tri-Port (added Party Internal :8082)
- All code examples converted to Go
- Same API contracts (backwards compatible)
