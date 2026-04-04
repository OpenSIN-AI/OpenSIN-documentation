# Sin Youtube Agent — Agent Reference Card

> **Agent:** sin-youtube-agent | **Team:** Youtube | **Status:** Active

## Agent Card

```json
{
  "name": "sin-youtube-agent",
  "version": "1.0.0",
  "description": "Autonomous A2A agent for sin youtube agent",
  "team": "youtube",
  "model": "openrouter/qwen/qwen3.6-plus:free",
  "fallback": "openrouter/nvidia/nemotron-3-super-free",
  "capabilities": ["automation", "monitoring", "reporting", "self-healing"],
  "maxSteps": 999999,
  "reasoning": "high",
  "contextWindow": 1000000
}
```

## Quick Reference

| Property | Value |
|----------|-------|
| **Name** | sin-youtube-agent |
| **Team** | Youtube |
| **Model** | qwen/qwen3.6-plus:free |
| **Fallback** | nvidia/nemotron-3-super-free |
| **Context** | 1,000,000 tokens |
| **Max Steps** | 999,999 |
| **Reasoning** | High |

## MCP Dependencies

| MCP | Required | Purpose |
|-----|----------|---------|
| sin-telegrambot | Yes | Notifications |
| n8n-workflow-builder | Yes | Workflow management |
| webauto-nodriver | No | Browser automation |
| serena | No | Code intelligence |

## n8n Integration

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| Auto-Doc Sync | Every 2h | Documentation sync |
| Staleness Detector | Every 6h | Detect stale docs |
| Quality Calculator | Daily | Calculate quality score |

## Performance Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Response Time | < 30s | < 15s |
| Error Rate | < 1% | < 0.1% |
| Uptime | > 99.9% | > 99.99% |
| Task Success | > 95% | > 98% |

## Escalation Path

| Level | Contact | Response Time |
|-------|---------|---------------|
| L1 | Agent self-healing | Immediate |
| L2 | Team Orchestrator | 5 minutes |
| L3 | SIN-Zeus | 15 minutes |
| L4 | Ops Team | 30 minutes |

## Related Documents

- [Playbooks](../playbooks/sin-youtube-agent/)
- [Configuration](../fleet/configs/sin-youtube-agent.md)
- [Troubleshooting](../fleet/troubleshooting/sin-youtube-agent.md)
- [Integration Guide](../../integrations/agents/sin-youtube-agent.md)

---

*Last updated: 2026-04-04 by SIN-Zeus*
