package handler

import (
	"encoding/json"
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/taxlien/gateway/internal/service"
)

// TasksHandler handles POST /internal/tasks/{id}/complete and /fail.
type TasksHandler struct {
	Queue *service.Queue
}

// CompleteTask handles POST /internal/tasks/{taskID}/complete.
func (h *TasksHandler) CompleteTask(w http.ResponseWriter, r *http.Request) {
	taskID := chi.URLParam(r, "taskID")
	workerID := workerID(r)

	ok, err := h.Queue.CompleteTask(r.Context(), workerID, taskID)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	_ = json.NewEncoder(w).Encode(map[string]bool{"success": ok})
}

// FailTask handles POST /internal/tasks/{taskID}/fail.
func (h *TasksHandler) FailTask(w http.ResponseWriter, r *http.Request) {
	taskID := chi.URLParam(r, "taskID")
	workerID := workerID(r)

	ok, err := h.Queue.FailTask(r.Context(), workerID, taskID)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	_ = json.NewEncoder(w).Encode(map[string]interface{}{"status": "reported", "success": ok})
}
