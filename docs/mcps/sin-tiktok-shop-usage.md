# Sin Tiktok Shop — Usage Guide

> **MCP:** sin-tiktok-shop | **Category:** Model Context Protocol

## Overview

This guide provides detailed usage instructions for the **Sin Tiktok Shop** MCP server.

## Available Tools

| Tool | Description |
|------|-------------|
| `tool_1` | Primary tool function |
| `tool_2` | Secondary tool function |
| `tool_3` | Utility tool function |

## Examples

### Example 1: Basic Usage
```typescript
const result = await mcp.call("sin-tiktok-shop", "tool_1", {});
```

### Example 2: Advanced Usage
```typescript
const result = await mcp.call("sin-tiktok-shop", "tool_2", { param: "value" });
```

## Configuration

```json
{
  "mcp": {
    "sin-tiktok-shop": {
      "command": "npx",
      "args": ["-y", "@opensin/sin-tiktok-shop"]
    }
  }
}
```

## Troubleshooting

If the MCP doesn't load:
1. Check if the package is installed
2. Verify the command path
3. Check environment variables

---

*Last updated: 2026-04-04 by SIN-Zeus*
