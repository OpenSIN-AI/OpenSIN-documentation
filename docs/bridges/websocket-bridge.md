# WebSocket Bridge

> **Status:** ✅ Active | **Type:** Real-time Communication

## Overview

WebSocket bridge enables real-time bidirectional communication between OpenSIN agents and external services.

## Architecture

```
Client ↔ WebSocket ↔ OpenSIN Agent ↔ MCP ↔ External Service
```

## Configuration

```json
{
  "websocket": {
    "port": 8080,
    "path": "/ws",
    "auth": "token"
  }
}
```

## Usage

Agents use WebSocket for real-time updates, streaming responses, and live data feeds.

---

*Last updated: 2026-04-04 by SIN-Zeus*
