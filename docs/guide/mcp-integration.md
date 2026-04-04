# MCP Integration

## What is MCP?

Model Context Protocol (MCP) enables agents to use external tools and services.

## Configuring MCP Servers

```javascript
const agent = new Agent({
  name: 'web-agent',
  mcpServers: [
    {
      name: 'web-search',
      command: 'node',
      args: ['mcp-web-search.js']
    },
    {
      name: 'web-scrape',
      command: 'node',
      args: ['mcp-web-scrape.js']
    }
  ]
});
```

## Available MCP Servers

| Server | Description |
|--------|-------------|
| `web-search` | Search the web |
| `web-scrape` | Scrape web pages |
| `file-system` | Access file system |
| `database` | Query databases |
| `email` | Send and receive emails |

## Creating Custom MCP Servers

```javascript
import { MCPServer } from '@opensin/mcp';

const server = new MCPServer({
  name: 'my-custom-server',
  tools: [
    {
      name: 'calculate',
      description: 'Perform calculations',
      handler: async (args) => {
        return eval(args.expression);
      }
    }
  ]
});

server.start();
```

## Next Steps
- [Deployment](/guide/deployment)
- [Best Practices](/best-practices/agent-design)
