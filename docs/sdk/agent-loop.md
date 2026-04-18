---
title: "Agent Loop"
---

# Agent Loop

The Agent Loop implements the ReAct (Reasoning + Acting) pattern — the core execution cycle that turns an LLM into an autonomous agent.

## How It Works

```
User Prompt
    │
    ▼
┌─────────────────────┐
│   LLM Call          │ ◄──────────────────┐
│   (with tools)      │                    │
└─────────┬───────────┘                    │
          │                                │
          ▼                                │
    ┌─────────────┐     Yes    ┌──────────┴──────────┐
    │ Tool calls? ├───────────►│ Execute tools       │
    └──────┬──────┘            │ (parallel if safe)  │
           │ No                └─────────────────────┘
           ▼
    ┌─────────────┐
    │ Return      │
    │ final answer│
    └─────────────┘
```

## Basic Usage

```typescript
import { AgentLoop } from '@opensin/sdk'

const agent = new AgentLoop({
  model: 'claude-sonnet-4-6',
  tools: toolRegistry,
  systemPrompt: 'You are a helpful coding assistant.',
  maxTurns: 20,
})

const result = await agent.run('Fix the failing test in auth.test.ts')
console.log(result.response)
console.log(`Completed in ${result.turns} turns`)
```

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `model` | `string \| ModelRouter` | required | LLM model or router instance |
| `tools` | `ToolRegistry` | required | Available tools |
| `systemPrompt` | `string` | `''` | System instructions |
| `maxTurns` | `number` | `25` | Maximum ReAct iterations |
| `earlyExit` | `boolean` | `true` | Stop when no tool calls are made |
| `streaming` | `boolean` | `false` | Enable streaming responses |
| `permissions` | `PermissionManager` | `null` | Permission gate for tools |
| `context` | `ContextCompressor` | `null` | Context window manager |
| `session` | `SessionManager` | `null` | Session persistence |

## Events

The agent loop emits events at each stage:

```typescript
agent.on('turn:start', ({ turn, messages }) => {
  console.log(`Turn ${turn} starting with ${messages.length} messages`)
})

agent.on('tool:call', ({ name, args }) => {
  console.log(`Calling tool: ${name}`)
})

agent.on('tool:result', ({ name, result, duration }) => {
  console.log(`Tool ${name} completed in ${duration}ms`)
})

agent.on('turn:end', ({ turn, response }) => {
  console.log(`Turn ${turn} complete`)
})

agent.on('complete', ({ turns, totalTokens }) => {
  console.log(`Agent finished in ${turns} turns, ${totalTokens} tokens`)
})
```

## Streaming

Enable real-time output streaming:

```typescript
const agent = new AgentLoop({
  model: 'claude-sonnet-4-6',
  tools: toolRegistry,
  streaming: true,
})

for await (const chunk of agent.stream('Explain this codebase')) {
  if (chunk.type === 'text') {
    process.stdout.write(chunk.text)
  } else if (chunk.type === 'tool_call') {
    console.log(`\nUsing tool: ${chunk.name}`)
  }
}
```

## Turn Management

Control how the agent progresses through turns:

```typescript
const agent = new AgentLoop({
  maxTurns: 10,
  earlyExit: true,
  onMaxTurns: 'summarize', // or 'error', 'continue'
})
```

- **`earlyExit: true`**: Stops when the LLM returns a response without tool calls
- **`onMaxTurns: 'summarize'`**: Summarizes progress when hitting the turn limit
- **`onMaxTurns: 'error'`**: Throws an error at the turn limit

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
