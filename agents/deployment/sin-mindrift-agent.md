# Sin Mindrift Agent — Deployment Guide

> **Agent:** sin-mindrift-agent | **Category:** A2A Agent Deployment | **Version:** 1.0 | **Status:** Active

## Overview

This guide provides step-by-step deployment instructions for the Sin Mindrift Agent.

## Prerequisites

- OpenCode CLI installed and configured
- Access to OpenSIN-AI organization
- n8n workflow engine running
- Supabase database accessible
- Telegram bot configured
- HF Spaces account (if deploying to HF)

## Deployment Architecture

```
[OpenCode] → [A2A Protocol] → [Agent Runtime] → [MCP Servers] → [External APIs]
```

## Deployment Steps

### Step 1: Clone Repository
```bash
git clone git@github.com:OpenSIN-AI/sin-mindrift-agent.git
cd sin-mindrift-agent
```

### Step 2: Install Dependencies
```bash
npm install  # or pip install -r requirements.txt
```

### Step 3: Configure Environment
```bash
cp .env.example .env
# Edit .env with your credentials:
# - OPENROUTER_API_KEY
# - TELEGRAM_BOT_TOKEN
# - TELEGRAM_CHAT_ID
# - SUPABASE_URL
# - SUPABASE_KEY
```

### Step 4: Register Agent
```bash
# Register agent in Supabase
curl -X POST http://92.5.60.87:8006/rest/v1/agent_registry \
  -H "apikey: $SUPABASE_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "sin-mindrift-agent", "status": "active", "model": "openrouter/qwen/qwen3.6-plus:free"}'
```

### Step 5: Configure n8n Integration
1. Open n8n UI at http://92.5.60.87:5678
2. Navigate to the agent's workflow
3. Configure credentials
4. Activate the workflow

### Step 6: Deploy to HF Spaces (Optional)
```bash
# Deploy to Hugging Face Spaces
huggingface-cli repo create sin-mindrift-agent --type space --space_sdk docker
git push https://huggingface.co/spaces/delqhi/sin-mindrift-agent
```

### Step 7: Verify Deployment
```bash
# Check agent health
curl http://localhost:8080/health

# Check n8n workflow
curl -s http://92.5.60.87:5678/api/v1/workflows \
  -H "X-N8N-API-KEY: $N8N_API_KEY"

# Check Supabase registration
curl http://92.5.60.87:8006/rest/v1/agent_registry?name=eq.sin-mindrift-agent \
  -H "apikey: $SUPABASE_KEY"
```

## Configuration Reference

| Setting | Value | Description |
|---------|-------|-------------|
| Model | openrouter/qwen/qwen3.6-plus:free | Primary LLM model |
| Fallback | openrouter/nvidia/nemotron-3-super-free | Fallback model |
| Max Steps | 999999 | Maximum execution steps |
| Reasoning | high | Reasoning depth |
| Context Window | 1000000 | Context window size |

## Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Response Time | < 30s | Telegram |
| Error Rate | < 1% | GitHub Issue |
| Uptime | > 99.9% | Ops escalation |
| Task Success | > 95% | Team notification |

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Agent not starting | Check model availability, credentials |
| High error rate | Verify API credentials, rate limits |
| Slow response | Switch to fallback model |
| Token exhausted | Trigger token rotation |

## Related Documents

- [Agent Reference Card](../reference-cards/sin-mindrift-agent.md)
- [Integration Guide](../../integrations/agents/sin-mindrift-agent.md)
- [Team Playbook](../team-playbooks/)
- [Agent Configuration](../fleet/configs/sin-mindrift-agent.md)

---

*Last updated: 2026-04-04 by SIN-Zeus*
