# Sora — API Reference

> **Skill:** sora | **Type:** OpenCode Skill

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/skills/sora/status` | GET | Check skill status |
| `/skills/sora/execute` | POST | Execute skill |
| `/skills/sora/config` | GET | Get configuration |

## Request Format

```json
{
  "skill": "sora",
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
