# Agent Memory Plugin

Letta-style persistent memory for OpenSIN CLI.

## Overview

Cross-session memory persistence and retrieval with categories, importance scoring, and auto-consolidation.

## Installation

```bash
bun add @opensin/plugin-agent-memory
```

## Usage

```typescript
import { AgentMemoryPlugin } from "@opensin/plugin-agent-memory";

const plugin = new AgentMemoryPlugin({ maxEntries: 1000 });

// Add memory
const entry = plugin.add("facts", "The API endpoint is /v1/chat", 0.8);

// Retrieve memory
const memory = plugin.get(entry.id);

// Query memories
const results = plugin.query({
  category: "facts",
  minImportance: 0.5,
  limit: 10,
});

// Get stats
const stats = plugin.getStats();
console.log(`Total: ${stats.totalEntries} entries`);
```

## API

### `AgentMemoryPlugin`

Class with `add()`, `get()`, `query()`, `update()`, `delete()`, `getCategories()`, `getStats()`, `consolidate()`, `getConfig()`, `setConfig()` methods.

## Configuration

```json
{
  "maxEntries": 1000,
  "maxEntriesPerCategory": 200,
  "minImportance": 0,
  "autoConsolidate": true
}
```

## Testing

```bash
bun test
# 14 tests passing
```

---

## Relevante Mandate

| Mandat                  | Priority | Regel                               |
| ----------------------- | -------- | ----------------------------------- |
| **Bun-Only**            | -1.5     | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot**     | -5.0     | KEINE Diagnose ohne Beweis          |
| **Test-Beweis-Pflicht** | 0.0      | KEIN "Done" ohne echten Test-Lauf   |

→ [Alle Mandate](/best-practices/code-quality)
