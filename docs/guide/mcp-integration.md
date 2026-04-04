# MCP Integration

The Model Context Protocol (MCP) enables OpenSIN agents to connect to external tools and data sources.

## Overview

MCP provides a standardized way for agents to:
- Discover available tools
- Execute tool calls
- Receive tool results
- Manage tool permissions

## Supported Transports

| Transport | Description |
|-----------|-------------|
| stdio | Local process communication |
| SSE | Server-sent events |
| HTTP | REST API communication |
| WebSocket | Real-time bidirectional |
| in-process | Direct function calls (fastest) |

## Next Steps

- [A2A Protocol](/guide/a2a-protocol)
- [Agent Basics](/guide/agent-basics)
