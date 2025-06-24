package main

import (
    "encoding/json"
    "log"
    "net/http"
)

type Metadata struct {
    Name    string `json:"name"`
    Version string `json:"version"`
}

func metadataHandler(w http.ResponseWriter, r *http.Request) {
    meta := Metadata{Name: "mnist", Version: "v1.0"}
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(meta)
}

func main() {
    http.HandleFunc("/metadata", metadataHandler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}
