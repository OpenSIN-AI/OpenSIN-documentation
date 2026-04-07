---
title: "MCP Integration Best Practices"
---

# MCP Integration Best Practices

Guidelines for connecting OpenSIN agents to external tools and services via the Model Context Protocol.

## Transport Selection

| Transport | Latency | Use Case |
|-----------|---------|----------|
| stdio | Low | Local tools, CLI utilities |
| in-process | Lowest | Embedded functions, no process overhead |
| SSE | Medium | Server-pushed events |
| HTTP | Medium | REST APIs, remote services |
| WebSocket | Low | Real-time bidirectional (OpenSIN Bridge) |

## Connection Management

### Connection Pooling

```typescript
const mcp = new MCPClient({
  servers: {
    filesystem: {
      command: 'npx',
      args: ['-y', '@modelcontextprotocol/server-filesystem', '/workspace'],
    },
    chrome: {
      transport: 'websocket',
      url: 'ws://localhost:8080/mcp',
    },
  },
  poolSize: 4,
  reuseConnections: true,
  idleTimeout: 60_000,
  connectionTimeout: 10_000,
})
```

### Health Checks

```typescript
async function checkMCPHealth(serverName: string): Promise<boolean> {
  try {
    const client = mcp.getClient(serverName)
    const tools = await client.listTools()
    return tools.length > 0
  } catch {
    return false
  }
}

// Periodic health check
setInterval(async () => {
  for (const server of configuredServers) {
    const healthy = await checkMCPHealth(server.name)
    if (!healthy) {
      await restartMCPServer(server.name)
    }
  }
}, 30_000)
```

## Tool Security

### Permission Gates

```typescript
const mcpConfig = {
  servers: {
    'trusted-server': {
      command: 'node',
      args: ['server.js'],
      permissions: {
        filesystem: ['read'],
        network: ['localhost:*'],
        tools: {
          'file:read': { requireConfirmation: false },
          'file:write': { requireConfirmation: true },
          'bash:execute': { requireConfirmation: true },
        },
      },
    },
  },
}
```

### Allowlisting

```typescript
const allowedMCPServers = [
  '@modelcontextprotocol/server-filesystem',
  '@modelcontextprotocol/server-postgres',
  'opensin-bridge-mcp',
]

function isMCPServerAllowed(command: string): boolean {
  return allowedMCPServers.some((allowed) => command.includes(allowed))
}
```

## OpenSIN Bridge

### Chrome Extension MCP (39 Tools)

The OpenSIN Bridge provides the most comprehensive browser automation MCP:

```typescript
const bridge = new MCPClient({
  transport: 'websocket',
  url: 'ws://localhost:8080/mcp',
})

// Available tool categories:
// - Video Recording (chrome.tabCapture)
// - Cookie CRUD
// - webRequest Logging (500 entries)
// - Stealth Mode (Anti-Detection)
// - DOM Interaction
// - Network Monitoring
```

### Browser Automation Policy

**🚫 Technology Sovereignty Mandate:**
- **Playwright, Puppeteer, Selenium, Camoufox are PERMANENTLY BANNED**
- Use **OpenSIN Bridge Chrome Extension** via MCP WebSocket
- Alternatively: `webauto-nodriver-mcp` for OS-level isolation

## Error Handling

### Graceful Degradation

```typescript
async function callMCPTool(
  server: string,
  tool: string,
  args: Record<string, unknown>
) {
  try {
    return await mcp.callTool(server, tool, args)
  } catch (error) {
    if (error.code === 'CONNECTION_LOST') {
      await mcp.reconnect(server)
      return await mcp.callTool(server, tool, args)
    }
    if (error.code === 'TOOL_NOT_FOUND') {
      const available = await mcp.listTools(server)
      throw new Error(
        `Tool '${tool}' not found. Available: ${available.map((t) => t.name).join(', ')}`
      )
    }
    throw error
  }
}
```

## Performance

### Caching Tool Results

```typescript
const toolCache = new Map<string, { result: unknown; expiry: number }>()

async function getCachedToolResult(
  server: string,
  tool: string,
  args: Record<string, unknown>,
  ttl = 60_000
) {
  const key = `${server}:${tool}:${JSON.stringify(args)}`
  const cached = toolCache.get(key)

  if (cached && cached.expiry > Date.now()) {
    return cached.result
  }

  const result = await mcp.callTool(server, tool, args)
  toolCache.set(key, { result, expiry: Date.now() + ttl })
  return result
}
```

## Checklist

- [ ] MCP servers are allowlisted
- [ ] Connection pooling enabled
- [ ] Health checks configured
- [ ] Permission gates set for destructive tools
- [ ] Error handling includes reconnection logic
- [ ] No banned browser automation libraries
- [ ] Tool results cached where appropriate
- [ ] Connection timeouts configured
