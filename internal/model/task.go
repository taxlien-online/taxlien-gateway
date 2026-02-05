package model

import "time"

// WorkTask represents a task for a parser worker.
type WorkTask struct {
	TaskID   string     `json:"task_id"`
	Type     string     `json:"type"`
	Platform string     `json:"platform"`
	Target   Target     `json:"target"`
	Priority int        `json:"priority"`
	CreatedAt time.Time `json:"created_at"`
}

// Target holds parcel identifiers for a scrape task.
type Target struct {
	ParcelID string `json:"parcel_id"`
	State    string `json:"state"`
	County   string `json:"county"`
	URL      string `json:"url,omitempty"`
}

// WorkResponse is the response for GET /internal/work.
type WorkResponse struct {
	Tasks      []WorkTask `json:"tasks"`
	RetryAfter int        `json:"retry_after"`
}

// ParcelResult is submitted by workers.
type ParcelResult struct {
	TaskID          string                 `json:"task_id"`
	ParcelID        string                 `json:"parcel_id"`
	Platform        string                 `json:"platform"`
	State           string                 `json:"state"`
	County          string                 `json:"county"`
	Data            map[string]interface{} `json:"data"`
	ScrapedAt       time.Time              `json:"scraped_at"`
	ParseDurationMs int                    `json:"parse_duration_ms"`
	RawHTMLHash     string                 `json:"raw_html_hash,omitempty"`
}

// SubmitResponse is the response for POST /internal/results.
type SubmitResponse struct {
	Inserted int      `json:"inserted"`
	Updated  int      `json:"updated"`
	Failed   int      `json:"failed"`
	Errors   []string `json:"errors"`
}

// WorkerStatus is sent in heartbeat.
type WorkerStatus struct {
	ActiveTasks         int      `json:"active_tasks"`
	CompletedLastMinute int      `json:"completed_last_minute"`
	FailedLastMinute    int      `json:"failed_last_minute"`
	Platforms           []string `json:"platforms"`
	CPUPercent          float64  `json:"cpu_percent"`
	MemoryPercent       float64  `json:"memory_percent"`
}

// HeartbeatResponse is the response for POST /internal/heartbeat.
type HeartbeatResponse struct {
	Acknowledged bool     `json:"acknowledged"`
	Commands     []string `json:"commands"`
}
