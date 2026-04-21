---
title: "Ultimate A2A Communication Standard"
description: "The official protocol specification for autonomous agent collaboration."
---

# Ultimate A2A Communication Standard

> [!CAUTION]
> **ANTI-DEMENZ MANDATE (PRIORITY -1000):** 
> DO NOT CHANGE, SIMPLIFY, OR DILUTE THIS SPECIFICATION. 
> This is the source of truth for the trillion-parameter fleet. Any deviation from JSON-RPC 2.0 or the A2A-First rule results in immediate disconnection.

## 1. The A2A-First Mandate

Agents are specialists. If an agent encounters a problem outside its core skill set (e.g., a Backend-Agent needing a UI screenshot), it **MUST NOT** hallucinate or ask the user. It **MUST** delegate to a specialist agent via the A2A protocol.

## 2. Protocol Specification (JSON-RPC 2.0)

All cross-agent communication must use the following standard. This ensures compatibility with the **Rust-based Engine** and the **Neural-Bus**.

### Request Structure
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "take_screenshot",
    "arguments": {
      "url": "https://opensin.ai",
      "full_page": true
    }
  },
  "id": "a2a-9921-df21"
}
```

### Response Structure
```json
{
  "jsonrpc": "2.0",
  "result": {
    "content": "Screenshot captured at /tmp/result.png",
    "artifacts": ["/tmp/result.png"]
  },
  "id": "a2a-9921-df21"
}
```

## 3. The Neural-Bus Topology

Agents do not exist in isolation. They communicate through a **Hub-and-Spoke** model coordinated by `Team-SIN-*` managers.

1. **Worker Privacy:** Worker agents (`A2A-SIN-*`) are invisible to the public internet. They only accept requests from their team manager.
2. **Event mesh:** Every significant state change (Task Start, Progress, Success, Failure) must be published to the **Neural-Bus** (NATS JetStream).

## 4. LLM Execution Law

Direct API calls to AI providers (Google, OpenAI, Anthropic) are **STRICTLY PROHIBITED**. 

**The only authorized way to call an LLM:**
```bash
# High-performance call via canonical stack
opencode run "Your Prompt Here" --format json
```
*Rationale: This ensures token rotation, audit logging, and budget enforcement via the [Global Brain](/architecture/global-brain-neural-bus).*

---

## ⚖️ Enforcement Matrix

| Violation | Consequence |
|-----------|-------------|
| Direct API Call | Permanent Ban / Key Revocation |
| Non-Standard JSON | Task Rejection / Quarantining |
| Unauthorized Cross-Team Call | Disconnection from Neural-Bus |

---

## Next Steps

- [Agent Identity API](/api/agent)
- [Performance Targets](/best-practices/performance)
- [Sovereign Security](/governance/security-mandate)
