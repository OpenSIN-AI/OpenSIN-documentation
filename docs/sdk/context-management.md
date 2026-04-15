---
title: "Context Management"
---

# Context Management

The Context Management module keeps the agent's conversation within token limits by intelligently compressing message history.

## The Problem

LLMs have finite context windows (8K-200K tokens). Long agent sessions accumulate messages, tool calls, and results that quickly exceed the limit. Without compression, the agent either crashes or loses important context.

## Context Compressor

```typescript
import { ContextCompressor } from '@opensin/sdk'

const compressor = new ContextCompressor({
  maxTokens: 8000,
  strategy: 'sliding-window',
})

// Before sending to LLM, compress the history
const compressed = compressor.compress(messages)
// compressed.length <= maxTokens (approximately)
```

## Strategies

### Sliding Window

Keeps the most recent N messages and the system prompt. Simple and predictable.

```typescript
const compressor = new ContextCompressor({
  strategy: 'sliding-window',
  maxTokens: 8000,
  keepSystemPrompt: true,  // always keep system prompt
  keepFirstN: 2,           // keep first 2 user messages for context
})
```

**Best for**: Long interactive sessions, code editing

### Summarize

Replaces older messages with a summary, preserving key decisions and context.

```typescript
const compressor = new ContextCompressor({
  strategy: 'summarize',
  maxTokens: 8000,
  summaryModel: 'openai/gpt-5.4-mini',  // cheap model for summaries
  summaryMaxTokens: 500,
})
```

**Best for**: Research tasks, multi-step investigations

### Relevance

Scores each message by relevance to the current task and keeps only the most relevant.

```typescript
const compressor = new ContextCompressor({
  strategy: 'relevance',
  maxTokens: 8000,
  relevanceThreshold: 0.3,
})
```

**Best for**: Focused code editing, single-file tasks

## Token Counting

The compressor uses tiktoken-compatible counting:

```typescript
const tokenCount = compressor.countTokens(messages)
console.log(`Current context: ${tokenCount} tokens`)
console.log(`Limit: ${compressor.maxTokens} tokens`)
console.log(`Utilization: ${(tokenCount / compressor.maxTokens * 100).toFixed(1)}%`)
```

## Tool Result Truncation

Large tool results (file contents, grep output) are automatically truncated:

```typescript
const compressor = new ContextCompressor({
  maxTokens: 8000,
  toolResultMaxTokens: 2000,  // cap individual tool results
  toolResultStrategy: 'head-tail',  // keep start and end
})
```

## Integration

The compressor integrates seamlessly with the agent loop:

```typescript
const agent = new AgentLoop({
  model: 'claude-sonnet-4-6',
  tools: toolRegistry,
  context: new ContextCompressor({
    maxTokens: 8000,
    strategy: 'sliding-window',
  }),
})
```

The agent loop calls `compressor.compress(messages)` before each LLM call, ensuring the context always fits within the model's window.
