# Deployment Guide

## Overview

This guide covers deploying OpenSIN to production.

## Prerequisites

- Docker and Docker Compose
- Server with at least 4GB RAM
- Domain name (optional)
- SSL certificate (optional)

## Step 1: Clone Repository

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN.git
cd OpenSIN
```

## Step 2: Configure Environment

Create `.env` file:

```env
NODE_ENV=production
PORT=3000
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
TELEGRAM_BOT_TOKEN=your_token
DISCORD_BOT_TOKEN=your_token
```

## Step 3: Deploy with Docker

```bash
docker-compose up -d
```

## Step 4: Verify Deployment

```bash
curl http://localhost:3000/health
```

## Step 5: Set Up SSL

```bash
# Using Let's Encrypt
certbot --nginx -d your-domain.com
```

## Step 6: Set Up Monitoring

```bash
docker-compose -f docker-compose.monitoring.yml up -d
```

## Scaling

```bash
docker-compose up -d --scale opensin-core=3
```

## Backup

```bash
# Backup database
docker exec postgres pg_dump -U opensin opensin > backup.sql

# Backup volumes
docker-compose cp opensin-core:/app/data ./backup
```

## Next Steps
- [Monitoring](/guide/monitoring)
- [Scaling](/guide/scaling)
- [Troubleshooting](/guide/troubleshooting)
