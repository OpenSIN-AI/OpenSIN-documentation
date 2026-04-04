# tavily

> **Status:** ✅ Configured | **Type:** MCP Server

## Overview

Web search.

## Configuration

```json
{
  "type": "local",
  "command": [
    "npx",
    "-y",
    "@tavily/claude-mcp"
  ],
  "environment": {
    "TAVILY_API_KEY": "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"
  },
  "enabled": false
}
```

## Available Tools

See MCP server documentation

## Usage

This MCP is automatically loaded when OpenCode starts. Agents can invoke its tools directly.

---

*Last updated: 2026-04-04 by SIN-Zeus*
