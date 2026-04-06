---
title: "Smart Model Routing"
---

# Smart Model Routing

The `SmartModelRouter` automatically selects the optimal LLM model based on task complexity, saving costs by routing simple tasks to cheaper models.

## How It Works

1. Analyze the prompt to classify complexity (trivial/simple/moderate/complex/expert)
2. Route to the appropriate model tier
3. Fall back to a higher tier if the selected model fails

```
"fix typo" ──► trivial ──► gpt-4o-mini ($0.15/M)
"add button" ──► simple ──► gpt-4o-mini ($0.15/M)
"refactor auth" ──► complex ──► claude-sonnet ($3/M)
"design system" ──► expert ──► claude-opus ($15/M)
```

## Usage

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
  fallbackOnError: true,
})

// Automatic selection
const model = router.selectModel('Fix the typo in README.md')
// Returns: 'gpt-4o-mini'

const model2 = router.selectModel('Refactor the entire authentication system to use JWT')
// Returns: 'claude-sonnet-4-6'
```

## Complexity Classification

The router uses keyword analysis and prompt structure to classify tasks:

| Level | Indicators | Examples |
|-------|-----------|----------|
| **Trivial** | typo, rename, comment | "Fix typo in line 5" |
| **Simple** | add, update, format | "Add a loading spinner" |
| **Moderate** | implement, create, build | "Implement pagination" |
| **Complex** | refactor, redesign, migrate | "Refactor auth to OAuth2" |
| **Expert** | architect, design system, security audit | "Design the plugin system" |

## Fallback Chain

When a model fails (rate limit, error, insufficient output), the router automatically escalates:

```
gpt-4o-mini → gpt-4o → claude-sonnet → claude-opus
```

```typescript
const router = new SmartModelRouter({
  models: { ... },
  fallbackOnError: true,
  maxRetries: 2,
  fallbackChain: ['gpt-4o-mini', 'gpt-4o', 'claude-sonnet-4-6', 'claude-opus-4-6'],
})
```

## Cost Savings

Typical cost reduction with smart routing vs. always using the best model:

| Workload | Without Routing | With Routing | Savings |
|----------|----------------|--------------|---------|
| 100 tasks (mixed) | $4.20 | $0.95 | **77%** |
| Code review (simple) | $1.50 | $0.15 | **90%** |
| Architecture (expert) | $7.50 | $7.50 | 0% |

Smart routing saves the most when your workload has a mix of simple and complex tasks, which is the typical case for coding agents.

## Integration with Agent Loop

```typescript
const agent = new AgentLoop({
  model: router,  // pass router instead of model string
  tools: toolRegistry,
})
```

The agent loop calls `router.selectModel(prompt)` on each turn, so the model can change mid-conversation as task complexity evolves.
