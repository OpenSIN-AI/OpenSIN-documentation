---
title: "Memory Manager"
---

# Memory Manager

The Memory Manager provides persistent, searchable memory for agents — allowing them to remember context across sessions.

## Overview

```typescript
import { MemoryManager, FileMemoryProvider } from "@opensin/sdk";

const memory = new MemoryManager({
  provider: new FileMemoryProvider({
    directory: ".opensin/memory",
  }),
});
```

## Writing Memories

```typescript
await memory.write({
  name: "auth/login-flow",
  content: `
## Login Flow
The login system uses JWT tokens with refresh rotation.
- Access tokens expire after 15 minutes
- Refresh tokens expire after 7 days
- Tokens are stored in httpOnly cookies
  `,
  tags: ["auth", "security", "jwt"],
});
```

## Reading Memories

```typescript
const mem = await memory.read("auth/login-flow");
console.log(mem.content);
console.log(mem.lastAccessed); // tracks access time
```

## Searching

Search across all memories by content or tags:

```typescript
// Full-text search
const results = await memory.search("JWT token");
// Returns matching memories ranked by relevance

// Tag-based filtering
const authMemories = await memory.findByTags(["auth"]);
```

## Memory Organization

Memories are organized by name paths using `/` as a separator:

```
auth/
  login-flow
  oauth-config
  session-management
database/
  schema
  migrations
  connection-pool
api/
  endpoints
  error-handling
```

## CRUD Operations

```typescript
// Create
await memory.write({ name: "project/overview", content: "..." });

// Read
const mem = await memory.read("project/overview");

// Update (overwrite)
await memory.write({ name: "project/overview", content: "updated..." });

// Delete
await memory.delete("project/overview");

// List all
const all = await memory.list();
const byTopic = await memory.list("auth");
```

## Access Tracking

The memory manager tracks when each memory was last accessed, helping identify stale or frequently-used context:

```typescript
const mem = await memory.read("auth/login-flow");
console.log(mem.createdAt); // when it was first written
console.log(mem.updatedAt); // when it was last modified
console.log(mem.lastAccessed); // when it was last read
console.log(mem.accessCount); // total read count
```

## File Memory Provider

The default provider stores memories as markdown files on disk:

```
.opensin/memory/
├── auth/
│   ├── login-flow.md
│   └── oauth-config.md
├── database/
│   └── schema.md
└── global/
    └── code-style.md
```

Each file includes frontmatter metadata:

```markdown
---
tags: [auth, security, jwt]
createdAt: 2026-04-01T10:00:00Z
updatedAt: 2026-04-05T14:30:00Z
---

## Login Flow

The login system uses JWT tokens...
```

## Global Memories

Use the `global/` prefix for memories shared across projects:

```typescript
await memory.write({
  name: "global/typescript/style-guide",
  content: "Always use strict TypeScript, no `any` types...",
});
```

Global memories are stored in `~/.config/opencode/memory/` and are accessible from any project.

---

## Relevante Mandate

| Mandat                  | Priority | Regel                               |
| ----------------------- | -------- | ----------------------------------- |
| **Bun-Only**            | -1.5     | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot**     | -5.0     | KEINE Diagnose ohne Beweis          |
| **Test-Beweis-Pflicht** | 0.0      | KEIN "Done" ohne echten Test-Lauf   |

→ [Alle Mandate](/best-practices/code-quality)
