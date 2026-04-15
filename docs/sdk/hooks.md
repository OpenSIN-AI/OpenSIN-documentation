---
title: "Hooks & Lifecycle"
---

# Hooks & Lifecycle

The Hook System provides event-driven customization points throughout the agent lifecycle, allowing you to add logging, validation, rate limiting, and custom behavior without modifying core code.

## Hook Points

```
agent:init
    │
    ▼
turn:before ──► llm:before ──► llm:after ──► tool:before ──► tool:after
    │                                                              │
    │◄─────────────────────────────────────────────────────────────┘
    │
turn:after
    │
    ▼
agent:complete
```

## Registering Hooks

```typescript
import { HookSystem } from '@opensin/sdk'

const hooks = new HookSystem()

// Log every tool call
hooks.on('tool:before', ({ name, args }) => {
  console.log(`[TOOL] ${name}(${JSON.stringify(args)})`)
})

// Track token usage
hooks.on('llm:after', ({ model, inputTokens, outputTokens }) => {
  totalTokens += inputTokens + outputTokens
  console.log(`[LLM] ${model}: ${inputTokens}+${outputTokens} tokens`)
})

// Validate outputs before returning
hooks.on('agent:complete', ({ response }) => {
  if (response.includes('TODO')) {
    console.warn('[WARN] Response contains TODO markers')
  }
})
```

## Available Hooks

| Hook | Timing | Arguments |
|------|--------|-----------|
| `agent:init` | Agent starts | `{ config, tools }` |
| `turn:before` | Before each ReAct turn | `{ turn, messages }` |
| `llm:before` | Before LLM call | `{ messages, model }` |
| `llm:after` | After LLM response | `{ response, model, tokens }` |
| `tool:before` | Before tool execution | `{ name, args }` |
| `tool:after` | After tool execution | `{ name, args, result, duration }` |
| `turn:after` | After each ReAct turn | `{ turn, toolCalls, response }` |
| `agent:complete` | Agent finishes | `{ response, turns, tokens }` |
| `agent:error` | On unhandled error | `{ error, turn }` |

## Async Hooks

Hooks can be async and will be awaited:

```typescript
hooks.on('tool:after', async ({ name, result, duration }) => {
  // Upload to Box.com Storage (A2A-SIN-Box-Storage)
  await boxStorage.upload({
    tool: name,
    duration,
    resultSize: result.content.length,
  })
})
```

## Hook Ordering

Multiple hooks on the same event run in registration order:

```typescript
hooks.on('turn:before', () => console.log('First'))
hooks.on('turn:before', () => console.log('Second'))
// Output: First, Second
```

## Practical Examples

### Rate Limiting

```typescript
const rateLimiter = { calls: 0, resetAt: Date.now() + 60000 }

hooks.on('llm:before', async () => {
  rateLimiter.calls++
  if (rateLimiter.calls > 20) {
    const waitMs = rateLimiter.resetAt - Date.now()
    if (waitMs > 0) await sleep(waitMs)
    rateLimiter.calls = 0
    rateLimiter.resetAt = Date.now() + 60000
  }
})
```

### Audit Logging

```typescript
hooks.on('tool:after', async ({ name, args, result, duration }) => {
  await auditLog.append({
    timestamp: new Date(),
    tool: name,
    args: sanitize(args),
    success: !result.isError,
    duration,
  })
})
```

### Cost Tracking

```typescript
const pricing = new UsagePricing()

hooks.on('llm:after', ({ model, inputTokens, outputTokens }) => {
  pricing.record({ model, inputTokens, outputTokens })
})

hooks.on('agent:complete', () => {
  const summary = pricing.getSummary()
  console.log(`Session cost: $${summary.totalCost.toFixed(4)}`)
})
```

## Integration

```typescript
const agent = new AgentLoop({
  model: 'claude-sonnet-4-6',
  tools: toolRegistry,
  hooks: hooks,
})
```

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
