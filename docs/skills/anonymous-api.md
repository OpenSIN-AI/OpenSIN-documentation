# Anonymous — API Reference

> **Skill:** anonymous | **Type:** OpenCode Skill

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/skills/anonymous/status` | GET | Check skill status |
| `/skills/anonymous/execute` | POST | Execute skill |
| `/skills/anonymous/config` | GET | Get configuration |

## Request Format

```json
{
  "skill": "anonymous",
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
