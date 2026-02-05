-- User and app tables (sdd-taxlien-gateway-supabase)
-- Depends on: 01_base_tables (parcels). References auth.users (Supabase built-in).

-- User profiles (extends auth.users)
CREATE TABLE user_profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,

    display_name TEXT,
    avatar_url TEXT,

    tier TEXT DEFAULT 'free',
    tier_expires_at TIMESTAMPTZ,

    preferred_states TEXT[],
    preferred_property_types TEXT[],
    max_lien_amount NUMERIC,

    swipes_today INTEGER DEFAULT 0,
    swipes_reset_at DATE DEFAULT CURRENT_DATE,

    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_user_profiles_tier ON user_profiles (tier) WHERE tier IS NOT NULL;

-- Favorites
CREATE TABLE favorites (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    parcel_id UUID NOT NULL REFERENCES parcels(id) ON DELETE CASCADE,

    notes TEXT,
    tags TEXT[],

    created_at TIMESTAMPTZ DEFAULT NOW(),

    UNIQUE(user_id, parcel_id)
);

CREATE INDEX idx_favorites_user_id ON favorites (user_id);
CREATE INDEX idx_favorites_parcel_id ON favorites (parcel_id);

-- Swipe history (Deal Detective)
CREATE TABLE swipes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    parcel_id UUID NOT NULL REFERENCES parcels(id) ON DELETE CASCADE,

    action TEXT NOT NULL,

    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_swipes_user_id ON swipes (user_id);
CREATE INDEX idx_swipes_parcel_id ON swipes (parcel_id);
CREATE INDEX idx_swipes_created_at ON swipes (created_at DESC);

-- Annotations (expert markup)
CREATE TABLE annotations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    parcel_id UUID NOT NULL REFERENCES parcels(id) ON DELETE CASCADE,
    image_path TEXT,

    annotation_type TEXT,
    coordinates JSONB,
    label TEXT,
    category TEXT,

    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_annotations_user_id ON annotations (user_id);
CREATE INDEX idx_annotations_parcel_id ON annotations (parcel_id);

-- Auto-update updated_at for user_profiles (set_updated_at from 01_base_tables)
CREATE TRIGGER user_profiles_updated_at
    BEFORE UPDATE ON user_profiles
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();
