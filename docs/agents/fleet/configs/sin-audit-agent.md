# Sin Audit Agent — Configuration Reference

> **Agent:** sin-audit-agent | **Status:** ✅ Active

## Configuration File

```yaml
agent:
  name: sin-audit-agent
  model: openrouter/qwen/qwen3.6-plus:free
  fallback: openrouter/nvidia/nemotron-3-super-free
  maxSteps: 999999
  reasoning: high
  capabilities:
    - automation
    - monitoring
    - reporting
    - self-healing
```

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `SIN_AUDIT_AGENT_API_KEY` | No | — | API key for external services |
| `SIN_AUDIT_AGENT_ENDPOINT` | No | — | Custom endpoint URL |
| `SIN_AUDIT_AGENT_TIMEOUT` | No | 30 | Request timeout in seconds |

## MCP Dependencies

| MCP | Required | Purpose |
|-----|----------|---------|
| sin-telegrambot | Yes | Notifications |
| n8n-workflow-builder | Yes | Workflow management |
| webauto-nodriver | No | Browser automation |

## Performance Tuning

| Setting | Recommended | Description |
|---------|-------------|-------------|
| maxSteps | 999999 | Maximum execution steps |
| reasoning | high | Reasoning depth |
| context | 1000000 | Context window size |

---

*Last updated: 2026-04-04 by SIN-Zeus*
