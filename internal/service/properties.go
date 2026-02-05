package service

import (
	"context"
	"encoding/json"

	"github.com/jackc/pgx/v5/pgxpool"
	"github.com/taxlien/gateway/internal/model"
)

// Properties handles parcel persistence.
type Properties struct {
	pool *pgxpool.Pool
}

// NewProperties creates a properties service.
func NewProperties(pool *pgxpool.Pool) *Properties {
	return &Properties{pool: pool}
}

// UpsertParcel inserts or updates a parcel. Returns true if inserted.
func (p *Properties) UpsertParcel(ctx context.Context, r model.ParcelResult, workerID string) (inserted bool, err error) {
	dataJSON, err := json.Marshal(r.Data)
	if err != nil {
		return false, err
	}

	var existed bool
	_ = p.pool.QueryRow(ctx,
		`SELECT EXISTS(SELECT 1 FROM parcels WHERE parcel_id=$1 AND platform=$2 AND state=$3 AND county=$4)`,
		r.ParcelID, r.Platform, r.State, r.County,
	).Scan(&existed)

	query := `
	INSERT INTO parcels (parcel_id, platform, state, county, data, scraped_at, worker_id)
	VALUES ($1, $2, $3, $4, $5, $6, $7)
	ON CONFLICT (parcel_id, platform, state, county)
	DO UPDATE SET data = EXCLUDED.data, scraped_at = EXCLUDED.scraped_at, worker_id = EXCLUDED.worker_id
	`
	_, err = p.pool.Exec(ctx, query,
		r.ParcelID, r.Platform, r.State, r.County, dataJSON, r.ScrapedAt, workerID,
	)
	if err != nil {
		return false, err
	}
	return !existed, nil
}
