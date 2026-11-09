package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		fmt.Fprintf(w, "{\"status\":\"ok\"}")
	})
	fmt.Println("NexusCore API starting on :8080")
	http.ListenAndServe(":8080", nil)
}