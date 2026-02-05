package handler

import (
	"encoding/json"
	"net/http"
	"os"
	"path/filepath"
	"strings"
	"time"

	appmw "github.com/taxlien/gateway/internal/middleware"
)

// RawFilesHandler handles POST /internal/raw-files.
type RawFilesHandler struct {
	StoragePath string
}

// UploadRawFile handles multipart form: file + metadata.
func (h *RawFilesHandler) UploadRawFile(w http.ResponseWriter, r *http.Request) {
	if err := r.ParseMultipartForm(32 << 20); err != nil {
		appmw.RespondError(w, http.StatusBadRequest, "INVALID_REQUEST", "failed to parse multipart form")
		return
	}

	file, fh, err := r.FormFile("file")
	if err != nil {
		appmw.RespondError(w, http.StatusBadRequest, "INVALID_REQUEST", "missing file")
		return
	}
	defer file.Close()

	filename := sanitizeFilename(fh.Filename)
	if filename == "" {
		filename = "raw_" + time.Now().Format("20060102_150405")
	}

	if err := os.MkdirAll(h.StoragePath, 0755); err != nil {
		appmw.RespondError(w, http.StatusInternalServerError, "INTERNAL_ERROR", err.Error())
		return
	}

	path := filepath.Join(h.StoragePath, filename)
	dst, err := os.Create(path)
	if err != nil {
		appmw.RespondError(w, http.StatusInternalServerError, "INTERNAL_ERROR", err.Error())
		return
	}
	defer dst.Close()

	if _, err := dst.ReadFrom(file); err != nil {
		appmw.RespondError(w, http.StatusInternalServerError, "INTERNAL_ERROR", err.Error())
		return
	}

	w.Header().Set("Content-Type", "application/json")
	_ = json.NewEncoder(w).Encode(map[string]string{"status": "ok", "path": path})
}

func sanitizeFilename(s string) string {
	s = filepath.Base(s)
	s = strings.TrimSpace(s)
	s = strings.ReplaceAll(s, "..", "")
	if len(s) > 200 {
		s = s[:200]
	}
	if s == "" || s == "." {
		return ""
	}
	return s
}
