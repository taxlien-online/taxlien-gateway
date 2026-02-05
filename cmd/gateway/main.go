package main

import (
	"context"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/taxlien/gateway/internal/config"
	"github.com/taxlien/gateway/pkg/db"
	"github.com/taxlien/gateway/pkg/redis"
	"github.com/taxlien/gateway/internal/server"
	"go.uber.org/zap"
)

func main() {
	log, _ := zap.NewProduction()
	defer log.Sync()

	cfg := config.Load()

	rdbClient, err := redis.New(cfg.RedisURL)
	if err != nil {
		log.Fatal("redis connect", zap.Error(err))
	}
	defer rdbClient.Close()

	ctx := context.Background()
	pgPool, err := db.New(ctx, cfg.PostgresURL)
	if err != nil {
		log.Fatal("postgres connect", zap.Error(err))
	}
	defer pgPool.Close()

	deps := server.NewDeps(rdbClient.Redis(), pgPool.Pool, cfg.RawStorage)
	srv := server.New(cfg, log, deps)

	go func() {
		if err := srv.Start(); err != nil && err != http.ErrServerClosed {
			log.Fatal("server failed", zap.Error(err))
		}
	}()

	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)
	<-sig

	log.Info("shutting down")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	_ = srv.Shutdown(ctx)
}
