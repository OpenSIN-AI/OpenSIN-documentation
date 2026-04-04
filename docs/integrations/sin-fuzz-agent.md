# Sin Fuzz Agent — Integration Guide

> **Agent:** sin-fuzz-agent | **Category:** A2A Agent Integration | **Status:** Active

## Overview

This guide provides detailed integration instructions for the Sin Fuzz Agent within the OpenSIN-AI ecosystem.

## Prerequisites

- OpenCode CLI installed and configured
- Access to OpenSIN-AI organization
- n8n workflow engine running
- Supabase database accessible
- Telegram bot configured

## Agent Configuration

```json
{
  "agent": {
    "sin-fuzz-agent": {
      "model": "openrouter/qwen/qwen3.6-plus:free",
      "fallback": "openrouter/nvidia/nemotron-3-super-free",
      "maxSteps": 999999,
      "reasoning": "high",
      "capabilities": ["automation", "monitoring", "reporting", "self-healing"]
    }
  }
}
```

## MCP Dependencies

| MCP | Required | Purpose |
|-----|----------|---------|
| sin-telegrambot | Yes | Notifications and alerts |
| n8n-workflow-builder | Yes | Workflow management |
| webauto-nodriver | No | Browser automation |
| serena | No | Code intelligence |

## n8n Integration

The agent integrates with n8n through the following workflows:
- Auto-Documentation Sync Engine
- Documentation Staleness Detector
- Cross-Repo Documentation Consistency Checker
- Quality Score Calculator

## Supabase Integration

The agent stores data in the following Supabase tables:
- `agent_registry` — Agent registration and status
- `work_items` — Task queue
- `incidents` — Incident tracking
- `agent_metrics` — Performance metrics

## Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Response Time | < 30s | Telegram alert |
| Error Rate | < 1% | GitHub issue |
| Uptime | > 99.9% | Ops escalation |
| Task Success | > 95% | Team notification |

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Agent offline | Check model availability, restart agent |
| High error rate | Verify API credentials, check rate limits |
| Slow response | Check network latency, switch to fallback model |
| Token exhausted | Trigger token rotation, wait for refill |

## Related Documents

- [Agent Playbooks](../../agents/playbooks/sin-fuzz-agent/)
- [Agent Configuration](../../agents/fleet/configs/sin-fuzz-agent.md)
- [Agent Troubleshooting](../../agents/fleet/troubleshooting/sin-fuzz-agent.md)

---

*Last updated: 2026-04-04 by SIN-Zeus*
