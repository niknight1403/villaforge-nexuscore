build:
	go build -o bin/nexuscore ./cmd/api

test:
	go test ./internal/...

smoke:
	./bin/nexuscore --mode=test & sleep 2 && curl -f http://localhost:8080/health || exit 1

all: build test smoke