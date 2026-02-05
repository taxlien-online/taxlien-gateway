package handler

import (
	"encoding/json"
	"net/http"
	"strconv"

	"github.com/taxlien/gateway/internal/model"
	"github.com/taxlien/gateway/internal/service"
)

// WorkHandler handles /internal/work.
type WorkHandler struct {
	Queue *service.Queue
}

// GetWork handles GET /internal/work.
func (h *WorkHandler) GetWork(w http.ResponseWriter, r *http.Request) {
	workerID := workerID(r)
	capacity, _ := strconv.Atoi(r.URL.Query().Get("capacity"))
	if capacity <= 0 {
		capacity = 10
	}
	if capacity > 100 {
		capacity = 100
	}
	platforms := r.URL.Query()["platforms"]
	if len(platforms) == 0 {
		platforms = []string{"beacon", "qpublic", "floridatax"}
	}

	tasks, err := h.Queue.PopTasks(r.Context(), workerID, platforms, capacity)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	retryAfter := 30
	if len(tasks) > 0 {
		retryAfter = 5
	}

	w.Header().Set("Content-Type", "application/json")
	_ = json.NewEncoder(w).Encode(model.WorkResponse{
		Tasks:      tasks,
		RetryAfter: retryAfter,
	})
}
