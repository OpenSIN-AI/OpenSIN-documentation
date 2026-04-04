# Docker Compose Deployment

> **Status:** ✅ Active | **Type:** Container Deployment

## Overview

Docker Compose deploys the full OpenSIN stack on OCI VM.

## docker-compose.yml

```yaml
version: '3.8'
services:
  n8n:
    image: docker.n8n.io/n8nio/n8n:latest
    ports:
      - "5678:5678"
    environment:
      - N8N_API_KEY_ENABLED=true
      - N8N_SECURE_COOKIE=false
    volumes:
      - n8n_data:/home/node/.n8n

  supabase-db:
    image: supabase/postgres:15
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  n8n_data:
  db_data:
```

## Usage

```bash
docker-compose up -d
docker-compose ps
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
