# SIN In-Process MCP Transport — 325MB pro Subprozess sparen

> **OpenSIN's In-Process MCP** — Geklont aus Claude Code. MCP Server im selben Prozess statt als Subprozess.

## Das Problem

Jeder MCP Subprozess verbraucht ~325MB RAM. Bei vielen Agents/Tools = enormer Speicherverbrauch.

## Die Lösung: In-Process Transport

```python
from opensin.mcp import InProcessTransport

# Statt: subprocess.Popen(["npx", "-y", "@mcp/server-github"])
# Jetzt: Direkter Import im selben Prozess

transport = InProcessTransport(
    server_module="mcp_server_github",
    create_linked_transport_pair=True
)

client = MCPClient(transport=transport)
```

## Linked Transport Pair

```python
from opensin.mcp import create_linked_transport_pair

# Erstellt ein verbundenes Transport-Paar
# Parent und Child kommunizieren direkt ohne Subprozess
parent_transport, child_transport = create_linked_transport_pair()

# Parent nutzt parent_transport
# Child nutzt child_transport
# Kein Subprozess-Overhead!
```

## Performance Impact

| Scenario | RAM pro Server | 10 Server | 50 Server |
|----------|---------------|-----------|-----------|
| Subprozess | 325MB | 3.25GB | 16.25GB |
| In-Process | 15MB | 150MB | 750MB |
| **Ersparnis** | **95%** | **3.1GB** | **15.5GB** |

## Implementation

```python
class InProcessTransport:
    def __init__(self, server_module: str):
        self.server = import_module(server_module)
        self.request_queue = asyncio.Queue()
        self.response_queue = asyncio.Queue()
    
    async def connect(self):
        await self.server.initialize()
        asyncio.create_task(self._process_requests())
    
    async def _process_requests(self):
        while True:
            request = await self.request_queue.get()
            response = await self.server.handle_request(request)
            await self.response_queue.put(response)
    
    async def send_request(self, request: dict) -> dict:
        await self.request_queue.put(request)
        return await self.response_queue.get()
```

## Best Practices

1. **In-Process wo möglich** — Spart massiv RAM
2. **Subprozess für Isolation** — Wenn Security kritisch
3. **Linked Transport Pairs** — Für Parent-Child Kommunikation
4. **Monitor Memory** — Tracke RAM Usage pro Server

## Next Steps

- [SIN MCP Integration](/guide/sin-mcp-integration)
- [Performance Optimization](/guide/performance-optimization)
