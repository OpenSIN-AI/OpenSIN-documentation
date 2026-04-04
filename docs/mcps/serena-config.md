# serena — Configuration Reference

> **Status:** ✅ Active | **Type:** MCP Server

## Configuration

```json
{
  "type": "local",
  "command": [
    "/Users/jeremy/.local/bin/serena-mcp-server",
    "--project-from-cwd",
    "--log-level",
    "ERROR",
    "--enable-web-dashboard",
    "false",
    "--open-web-dashboard",
    "false"
  ],
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
