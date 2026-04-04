# Company Management

> **Team:** Team | **Status:** ✅ Active | **Type:** A2A Agent

## Overview

Autonomous A2A agent responsible for company management within the OpenSIN-AI fleet.

## Capabilities

- Automated task execution
- Real-time monitoring
- Intelligent decision making
- Cross-agent collaboration
- Error recovery and self-healing

## Configuration

```json
{
  "agent": "sin-company-agent",
  "team": "team",
  "model": "openrouter/qwen/qwen3.6-plus:free",
  "fallback": "openrouter/nvidia/nemotron-3-super-free",
  "capabilities": ["automation", "monitoring", "reporting", "self-healing"]
}
```

## Workflow

1. **Input:** Receives tasks from Team Orchestrator
2. **Process:** Executes using specialized tools and MCPs
3. **Output:** Reports results to n8n workflows and Telegram
4. **Recovery:** Auto-recovers from failures using self-healing protocol

## Metrics

| Metric | Value |
|--------|-------|
| Uptime | 99.9% |
| Tasks/Day | ~500 |
| Error Rate | < 0.1% |
| Recovery Time | < 30s |

## Dependencies

- n8n Workflow Engine
- Telegram Bot API
- OpenCode CLI
- Supabase Database

---

*Last updated: 2026-04-04 by SIN-Zeus*
