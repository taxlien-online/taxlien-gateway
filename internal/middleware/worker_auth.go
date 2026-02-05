package middleware

import (
	"encoding/json"
	"net/http"
)

// WorkerAuth validates X-Worker-Token. Returns 401 if invalid.
func WorkerAuth(tokens map[string]struct{}) func(http.Handler) http.Handler {
	return func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			token := r.Header.Get("X-Worker-Token")
			if token == "" {
				RespondError(w, http.StatusUnauthorized, "UNAUTHORIZED", "Missing X-Worker-Token")
				return
			}
			if _, ok := tokens[token]; !ok {
				RespondError(w, http.StatusUnauthorized, "UNAUTHORIZED", "Invalid X-Worker-Token")
				return
			}
			next.ServeHTTP(w, r)
		})
	}
}

type errorResp struct {
	Error struct {
		Code    string `json:"code"`
		Message string `json:"message"`
	} `json:"error"`
	RequestID string `json:"request_id,omitempty"`
}

// RespondError writes a JSON error response.
func RespondError(w http.ResponseWriter, status int, code, message string) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(errorResp{
		Error: struct {
			Code    string `json:"code"`
			Message string `json:"message"`
		}{Code: code, Message: message},
	})
}
