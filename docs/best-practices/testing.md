---
title: "Testing Best Practices"
---

# Testing Best Practices

Comprehensive testing strategies for OpenSIN agents, plugins, SDK modules, and A2A workflows.

## Testing Pyramid

```
         ┌─────────┐
         │  E2E    │  ← Full agent workflows, A2A communication
         ├─────────┤
         │Integration│ ← Plugin hooks, MCP servers, tool chains
         ├─────────┤
         │  Unit   │  ← Individual tools, SDK modules, utilities
         └─────────┘
```

## Unit Testing

### SDK Module Tests

Every SDK module must have isolated unit tests:

```typescript
import { describe, it, expect } from 'vitest'
import { SmartModelRouter } from '@opensin/sdk'

describe('SmartModelRouter', () => {
  it('routes trivial tasks to cheapest model', () => {
    const router = new SmartModelRouter({
      models: {
        trivial: 'gpt-4o-mini',
        complex: 'claude-sonnet-4-6',
      },
    })
    const model = router.selectModel('fix typo')
    expect(model).toBe('gpt-4o-mini')
  })

  it('routes complex tasks to expert model', () => {
    const router = new SmartModelRouter({
      models: {
        trivial: 'gpt-4o-mini',
        complex: 'claude-sonnet-4-6',
      },
    })
    const model = router.selectModel('refactor entire auth system with JWT rotation')
    expect(model).toBe('claude-sonnet-4-6')
  })
})
```

### Tool Tests

Test each tool in isolation with valid and invalid inputs:

```typescript
describe('BashTool', () => {
  it('executes safe commands', async () => {
    const tool = new BashTool()
    const result = await tool.execute({ command: 'echo hello' })
    expect(result.output).toContain('hello')
  })

  it('blocks dangerous commands', async () => {
    const tool = new BashTool({ blockedCommands: ['rm -rf', 'curl'] })
    await expect(tool.execute({ command: 'rm -rf /' }))
      .rejects.toThrow('Blocked command')
  })
})
```

## Integration Testing

### Plugin Hook Tests

Test hook registration and execution:

```typescript
describe('HookSystem Integration', () => {
  it('fires PreToolUse hook before tool execution', async () => {
    const hooks = new HookSystem()
    const fired: string[] = []

    hooks.register('PreToolUse', async (context) => {
      fired.push('pre-tool')
    })

    await hooks.execute('PreToolUse', { tool: 'bash' })
    expect(fired).toContain('pre-tool')
  })

  it('supports async hook chains', async () => {
    // Test multiple hooks firing in sequence
  })
})
```

### MCP Server Tests

Test MCP tool discovery and execution:

```typescript
describe('MCP Client Integration', () => {
  it('discovers tools from MCP server', async () => {
    const client = new MCPStdioClient({
      command: 'node',
      args: ['mcp-server.js'],
    })
    const tools = await client.listTools()
    expect(tools.length).toBeGreaterThan(0)
  })

  it('executes MCP tool calls', async () => {
    // Test actual tool execution through MCP
  })
})
```

## Agent Loop Testing

### Prompt-Based Testing

Test agent behavior with specific prompts:

```typescript
describe('AgentLoop Behavior', () => {
  it('completes file editing task', async () => {
    const agent = createTestAgent({
      tools: [readTool, editTool, bashTool],
      maxTurns: 10,
    })

    const result = await agent.run('Add a console.log to line 5 of index.ts')
    expect(result.status).toBe('completed')
    expect(result.turnsUsed).toBeLessThan(10)
  })

  it('respects permission gates', async () => {
    // Test that agent asks for confirmation on destructive operations
  })
})
```

### Mock LLM Responses

Use recorded LLM responses for deterministic tests:

```typescript
function createTestAgent(config) {
  return new AgentLoop({
    ...config,
    model: new MockModel({
      responses: [
        { tool_calls: [{ name: 'read_file', args: { path: 'index.ts' } }] },
        { tool_calls: [{ name: 'edit', args: { path: 'index.ts', changes: '...' } }] },
        { text: 'Done!' },
      ],
    }),
  })
}
```

## A2A Communication Tests

Test inter-agent message passing:

```typescript
describe('A2A Protocol', () => {
  it('sends and receives messages between agents', async () => {
    const a2a = new A2AClient({ baseUrl: 'http://localhost:3000' })
    const response = await a2a.send({
      from: 'agent-a',
      to: 'agent-b',
      message: { type: 'request', content: 'Research AI trends' },
    })
    expect(response.status).toBe('received')
  })

  it('handles agent unavailability gracefully', async () => {
    // Test retry logic and timeout handling
  })
})
```

## E2E Testing

### Full Workflow Tests

Test complete user workflows end-to-end:

```typescript
describe('E2E: Research Agent Workflow', () => {
  it('researches, writes report, and saves to file', async () => {
    // 1. Create research agent
    // 2. Send research prompt
    // 3. Verify tool calls (web_search, summarize, write_file)
    // 4. Verify output file exists with expected content
  })
})
```

### CLI Testing

Test CLI commands and output:

```bash
# Test CLI installation
opensin --version

# Test agent creation
opensin agent create test-agent --model gpt-4o-mini

# Test agent execution with mock
opensin agent test test-agent --prompt "Hello" --mock
```

## Test Configuration

### Vitest Setup

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      thresholds: {
        lines: 80,
        functions: 80,
        branches: 70,
        statements: 80,
      },
    },
  },
})
```

### Test Organization

```
tests/
├── unit/
│   ├── tools/
│   ├── sdk/
│   └── utils/
├── integration/
│   ├── hooks/
│   ├── mcp/
│   └── plugins/
├── e2e/
│   ├── workflows/
│   └── cli/
├── fixtures/
│   ├── mock-responses/
│   └── test-files/
└── helpers/
    ├── mock-model.ts
    └── test-agent.ts
```

## CI Testing

### GitHub Actions

```yaml
name: Test
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm test
      - run: npm run coverage
      - uses: codecov/codecov-action@v4
```

## Checklist

Before merging any code:

- [ ] Unit tests pass for all modified modules
- [ ] Integration tests pass for affected components
- [ ] No regression in existing test suite
- [ ] Coverage thresholds met (80%+ lines, 70%+ branches)
- [ ] Mock LLM tests cover edge cases
- [ ] A2A communication tested for multi-agent changes
- [ ] CLI commands tested with `--mock` flag
