# Deployment Guide

## Prerequisites

- Docker and Docker Compose
- Server with 4GB+ RAM
- Domain name (optional)

## Step 1: Clone

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN.git
cd OpenSIN
```

## Step 2: Configure

```env
NODE_ENV=production
PORT=3000
OPENAI_API_KEY=your_key
TELEGRAM_BOT_TOKEN=your_token
DISCORD_BOT_TOKEN=your_token
```

## Step 3: Deploy

```bash
docker-compose up -d
```

## Step 4: Verify

```bash
curl http://localhost:3000/health
```

## Scaling

```bash
docker-compose up -d --scale opensin-core=3
```

## Next Steps
- [Monitoring](/guide/monitoring)
- [Scaling](/guide/scaling)
