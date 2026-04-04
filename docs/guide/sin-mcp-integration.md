# SIN MCP Integration — Multi-Transport MCP

> **OpenSIN's MCP System** — Geklont aus 1343+ Zeilen Claude Code MCP Client. 9 Transport-Typen mit OAuth.

## Transport Types

| Transport | Use Case | Performance |
|-----------|----------|-------------|
| `stdio` | Lokale MCP Server | Schnell |
| `sse` | Remote MCP Server | Mittel |
| `http` | Streamable HTTP | Mittel |
| `ws` | WebSocket MCP | Schnell |
| `claudeai-proxy` | Anthropic Proxy | Variabel |
| `sdk` | In-Process SDK | Am schnellsten |
| `in-process` | Chrome/Computer Use | 325MB gespart |

## MCP Client Configuration

```python
from opensin.mcp import MCPClient

client = MCPClient(
    name="github",
    transport="stdio",
    command="npx",
    args=["-y", "@modelcontextprotocol/server-github"],
    env={"GITHUB_TOKEN": "..."}
)

await client.connect()

# Tools entdecken
tools = await client.list_tools()

# Tool aufrufen
result = await client.call_tool("search_repositories", {"query": "opensin"})
```

## In-Process Transport

```python
from opensin.mcp import InProcessTransport

# Spart ~325MB pro Subprozess im Vergleich zu stdio
transport = InProcessTransport(
    server_module="chrome_mcp_server",
    create_linked_transport_pair=True
)

client = MCPClient(transport=transport)
```

## OAuth Authentication

```python
from opensin.mcp import MCPAuth

auth = MCPAuth(
    cache_ttl=900,  # 15 Minuten
    serialized_writes=True  # Verhindert Race Conditions
)

# OAuth Flow
token = await auth.get_token(server_url)

# 401 Retry mit Token Deduplication
# Wenn mehrere Server gleichzeitig 401 returned:
# Prüfe ob Token sich wirklich geändert hat → vermeide doppelte RTT
```

## Session Expiry Detection

```python
# Erkennt "Session not found" Errors (HTTP 404 + JSON-RPC -32001)
# Und triggered automatische Reconnection

if error.code == -32001 and error.http_status == 404:
    await client.reconnect()
```

## Consecutive Error Reconnection

```python
# Trackt MAX_ERRORS_BEFORE_RECONNECT (3) terminal errors
# Und schließt Transport manuell wenn SDK onclose nicht callt

class ErrorTracker:
    def __init__(self, max_errors=3):
        self.consecutive_errors = 0
        self.max_errors = max_errors
    
    def record_error(self, error):
        self.consecutive_errors += 1
        if self.consecutive_errors >= self.max_errors:
            self.force_reconnect()
```

## Batched Server Connections

```python
# Kontrolliert parallele Verbindungsversuche
# Local: 3 parallel, Remote: 20 parallel

batch_size = get_mcp_server_connection_batch_size(is_remote=False)  # 3
batch_size = get_mcp_server_connection_batch_size(is_remote=True)   # 20
```

## Best Practices

1. **In-Process Transport** — Spart 325MB pro Subprozess
2. **OAuth Cache** — 15 Minuten TTL, serialized writes
3. **Session Expiry Detection** — Auto-Reconnect
4. **Batched Connections** — Nicht alle Server gleichzeitig
5. **Error Tracking** — Reconnect nach 3 Fehlern

## Next Steps

- [MCP Integration](/guide/mcp-integration)
- [SIN Tool System](/guide/sin-tool-system)
