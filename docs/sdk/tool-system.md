---
title: "Tool System"
---

# Tool System

The tool system lets you define, validate, and execute tools that the agent can invoke during its ReAct loop.

## Defining Tools

```typescript
import { ToolRegistry } from '@opensin/sdk'

const tools = new ToolRegistry()

tools.register({
  name: 'read_file',
  description: 'Read the contents of a file',
  parameters: {
    type: 'object',
    properties: {
      path: {
        type: 'string',
        description: 'Absolute or relative file path',
      },
      encoding: {
        type: 'string',
        enum: ['utf-8', 'base64'],
        default: 'utf-8',
      },
    },
    required: ['path'],
  },
  execute: async ({ path, encoding = 'utf-8' }) => {
    const content = await fs.readFile(path, encoding)
    return { content }
  },
})
```

## Built-in Tools (CLI)

The OpenSIN CLI ships with 11 built-in tools:

| Tool | Description |
|------|-------------|
| `bash` | Execute shell commands (with `execFile` for safety) |
| `read` | Read file contents with line numbers |
| `write` | Create or overwrite files |
| `edit` | Exact string replacement in files |
| `grep` | Search file contents (literal by default, opt-in regex) |
| `glob` | Find files by pattern matching |
| `web_fetch` | Fetch content from URLs |
| `web_search` | Search the web and return results |
| `todo_write` | Manage a structured task list |
| `worktree` | Git worktree management |
| `plan_mode` | Structured planning mode |

## JSON Schema Validation

Tool parameters are validated against their JSON Schema before execution:

```typescript
// This will throw a validation error
await tools.execute('read_file', { path: 123 }) // path must be string

// This passes validation
await tools.execute('read_file', { path: 'src/app.ts' })
```

## Tool Results

Tools return structured results:

```typescript
interface ToolResult {
  content: string       // Text content for the LLM
  isError?: boolean     // Whether the execution failed
  metadata?: Record<string, unknown>  // Additional structured data
}
```

## MCP Tool Integration

Load tools from MCP (Model Context Protocol) servers:

```typescript
import { MCPStdioClient } from '@opensin/sdk'

const mcp = new MCPStdioClient({
  command: 'node',
  args: ['path/to/mcp-server.js'],
})

await mcp.connect()

// List available tools
const mcpTools = await mcp.listTools()

// Register MCP tools in the tool registry
for (const tool of mcpTools) {
  tools.registerMCP(tool, mcp)
}
```

## Custom Tool Categories

Organize tools by category for better LLM context:

```typescript
tools.register({
  name: 'query_database',
  category: 'database',
  description: 'Run a SQL query',
  // ...
})

tools.register({
  name: 'insert_record',
  category: 'database',
  description: 'Insert a record',
  // ...
})

// Get tools by category
const dbTools = tools.getByCategory('database')
```

## Error Handling

Tool errors are caught and returned to the LLM as error results:

```typescript
tools.register({
  name: 'risky_tool',
  // ...
  execute: async (args) => {
    try {
      const result = await riskyOperation(args)
      return { content: result }
    } catch (error) {
      return {
        content: `Error: ${error.message}`,
        isError: true,
      }
    }
  },
})
```

The agent loop will see the error and can decide to retry, try a different approach, or report the failure to the user.

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
