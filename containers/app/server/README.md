# Message Board

[![PyPI - Version](https://img.shields.io/pypi/v/agility-game.svg)](https://pypi.org/project/agility-game)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/agility-game.svg)](https://pypi.org/project/agility-game)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install agility-game
```

# Hetzner Deployment with Faster Than Light (FTL)

## Prerequisites
- Hetzner Cloud Account
- Hetzner API Token
- FTL CLI installed
- Docker Image on Docker Hub

## FTL Configuration (.ftl/config.yaml)
```yaml
project_name: flask-application
version: 0.1.0

# Hetzner-specific configuration
cloud_provider: hetzner
region: fsn1  # Falkenstein, Germany
server_type: cx21  # 2 vCPU, 4GB RAM

# Deployment Configuration
deployment:
  container_registry: dockerhub
  container_image: yourusername/flask-application
  port: 5000
  health_check_path: /health

# Infrastructure Provisioning
infrastructure:
  firewall_rules:
    - direction: inbound
      protocol: tcp
      port: 80
    - direction: inbound
      protocol: tcp
      port: 443
    - direction: inbound
      protocol: tcp
      port: 5000

# Networking
networking:
  load_balancer: true
  domain: yourdomain.com
  ssl_certificate: true

# Scaling and Updates
scaling:
  min_instances: 1
  max_instances: 3
  update_strategy: rolling_update
```

## FTL Deployment Script (.ftl/deploy.sh)
```bash
#!/bin/bash
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
    hcloud context create flask-application

    # Create server group
    ftl server create \
        --name "flask-app-${environment}" \
        --type cx21 \
        --image docker \
        --location fsn1

    # Deploy Docker container
    ftl container deploy \
        --image "yourusername/flask-application:latest" \
        --port 5000 \
        --environment "$environment"

    # Configure networking
    ftl network configure \
        --domain "flask-${environment}.yourdomain.com" \
        --ssl-certificate

    echo "Deployment to ${environment} completed successfully!"
}

# Run deployment
deploy_to_hetzner "$@"
```

## GitHub Actions Workflow for Hetzner Deployment
```yaml
name: Hetzner Deployment with FTL

on:
  push:
    branches:
      - main
      - staging
      - develop

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install FTL CLI
        run: |
          wget https://github.com/your-org/ftl/releases/latest/download/ftl-linux-amd64
          chmod +x ftl-linux-amd64
          sudo mv ftl-linux-amd64 /usr/local/bin/ftl

      - name: Determine Environment
        id: set-env
        run: |
          if [[ "${{ github.ref }}" == "refs/heads/main" ]]; then
            echo "environment=production" >> $GITHUB_OUTPUT
          elif [[ "${{ github.ref }}" == "refs/heads/staging" ]]; then
            echo "environment=staging" >> $GITHUB_OUTPUT
          else
            echo "environment=development" >> $GITHUB_OUTPUT
          fi

      - name: Configure Hetzner Credentials
        run: |
          echo "${{ secrets.HETZNER_API_TOKEN }}" | ftl auth login

      - name: Deploy with FTL
        run: |
          chmod +x .ftl/deploy.sh
          .ftl/deploy.sh ${{ steps.set-env.outputs.environment }}

      - name: Health Check
        run: |
          sleep 60
          curl https://flask-${{ steps.set-env.outputs.environment }}.yourdomain.com/health
```

## Required Secrets and Configuration
1. Docker Hub
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`

2. Hetzner Cloud
   - `HETZNER_API_TOKEN`

3. Domain and SSL
   - Configure DNS for your domain
   - Obtain SSL certificate (Let's Encrypt recommended)

## Deployment Environments
- `develop` → Development server
- `staging` → Staging server
- `main` → Production server

## Post-Deployment Steps
1. Set up monitoring
2. Configure log rotation
3. Implement backup strategy
4. Set up alerts for server health
```

## License

`agility-game` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
