# Sin Vision Colab — API Reference

> **Skill:** sin-vision-colab | **Type:** OpenCode Skill

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/skills/sin-vision-colab/status` | GET | Check skill status |
| `/skills/sin-vision-colab/execute` | POST | Execute skill |
| `/skills/sin-vision-colab/config` | GET | Get configuration |

## Request Format

```json
{
  "skill": "sin-vision-colab",
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
