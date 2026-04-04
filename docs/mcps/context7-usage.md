# Context7 — Usage Guide

> **MCP:** context7 | **Category:** Model Context Protocol

## Overview

This guide provides detailed usage instructions for the **Context7** MCP server.

## Available Tools

| Tool | Description |
|------|-------------|
| `tool_1` | Primary tool function |
| `tool_2` | Secondary tool function |
| `tool_3` | Utility tool function |

## Examples

### Example 1: Basic Usage
```typescript
const result = await mcp.call("context7", "tool_1", {});
```

### Example 2: Advanced Usage
```typescript
const result = await mcp.call("context7", "tool_2", { param: "value" });
```

## Configuration

```json
{
  "mcp": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@opensin/context7"]
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
