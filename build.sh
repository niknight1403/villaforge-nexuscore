#!/bin/bash

# Install dependencies
make install

# Run tests
make test

# Build project
make build

# Run smoke tests
make smoke

# Deploy
make deploy
