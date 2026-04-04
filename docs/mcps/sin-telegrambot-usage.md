# Sin Telegrambot — Usage Guide

> **MCP:** sin-telegrambot | **Category:** Model Context Protocol

## Overview

This guide provides detailed usage instructions for the **Sin Telegrambot** MCP server.

## Available Tools

| Tool | Description |
|------|-------------|
| `tool_1` | Primary tool function |
| `tool_2` | Secondary tool function |
| `tool_3` | Utility tool function |

## Examples

### Example 1: Basic Usage
```typescript
const result = await mcp.call("sin-telegrambot", "tool_1", {});
```

### Example 2: Advanced Usage
```typescript
const result = await mcp.call("sin-telegrambot", "tool_2", { param: "value" });
```

## Configuration

```json
{
  "mcp": {
    "sin-telegrambot": {
      "command": "npx",
      "args": ["-y", "@opensin/sin-telegrambot"]
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
