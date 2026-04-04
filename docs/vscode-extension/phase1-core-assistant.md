# Phase 1: Core AI Assistant

Phase 1 establishes the foundational AI chat experience with specialized agent modes, streaming responses, memory consolidation, and LSP integration.

## 1.1 Agent Mode Selector

SIN Code provides 5 specialized agent modes, each with a distinct system prompt and behavior profile.

### Mode Definitions

| Mode | ID | Icon | System Prompt Summary |
|------|-----|------|----------------------|
| **Architect** | `architect` | 🏗️ | High-level design, patterns, roadmaps. No implementation code unless asked. |
| **Code** | `code` | 💻 | Clean, production-ready code. Best practices and project conventions. **Default mode.** |
| **Debug** | `debug` | 🐛 | Root cause analysis. Read logs, trace execution, evidence-based fixes. |
| **Ask** | `ask` | ❓ | Explain code, answer questions, provide docs. No code changes unless asked. |
| **Proactive** | `proactive` | ⚡ | Always-on background analysis. Anticipate needs, suggest improvements. |

### Mode Switching

**Via Status Bar:**
1. Click the mode selector on the left status bar: `$(symbol-misc) Code`
2. Choose a mode from the Quick Pick dropdown

**Via Command Palette:**
1. `Cmd+Shift+P` → `SIN Code: Select Mode`
2. Select desired mode

### Mode in Prompts

Each mode injects its system prompt into every request:
```
[Mode: You are SIN Code in Code Mode. Focus on writing clean, production-ready code...]

[Context Files: /path/to/file.ts]

[LSP Context]
**Current File:** /path/to/file.ts
**Cursor Word:** myFunction
**Diagnostics (2):**
- [ERROR] Line 15: Cannot find name 'foo'
- [WARNING] Line 22: Unused variable 'bar'

**Symbols in File:** myFunction, MyClass, helper

User: How do I fix this error?
```

## 1.2 Sidebar Chat Panel

The main interaction surface is a webview-based chat panel in the VS Code sidebar.

### UI Components

```
┌─────────────────────────────────────┐
│ SIN Code              [Code]        │  ← Header with mode badge
├─────────────────────────────────────┤
│                                     │
│  [User messages]                    │  ← Chat history
│  [AI responses]                     │     (streaming)
│                                     │
├─────────────────────────────────────┤
│ [Status: SIN Code is thinking...]   │  ← Status indicator
├─────────────────────────────────────┤
│ [Ask SIN Code...] [Send] [Stop]     │  ← Input area
├─────────────────────────────────────┤
│ 🐝 Swarm Coordinator                │
│ [Dispatch Agent]                    │  ← Swarm quick-access
├─────────────────────────────────────┤
│ 🤖 Agent Marketplace                │
│ [Open Marketplace]                  │  ← Marketplace quick-access
└─────────────────────────────────────┘
```

### Features

- **Streaming responses** — Tokens appear in real-time via JSON event stream parsing
- **Mode badge** — Shows current active mode in the header
- **Cancel button** — Stops any running generation (SIGTERM to CLI process)
- **Context file tracking** — Added files shown in prompt context
- **Status indicator** — Shows "thinking...", "Done.", or error messages

### Opening the Sidebar

- Click the SIN Code icon in the activity bar
- Command palette: `SIN Code: Start`
- Keyboard: No default shortcut (configurable)

## 1.3 Memory Consolidation

Automatic loading and watching of project memory files.

### Supported Memory Files

| File | Priority | Description |
|------|----------|-------------|
| `AGENTS.md` | High | Agent instructions and project conventions |
| `SIN-MEMORY.md` | High | Persistent session memory |
| `CLAUDE.md` | Medium | Compatibility with Claude Code projects |
| `.sincode-memory.md` | Low | Hidden memory file |

### How It Works

1. **Scan** — On extension activation, scans workspace root for memory files
2. **Load** — Reads all found files and concatenates with section headers
3. **Watch** — Creates `FileSystemWatcher` for changes to memory files
4. **Refresh** — On change, re-scans and shows notification: "Memory files updated, context refreshed."

### Memory Format in Prompts

```
[Memory Context]

--- AGENTS.md ---
# Project Rules
- Always use TypeScript
- Follow the Global Fleet Self-Healing Protocol

--- SIN-MEMORY.md ---
## 2026-04-03T10:30:00.000Z
User prefers functional programming patterns.
```

### Appending Memory

Memory can be appended programmatically with timestamps:
```
## 2026-04-03T10:30:00.000Z
New memory entry with timestamp
```

## 1.4 LSP Integration

Semantic context extraction via VS Code's diagnostic API and `simone-mcp`.

### Diagnostic Extraction

Reads from `vscode.languages.getDiagnostics()` for the active editor:

```typescript
{
  file: "/path/to/file.ts",
  severity: "error" | "warning" | "info",
  message: "Cannot find name 'foo'",
  line: 14,
  character: 5
}
```

Up to 5 most relevant diagnostics are included in the context.

### Symbol Extraction

Spawns `simone-mcp symbols --file <path> --format json` to extract:
- Function names
- Class definitions
- Variable declarations
- Interface/type definitions

### Cursor-Aware Context

The word at the current cursor position is included:
```
**Cursor Word:** myFunction
```

### Full LSP Context Output

```
**Current File:** /Users/jeremy/dev/project/src/index.ts
**Cursor Word:** processData
**Diagnostics (2):**
- [ERROR] Line 15: Cannot find name 'foo'
- [WARNING] Line 22: Unused variable 'bar'
**Symbols in File:** processData, DataHandler, Config, init
```

## 1.5 Model Selector

Choose from all models configured in `~/.config/opencode/`.

### Auto-Discovery

Models are fetched via:
```bash
opencode config list-models --format json
```

### Fallback Models

If model discovery fails, defaults to:
- `opencode/qwen3.6-plus-free`
- `google/antigravity-gemini-3.1-pro`
- `google/antigravity-claude-sonnet-4-6`

### Changing Models

1. Click the model selector: `$(symbol-constant) qwen3.6-plus`
2. Choose from the Quick Pick list
3. The change takes effect immediately for the next prompt

## 1.6 File Context Management

Add any open file to the conversation context.

### Methods

- **Command Palette:** `SIN Code: Add File to Context`
- **Editor Context Menu:** Right-click → `Add File to SIN Code Context`

### Behavior

Added files are tracked in the `contextFiles` array and included in every prompt:
```
[Context Files: /path/to/file1.ts, /path/to/file2.ts]
```

### Buddy XP Reward

Adding a file to context earns **+5 XP** for BUDDY.
