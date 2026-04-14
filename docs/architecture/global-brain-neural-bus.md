# Global Brain & Neural-Bus

> The persistent knowledge and communication layer for the entire OpenSIN-AI agent fleet.

## Overview

The OpenSIN ecosystem uses two complementary systems for fleet-wide intelligence:

| System | Purpose | Repository |
|--------|---------|-----------|
| **Global Brain (PCPM)** | Persistent Code Plan Memory — cross-project knowledge, rules, plans | [global-brain](https://github.com/Delqhi/global-brain) |
| **Neural-Bus (JetStream)** | Real-time agent-to-agent messaging via NATS JetStream | [OpenSIN-Neural-Bus](https://github.com/OpenSIN-AI/OpenSIN-Neural-Bus) |

## Global Brain (PCPM)

The **Persistent Code Plan Memory (PCPM)** system ensures that knowledge, rules, and plans persist across all agent sessions and projects.

### Key Features

- **sin-brain CLI** — Add rules, sync knowledge, check Neural-Bus status
- **sin-brain MCP** — Real-time rule management for agents (`add_rule`, `sync_brain`, `list_global_rules`)
- **Preview MCP** — Opens images directly in macOS Preview.app (`open_in_preview`, `open_image_in_preview`)
- **Auto-Sync Hooks** — After every OpenCode run, knowledge is automatically synced via `sync-chat-turn`
- **Bidirectional Sync** — Global brain ↔ local project `.pcpm/` directories

### CLI Commands

```bash
# Add a rule to global brain
node src/cli.js add-rule --text "Your rule" --priority -5 --scope global

# Sync after chat turn (runs automatically via afterRun hook)
node src/cli.js sync-chat-turn

# Check Neural-Bus status
node src/cli.js neural-bus-status

# Setup hooks in a project
node src/cli.js setup-hooks --project my-project --project-root /path/to/repo
```

### MCP Tools

| Tool | Server | Description |
|------|--------|-------------|
| `add_rule` | sin-brain MCP | Add rules to global AGENTS.md and/or local .pcpm |
| `sync_brain` | sin-brain MCP | Run bidirectional sync between local and global brain |
| `open_image_in_preview` | sin-brain MCP | Open an image file in macOS Preview.app |
| `list_global_rules` | sin-brain MCP | List all rules currently in the global brain |
| `open_in_preview` | Preview MCP | Opens an image file in Preview.app with validation |

### Project Brain Structure

Every project connected to the Global Brain has a `.pcpm/` directory:

```
.pcpm/
├── knowledge-summary.json  # Global rules + project facts/mistakes/solutions
├── plan/
│   └── latest.json         # Current plan with step tracking
└── active-context.json     # Current goal state + forbidden strategies
```

### Auto-Sync Integration

After every OpenCode run, the `afterRun` hook automatically executes:

```bash
node "$BRAIN_CLI" sync-chat-turn 2>/dev/null
```

This ensures knowledge is never lost between sessions — all bug fixes, architectural decisions, and discovered patterns are persistently stored.

## Neural-Bus (JetStream)

The **OpenSIN-Neural-Bus** is a NATS JetStream-based message bus connecting all A2A agents, OpenCode runtimes, and the Global Brain through a unified event system.

### Architecture

```
OpenCode CLI / Agent Runtime
  ↓
OpenSinAgentRuntime (agentId, sessionId, bus)
  ↓
JetStream (nats://127.0.0.1:4222)
  ↓
Subjects: workflow.request, workflow.reply, agent.observation, agent.lesson
  ↓
Ouroboros Bridge → rememberLesson() / registerCapability()
  ↓
Global Brain (.pcpm/ → AGENTS.md → knowledge graph)
```

### Core Exports

| Export | Language | Purpose |
|--------|----------|---------|
| `OpenCodeJetStreamClient` | TypeScript | NATS/JetStream client for OpenCode |
| `OpenSinAgentRuntime` | TypeScript | Agent runtime wrapper with publish/consume |
| `SUBJECTS` | TypeScript | Canonical subject taxonomy |
| `createEventEnvelope` | TypeScript | Validated event envelopes |
| `OuroborosMemory` | Python | SQLite-backed memory store |
| `OuroborosCLI` | Python | Python CLI for Ouroboros memory |

### Subject Taxonomy

| Subject | Direction | Purpose |
|---------|-----------|---------|
| `workflow.request` | Client → Server | Work request to agent |
| `workflow.reply` | Server → Client | Answer/result |
| `agent.observation` | Agent → Brain | State report (boot, error, done) |
| `agent.lesson` | Agent → Brain | Learned lesson (written to brain memory) |
| `agent.capability` | Agent → Brain | New capability registered |

### Durable Consumer Pattern

```typescript
const worker = await runtime.consumeAssignedWork({
  subject: SUBJECTS.workflowRequest,
  stream: "OPENSIN_WORKFLOW_EVENTS",
  durableName: "issue-8-worker",  // Same name = resume after restart
  deliverPolicy: "all",
  ackWaitMs: 500,
}, async (event) => {
  // Process work
});
```

### Lesson Publishing

```typescript
await runtime.publishLessonLearned({
  context: "JetStream reconnect handling",
  lesson: "Reuse the same durable consumer name so restart recovery is automatic.",
  successRate: 1.0,
});
// → Automatically written to Global Brain via Ouroboros Bridge
```

### Local Verification

```bash
cd ~/dev/OpenSIN-Neural-Bus
docker compose up -d nats
npm install && npm test
```

## Integration with OpenCode

Both systems are integrated into the global OpenCode configuration:

```json
{
  "mcp": {
    "sin-brain": {
      "type": "local",
      "command": ["node", "/Users/jeremy/dev/global-brain/src/mcp/sin-brain-server.mjs"],
      "enabled": true
    },
    "sin-preview": {
      "type": "local",
      "command": ["node", "/Users/jeremy/dev/global-brain/src/mcp/preview-server.mjs"],
      "enabled": true
    }
  }
}
```

## Related

- [PCPM AGENTS.md](https://github.com/Delqhi/global-brain/blob/main/AGENTS.md)
- [Neural-Bus Subject Taxonomy](https://github.com/OpenSIN-AI/OpenSIN-Neural-Bus/blob/main/docs/jetstream-subject-taxonomy.md)
- [OpenCode Configuration](https://github.com/Delqhi/global-brain/blob/main/src/cli.js)
