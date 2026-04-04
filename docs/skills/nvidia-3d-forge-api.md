# Nvidia 3D Forge — API Reference

> **Skill:** nvidia-3d-forge | **Type:** OpenCode Skill

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/skills/nvidia-3d-forge/status` | GET | Check skill status |
| `/skills/nvidia-3d-forge/execute` | POST | Execute skill |
| `/skills/nvidia-3d-forge/config` | GET | Get configuration |

## Request Format

```json
{
  "skill": "nvidia-3d-forge",
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
