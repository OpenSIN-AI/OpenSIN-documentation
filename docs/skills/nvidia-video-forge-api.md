# Nvidia Video Forge — API Reference

> **Skill:** nvidia-video-forge | **Type:** OpenCode Skill

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/skills/nvidia-video-forge/status` | GET | Check skill status |
| `/skills/nvidia-video-forge/execute` | POST | Execute skill |
| `/skills/nvidia-video-forge/config` | GET | Get configuration |

## Request Format

```json
{
  "skill": "nvidia-video-forge",
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
