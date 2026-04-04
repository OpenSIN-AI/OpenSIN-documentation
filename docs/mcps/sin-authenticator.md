# sin-authenticator

> **Status:** ✅ Configured | **Type:** MCP Server

## Overview

2FA/OTP management.

## Configuration

```json
{
  "type": "local",
  "command": [
    "/Users/jeremy/dev/OpenSIN-backend/bin/sin-authenticator",
    "serve-mcp"
  ],
  "environment": {
    "AUTHD_HOST": "127.0.0.1",
    "AUTHD_PORT": "44711",
    "SIN_AUTH_HOST": "127.0.0.1",
    "SIN_AUTH_PORT": "45871",
    "SIN_AUTH_PUBLIC_BASE_URL": "https://delqhi-sin-authenticator.hf.space"
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
