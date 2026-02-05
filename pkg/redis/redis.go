package redis

import (
	"context"
	"fmt"

	"github.com/redis/go-redis/v9"
)

// Client wraps go-redis client.
type Client struct {
	inner *redis.Client
}

// Redis returns the underlying redis client.
func (c *Client) Redis() *redis.Client {
	return c.inner
}

// Close closes the connection.
func (c *Client) Close() error {
	return c.inner.Close()
}

// New creates a Redis client.
func New(url string) (*Client, error) {
	opt, err := redis.ParseURL(url)
	if err != nil {
		return nil, fmt.Errorf("parse redis url: %w", err)
	}
	client := redis.NewClient(opt)
	if err := client.Ping(context.Background()).Err(); err != nil {
		return nil, fmt.Errorf("redis ping: %w", err)
	}
	return &Client{inner: client}, nil
}
