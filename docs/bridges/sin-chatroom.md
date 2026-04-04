# SIN-Chatroom — Universal Messenger Bridge Hub

## Overview
SIN-Chatroom connects ALL 37+ messaging platforms through Matrix bridges.

## Deployment
- **URL:** https://easeeeclip-A2A-SIN-Chatroom.hf.space
- **Account:** easeeeclip
- **Hardware:** cpu-basic (FREE $0/month)
- **Status:** ✅ RUNNING

## Endpoints
| Endpoint | URL | Status |
|----------|-----|--------|
| Health | /health | ✅ 200 OK |
| A2A Protocol | /a2a/v1 | ✅ 200 OK |
| Agent Card | /.well-known/agent-card.json | ✅ 200 OK |

## Supported Bridges (27+)
| Category | Bridges |
|----------|---------|
| Messenger | WhatsApp, Telegram, Signal, iMessage, SMS, Email |
| Social Media | X/Twitter, Reddit, Instagram, TikTok, YouTube, Medium, LinkedIn, Nostr |
| Enterprise | Slack, Teams, Google Chat, Zoom, WebChat |
| Gaming | Xbox, PlayStation, Nintendo |
| Protocols | Matrix, IRC, LINE, WeChat, Discord |

## A2A Protocol
```json
{
  "name": "SIN-Chatroom",
  "protocol": "A2A",
  "version": "1.0.0",
  "endpoints": {
    "post": "/a2a/v1",
    "card": "/.well-known/agent-card.json",
    "health": "/health"
  }
}
```

## Skills
- `connect_bridge` — Connect a messaging platform bridge
- `list_bridges` — List all connected bridges
- `send_message` — Send message via bridge
