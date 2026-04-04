# Create A2A Mcp — API Reference

> **Skill:** create-a2a-mcp | **Type:** OpenCode Skill

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/skills/create-a2a-mcp/status` | GET | Check skill status |
| `/skills/create-a2a-mcp/execute` | POST | Execute skill |
| `/skills/create-a2a-mcp/config` | GET | Get configuration |

## Request Format

```json
{
  "skill": "create-a2a-mcp",
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
