package config

import (
	"strings"
)

// Config holds gateway configuration from environment.
type Config struct {
	Port         int
	PostgresURL  string
	RedisURL     string
	WorkerTokens map[string]struct{}
	RawStorage   string
}

// Load reads configuration from environment variables.
// Env prefix: GATEWAY_
func Load() *Config {
	port := getEnvInt("GATEWAY_PORT", 8081)
	postgres := getEnv("GATEWAY_POSTGRES_URL", "postgres://localhost:5432/taxlien")
	redis := getEnv("GATEWAY_REDIS_URL", "redis://localhost:6379/0")
	tokensRaw := getEnv("GATEWAY_WORKER_TOKENS", "")
	rawStorage := getEnv("GATEWAY_RAW_STORAGE_PATH", "/data/raw")

	tokens := make(map[string]struct{})
	for _, t := range strings.Split(tokensRaw, ",") {
		t = strings.TrimSpace(t)
		if t != "" {
			tokens[t] = struct{}{}
		}
	}

	return &Config{
		Port:         port,
		PostgresURL:  postgres,
		RedisURL:     redis,
		WorkerTokens: tokens,
		RawStorage:   rawStorage,
	}
}
