package main

import (
	"fmt"
	"nexuscore/internal/core"
)

func main() {
	fmt.Println("Starting NexusCore...")
	core.StartGateway()
}