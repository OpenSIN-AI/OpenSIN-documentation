---
title: "Performance Best Practices"
---

# Performance Best Practices

Optimize your OpenSIN agents and workflows for speed, cost, and resource efficiency.

## Model Routing

Use the SmartModelRouter to automatically select the cheapest model capable of handling each task:

```typescript
import { SmartModelRouter } from '@opensin/sdk'

const router = new SmartModelRouter({
  models: {
    trivial: 'gpt-4o-mini',
    simple: 'gpt-4o-mini',
    moderate: 'gpt-4o',
    complex: 'claude-sonnet-4-6',
    expert: 'claude-opus-4-6',
  },
})

// Automatically classifies task complexity and routes
const model = router.selectModel(prompt)
// "fix typo in README" → gpt-4o-mini (cheap)
// "refactor auth system" → claude-opus-4-6 (expert)
```

This alone can reduce LLM costs by **60-80%** for typical workloads.

## Context Window Management

Large context windows are expensive. Use the ContextCompressor to keep token usage minimal:

```typescript
import { ContextCompressor } from '@opensin/sdk'

const compressor = new ContextCompressor({
  maxTokens: 8000,
  strategy: 'sliding-window', // or 'summarize', 'relevance'
})

// Compress conversation history before sending to LLM
const compressed = compressor.compress(messages)
```

### Strategies

| Strategy | Best For | Token Savings |
|----------|----------|---------------|
| `sliding-window` | Long conversations | 40-60% |
| `summarize` | Research tasks | 50-70% |
| `relevance` | Code editing | 60-80% |

## Parallel Tool Execution

Run independent tool calls concurrently instead of sequentially:

```typescript
import { ParallelToolExecutor } from '@opensin/sdk'

const executor = new ParallelToolExecutor({
  maxWorkers: 8,
  timeout: 30_000,
})

// These run in parallel (3x faster than sequential)
const results = await executor.execute([
  { tool: 'read', args: { path: 'src/auth.ts' } },
  { tool: 'read', args: { path: 'src/db.ts' } },
  { tool: 'grep', args: { pattern: 'TODO', path: 'src/' } },
])
```

The executor uses path-scoped concurrency control to prevent conflicting writes to the same file.

## Caching

### Session Caching

Persist session state to avoid re-reading files on every turn:

```typescript
import { SessionManager } from '@opensin/sdk'

const session = new SessionManager({
  persistence: 'file',    // or 'memory', 'supabase'
  cacheReads: true,        // cache file reads within session
  ttl: 3600,               // 1 hour cache TTL
})
```

### MCP Connection Pooling

Reuse MCP connections instead of spawning new processes:

```typescript
const mcp = new MCPClient({
  poolSize: 4,             // maintain 4 warm connections
  reuseConnections: true,
  idleTimeout: 60_000,
})
```

## Cost Tracking

Monitor spend in real-time with the UsagePricing module:

```typescript
import { UsagePricing } from '@opensin/sdk'

const pricing = new UsagePricing()

// Record each LLM call
pricing.record({
  model: 'claude-sonnet-4-6',
  inputTokens: 2500,
  outputTokens: 800,
})

// Get session summary
const summary = pricing.getSummary()
// { totalCost: 0.0234, totalTokens: 3300, calls: 1 }
```

## Agent Loop Optimization

### Reduce Round-Trips

- Batch independent tool calls in a single turn
- Use `glob` + `read` together instead of multiple `grep` calls
- Prefer `edit` over `write` for partial file changes

### Early Exit

Configure the agent loop to stop early when the task is clearly complete:

```typescript
const agent = new AgentLoop({
  maxTurns: 20,
  earlyExit: true,         // stop when no more tool calls
  idleTimeout: 10_000,     // stop after 10s of no activity
})
```

## Infrastructure Sizing

| Component | Recommended | Notes |
|-----------|-------------|-------|
| n8n (OCI VM) | 2 OCPU, 12GB RAM | Handles 50+ concurrent workflows |
| Supabase (OCI VM) | 200GB storage | Connection pooling enabled |
| HF Spaces | Free tier | Use keep-alive pings |
| MCP servers | 256MB per process | Pool and reuse connections |

## Benchmarks

Typical performance for an OpenSIN agent on a standard workload (read 10 files, edit 3, run tests):

| Metric | Without Optimization | With Optimization |
|--------|---------------------|-------------------|
| Total time | 45s | 18s |
| LLM calls | 12 | 6 |
| Tokens used | 85,000 | 32,000 |
| Estimated cost | $0.42 | $0.11 |
