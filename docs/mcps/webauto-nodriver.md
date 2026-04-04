# webauto-nodriver

> **Status:** ✅ Configured | **Type:** MCP Server

## Overview

87+ tools — Browser automation, screen capture, keyboard/mouse control, WhatsApp, Apple Notes/Calendar, iPhone, macOS admin, shortcuts.

## Configuration

```json
{
  "type": "local",
  "command": [
    "python3",
    "/Users/jeremy/dev/webauto-nodriver-mcp/webauto_nodriver_mcp.py"
  ],
  "environment": {
    "WEBAUTO_CDP_PORT": "9335",
    "WEBAUTO_PROFILE_DIR": "/Users/jeremy/Library/Application Support/Google/Chrome/Default",
    "WEBAUTO_PROFILE_DIRECTORY": "Default",
    "WEBAUTO_DESKTOPGRAB_ENABLED": "true",
    "WEBAUTO_DESKTOPGRAB_FPS": "10",
    "WEBAUTO_ATTACH_FRAMES_PER_ACTION": "1",
    "WEBAUTO_ATTACH_DESKTOP_FRAMES_PER_ACTION": "1",
    "WEBAUTO_EXPORT_DIR": "/Users/jeremy/Desktop/webauto_exports"
  },
  "enabled": true
}
```

## Available Tools

Browser automation, screen capture, keyboard/mouse control, WhatsApp, Apple Notes/Calendar, iPhone, macOS admin, shortcuts

## Usage

This MCP is automatically loaded when OpenCode starts. Agents can invoke its tools directly.

---

*Last updated: 2026-04-04 by SIN-Zeus*
