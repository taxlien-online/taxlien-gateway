package service

import (
	"context"
	"fmt"
	"strings"
	"time"

	"github.com/redis/go-redis/v9"
	"github.com/taxlien/gateway/internal/model"
)

const heartbeatTTL = 300 * time.Second

// WorkerRegistry tracks worker status in Redis.
type WorkerRegistry struct {
	rdb *redis.Client
}

// NewWorkerRegistry creates a worker registry.
func NewWorkerRegistry(rdb *redis.Client) *WorkerRegistry {
	return &WorkerRegistry{rdb: rdb}
}

func workerKey(workerID string) string {
	return fmt.Sprintf("worker:%s:status", workerID)
}

// Update stores worker status.
func (r *WorkerRegistry) Update(ctx context.Context, workerID string, status model.WorkerStatus) error {
	key := workerKey(workerID)
	now := time.Now().Unix()
	err := r.rdb.HSet(ctx, key, map[string]interface{}{
		"last_seen":      now,
		"active_tasks":   status.ActiveTasks,
		"platforms":      strings.Join(status.Platforms, ","),
		"cpu":            status.CPUPercent,
		"memory":         status.MemoryPercent,
	}).Err()
	if err != nil {
		return err
	}
	return r.rdb.Expire(ctx, key, heartbeatTTL).Err()
}

// GetCommands returns pending commands (placeholder).
func (r *WorkerRegistry) GetCommands(ctx context.Context, workerID string) ([]string, error) {
	_ = workerID
	return nil, nil
}
