# Opencode Subagent Delegation — API Reference

> **Skill:** opencode-subagent-delegation | **Type:** OpenCode Skill

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/skills/opencode-subagent-delegation/status` | GET | Check skill status |
| `/skills/opencode-subagent-delegation/execute` | POST | Execute skill |
| `/skills/opencode-subagent-delegation/config` | GET | Get configuration |

## Request Format

```json
{
  "skill": "opencode-subagent-delegation",
  "action": "execute",
  "params": {}
}
```

## Response Format

```json
{
  "status": "success",
  "result": {},
  "timestamp": "2026-04-04T10:00:00Z"
}
```

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid parameters |
| 404 | Skill not found |
| 500 | Internal server error |

---

*Last updated: 2026-04-04 by SIN-Zeus*
