-- Base tables for TAXLIEN Supabase backend (sdd-taxlien-gateway-supabase)
-- Order: parcels → auctions → liens (FK dependencies)

-- Parcels (property records)
CREATE TABLE parcels (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parcel_id TEXT NOT NULL,
    state TEXT NOT NULL,
    county TEXT NOT NULL,
    platform TEXT,

    address TEXT,
    city TEXT,
    zip TEXT,

    property_type TEXT,
    land_area_sqft NUMERIC,
    building_area_sqft NUMERIC,
    year_built INTEGER,
    bedrooms INTEGER,
    bathrooms NUMERIC,

    assessed_value NUMERIC,
    market_value NUMERIC,
    land_value NUMERIC,
    building_value NUMERIC,

    owner_name TEXT,
    owner_address TEXT,

    scraped_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),

    UNIQUE(state, county, parcel_id)
);

CREATE INDEX idx_parcels_state_county ON parcels (state, county);
CREATE INDEX idx_parcels_parcel_id ON parcels (parcel_id);
CREATE INDEX idx_parcels_platform ON parcels (platform) WHERE platform IS NOT NULL;

-- Auctions
CREATE TABLE auctions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    state TEXT NOT NULL,
    county TEXT NOT NULL,

    auction_date DATE NOT NULL,
    auction_type TEXT,
    registration_deadline DATE,
    deposit_required NUMERIC,

    platform TEXT,
    platform_url TEXT,

    status TEXT,
    total_items INTEGER,

    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_auctions_state_county ON auctions (state, county);
CREATE INDEX idx_auctions_status ON auctions (status) WHERE status IS NOT NULL;
CREATE INDEX idx_auctions_auction_date ON auctions (auction_date);

-- Liens (tax lien records; references parcels and auctions)
CREATE TABLE liens (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parcel_id UUID NOT NULL REFERENCES parcels(id),

    certificate_number TEXT,
    lien_amount NUMERIC NOT NULL,
    interest_rate NUMERIC,
    penalty_rate NUMERIC,

    sale_date DATE,
    redemption_deadline DATE,
    struck_off_date DATE,

    status TEXT,
    is_otc BOOLEAN DEFAULT FALSE,
    prior_years_owed INTEGER DEFAULT 0,

    redemption_probability NUMERIC,
    foreclosure_probability NUMERIC,
    miw_score NUMERIC,
    karma_score NUMERIC,

    auction_id UUID REFERENCES auctions(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_liens_parcel_id ON liens (parcel_id);
CREATE INDEX idx_liens_auction_id ON liens (auction_id) WHERE auction_id IS NOT NULL;
CREATE INDEX idx_liens_status ON liens (status) WHERE status IS NOT NULL;
CREATE INDEX idx_liens_foreclosure_prob ON liens (foreclosure_probability) WHERE foreclosure_probability IS NOT NULL;
CREATE INDEX idx_liens_miw_score ON liens (miw_score DESC NULLS LAST);

-- Trigger: auto-update updated_at for parcels
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER parcels_updated_at
    BEFORE UPDATE ON parcels
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE TRIGGER liens_updated_at
    BEFORE UPDATE ON liens
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();
