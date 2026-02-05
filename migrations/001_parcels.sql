-- parcels table for worker results (Supabase / PostgreSQL)
CREATE TABLE IF NOT EXISTS parcels (
    id SERIAL PRIMARY KEY,
    parcel_id VARCHAR(255) NOT NULL,
    platform VARCHAR(64) NOT NULL,
    state VARCHAR(8) NOT NULL,
    county VARCHAR(255) NOT NULL,
    data JSONB NOT NULL,
    scraped_at TIMESTAMPTZ NOT NULL,
    worker_id VARCHAR(255),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE UNIQUE INDEX IF NOT EXISTS _parcel_platform_uc
    ON parcels (parcel_id, platform, state, county);

CREATE INDEX IF NOT EXISTS idx_parcels_parcel_id ON parcels (parcel_id);
CREATE INDEX IF NOT EXISTS idx_parcels_platform ON parcels (platform);
