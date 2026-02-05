package service

import (
	"context"
	"encoding/json"
	"fmt"

	"github.com/redis/go-redis/v9"
	"github.com/taxlien/gateway/internal/model"
)

// Queue manages task queues in Redis.
type Queue struct {
	rdb *redis.Client
}

// NewQueue creates a queue service.
func NewQueue(rdb *redis.Client) *Queue {
	return &Queue{rdb: rdb}
}

func queueKey(platform string, priority int) string {
	return fmt.Sprintf("queue:%s:p%d", platform, priority)
}

func processingKey(workerID string) string {
	return fmt.Sprintf("processing:%s", workerID)
}

// PopTasks pops tasks from queues for the worker.
func (q *Queue) PopTasks(ctx context.Context, workerID string, platforms []string, capacity int) ([]model.WorkTask, error) {
	var tasks []model.WorkTask
	procKey := processingKey(workerID)

	for _, platform := range platforms {
		if len(tasks) >= capacity {
			break
		}
		for priority := 1; priority <= 4; priority++ {
			if len(tasks) >= capacity {
				break
			}
			queueKey := queueKey(platform, priority)
			raw, err := q.rdb.RPopLPush(ctx, queueKey, procKey).Result()
			if err == redis.Nil {
				continue
			}
			if err != nil {
				return nil, err
			}
			var t model.WorkTask
			if err := json.Unmarshal([]byte(raw), &t); err != nil {
				return nil, err
			}
			tasks = append(tasks, t)
		}
	}
	return tasks, nil
}

// CompleteTask removes task from processing list.
func (q *Queue) CompleteTask(ctx context.Context, workerID, taskID string) (bool, error) {
	procKey := processingKey(workerID)
	items, err := q.rdb.LRange(ctx, procKey, 0, -1).Result()
	if err != nil {
		return false, err
	}
	for _, raw := range items {
		var t model.WorkTask
		if err := json.Unmarshal([]byte(raw), &t); err != nil {
			continue
		}
		if t.TaskID == taskID {
			return q.rdb.LRem(ctx, procKey, 1, raw).Err() == nil, nil
		}
	}
	return false, nil
}

// FailTask removes from processing; optionally requeue (not implemented for MVP).
func (q *Queue) FailTask(ctx context.Context, workerID, taskID string) (bool, error) {
	return q.CompleteTask(ctx, workerID, taskID)
}
