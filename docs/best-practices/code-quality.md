---
title: "Code Quality Best Practices"
---

# Code Quality Best Practices

Standards for writing, reviewing, and maintaining high-quality code across the OpenSIN ecosystem.

## Code Style

### TypeScript Standards

```typescript
// Use strict mode
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "forceConsistentCasingInFileNames": true
  }
}

// Prefer explicit types for public APIs
export interface AgentConfig {
  model: string
  maxTurns: number
  tools?: string[]
  systemPrompt?: string
}

// Use type guards for runtime validation
function isAgentConfig(obj: unknown): obj is AgentConfig {
  return (
    typeof obj === 'object' &&
    obj !== null &&
    'model' in obj &&
    typeof (obj as AgentConfig).model === 'string'
  )
}
```

### Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Variables | camelCase | `agentConfig` |
| Constants | UPPER_SNAKE_CASE | `MAX_TURNS` |
| Types/Interfaces | PascalCase | `AgentConfig` |
| Functions | camelCase | `createAgent()` |
| Private members | `_prefix` | `_internalState` |
| Files | kebab-case | `agent-loop.ts` |
| Repositories | `[Type]-SIN-[Name]` | `A2A-SIN-Research` |

## Architecture

### Module Design

```typescript
// Single responsibility per module
// agent-loop.ts — only the ReAct loop
// tool-system.ts — only tool registration and execution
// model-router.ts — only model selection logic

// Clear public API
export {
  // Core
  AgentLoop,
  AgentConfig,

  // Types
  ToolDefinition,
  ToolResult,
  Message,

  // Utilities
  createAgent,
  validateConfig,
}
```

### Dependency Management

```typescript
// Good: Dependency injection
class AgentLoop {
  constructor(
    private model: ModelProvider,
    private tools: ToolRegistry,
    private memory: MemoryManager
  ) {}
}

// Bad: Hardcoded dependencies
class AgentLoop {
  private model = new OpenAI()
  private tools = new ToolRegistry()
}
```

## Code Review

### Review Checklist

- [ ] Code follows existing patterns
- [ ] No hardcoded secrets or credentials
- [ ] Error handling covers edge cases
- [ ] Input validation present
- [ ] No `as any` or `@ts-ignore`
- [ ] No empty catch blocks
- [ ] Logging appropriate level
- [ ] Tests included
- [ ] Documentation updated

### Automated Reviews

OpenSIN-Code includes automated code review via the `sin-code-review` plugin:

```typescript
// Multi-agent review system
// 1. Security agent checks for vulnerabilities
// 2. Performance agent checks for bottlenecks
// 3. Style agent checks for consistency
// 4. Architecture agent checks for patterns
```

## Security

### Credential Management

```typescript
// NEVER hardcode secrets
const apiKey = process.env.OPENAI_API_KEY // ✅
const apiKey = 'sk-abc123...' // ❌

// Use PermissionManager for file access
const permissions = new PermissionManager({
  mode: 'strict',
  denylist: ['**/.env', '**/.git/config', '**/node_modules/**'],
})
```

### Input Sanitization

```typescript
// Path traversal prevention
function validatePath(path: string): boolean {
  if (path.includes('..')) return false
  if (!path.startsWith('/workspace/')) return false
  const sensitive = ['.env', '.ssh', 'credentials']
  if (sensitive.some((s) => path.includes(s))) return false
  return true
}
```

### Browser Automation

**🚫 Technology Sovereignty Mandate:**
- Playwright, Puppeteer, Selenium, Camoufox are **PERMANENTLY BANNED**
- Use OpenSIN Bridge Chrome Extension via MCP WebSocket
- Or `webauto-nodriver-mcp` for OS-level isolation

## Documentation

### Inline Documentation

```typescript
/**
 * Creates a new agent with the specified configuration.
 *
 * @param config - Agent configuration including model, tools, and system prompt
 * @returns A configured AgentLoop instance ready to process tasks
 * @throws {ValidationError} If the configuration is invalid
 *
 * @example
 * ```typescript
 * const agent = createAgent({
 *   model: 'claude-sonnet-4-6',
 *   tools: ['read', 'write', 'bash'],
 *   maxTurns: 20,
 * })
 * ```
 */
export function createAgent(config: AgentConfig): AgentLoop {
  validateConfig(config)
  return new AgentLoop(config)
}
```

### README Standards

Every repository must include:
- Purpose and description
- Installation instructions
- Usage examples
- Configuration options
- Links to related repos

## CI/CD

### Pipeline Requirements

```yaml
# Every PR triggers:
# 1. Lint check (ESLint)
# 2. Type check (TypeScript)
# 3. Unit tests (Vitest)
# 4. Build verification
# 5. Security audit (npm audit)
# 6. Code review (sin-code-review plugin)
```

## Checklist

- [ ] Strict TypeScript mode enabled
- [ ] ESLint configured and passing
- [ ] No type suppression (`as any`, `@ts-ignore`)
- [ ] No empty catch blocks
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] Error handling covers edge cases
- [ ] Tests included
- [ ] Documentation updated
- [ ] No banned browser automation libraries
