# sin-passwordmanager

> **Status:** ✅ Configured | **Type:** MCP Server

## Overview

Password management.

## Configuration

```json
{
  "type": "local",
  "command": [
    "node",
    "/Users/jeremy/dev/OpenSIN-backend/a2a/team-infratructur/A2A-SIN-Passwordmanager/dist/src/cli.js",
    "serve-mcp"
  ],
  "environment": {
    "SIN_PASSWORDMANAGER_HOST": "127.0.0.1",
    "SIN_PASSWORDMANAGER_PORT": "4646"
  },
  "enabled": true
}
```

## Available Tools

See MCP server documentation

## Usage

This MCP is automatically loaded when OpenCode starts. Agents can invoke its tools directly.

---

*Last updated: 2026-04-04 by SIN-Zeus*
