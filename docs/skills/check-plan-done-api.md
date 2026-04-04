# Check Plan Done — API Reference

> **Skill:** check-plan-done | **Type:** OpenCode Skill

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/skills/check-plan-done/status` | GET | Check skill status |
| `/skills/check-plan-done/execute` | POST | Execute skill |
| `/skills/check-plan-done/config` | GET | Get configuration |

## Request Format

```json
{
  "skill": "check-plan-done",
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
