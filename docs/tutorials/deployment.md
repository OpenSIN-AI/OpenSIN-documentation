# Tutorial: Deploying OpenSIN

## Duration: 45 minutes
## Difficulty: Advanced

## Step 1: Clone Repository

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN.git
cd OpenSIN
```

## Step 2: Configure Environment

```env
NODE_ENV=production
PORT=3000
OPENAI_API_KEY=your_key
TELEGRAM_BOT_TOKEN=your_token
DISCORD_BOT_TOKEN=your_token
```

## Step 3: Deploy with Docker

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
- [Monitoring](../guide/monitoring.md)
- [Scaling](../guide/scaling.md)
