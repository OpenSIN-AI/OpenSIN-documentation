# n8n-workflow-builder

> **Status:** ✅ Configured | **Type:** MCP Server

## Overview

7 tools — list, create, get, update, delete, activate, deactivate workflows.

## Configuration

```json
{
  "type": "local",
  "command": [
    "npx",
    "-y",
    "mcp-n8n-builder"
  ],
  "environment": {
    "N8N_HOST": "http://92.5.60.87:5678/api/v1",
    "N8N_API_KEY": "n8n_api_69175bcabef4b10d619b43598cd557a92ee38aac5ae4b1ca",
    "OUTPUT_VERBOSITY": "concise"
  },
  "enabled": true
}
```

## Available Tools

list, create, get, update, delete, activate, deactivate workflows

## Usage

This MCP is automatically loaded when OpenCode starts. Agents can invoke its tools directly.

---

*Last updated: 2026-04-04 by SIN-Zeus*
