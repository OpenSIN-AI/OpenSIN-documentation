# MCP API

## Overview

Model Context Protocol (MCP) API reference.

## Creating an MCP Server

```javascript
import { MCPServer } from '@opensin/mcp';

const server = new MCPServer({
  name: 'my-server',
  version: '1.0.0',
  tools: [
    {
      name: 'search',
      description: 'Search the web',
      parameters: {
        query: { type: 'string', required: true }
      },
      handler: async (args) => {
        return await searchWeb(args.query);
      }
    }
  ]
});

await server.start();
```

## Registering Tools

```javascript
server.registerTool({
  name: 'calculate',
  description: 'Perform calculations',
  parameters: {
    expression: { type: 'string', required: true }
  },
  handler: async (args) => {
    return eval(args.expression);
  }
});
```

## Tool Response Format

```json
{
  "status": "success",
  "data": {
    "result": 42
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid request |
| 404 | Tool not found |
| 500 | Internal server error |

## Next Steps
- [Events API](/api/events)
- [Deployment](/guide/deployment)
