# Enterprise Deep Debug — API Reference

> **Skill:** enterprise-deep-debug | **Type:** OpenCode Skill

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/skills/enterprise-deep-debug/status` | GET | Check skill status |
| `/skills/enterprise-deep-debug/execute` | POST | Execute skill |
| `/skills/enterprise-deep-debug/config` | GET | Get configuration |

## Request Format

```json
{
  "skill": "enterprise-deep-debug",
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
