# Sin Google Apps — Quick Reference Card

> **MCP:** sin-google-apps | **Category:** Model Context Protocol | **Status:** Active

## Quick Reference

| Property | Value |
|----------|-------|
| **Name** | sin-google-apps |
| **Type** | MCP Server |
| **Command** | npx -y @opensin/sin-google-apps |
| **Auth** | API Key via environment variable |
| **Protocol** | Model Context Protocol (MCP) |

## Available Tools

| Tool | Description | Parameters |
|------|-------------|------------|
| tool_1 | Primary function | param1, param2 |
| tool_2 | Secondary function | param1 |
| tool_3 | Utility function | param1, param2, param3 |

## Configuration

```json
{
  "mcpServers": {
    "sin-google-apps": {
      "command": "npx",
      "args": ["-y", "@opensin/sin-google-apps"],
      "env": {
        "API_KEY": "${API_KEY}"
      }
    }
  }
}
```

## Usage Examples

### Basic Usage
```typescript
const result = await mcp.call("sin-google-apps", "tool_1", { param1: "value" });
```

### Advanced Usage
```typescript
const result = await mcp.call("sin-google-apps", "tool_2", { 
  param1: "value1",
  param2: "value2"
});
```

## Error Codes

| Code | Description | Resolution |
|------|-------------|------------|
| MCP_NOT_FOUND | MCP server not found | Check installation |
| TOOL_NOT_FOUND | Tool not available | Verify tool name |
| AUTH_FAILED | Authentication failed | Update credentials |
| TIMEOUT | Request timed out | Increase timeout |

## Performance

| Metric | Value |
|--------|-------|
| Response Time | < 500ms |
| Concurrent Calls | 10 |
| Memory Usage | < 100MB |

## Related Documents

- [Reference Guide](../sin-google-apps-reference.md)
- [Troubleshooting](../sin-google-apps-troubleshooting.md)
- [Quick Reference](./sin-google-apps.md)

---

*Last updated: 2026-04-04 by SIN-Zeus*
