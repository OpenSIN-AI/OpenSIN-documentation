---
title: OpenSIN Bridge — Chrome Extension
description: Full-featured Chrome extension for browser automation, cookie management, and AI agent integration
---

# OpenSIN Bridge — Chrome Extension

**Version:** 2.5.0  
**Status:** ✅ Active  
**Repo:** [OpenSIN-backend/services/sin-chrome-extension](https://github.com/OpenSIN-AI/OpenSIN-backend/tree/main/services/sin-chrome-extension)  
**HF MCP Server:** https://huggingface.co/spaces/OpenJerro/opensin-bridge-mcp

---

## Overview

OpenSIN Bridge is a **Manifest V3 Chrome Extension** that provides full browser automation capabilities for AI agents. It is **better than Antigravity** — more tools, more features, fully open source, no vendor lock-in.

### Key Features

| Feature | Description |
|---------|-------------|
| **39 MCP Tools** | Tabs, navigation, DOM interaction, cookies, screenshots, storage, network, recording, stealth |
| **Content Scripts** | MAIN world injection on `<all_urls>` at `document_start` |
| **webRequest** | Full request/response/error logging (500-entry buffer) |
| **Cookie CRUD** | Full Chrome Cookie API (get, set, delete, clear) |
| **declarativeNetRequest** | URL blocking capability |
| **Offscreen Document** | Persistent background processing (DOM parser, blob, storage) |
| **External Messaging** | `onMessageExternal` for cross-origin communication |
| **Tab Events** | Auto-notify on tab load/create/close |
| **New Tab Override** | Custom OpenSIN landing page with brand icon |
| **Video Recording** | Screen recording via `chrome.tabCapture` |
| **Stealth Mode** | Anti-detection: webdriver removal, plugin/language spoofing |

---

## Tool Reference (39 Tools)

### Tab Management (5)
`tabs_list`, `tabs_create`, `tabs_update`, `tabs_close`, `tabs_activate`

### Navigation (4)
`navigate`, `go_back`, `go_forward`, `reload`

### DOM Interaction (8)
`click_element`, `type_text`, `get_text`, `get_html`, `get_attribute`, `wait_for_element`, `execute_script`, `inject_css`

### Page Info (3)
`get_page_info`, `get_all_links`, `get_all_inputs`

### Screenshot (2)
`screenshot`, `screenshot_full`

### Video Recording (3)
`start_recording`, `stop_recording`, `recording_status`

### Cookies (4)
`get_cookies`, `set_cookie`, `delete_cookie`, `clear_cookies`

### Storage (3)
`storage_get`, `storage_set`, `storage_clear`

### Network (2)
`get_network_requests`, `block_url`

### Stealth Mode (2)
`enable_stealth`, `stealth_status`

### System (3)
`health`, `list_tools`, `offscreen_status`

---

## Comparison: OpenSIN Bridge vs Antigravity

| Feature | Antigravity | OpenSIN Bridge v2.5.0 |
|---------|-------------|----------------------|
| Tools | ~15 | **39** |
| Content Scripts | ❌ | ✅ MAIN world |
| Cookie CRUD | ❌ | ✅ Full API |
| webRequest Log | ❌ | ✅ 500 entries |
| URL Blocking | ❌ | ✅ declarativeNetRequest |
| Offscreen Docs | ❌ | ✅ DOM Parser + Storage |
| Video Recording | ✅ | ✅ |
| Stealth Mode | ❌ | ✅ |
| Open Source | ❌ | ✅ |
| Cost | Free (preview) | **Free forever** |
| Vendor Lock-in | ✅ Google only | ❌ None |

---

## Installation

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN-backend.git
cd OpenSIN-backend/services/sin-chrome-extension
bash install.sh
```

Or manually:
1. Open `chrome://extensions/`
2. Enable Developer mode
3. Click "Load unpacked"
4. Select: `extension/`

---

## HF MCP Server

The MCP Server runs on Hugging Face Spaces and is always online:

- **URL:** https://huggingface.co/spaces/OpenJerro/opensin-bridge-mcp
- **Health:** https://openjerro-opensin-bridge-mcp.hf.space/health
- **WebSocket:** `wss://openjerro-opensin-bridge-mcp.hf.space`

The Chrome Extension auto-connects to this server on startup.

---

## Changelog

### v2.5.0 (2026-04-05) — Stealth Mode + Video Recording
- ✅ start_recording / stop_recording / recording_status
- ✅ enable_stealth / stealth_status
- ✅ 39 Tools total

### v2.4.1 (2026-04-04) — HF MCP URL Fixed
### v2.4.0 (2026-04-04) — HF MCP WebSocket Mode
### v2.3.0 (2026-04-04) — Pure Chrome API Mode
### v2.0.0 (2026-04-04) — Initial Release
