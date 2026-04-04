# serena

> **Status:** ✅ Configured | **Type:** MCP Server

## Overview

20+ tools — Code intelligence, find_symbol, find_references, replace_symbol, rename, search, AST operations.

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

## Available Tools

Code intelligence, find_symbol, find_references, replace_symbol, rename, search, AST operations

## Usage

This MCP is automatically loaded when OpenCode starts. Agents can invoke its tools directly.

---

*Last updated: 2026-04-04 by SIN-Zeus*
