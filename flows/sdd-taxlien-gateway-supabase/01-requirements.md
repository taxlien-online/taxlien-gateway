# Requirements: Supabase Backend

**Version:** 1.0
**Status:** REQUIREMENTS PHASE - DRAFTING
**Last Updated:** 2026-02-01
**Goal:** Unified backend using Supabase for database, auth, storage, and auto-generated APIs

---

## Architecture Decision

### Why Supabase?

**Decision (2026-02-01):** Заменить custom microservices на Supabase для:
- Меньше кода для поддержки
- Auto-generated REST API (PostgREST)
- Built-in Auth (заменяет Firebase)
- Built-in Storage с Image Transforms (заменяет MinIO + imgproxy)
- Row-Level Security (RLS) для авторизации
- Realtime subscriptions для live updates

### What Supabase Replaces

| Was | Becomes |
|-----|---------|
| Custom Go/Python CRUD handlers | PostgREST auto-API |
| Firebase Auth | Supabase Auth |
| MinIO (`sdd-taxlien-storage`) | Supabase Storage |
| imgproxy (`sdd-taxlien-imgproxy`) | Supabase Image Transforms |
| Custom rate limiting | Edge Functions + mini service |

### What Remains Custom

| Component | Reason |
|-----------|--------|
| Worker Internal API | Task queue, heartbeat - not supported by Supabase |
| ML Proxy (optional) | Long-running connections, caching |
| Complex rate limiting (optional) | Tier-based, per-user limits |

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TAXLIEN.online                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                              EXTERNAL CLIENTS                               │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                    │
│   │ Flutter App  │  │  SSR Site    │  │   Swipe App  │                    │
│   │ (Mobile)     │  │  (Next.js)   │  │   (Flutter)  │                    │
│   └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                    │
│          │                 │                 │                             │
│          │ Supabase SDK    │ Supabase SDK    │ Supabase SDK               │
│          └─────────────────┼─────────────────┘                             │
│                            ▼                                                │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                         SUPABASE                                     │  │
│   │                   api.taxlien.online                                 │  │
│   │                                                                      │  │
│   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │  │
│   │  │  PostgREST  │ │    Auth     │ │   Storage   │ │  Realtime   │   │  │
│   │  │  (REST API) │ │   (JWT)     │ │  (S3-like)  │ │  (WebSocket)│   │  │
│   │  │             │ │             │ │             │ │             │   │  │
│   │  │ /parcels    │ │ • Sign up   │ │ • images/   │ │ • Changes   │   │  │
│   │  │ /liens      │ │ • Sign in   │ │ • documents/│ │ • Presence  │   │  │
│   │  │ /auctions   │ │ • OAuth     │ │ • exports/  │ │ • Broadcast │   │  │
│   │  │ /users      │ │ • RLS       │ │             │ │             │   │  │
│   │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │  │
│   │                                                                      │  │
│   │  ┌─────────────┐ ┌─────────────┐                                    │  │
│   │  │    Edge     │ │   Image     │                                    │  │
│   │  │  Functions  │ │ Transforms  │                                    │  │
│   │  │   (Deno)    │ │             │                                    │  │
│   │  │             │ │ ?width=800  │                                    │  │
│   │  │ • Webhooks  │ │ ?quality=80 │                                    │  │
│   │  │ • ML proxy  │ │ ?resize=    │                                    │  │
│   │  │ • Rate limit│ │             │                                    │  │
│   │  └─────────────┘ └─────────────┘                                    │  │
│   │                                                                      │  │
│   │                      PostgreSQL                                      │  │
│   │  ┌───────────────────────────────────────────────────────────────┐  │  │
│   │  │  Tables: parcels, liens, auctions, users, favorites, swipes   │  │  │
│   │  │  Views: v_liens_with_scores, v_foreclosure_candidates         │  │  │
│   │  │  Functions: get_top_picks(), search_liens()                   │  │  │
│   │  │  RLS Policies: per-user access, tier-based visibility         │  │  │
│   │  └───────────────────────────────────────────────────────────────┘  │  │
│   │                                                                      │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                            │                                                │
│                            │ Direct DB connection                          │
│                            ▼                                                │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │              MINIMAL GO SERVICE (Worker API only)                    │  │
│   │              internal.taxlien.local:8081                             │  │
│   │                                                                      │  │
│   │   • GET  /internal/work         ← Workers pull tasks                │  │
│   │   • POST /internal/results      ← Workers submit data               │  │
│   │   • POST /internal/heartbeat    ← Worker health                     │  │
│   │                                                                      │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                            │                                                │
│           ┌────────────────┼────────────────┐                              │
│           ▼                ▼                ▼                              │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                    │
│   │ Parser       │  │ Party        │  │ ML Service   │                    │
│   │ Workers      │  │ Workers      │  │              │                    │
│   └──────────────┘  └──────────────┘  └──────────────┘                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Functional Requirements

### FR-1: Database Schema

**Core Tables:**

```sql
-- Parcels (property records)
CREATE TABLE parcels (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parcel_id TEXT NOT NULL,           -- County parcel ID
    state TEXT NOT NULL,
    county TEXT NOT NULL,
    platform TEXT,                      -- beacon, qpublic, etc.

    -- Address
    address TEXT,
    city TEXT,
    zip TEXT,

    -- Property details
    property_type TEXT,                 -- RESIDENTIAL, LOT, COMMERCIAL
    land_area_sqft NUMERIC,
    building_area_sqft NUMERIC,
    year_built INTEGER,
    bedrooms INTEGER,
    bathrooms NUMERIC,

    -- Values
    assessed_value NUMERIC,
    market_value NUMERIC,
    land_value NUMERIC,
    building_value NUMERIC,

    -- Owner
    owner_name TEXT,
    owner_address TEXT,

    -- Metadata
    scraped_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),

    UNIQUE(state, county, parcel_id)
);

-- Liens (tax lien records)
CREATE TABLE liens (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parcel_id UUID REFERENCES parcels(id),

    -- Lien details
    certificate_number TEXT,
    lien_amount NUMERIC NOT NULL,
    interest_rate NUMERIC,
    penalty_rate NUMERIC,

    -- Dates
    sale_date DATE,
    redemption_deadline DATE,
    struck_off_date DATE,

    -- Status
    status TEXT,                        -- ACTIVE, REDEEMED, FORECLOSED
    is_otc BOOLEAN DEFAULT FALSE,
    prior_years_owed INTEGER DEFAULT 0,

    -- ML Scores (computed)
    redemption_probability NUMERIC,
    foreclosure_probability NUMERIC,
    miw_score NUMERIC,
    karma_score NUMERIC,

    -- Metadata
    auction_id UUID REFERENCES auctions(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Auctions
CREATE TABLE auctions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    state TEXT NOT NULL,
    county TEXT NOT NULL,

    auction_date DATE NOT NULL,
    auction_type TEXT,                  -- TAX_LIEN, TAX_DEED, OTC
    registration_deadline DATE,
    deposit_required NUMERIC,

    platform TEXT,                      -- realauction, bid4assets, etc.
    platform_url TEXT,

    status TEXT,                        -- UPCOMING, ACTIVE, COMPLETED
    total_items INTEGER,

    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Users (extended from auth.users)
CREATE TABLE user_profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id),

    -- Profile
    display_name TEXT,
    avatar_url TEXT,

    -- Subscription
    tier TEXT DEFAULT 'free',           -- free, starter, premium, enterprise
    tier_expires_at TIMESTAMPTZ,

    -- Preferences
    preferred_states TEXT[],
    preferred_property_types TEXT[],
    max_lien_amount NUMERIC,

    -- Stats
    swipes_today INTEGER DEFAULT 0,
    swipes_reset_at DATE DEFAULT CURRENT_DATE,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- User favorites
CREATE TABLE favorites (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    parcel_id UUID REFERENCES parcels(id) ON DELETE CASCADE,

    notes TEXT,
    tags TEXT[],

    created_at TIMESTAMPTZ DEFAULT NOW(),

    UNIQUE(user_id, parcel_id)
);

-- Swipe history (for Deal Detective)
CREATE TABLE swipes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    parcel_id UUID REFERENCES parcels(id) ON DELETE CASCADE,

    action TEXT NOT NULL,               -- PASS, LIKE, SUPERLIKE

    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Annotations (expert markup)
CREATE TABLE annotations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    parcel_id UUID REFERENCES parcels(id) ON DELETE CASCADE,
    image_path TEXT,

    annotation_type TEXT,               -- POINT, AREA, LINE
    coordinates JSONB,                  -- {x, y} or [{x, y}, ...]
    label TEXT,
    category TEXT,                      -- construction, furniture, vehicle, etc.

    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

**Acceptance Criteria:**
- [ ] All tables created with proper constraints
- [ ] Indexes on frequently queried columns
- [ ] Foreign keys with appropriate ON DELETE actions
- [ ] Timestamps auto-updated via triggers

---

### FR-2: Views (Pre-computed Queries)

```sql
-- Liens with all scores and parcel data
CREATE VIEW v_liens_full AS
SELECT
    l.*,
    p.address,
    p.city,
    p.state,
    p.county,
    p.property_type,
    p.assessed_value,
    p.market_value,
    p.owner_name,
    p.year_built,
    -- Computed
    CASE WHEN p.market_value > 0
         THEN l.lien_amount / p.market_value
         ELSE NULL END AS lien_to_value_ratio
FROM liens l
JOIN parcels p ON l.parcel_id = p.id;

-- Foreclosure candidates (for sdd-miw-gift)
CREATE VIEW v_foreclosure_candidates AS
SELECT * FROM v_liens_full
WHERE prior_years_owed >= 2
  AND foreclosure_probability > 0.6
  AND status = 'ACTIVE';

-- OTC liens
CREATE VIEW v_otc_liens AS
SELECT * FROM v_liens_full
WHERE is_otc = TRUE
  AND status = 'ACTIVE';

-- Top picks by persona
CREATE VIEW v_top_picks AS
SELECT
    *,
    -- Flipper score: high value, low lien, good condition
    (market_value / NULLIF(lien_amount, 0)) * (1 - foreclosure_probability) AS flipper_score,
    -- Landlord score: rental potential
    (market_value / NULLIF(lien_amount, 0)) * redemption_probability AS landlord_score,
    -- Beginner score: low risk, low amount
    (1 - foreclosure_probability) * (1000 / NULLIF(lien_amount, 0)) AS beginner_score
FROM v_liens_full
WHERE status = 'ACTIVE';
```

**Acceptance Criteria:**
- [ ] Views created for common query patterns
- [ ] Views used by PostgREST for efficient queries
- [ ] Materialized views for expensive computations (optional)

---

### FR-3: Row-Level Security (RLS)

```sql
-- Enable RLS on all tables
ALTER TABLE parcels ENABLE ROW LEVEL SECURITY;
ALTER TABLE liens ENABLE ROW LEVEL SECURITY;
ALTER TABLE favorites ENABLE ROW LEVEL SECURITY;
ALTER TABLE swipes ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;

-- Parcels: everyone can read
CREATE POLICY "Parcels are viewable by everyone"
ON parcels FOR SELECT
USING (true);

-- Liens: tier-based access
CREATE POLICY "Liens viewable by tier"
ON liens FOR SELECT
USING (
    -- Free users: limited fields (handled in view/function)
    -- All authenticated users can see liens
    auth.role() = 'authenticated'
    OR
    -- Anonymous: only basic info (first 10 per day - handled elsewhere)
    auth.role() = 'anon'
);

-- Favorites: users can only see their own
CREATE POLICY "Users can view own favorites"
ON favorites FOR SELECT
USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own favorites"
ON favorites FOR INSERT
WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can delete own favorites"
ON favorites FOR DELETE
USING (auth.uid() = user_id);

-- Swipes: users can only see their own
CREATE POLICY "Users can view own swipes"
ON swipes FOR SELECT
USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own swipes"
ON swipes FOR INSERT
WITH CHECK (auth.uid() = user_id);

-- User profiles: users can only see/edit their own
CREATE POLICY "Users can view own profile"
ON user_profiles FOR SELECT
USING (auth.uid() = id);

CREATE POLICY "Users can update own profile"
ON user_profiles FOR UPDATE
USING (auth.uid() = id);
```

**Acceptance Criteria:**
- [ ] RLS enabled on all user-data tables
- [ ] Public data (parcels, liens) readable by all
- [ ] User data (favorites, swipes) restricted to owner
- [ ] Tier-based access enforced

---

### FR-4: Database Functions

```sql
-- Search liens with filters
CREATE OR REPLACE FUNCTION search_liens(
    p_state TEXT DEFAULT NULL,
    p_county TEXT DEFAULT NULL,
    p_max_amount NUMERIC DEFAULT NULL,
    p_min_foreclosure_prob NUMERIC DEFAULT NULL,
    p_prior_years_min INTEGER DEFAULT NULL,
    p_property_type TEXT DEFAULT NULL,
    p_is_otc BOOLEAN DEFAULT NULL,
    p_limit INTEGER DEFAULT 100,
    p_offset INTEGER DEFAULT 0
)
RETURNS TABLE (
    id UUID,
    parcel_id UUID,
    lien_amount NUMERIC,
    foreclosure_probability NUMERIC,
    miw_score NUMERIC,
    address TEXT,
    city TEXT,
    state TEXT,
    county TEXT,
    property_type TEXT,
    market_value NUMERIC,
    prior_years_owed INTEGER,
    is_otc BOOLEAN
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        l.id,
        l.parcel_id,
        l.lien_amount,
        l.foreclosure_probability,
        l.miw_score,
        p.address,
        p.city,
        p.state,
        p.county,
        p.property_type,
        p.market_value,
        l.prior_years_owed,
        l.is_otc
    FROM liens l
    JOIN parcels p ON l.parcel_id = p.id
    WHERE l.status = 'ACTIVE'
      AND (p_state IS NULL OR p.state = p_state)
      AND (p_county IS NULL OR p.county = p_county)
      AND (p_max_amount IS NULL OR l.lien_amount <= p_max_amount)
      AND (p_min_foreclosure_prob IS NULL OR l.foreclosure_probability >= p_min_foreclosure_prob)
      AND (p_prior_years_min IS NULL OR l.prior_years_owed >= p_prior_years_min)
      AND (p_property_type IS NULL OR p.property_type = p_property_type)
      AND (p_is_otc IS NULL OR l.is_otc = p_is_otc)
    ORDER BY l.miw_score DESC NULLS LAST
    LIMIT p_limit
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

-- Get top picks for county by persona
CREATE OR REPLACE FUNCTION get_top_picks(
    p_state TEXT,
    p_county TEXT,
    p_persona TEXT DEFAULT 'beginner',
    p_limit INTEGER DEFAULT 10
)
RETURNS TABLE (
    id UUID,
    lien_amount NUMERIC,
    address TEXT,
    property_type TEXT,
    market_value NUMERIC,
    score NUMERIC
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        l.id,
        l.lien_amount,
        p.address,
        p.property_type,
        p.market_value,
        CASE p_persona
            WHEN 'flipper' THEN (p.market_value / NULLIF(l.lien_amount, 0))
            WHEN 'landlord' THEN l.redemption_probability * 100
            WHEN 'beginner' THEN (1 - l.foreclosure_probability) * 100
            ELSE l.miw_score
        END AS score
    FROM liens l
    JOIN parcels p ON l.parcel_id = p.id
    WHERE p.state = p_state
      AND p.county = p_county
      AND l.status = 'ACTIVE'
    ORDER BY score DESC NULLS LAST
    LIMIT p_limit;
END;
$$ LANGUAGE plpgsql;

-- Increment swipe counter (with daily reset)
CREATE OR REPLACE FUNCTION increment_swipe()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE user_profiles
    SET
        swipes_today = CASE
            WHEN swipes_reset_at < CURRENT_DATE THEN 1
            ELSE swipes_today + 1
        END,
        swipes_reset_at = CURRENT_DATE
    WHERE id = NEW.user_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER on_swipe_insert
AFTER INSERT ON swipes
FOR EACH ROW EXECUTE FUNCTION increment_swipe();
```

**Acceptance Criteria:**
- [ ] Functions for complex queries
- [ ] Triggers for automatic updates
- [ ] Functions callable via PostgREST RPC

---

### FR-5: Storage Buckets

```sql
-- Create buckets via Supabase Dashboard or SQL

-- Property images (public via transforms)
INSERT INTO storage.buckets (id, name, public)
VALUES ('images', 'images', true);

-- Documents (private, user-specific access)
INSERT INTO storage.buckets (id, name, public)
VALUES ('documents', 'documents', false);

-- User exports (private, auto-delete)
INSERT INTO storage.buckets (id, name, public)
VALUES ('exports', 'exports', false);
```

**Storage Policies:**

```sql
-- Images: anyone can read
CREATE POLICY "Public read for images"
ON storage.objects FOR SELECT
USING (bucket_id = 'images');

-- Documents: only authenticated users
CREATE POLICY "Auth users can read documents"
ON storage.objects FOR SELECT
USING (bucket_id = 'documents' AND auth.role() = 'authenticated');

-- Exports: only owner
CREATE POLICY "Users can read own exports"
ON storage.objects FOR SELECT
USING (
    bucket_id = 'exports'
    AND auth.uid()::text = (storage.foldername(name))[1]
);
```

**Image Transforms:**

```
# Thumbnail
/storage/v1/object/public/images/fl/union/parcel-123/image1.jpg?width=200&height=150

# Preview
/storage/v1/object/public/images/fl/union/parcel-123/image1.jpg?width=800&quality=85

# Full (no transform)
/storage/v1/object/public/images/fl/union/parcel-123/image1.jpg
```

**Acceptance Criteria:**
- [ ] Buckets created with correct visibility
- [ ] Storage policies enforce access
- [ ] Image transforms working

---

### FR-6: Edge Functions

**Rate Limiting Function:**

```typescript
// supabase/functions/rate-limit/index.ts
import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from "https://esm.sh/@supabase/supabase-js@2"

serve(async (req) => {
  const supabase = createClient(
    Deno.env.get('SUPABASE_URL')!,
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
  )

  const authHeader = req.headers.get('Authorization')
  if (!authHeader) {
    return new Response(JSON.stringify({ error: 'No auth' }), { status: 401 })
  }

  const { data: { user } } = await supabase.auth.getUser(authHeader.replace('Bearer ', ''))

  if (!user) {
    return new Response(JSON.stringify({ error: 'Invalid token' }), { status: 401 })
  }

  // Get user tier
  const { data: profile } = await supabase
    .from('user_profiles')
    .select('tier, swipes_today, swipes_reset_at')
    .eq('id', user.id)
    .single()

  const limits = {
    'free': 20,
    'starter': 100,
    'premium': -1,  // unlimited
    'enterprise': -1
  }

  const limit = limits[profile?.tier || 'free']

  if (limit !== -1 && profile?.swipes_today >= limit) {
    return new Response(JSON.stringify({
      error: 'Rate limit exceeded',
      limit,
      reset_at: profile.swipes_reset_at
    }), {
      status: 429,
      headers: {
        'X-RateLimit-Limit': limit.toString(),
        'X-RateLimit-Remaining': '0',
        'Retry-After': '86400'
      }
    })
  }

  return new Response(JSON.stringify({
    allowed: true,
    remaining: limit === -1 ? 'unlimited' : limit - (profile?.swipes_today || 0) - 1
  }), { status: 200 })
})
```

**ML Proxy Function:**

```typescript
// supabase/functions/ml-predict/index.ts
import { serve } from "https://deno.land/std@0.168.0/http/server.ts"

const ML_SERVICE_URL = Deno.env.get('ML_SERVICE_URL')!

serve(async (req) => {
  if (req.method !== 'POST') {
    return new Response('Method not allowed', { status: 405 })
  }

  const body = await req.json()

  // Proxy to ML service
  const response = await fetch(`${ML_SERVICE_URL}/api/v1/predict/redemption`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  })

  const result = await response.json()

  return new Response(JSON.stringify(result), {
    status: response.status,
    headers: { 'Content-Type': 'application/json' }
  })
})
```

**Acceptance Criteria:**
- [ ] Rate limiting Edge Function deployed
- [ ] ML proxy Edge Function deployed (if needed)
- [ ] Functions handle errors gracefully

---

### FR-7: Realtime Subscriptions

```typescript
// Flutter/Dart client
final supabase = Supabase.instance.client;

// Subscribe to new liens in user's preferred states
final subscription = supabase
  .from('liens')
  .stream(primaryKey: ['id'])
  .eq('state', 'AZ')
  .listen((List<Map<String, dynamic>> data) {
    // Handle new liens
    print('New liens: $data');
  });

// Subscribe to auction updates
final auctionSub = supabase
  .from('auctions')
  .stream(primaryKey: ['id'])
  .eq('status', 'UPCOMING')
  .listen((data) {
    // Handle auction updates
  });
```

**Acceptance Criteria:**
- [ ] Realtime enabled for liens, auctions tables
- [ ] Clients can subscribe to filtered changes
- [ ] Presence for collaborative features (optional)

---

## API Endpoints (Auto-generated)

PostgREST auto-generates these endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/v1/parcels` | List parcels with filters |
| GET | `/rest/v1/parcels?id=eq.{id}` | Get single parcel |
| GET | `/rest/v1/liens` | List liens with filters |
| GET | `/rest/v1/liens?state=eq.AZ&lien_amount=lt.500` | Filter liens |
| GET | `/rest/v1/v_foreclosure_candidates` | View: foreclosure candidates |
| GET | `/rest/v1/v_otc_liens?state=eq.AZ` | View: OTC liens |
| POST | `/rest/v1/rpc/search_liens` | Function: search liens |
| POST | `/rest/v1/rpc/get_top_picks` | Function: top picks |
| GET | `/rest/v1/favorites` | User's favorites |
| POST | `/rest/v1/favorites` | Add favorite |
| DELETE | `/rest/v1/favorites?id=eq.{id}` | Remove favorite |
| GET | `/rest/v1/swipes` | User's swipe history |
| POST | `/rest/v1/swipes` | Record swipe |
| GET | `/rest/v1/auctions?state=eq.AZ` | List auctions |

**Query Examples:**

```bash
# Get foreclosure candidates in AZ under $500
curl 'https://api.taxlien.online/rest/v1/v_foreclosure_candidates?state=eq.AZ&lien_amount=lt.500&limit=20' \
  -H "apikey: ${SUPABASE_ANON_KEY}" \
  -H "Authorization: Bearer ${USER_JWT}"

# Search via function
curl 'https://api.taxlien.online/rest/v1/rpc/search_liens' \
  -H "apikey: ${SUPABASE_ANON_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"p_state": "AZ", "p_max_amount": 500, "p_prior_years_min": 2}'

# Add favorite
curl 'https://api.taxlien.online/rest/v1/favorites' \
  -H "apikey: ${SUPABASE_ANON_KEY}" \
  -H "Authorization: Bearer ${USER_JWT}" \
  -H "Content-Type: application/json" \
  -d '{"parcel_id": "uuid-here"}'
```

---

## Non-Functional Requirements

### Performance

| Metric | Target |
|--------|--------|
| API latency (P50) | < 100ms |
| API latency (P99) | < 500ms |
| Realtime latency | < 200ms |
| Image transform | < 500ms |

### Scalability

- Supabase Pro: 500 concurrent connections
- Supabase Enterprise: unlimited
- Read replicas for scaling reads

### Security

- [ ] RLS enabled on all tables
- [ ] API keys rotated regularly
- [ ] Storage policies enforced
- [ ] Edge Functions validate auth

---

## Migration Plan

### From Firebase Auth

```typescript
// Migrate users via Supabase Auth API
const { data, error } = await supabase.auth.admin.createUser({
  email: firebaseUser.email,
  password: generateTempPassword(),
  user_metadata: {
    firebase_uid: firebaseUser.uid,
    migrated_at: new Date().toISOString()
  }
})
```

### From Custom API

1. Deploy Supabase schema
2. Migrate data to Supabase PostgreSQL
3. Update clients to use Supabase SDK
4. Deprecate custom endpoints
5. Shutdown custom services

---

## Success Metrics

| Metric | Target |
|--------|--------|
| API uptime | 99.9% |
| Latency P50 | < 100ms |
| Client SDK adoption | 100% |
| Custom code reduction | 80% |

---

## Dependencies

| Component | Purpose |
|-----------|---------|
| Supabase Project | Hosted backend |
| Supabase SDK (Flutter) | Client integration |
| Supabase SDK (Next.js) | SSR integration |
| ML Service | Predictions (external) |
| Worker Service | Task queue (external) |

---

**Status:** REQUIREMENTS v1.0 DRAFT
**Next Phase:** SPECIFICATIONS (schema details, RLS policies)
**Owner:** Platform Team
