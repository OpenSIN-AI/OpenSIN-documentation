# Sin Cloudflare — Quick Reference Card

> **MCP:** sin-cloudflare | **Category:** Model Context Protocol | **Status:** Active

## Quick Reference

| Property | Value |
|----------|-------|
| **Name** | sin-cloudflare |
| **Type** | MCP Server |
| **Command** | npx -y @opensin/sin-cloudflare |
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
    "sin-cloudflare": {
      "command": "npx",
      "args": ["-y", "@opensin/sin-cloudflare"],
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
const result = await mcp.call("sin-cloudflare", "tool_1", { param1: "value" });
```

### Advanced Usage
```typescript
const result = await mcp.call("sin-cloudflare", "tool_2", { 
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

- [Reference Guide](../sin-cloudflare-reference.md)
- [Troubleshooting](../sin-cloudflare-troubleshooting.md)
- [Quick Reference](./sin-cloudflare.md)

---

*Last updated: 2026-04-04 by SIN-Zeus*
