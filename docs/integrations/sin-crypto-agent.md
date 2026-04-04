# Sin Crypto Agent — Integration Guide

> **Agent:** sin-crypto-agent | **Category:** A2A Agent Integration | **Status:** Active

## Overview

This guide provides detailed integration instructions for the Sin Crypto Agent within the OpenSIN-AI ecosystem.

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
    "sin-crypto-agent": {
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
- agent_registry — Agent registration and status
- work_items — Task queue
- incidents — Incident tracking
- agent_metrics — Performance metrics

## Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Response Time | Less than 30s | Telegram alert |
| Error Rate | Less than 1 percent | GitHub issue |
| Uptime | Greater than 99.9 percent | Ops escalation |
| Task Success | Greater than 95 percent | Team notification |

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Agent offline | Check model availability, restart agent |
| High error rate | Verify API credentials, check rate limits |
| Slow response | Check network latency, switch to fallback model |
| Token exhausted | Trigger token rotation, wait for refill |

## Related Documents

- Agent Playbooks
- Agent Configuration
- Agent Troubleshooting

---

*Last updated: 2026-04-04 by SIN-Zeus*
