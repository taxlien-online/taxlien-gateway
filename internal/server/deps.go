package server

import (
	"github.com/jackc/pgx/v5/pgxpool"
	"github.com/redis/go-redis/v9"
	"github.com/taxlien/gateway/internal/handler"
	"github.com/taxlien/gateway/internal/service"
)

// Deps holds server dependencies.
type Deps struct {
	Queue      *service.Queue
	Properties *service.Properties
	Registry   *service.WorkerRegistry
	Work       *handler.WorkHandler
	Results    *handler.ResultsHandler
	Tasks      *handler.TasksHandler
	RawFiles   *handler.RawFilesHandler
	Heartbeat  *handler.HeartbeatHandler
}

// NewDeps creates dependencies from Redis and Postgres.
func NewDeps(rdb *redis.Client, pool *pgxpool.Pool, rawStoragePath string) *Deps {
	queue := service.NewQueue(rdb)
	props := service.NewProperties(pool)
	registry := service.NewWorkerRegistry(rdb)

	return &Deps{
		Queue:      queue,
		Properties: props,
		Registry:   registry,
		Work:       &handler.WorkHandler{Queue: queue},
		Results: &handler.ResultsHandler{
			Queue:      queue,
			Properties: props,
		},
		Tasks:     &handler.TasksHandler{Queue: queue},
		RawFiles:  &handler.RawFilesHandler{StoragePath: rawStoragePath},
		Heartbeat: &handler.HeartbeatHandler{Registry: registry},
	}
}
