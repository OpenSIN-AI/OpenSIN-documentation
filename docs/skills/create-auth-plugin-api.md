# Create Auth Plugin — API Reference

> **Skill:** create-auth-plugin | **Type:** OpenCode Skill

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/skills/create-auth-plugin/status` | GET | Check skill status |
| `/skills/create-auth-plugin/execute` | POST | Execute skill |
| `/skills/create-auth-plugin/config` | GET | Get configuration |

## Request Format

```json
{
  "skill": "create-auth-plugin",
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
