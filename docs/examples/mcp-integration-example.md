# MCP Integration Example

> **Category:** Integration | **Difficulty:** Intermediate

## Overview

Example of integrating a custom MCP with OpenCode.

## MCP Configuration

```json
{
  "mcp": {
    "custom-mcp": {
      "command": "npx",
      "args": ["-y", "@scope/custom-mcp"]
    }
  }
}
```

## Usage

```typescript
// In your agent code
const result = await mcp.call("custom-mcp", "toolName", { param: "value" });
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
