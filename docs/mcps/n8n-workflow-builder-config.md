# n8n-workflow-builder — Configuration Reference

> **Status:** ✅ Active | **Type:** MCP Server

## Configuration

```json
{
  "type": "local",
  "command": [
    "npx",
    "-y",
    "mcp-n8n-builder"
  ],
  "environment": {
    "N8N_HOST": "http://92.5.60.87:5678/api/v1",
    "N8N_API_KEY": "n8n_api_69175bcabef4b10d619b43598cd557a92ee38aac5ae4b1ca",
    "OUTPUT_VERBOSITY": "concise"
  },
  "enabled": true
}
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| API_KEY | Yes | API key for the service |
| BASE_URL | No | Custom base URL |

## Troubleshooting

Common issues and solutions.

---

*Last updated: 2026-04-04 by SIN-Zeus*
