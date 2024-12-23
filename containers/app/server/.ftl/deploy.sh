#!/bin/bash
# .ftl/deploy.sh

set -e

# Hetzner Deployment Script
deploy_to_hetzner() {
    local environment=$1

    # Validate input
    if [[ -z "$environment" ]]; then
        echo "Usage: $0 <environment>"
        exit 1
    }

    # Authenticate with Hetzner Cloud
    hcloud context create agility-game-server

    # Create server group
    ftl server create \
        --name "agility-game-server-${environment}" \
        --type cx21 \
        --image docker \
        --location fsn1

    # Deploy Docker container
    ftl container deploy \
        --image "agilitygame/agility-game-server:latest" \
        --port 5000 \
        --environment "$environment"

    # Configure networking
    ftl network configure \
        --domain "agility-game-server-${environment}.agility-game.com" \
        --ssl-certificate

    echo "Deployment to ${environment} completed successfully!"
}

# Run deployment
deploy_to_hetzner "$@"