package server

import (
	"context"
	"fmt"
	"net/http"

	"github.com/go-chi/chi/v5"
	chimw "github.com/go-chi/chi/v5/middleware"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"github.com/taxlien/gateway/internal/config"
	"github.com/taxlien/gateway/internal/handler"
	appmw "github.com/taxlien/gateway/internal/middleware"
	"go.uber.org/zap"
)

// Server runs the internal API on :8081.
type Server struct {
	cfg    *config.Config
	log    *zap.Logger
	router chi.Router
	http   *http.Server
}

// New creates a new server.
func New(cfg *config.Config, log *zap.Logger, deps *Deps) *Server {
	r := chi.NewRouter()

	r.Use(appmw.RequestID)
	r.Use(chimw.Recoverer)
	r.Use(chimw.RealIP)
	r.Use(appmw.Metrics)
	r.Use(appmw.Logging(log))

	r.Get("/health", handler.Health)
	r.Handle("/metrics", promhttp.Handler())

	r.Group(func(r chi.Router) {
		r.Use(appmw.WorkerAuth(cfg.WorkerTokens))
		r.Route("/internal", func(r chi.Router) {
			r.Get("/work", deps.Work.GetWork)
			r.Post("/results", deps.Results.SubmitResults)
			r.Post("/tasks/{taskID}/complete", deps.Tasks.CompleteTask)
			r.Post("/tasks/{taskID}/fail", deps.Tasks.FailTask)
			r.Post("/raw-files", deps.RawFiles.UploadRawFile)
			r.Post("/heartbeat", deps.Heartbeat.Heartbeat)
		})
	})

	addr := fmt.Sprintf(":%d", cfg.Port)
	return &Server{
		cfg:  cfg,
		log:  log,
		router: r,
		http: &http.Server{
			Addr:    addr,
			Handler: r,
		},
	}
}

// Start starts the HTTP server.
func (s *Server) Start() error {
	s.log.Info("starting server", zap.String("addr", s.http.Addr))
	return s.http.ListenAndServe()
}

// Shutdown gracefully stops the server.
func (s *Server) Shutdown(ctx context.Context) error {
	return s.http.Shutdown(ctx)
}
