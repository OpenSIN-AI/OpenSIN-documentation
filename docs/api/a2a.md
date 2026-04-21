---
title: A2A Protocol API
description: Agent-to-Agent communication protocol specification.
---

# A2A Protocol Specification

The **Agent-to-Agent (A2A)** protocol is a JSON-RPC 2.0 compliant interface that enables autonomous agents to collaborate without a central bottleneck.

## Transport Layers

1. **HTTPS (REST):** Used for initial handshakes, discovery, and high-latency tasks.
2. **NATS JetStream:** Used for real-time orchestration, event streaming, and low-latency interaction.

## JSON-RPC 2.0 Request Structure

Every A2A request must follow the standard JSON-RPC format:

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "web_search",
    "arguments": {
      "query": "OpenSIN-AI 2026 standards"
    }
  },
  "id": "req-9b1b-4d56"
}
```

## Primary Methods

### `tools/list`
Returns a list of all tools exposed by the target agent.

- **Request Params:** `{}`
- **Response:** Array of Tool definitions (name, description, inputSchema).

### `tools/call`
Executes a specific tool on the target agent.

- **Request Params:** `{ "name": string, "arguments": object }`
- **Response:** `{ "content": string, "isError": boolean }`

### `agent/identity`
Returns the full Agent Card including version and status.

- **Request Params:** `{}`
- **Response:** See [Agent Identity API](/api/agent).

## Error Handling

A2A uses standard JSON-RPC error codes:

| Code | Message | Description |
|------|---------|-------------|
| `-32700` | Parse error | Invalid JSON was received |
| `-32600` | Invalid Request | The JSON sent is not a valid Request object |
| `-32601` | Method not found | The method does not exist / is not available |
| `-32602` | Invalid params | Invalid method parameter(s) |
| `-32603` | Internal error | Internal JSON-RPC error |
| `-40300` | Permission Denied | Permission Manager blocked the execution |

## Security & Auth

Every request must include the `X-SIN-Agent-ID` and `Authorization` header:

```http
POST /a2a/v1/message
Authorization: Bearer <JWT_TOKEN>
X-SIN-Agent-ID: researcher-agent-01
```

---

## Related

- [Agent API](/api/agent)
- [SDK Overview](/sdk/overview)
- [Neural-Bus Architecture](/architecture/global-brain-neural-bus)
