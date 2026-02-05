package handler

import (
	"net/http"
)

const workerIDHeader = "X-Worker-ID"

func workerID(r *http.Request) string {
	if id := r.Header.Get(workerIDHeader); id != "" {
		return id
	}
	return "unknown"
}
