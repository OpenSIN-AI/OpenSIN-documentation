---
title: "Parallel Execution"
---

# Parallel Tool Execution

The `ParallelToolExecutor` runs independent tool calls concurrently, significantly reducing agent turn time when multiple tools can run simultaneously.

## The Problem

Sequential execution wastes time when tools are independent:

```
Sequential (slow):
  read(a.ts) ──► read(b.ts) ──► read(c.ts) ──► grep(TODO)
  Total: 400ms + 350ms + 380ms + 200ms = 1330ms

Parallel (fast):
  read(a.ts) ──┐
  read(b.ts) ──┤──► grep(TODO)
  read(c.ts) ──┘
  Total: max(400, 350, 380) + 200 = 600ms (2.2x faster)
```

## Usage

```typescript
import { ParallelToolExecutor } from "@opensin/sdk";

const executor = new ParallelToolExecutor({
  maxWorkers: 8,
  timeout: 30_000,
});

const results = await executor.execute([
  { tool: "read", args: { path: "src/auth.ts" } },
  { tool: "read", args: { path: "src/db.ts" } },
  { tool: "read", args: { path: "src/api.ts" } },
  { tool: "grep", args: { pattern: "TODO", path: "src/" } },
]);
```

## Path-Scoped Concurrency

The executor prevents conflicting operations on the same file:

```typescript
// These run in PARALLEL (different files):
executor.execute([
  { tool: "write", args: { path: "a.ts", content: "..." } },
  { tool: "write", args: { path: "b.ts", content: "..." } },
]);

// These run SEQUENTIALLY (same file):
executor.execute([
  { tool: "read", args: { path: "a.ts" } },
  { tool: "write", args: { path: "a.ts", content: "..." } },
]);
```

The locking is automatic — the executor extracts file paths from tool arguments and acquires per-path locks.

## Configuration

| Option        | Type      | Default | Description                            |
| ------------- | --------- | ------- | -------------------------------------- |
| `maxWorkers`  | `number`  | `8`     | Maximum concurrent tool executions     |
| `timeout`     | `number`  | `30000` | Per-tool timeout in milliseconds       |
| `pathLocking` | `boolean` | `true`  | Enable path-scoped concurrency control |

## Error Handling

Errors in one tool don't block others:

```typescript
const results = await executor.execute([
  { tool: "read", args: { path: "exists.ts" } }, // succeeds
  { tool: "read", args: { path: "missing.ts" } }, // fails
  { tool: "grep", args: { pattern: "fn", path: "." } }, // succeeds
]);

// results[0] = { content: '...' }
// results[1] = { content: 'Error: ENOENT', isError: true }
// results[2] = { content: '...' }
```

## Integration with Agent Loop

The agent loop uses parallel execution automatically when the LLM returns multiple tool calls in a single response:

```typescript
const agent = new AgentLoop({
  model: "claude-sonnet-4-6",
  tools: toolRegistry,
  parallelExecution: new ParallelToolExecutor({
    maxWorkers: 8,
  }),
});
```

When the LLM says "I'll read these 5 files," all 5 reads happen concurrently instead of one at a time.
