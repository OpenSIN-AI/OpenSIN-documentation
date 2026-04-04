# N8N Workflow Builder — Quick Reference Card

> **MCP:** n8n-workflow-builder | **Category:** Model Context Protocol | **Status:** Active

## Quick Reference

| Property | Value |
|----------|-------|
| **Name** | n8n-workflow-builder |
| **Type** | MCP Server |
| **Command** | npx -y @opensin/n8n-workflow-builder |
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
    "n8n-workflow-builder": {
      "command": "npx",
      "args": ["-y", "@opensin/n8n-workflow-builder"],
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
const result = await mcp.call("n8n-workflow-builder", "tool_1", { param1: "value" });
```

### Advanced Usage
```typescript
const result = await mcp.call("n8n-workflow-builder", "tool_2", { 
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

- [Reference Guide](../n8n-workflow-builder-reference.md)
- [Troubleshooting](../n8n-workflow-builder-troubleshooting.md)
- [Quick Reference](./n8n-workflow-builder.md)

---

*Last updated: 2026-04-04 by SIN-Zeus*
