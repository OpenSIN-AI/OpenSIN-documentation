---
name: anonymous
description: "Provides browser automation capabilities via the webauto-nodriver-mcp server. Enables agents to perform web interactions, UI automation, and cross-platform tasks using nodriver with stealth capabilities."
license: MIT
compatibility: opencode
metadata:
  audience: all-agents
  workflow: browser-automation
  trigger: webauto-nodriver
---

# Anonymous Skill

This skill provides access to the webauto-nodriver-mcp server, which offers a comprehensive set of tools for browser automation, UI control, and cross-platform tasks.

## Purpose

The Anonymous skill enables agents to:
- Automate browser interactions using nodriver with Chrome DevTools Protocol (CDP)
- Perform UI automation on macOS (AppleScript, keyboard/mouse control)
- Interact with WhatsApp, Apple Notes, Calendar, and iMessage
- Make phone calls and send SMS/iMessage
- Execute shell commands and AppleScripts
- Manage Chrome profiles and sessions
- All with built-in stealth capabilities to avoid bot detection

## How It Works

When this skill is loaded, it enables access to the webauto-nodriver-mcp server which is already configured globally in the OpenCode configuration. The skill doesn't start the server itself but makes the tools available to agents.

## Tool Categories

The skill provides tools in these categories:

1. **Browser & Stealth (Anti-Bot Bypass):**
   - `observe_screen`, `record_screen`, `goto`, `click`, `type_text`, `press_key`, `screenshot_to_file`
   - Stealth mode with anti-detection flags, real Chrome profile usage

2. **WhatsApp (WhatsApp MCP Center):**
   - `whatsapp_send`, `whatsapp_status`, `whatsapp_add_instance`
   - Fallbacks: `web_whatsapp_send`, `mac_whatsapp_send`

3. **Apple Notes & Calendar:**
   - `mac_notes_create`, `mac_notes_read`, `mac_calendar_create`

4. **iPhone & SMS (Continuity & USB):**
   - `make_phone_call`, `send_sms`, `iphone_pair`, `iphone_screenshot`, `run_ios_shortcut`

5. **macOS Admin & Hacker Tools:**
   - `execute_applescript`, `run_shell`, `sudo_cmd`, `get_clipboard`, `set_clipboard`
   - `open_app`, `kill_app`, `list_apps`, `run_shortcut`

## Usage

Once loaded, agents can use any of the tools provided by the webauto-nodriver-mcp server. The tools are available in the agent's toolset and can be invoked directly.

## Example

```python
# Example usage in an agent
await webauto_nodriver_goto({"url": "https://google.com"})
await webauto_nodriver_click({"x": 100, "y": 200})
await webauto_nodriver_type_text({"text": "Hello World"})
```

## Notes

- The skill uses the default Chrome profile (`/Users/jeremy/Library/Application Support/Google/Chrome/Default`) which must be logged into Google accounts for automation requiring authentication.
- For stealth automation, the skill uses nodriver with Chrome DevTools Protocol and avoids headless mode.
- All browser automation actions include human-like delays and behavioral emulation to avoid detection.
