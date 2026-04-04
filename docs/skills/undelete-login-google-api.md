# Undelete Login Google — API Reference

> **Skill:** undelete-login-google | **Type:** OpenCode Skill

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/skills/undelete-login-google/status` | GET | Check skill status |
| `/skills/undelete-login-google/execute` | POST | Execute skill |
| `/skills/undelete-login-google/config` | GET | Get configuration |

## Request Format

```json
{
  "skill": "undelete-login-google",
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
