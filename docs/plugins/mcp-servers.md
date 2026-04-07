---
title: "MCP Servers"
---

# MCP Server Registry

OpenSIN nutzt Model Context Protocol (MCP) Server für Browser-Automation, Desktop-Control und Plattform-Integration.

## 🔌 VERFÜGBARE MCP SERVER

| Server | Zweck | Team |
|--------|-------|------|
| [MCP-SIN-chrome-extension](https://github.com/OpenSIN-AI/MCP-SIN-chrome-extension) | Chrome Extension MCP - Browser Automation via Extension | Infrastructure |
| [MCP-SIN-computer-use](https://github.com/OpenSIN-AI/MCP-SIN-computer-use) | Computer Use MCP - Desktop Control (macOS/Windows/Linux) | Infrastructure |
| [MCP-SIN-in-chrome](https://github.com/OpenSIN-AI/MCP-SIN-in-chrome) | In-Chrome MCP - Tab/Content Access, DOM Manipulation | Infrastructure |
| [MCP-SIN-mcp-gateway](https://github.com/OpenSIN-AI/MCP-SIN-mcp-gateway) | MCP Gateway - Central Routing & Load Balancing | Infrastructure |
| [MCP-SIN-memory](https://github.com/OpenSIN-AI/MCP-SIN-memory) | Memory MCP - Persistent Storage & Retrieval | Infrastructure |
| [MCP-SIN-platform-auth](https://github.com/OpenSIN-AI/MCP-SIN-platform-auth) | Platform Auth - OAuth/SSO für externe Plattformen | Infrastructure |
| [MCP-SIN-usebrowser](https://github.com/OpenSIN-AI/MCP-SIN-usebrowser) | UseBrowser - Web Automation via nodriver/CDP | Infrastructure |

## 🛠️ KONFIGURATION

MCP Server werden in `opencode.json` konfiguriert:

```json
{
  "mcpServers": {
    "sin-chrome-extension": {
      "command": "node",
      "args": ["dist/index.js"],
      "env": {
        "CHROME_PROFILE": "Default",
        "CDP_PORT": "9335"
      }
    }
  }
}
```

## 📡 TEAM-ZUORDNUNG

Alle MCP Server sind dem **Team-SIN-Infrastructure** unterstellt und werden von dort aus orchestriert.
