---
title: "Usage & Pricing"
---

# Usage & Pricing

The `UsagePricing` module tracks token usage and estimates costs per model in real-time, giving you visibility into agent spend.

## Usage

```typescript
import { UsagePricing } from '@opensin/sdk'

const pricing = new UsagePricing()

// Record each LLM call
pricing.record({
  model: 'claude-sonnet-4-6',
  inputTokens: 2500,
  outputTokens: 800,
})

pricing.record({
  model: 'gpt-5.4-mini',
  inputTokens: 500,
  outputTokens: 200,
})

// Get session summary
const summary = pricing.getSummary()
console.log(summary)
// {
//   totalCost: 0.0249,
//   totalInputTokens: 3000,
//   totalOutputTokens: 1000,
//   totalCalls: 2,
//   byModel: {
//     'claude-sonnet-4-6': { cost: 0.0234, calls: 1, inputTokens: 2500, outputTokens: 800 },
//     'gpt-5.4-mini': { cost: 0.0015, calls: 1, inputTokens: 500, outputTokens: 200 }
//   }
// }
```

## Supported Models

Pricing data for 10+ models:

| Model | Input (per 1M) | Output (per 1M) |
|-------|---------------|-----------------|
| `gpt-5.4-mini` | $0.15 | $0.60 |
| `gpt-5.4` | $5.00 | $15.00 |
| `claude-sonnet-4-6` | $3.00 | $15.00 |
| `claude-opus-4-6` | $15.00 | $75.00 |
| `gemini-3-flash` | $0.15 | $0.60 |
| `gemini-3.1-pro` | $2.50 | $10.00 |
| `qwen-3.5-122b` | $0.30 | $1.20 |
| `qwen-3.5-397b` | $1.00 | $4.00 |

## Cost Estimation

Estimate cost before making a call:

```typescript
const estimate = pricing.estimate({
  model: 'claude-opus-4-6',
  inputTokens: 10000,
  outputTokens: 5000,
})
console.log(`Estimated cost: $${estimate.toFixed(4)}`)
// Estimated cost: $0.5250
```

## Formatting

Format token counts and costs for display:

```typescript
console.log(pricing.formatTokens(1500000))
// '1.5M tokens'

console.log(pricing.formatCost(0.0523))
// '$0.0523'

console.log(pricing.formatSummary())
// 'Session: 3.3K tokens, $0.0249 (2 calls)'
```

## Budget Limits

Set spending limits to prevent runaway costs:

```typescript
const pricing = new UsagePricing({
  budget: {
    maxCostPerSession: 1.00,   // $1 per session
    maxCostPerTurn: 0.10,      // $0.10 per turn
    warnAt: 0.75,              // warn at 75% of budget
  },
})

pricing.on('budget:warning', ({ spent, limit }) => {
  console.warn(`Budget warning: $${spent} of $${limit} used`)
})

pricing.on('budget:exceeded', ({ spent, limit }) => {
  throw new Error(`Budget exceeded: $${spent} > $${limit}`)
})
```

## Integration with Hooks

Use hooks to automatically track all LLM costs:

```typescript
const pricing = new UsagePricing()

hooks.on('llm:after', ({ model, inputTokens, outputTokens }) => {
  pricing.record({ model, inputTokens, outputTokens })
})

hooks.on('agent:complete', () => {
  console.log(pricing.formatSummary())
})
```

## Combined with Model Routing

When combined with SmartModelRouter, cost tracking shows the savings from intelligent routing:

```typescript
const summary = pricing.getSummary()
// Without routing: would have used claude-opus for everything = $7.50
// With routing: mixed models = $0.95
// Savings: 87%
```
