# sin-passwordmanager — Configuration Reference

> **Status:** ✅ Active | **Type:** MCP Server

## Configuration

```json
{
  "type": "local",
  "command": [
    "node",
    "/Users/jeremy/dev/OpenSIN-backend/a2a/team-infratructur/A2A-SIN-Passwordmanager/dist/src/cli.js",
    "serve-mcp"
  ],
  "environment": {
    "SIN_PASSWORDMANAGER_HOST": "127.0.0.1",
    "SIN_PASSWORDMANAGER_PORT": "4646"
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
