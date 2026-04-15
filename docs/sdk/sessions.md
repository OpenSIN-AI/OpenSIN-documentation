---
title: "Session Persistence"
---

# Session Persistence

The Session Manager saves and restores agent conversation state across restarts, enabling long-running tasks that survive process termination.

## Basic Usage

```typescript
import { SessionManager } from '@opensin/sdk'

const session = new SessionManager({
  persistence: 'file',
  directory: '.opensin/sessions',
})

// Save session state
await session.save({
  id: 'ses_abc123',
  messages: conversationHistory,
  metadata: {
    task: 'Refactoring auth module',
    startedAt: new Date(),
    model: 'claude-sonnet-4-6',
  },
})

// Restore session
const restored = await session.load('ses_abc123')
console.log(restored.messages.length) // conversation continues
```

## Storage Backends

| Backend | Use Case | Configuration |
|---------|----------|---------------|
| `file` | Local development | `{ persistence: 'file', directory: '.opensin/sessions' }` |
| `memory` | Testing, ephemeral | `{ persistence: 'memory' }` |
| `supabase` | Production, multi-agent | `{ persistence: 'supabase', url: '...', key: '...' }` |

## Session Lifecycle

```
create → active → [paused] → completed
                      │
                      └──→ resumed → active → completed
```

```typescript
// Create a new session
const session = await sessionManager.create({
  task: 'Build login page',
  model: 'claude-sonnet-4-6',
})

// Pause (save state to disk)
await sessionManager.pause(session.id)

// Resume later
const resumed = await sessionManager.resume(session.id)

// Mark complete
await sessionManager.complete(session.id, {
  result: 'Login page implemented successfully',
  turns: 15,
  tokensUsed: 42000,
})
```

## Listing Sessions

```typescript
// List all sessions
const sessions = await sessionManager.list()

// Filter by status
const active = await sessionManager.list({ status: 'active' })
const completed = await sessionManager.list({ status: 'completed' })

// Search sessions
const results = await sessionManager.search('auth refactor')
```

## File Format

Sessions are stored as JSON files:

```
.opensin/sessions/
├── ses_abc123.json
├── ses_def456.json
└── ses_ghi789.json
```

Each file contains:

```json
{
  "id": "ses_abc123",
  "status": "completed",
  "createdAt": "2026-04-01T10:00:00Z",
  "updatedAt": "2026-04-01T10:15:00Z",
  "metadata": {
    "task": "Refactoring auth module",
    "model": "claude-sonnet-4-6",
    "turns": 12,
    "tokensUsed": 35000
  },
  "messages": [
    { "role": "system", "content": "..." },
    { "role": "user", "content": "..." },
    { "role": "assistant", "content": "..." }
  ]
}
```

## Integration with Agent Loop

```typescript
const agent = new AgentLoop({
  model: 'claude-sonnet-4-6',
  tools: toolRegistry,
  session: new SessionManager({ persistence: 'file' }),
})

// Agent automatically saves state after each turn
const result = await agent.run('Refactor the auth module')

// Later, resume from where we left off
const result2 = await agent.resume(result.sessionId, 'Also add tests')
```

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
