package handler

import (
	"encoding/json"
	"net/http"

	"github.com/taxlien/gateway/internal/model"
	"github.com/taxlien/gateway/internal/service"
)

// ResultsHandler handles POST /internal/results.
type ResultsHandler struct {
	Queue      *service.Queue
	Properties *service.Properties
}

// SubmitResults handles POST /internal/results.
func (h *ResultsHandler) SubmitResults(w http.ResponseWriter, r *http.Request) {
	var results []model.ParcelResult
	if err := json.NewDecoder(r.Body).Decode(&results); err != nil {
		http.Error(w, "invalid JSON", http.StatusBadRequest)
		return
	}

	workerID := workerID(r)
	resp := model.SubmitResponse{}

	for _, res := range results {
		inserted, err := h.Properties.UpsertParcel(r.Context(), res, workerID)
		if err != nil {
			resp.Failed++
			resp.Errors = append(resp.Errors, res.ParcelID+": "+err.Error())
			if len(resp.Errors) > 10 {
				break
			}
			continue
		}
		if inserted {
			resp.Inserted++
		} else {
			resp.Updated++
		}
		_, _ = h.Queue.CompleteTask(r.Context(), workerID, res.TaskID)
	}

	w.Header().Set("Content-Type", "application/json")
	_ = json.NewEncoder(w).Encode(resp)
}
