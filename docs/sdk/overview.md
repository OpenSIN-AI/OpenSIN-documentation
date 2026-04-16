---
title: "SDK Overview"
---

# OpenSIN SDK

The `@opensin/sdk` package provides the core building blocks for creating AI agents, tools, and workflows.

## Installation

```bash
bun add @opensin/sdk
```

## Module Overview

| Module | Description |
|--------|-------------|
| [Agent Loop](/sdk/agent-loop) | ReAct loop with tool calling, streaming, and turn management |
| [Tool System](/sdk/tool-system) | Define, validate, and execute tools with JSON Schema parameters |
| [Model Routing](/sdk/model-routing) | Smart model selection based on task complexity |
| [Memory Manager](/sdk/memory) | Persistent memory with search, tags, and access tracking |
| [Context Management](/sdk/context-management) | Token-aware context compression and sliding windows |
| [Safety & Permissions](/sdk/safety) | Destructive command detection and permission gates |
| [Session Persistence](/sdk/sessions) | Save and restore agent sessions across restarts |
| [Hooks & Lifecycle](/sdk/hooks) | Event-driven lifecycle hooks for agent customization |
| [Parallel Execution](/sdk/parallel-execution) | Concurrent tool execution with path-scoped locking |
| [Usage & Pricing](/sdk/usage-pricing) | Token counting and cost estimation per model |

## Quick Start

```typescript
import {
  AgentLoop,
  ToolRegistry,
  SmartModelRouter,
  PermissionManager,
  SessionManager,
  ContextCompressor,
  SafetyDetector,
  UsagePricing,
} from '@opensin/sdk'

// 1. Set up model routing
const router = new SmartModelRouter({
  models: {
    trivial: 'gpt-5.4-mini',
    simple: 'gpt-5.4-mini',
    moderate: 'gpt-5.4',
    complex: 'claude-sonnet-4-6',
    expert: 'claude-opus-4-6',
  },
})

// 2. Register tools
const tools = new ToolRegistry()
tools.register({
  name: 'read_file',
  description: 'Read a file from the workspace',
  parameters: {
    type: 'object',
    properties: {
      path: { type: 'string' },
    },
    required: ['path'],
  },
  execute: async ({ path }) => {
    const content = await fs.readFile(path, 'utf-8')
    return { content }
  },
})

// 3. Create the agent loop
const agent = new AgentLoop({
  model: router,
  tools,
  permissions: new PermissionManager({ mode: 'interactive' }),
  session: new SessionManager({ persistence: 'file' }),
  context: new ContextCompressor({ maxTokens: 8000 }),
  safety: new SafetyDetector(),
  pricing: new UsagePricing(),
  maxTurns: 25,
})

// 4. Run
const result = await agent.run('Read the README and summarize it')
```

## Architecture

```
┌─────────────────────────────────────────────────┐
│                   Agent Loop                     │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │
│  │  Model   │  │  Tool    │  │   Context     │  │
│  │  Router  │  │  System  │  │   Compressor  │  │
│  └──────────┘  └──────────┘  └───────────────┘  │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │
│  │ Session  │  │ Safety   │  │   Permission  │  │
│  │ Manager  │  │ Detector │  │   Manager     │  │
│  └──────────┘  └──────────┘  └───────────────┘  │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │
│  │  Memory  │  │  Hooks   │  │   Usage       │  │
│  │  Manager │  │  System  │  │   Pricing     │  │
│  └──────────┘  └──────────┘  └───────────────┘  │
└─────────────────────────────────────────────────┘
```

## Package Exports

All modules are exported from the main package entry:

```typescript
import {
  // Agent Loop
  AgentLoop,
  
  // Tool System
  ToolRegistry,
  MCPStdioClient,
  
  // Intelligence
  SmartModelRouter,
  ContextCompressor,
  MemoryManager,
  FileMemoryProvider,
  
  // Safety
  SafetyDetector,
  PermissionManager,
  
  // Infrastructure
  SessionManager,
  HookSystem,
  ParallelToolExecutor,
  UsagePricing,
  
  // Prompt Building
  PromptBuilder,
  
  // Skills
  SkillSystem,
} from '@opensin/sdk'
```

## Test Coverage

The SDK has **573+ passing tests** across all modules, verified with Vitest:

```bash
cd packages/opensin-sdk
npm test

# Output:
# Test Files  15 passed
# Tests       573 passed
# Duration    4.2s
```

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
