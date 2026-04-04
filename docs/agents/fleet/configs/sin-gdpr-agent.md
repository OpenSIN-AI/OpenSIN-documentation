# Sin Gdpr Agent — Configuration Reference

> **Agent:** sin-gdpr-agent | **Team:** Gdpr | **Status:** ✅ Active

## Agent Card

```json
{
  "name": "sin-gdpr-agent",
  "version": "1.0.0",
  "description": "Autonomous A2A agent for sin gdpr agent",
  "team": "gdpr",
  "model": "openrouter/qwen/qwen3.6-plus:free",
  "fallback": "openrouter/nvidia/nemotron-3-super-free",
  "capabilities": ["automation", "monitoring", "reporting", "self-healing"],
  "maxSteps": 999999,
  "reasoning": "high"
}
```

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `SIN_GDPR_AGENT_API_KEY` | No | — | API key for external services |
| `SIN_GDPR_AGENT_ENDPOINT` | No | — | Custom endpoint URL |
| `SIN_GDPR_AGENT_TIMEOUT` | No | 30 | Request timeout in seconds |
| `SIN_GDPR_AGENT_RETRIES` | No | 3 | Number of retries on failure |
| `SIN_GDPR_AGENT_LOG_LEVEL` | No | info | Logging level |

## MCP Dependencies

| MCP | Required | Purpose |
|-----|----------|---------|
| sin-telegrambot | Yes | Notifications and alerts |
| n8n-workflow-builder | Yes | Workflow management |
| webauto-nodriver | No | Browser automation |
| serena | No | Code intelligence |

## Performance Tuning

| Setting | Recommended | Description |
|---------|-------------|-------------|
| maxSteps | 999999 | Maximum execution steps |
| reasoning | high | Reasoning depth |
| context | 1000000 | Context window size |
| timeout | 300 | Request timeout |

## Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Response Time | < 30s | Telegram alert |
| Error Rate | < 1% | GitHub issue |
| Uptime | > 99.9% | Ops escalation |
| Task Success | > 95% | Team notification |

---

*Last updated: 2026-04-04 by SIN-Zeus*
