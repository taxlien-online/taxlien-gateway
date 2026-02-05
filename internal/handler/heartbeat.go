package handler

import (
	"encoding/json"
	"net/http"

	"github.com/taxlien/gateway/internal/model"
	"github.com/taxlien/gateway/internal/service"
)

// HeartbeatHandler handles POST /internal/heartbeat.
type HeartbeatHandler struct {
	Registry *service.WorkerRegistry
}

// Heartbeat handles POST /internal/heartbeat.
func (h *HeartbeatHandler) Heartbeat(w http.ResponseWriter, r *http.Request) {
	var status model.WorkerStatus
	if err := json.NewDecoder(r.Body).Decode(&status); err != nil {
		http.Error(w, "invalid JSON", http.StatusBadRequest)
		return
	}

	workerID := workerID(r)
	if err := h.Registry.Update(r.Context(), workerID, status); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	commands, _ := h.Registry.GetCommands(r.Context(), workerID)

	w.Header().Set("Content-Type", "application/json")
	_ = json.NewEncoder(w).Encode(model.HeartbeatResponse{
		Acknowledged: true,
		Commands:     commands,
	})
}
