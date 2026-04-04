# Agent Interoperability

Make agents work across different systems and protocols.

## Interoperability Layers

### 1. Protocol Layer

OpenSIN supports multiple communication protocols:

| Protocol | Use Case | Status |
|----------|----------|--------|
| A2A | Agent-to-Agent | ✅ Stable |
| MCP | Tool integration | ✅ Stable |
| HTTP/REST | External APIs | ✅ Stable |
| WebSocket | Real-time | ✅ Stable |
| gRPC | High-performance | 🔄 Beta |
| GraphQL | Flexible queries | 🔄 Beta |

### 2. Data Format Layer

```python
# Standard message format
message = {
    "version": "1.0.0",
    "type": "request",  # or "response", "notification", "error"
    "id": "msg_123",
    "from": "agent_a",
    "to": "agent_b",
    "content": {
        "text": "Research AI trends",
        "attachments": [],
        "metadata": {}
    },
    "timestamp": "2026-04-04T10:00:00Z"
}
```

### 3. Capability Layer

```python
# Agent capability declaration
capabilities = {
    "name": "researcher",
    "version": "1.2.0",
    "capabilities": [
        {"type": "web_search", "version": "1.0"},
        {"type": "summarization", "version": "1.0"},
        {"type": "fact_checking", "version": "1.0"},
    ],
    "protocols": ["a2a", "http"],
    "data_formats": ["json", "text"],
    "languages": ["en", "de", "es"]
}
```

## Cross-Platform Integration

### OpenSIN ↔ LangChain

```python
from opensin import Agent
from langchain.agents import AgentExecutor

# Use OpenSIN agent in LangChain
opensin_agent = Agent(name="researcher")
langchain_agent = AgentExecutor.from_opensin(opensin_agent)

# Use LangChain tools in OpenSIN
from opensin.tools import LangChainTool
agent.register_tool(LangChainTool(langchain_tool))
```

### OpenSIN ↔ AutoGen

```python
from opensin import Agent
from autogen import AssistantAgent

# Bridge OpenSIN to AutoGen
opensin_agent = Agent(name="researcher")
autogen_agent = AssistantAgent.from_opensin(opensin_agent)
```

## Standard Protocols

### A2A Protocol

```python
from opensin.a2a import AgentCard, Message

# Discover agent
card = await AgentCard.discover("https://agent.example.com")

# Send message
message = Message(
    type="request",
    from_agent="my-agent",
    to_agent=card.name,
    content="Research AI trends"
)

response = await card.send(message)
```

### MCP Protocol

```python
from opensin.mcp import MCPClient

client = MCPClient(
    command="python",
    args=["-m", "mcp_server"],
    transport="stdio"
)

# List tools
tools = await client.list_tools()

# Call tool
result = await client.call_tool("web_search", {"query": "AI trends"})
```

## Best Practices

1. **Use standard protocols** — A2A and MCP preferred
2. **Declare capabilities** — Make capabilities discoverable
3. **Version interfaces** — Track protocol versions
4. **Handle failures** — Graceful degradation
5. **Test interoperability** — Test with different systems

## Next Steps

- [A2A Protocol](/guide/a2a-protocol)
- [MCP Integration](/guide/mcp-integration)
