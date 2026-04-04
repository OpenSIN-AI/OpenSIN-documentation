# N8N Self Hosted Deployment

> **Category:** Deployment Guide | **Difficulty:** Intermediate | **Status:** ✅ Active

## Overview

This guide provides step-by-step instructions for n8n self hosted deployment in the OpenSIN-AI ecosystem.

## Prerequisites

- Docker installed
- Access to OpenSIN-AI repositories
- Required credentials configured
- Network access to target environment

## Step-by-Step Guide

### Step 1: Preparation

```bash
# Clone the repository
git clone git@github.com:OpenSIN-AI/n8n-self-hosted-deployment.git
cd n8n-self-hosted-deployment
```

### Step 2: Configuration

```bash
# Copy environment template
cp .env.example .env
# Edit with your credentials
nano .env
```

### Step 3: Build

```bash
# Build the application
docker build -t opensin/n8n-self-hosted-deployment:latest .
```

### Step 4: Deploy

```bash
# Deploy to target environment
docker-compose up -d
# or
kubectl apply -f k8s/
```

### Step 5: Verify

```bash
# Check deployment status
docker ps
# or
kubectl get pods
```

## Configuration Reference

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| API_KEY | Yes | — | API key for authentication |
| ENDPOINT | No | https://api.opensin.ai | API endpoint URL |
| LOG_LEVEL | No | info | Logging level |
| PORT | No | 8080 | Service port |

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Build fails | Check Dockerfile syntax |
| Deployment fails | Verify credentials |
| Service unreachable | Check network configuration |

## Rollback

```bash
# Rollback to previous version
docker-compose down
docker-compose up -d opensin/n8n-self-hosted-deployment:previous
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
