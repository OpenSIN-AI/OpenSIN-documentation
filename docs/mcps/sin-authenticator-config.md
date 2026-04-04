# sin-authenticator — Configuration Reference

> **Status:** ✅ Active | **Type:** MCP Server

## Configuration

```json
{
  "type": "local",
  "command": [
    "/Users/jeremy/dev/OpenSIN-backend/bin/sin-authenticator",
    "serve-mcp"
  ],
  "environment": {
    "AUTHD_HOST": "127.0.0.1",
    "AUTHD_PORT": "44711",
    "SIN_AUTH_HOST": "127.0.0.1",
    "SIN_AUTH_PORT": "45871",
    "SIN_AUTH_PUBLIC_BASE_URL": "https://delqhi-sin-authenticator.hf.space"
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
