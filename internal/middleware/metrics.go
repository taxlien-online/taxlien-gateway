package middleware

import (
	"net/http"
	"strconv"
	"time"

	"github.com/go-chi/chi/v5"
	"github.com/taxlien/gateway/internal/metrics"
)

// Metrics records Prometheus metrics for each request.
func Metrics(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		wrapped := &metricsResponseWriter{ResponseWriter: w, status: http.StatusOK}
		next.ServeHTTP(wrapped, r)

		path := r.URL.Path
		if p := chi.RouteContext(r.Context()).RoutePattern(); p != "" {
			path = p
		}
		status := strconv.Itoa(wrapped.status)
		method := r.Method

		metrics.RequestsTotal.WithLabelValues(method, path, status).Inc()
		metrics.RequestDurationSeconds.WithLabelValues(method, path).Observe(time.Since(start).Seconds())
	})
}

type metricsResponseWriter struct {
	http.ResponseWriter
	status int
}

func (w *metricsResponseWriter) WriteHeader(code int) {
	w.status = code
	w.ResponseWriter.WriteHeader(code)
}
