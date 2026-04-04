# Extension Architecture Overview

## System Architecture

The SIN Code VS Code Extension is built on a modular architecture with 10 source modules that communicate through a central `SINCodeViewProvider`. The extension acts as a bridge between VS Code's extension APIs and the `opencode` CLI, which serves as the AI inference engine.

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          VS Code Extension Host                         │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                    SINCodeViewProvider                            │  │
│  │  ┌─────────────┐  ┌──────────────────┐  ┌──────────────────────┐ │  │
│  │  │ Mode System │  │ MemoryConsolidate│  │   LspProvider        │ │  │
│  │  │ (5 modes)   │  │ r                │  │   (diagnostics +     │ │  │
│  │  └──────┬──────┘  └────────┬─────────┘  │    symbols)          │ │  │
│  │         │                  │            └──────────┬───────────┘ │  │
│  │  ┌──────▼──────────────────▼───────────────────────▼───────────┐ │  │
│  │  │              buildFullPrompt()                              │ │  │
│  │  │  [Mode SystemPrompt] + [Context Files] + [LSP Context]     │ │  │
│  │  │  + [Memory Context] + [User Input]                          │ │  │
│  │  └──────────────────────────┬──────────────────────────────────┘ │  │
│  │                             │                                    │  │
│  │                    ┌────────▼────────┐                           │  │
│  │                    │  SinCodeBridge   │                           │  │
│  │                    │  (CLI Bridge)    │                           │  │
│  │                    │  opencode run    │                           │  │
│  │                    └────────┬────────┘                           │  │
│  │                             │                                    │  │
│  │                    ┌────────▼────────┐                           │  │
│  │                    │  Stream Parser   │                           │  │
│  │                    │  (JSON events)   │                           │  │
│  │                    └────────┬────────┘                           │  │
│  │                             │                                    │  │
│  │                    ┌────────▼────────┐                           │  │
│  │                    │  BuddySystem     │                           │  │
│  │                    │  (XP + Levels)   │                           │  │
│  │                    └─────────────────┘                           │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────┐  │
│  │ SwarmCoordinator │  │InlineChatProvider│  │ SINCodeActionProvider│  │
│  │ (4 agents)       │  │ (ghost text)     │  │ (QuickFix/Refactor)  │  │
│  └──────────────────┘  └──────────────────┘  └──────────────────────┘  │
│                                                                         │
│  ┌──────────────────┐  ┌──────────────────┐                             │
│  │ MarketplacePanel │  │  Git HEAD Watcher│                             │
│  │ (6 agents)       │  │  (commit detect) │                             │
│  └──────────────────┘  └──────────────────┘                             │
└─────────────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        External Processes                               │
│                                                                         │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────┐  │
│  │  opencode CLI    │  │  simone-mcp CLI  │  │  npm test            │  │
│  │  (AI inference)  │  │  (LSP symbols)   │  │  (auto test runner)  │  │
│  └──────────────────┘  └──────────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

### Module Dependency Graph

```
extension.ts (entry point)
├── cliBridge.ts          → child_process (spawn opencode)
├── modes.ts              → pure data (AGENT_MODES array)
├── lspProvider.ts        → vscode.languages + child_process (simone-mcp)
├── swarmCoordinator.ts   → child_process (spawn opencode --agent)
├── buddyGamification.ts  → vscode.window (StatusBarItem)
├── memoryConsolidation.ts → vscode.workspace + fs (file watching)
├── inlineChat.ts         → cliBridge.ts + vscode.languages
├── codeActions.ts        → cliBridge.ts + vscode.languages
└── agentMarketplace.ts   → vscode.window (WebviewPanel)
```

## File Structure

```
kairos-vscode/
├── src/                              # TypeScript source (compiled to out/)
│   ├── extension.ts                  # Main entry, WebviewView provider, command registration
│   ├── cliBridge.ts                  # RPC bridge to `opencode` CLI
│   ├── modes.ts                      # Agent mode definitions (5 modes)
│   ├── lspProvider.ts                # LSP diagnostics & semantic context
│   ├── swarmCoordinator.ts           # Multi-agent dispatch manager
│   ├── buddyGamification.ts          # BUDDY pet status bar system
│   ├── memoryConsolidation.ts        # AGENTS.md / SIN-MEMORY.md watcher
│   ├── inlineChat.ts                 # InlineCompletionItemProvider
│   ├── codeActions.ts                # CodeActionProvider (Fix/Refactor/Explain/Tests)
│   └── agentMarketplace.ts           # Agent Marketplace webview panel
├── out/                              # Compiled JavaScript (tsc output)
│   ├── extension.js
│   ├── cliBridge.js
│   ├── modes.js
│   ├── lspProvider.js
│   ├── swarmCoordinator.js
│   ├── buddyGamification.js
│   ├── memoryConsolidation.js
│   ├── inlineChat.js
│   ├── codeActions.js
│   └── agentMarketplace.js
├── media/
│   └── icon.png                      # Activity bar icon
├── package.json                      # Extension manifest
├── tsconfig.json                     # TypeScript configuration
├── CHANGELOG.md                      # Version history
└── README.md                         # Extension overview
```

## Core Components

### 1. SINCodeViewProvider (extension.ts)

The central orchestrator. Implements `WebviewViewProvider` to render the sidebar chat panel.

**Responsibilities:**
- Renders the chat UI as inline HTML/CSS/JS in a webview
- Manages the `SinCodeBridge` instance for CLI communication
- Builds full prompts by combining mode, context files, LSP data, and memory
- Handles mode/model selection state
- Routes webview messages to appropriate handlers

**Key Methods:**
| Method | Purpose |
|--------|---------|
| `resolveWebviewView()` | Initializes the webview with HTML and message handlers |
| `buildFullPrompt(userInput)` | Assembles the complete prompt from all context sources |
| `setCurrentMode(mode)` | Updates the active agent mode |
| `setCurrentModel(model)` | Updates the selected LLM model |
| `addFileToContext(path)` | Adds a file path to the context array |
| `notifyModeChange(mode, message)` | Sends mode-change events to the webview |

### 2. SinCodeBridge (cliBridge.ts)

The mandatory communication layer to the `opencode` CLI.

**Responsibilities:**
- Spawns `opencode run <prompt> --format json` with optional `--mode=<mode>` flag
- Parses streaming JSON line-by-line, extracting `type: "text"` events
- Supports process cancellation via SIGTERM
- Auto-discovers available models with fallback defaults
- Routes stderr to the chat UI for debugging

**Data Flow:**
```
User Prompt → buildFullPrompt() → bridge.call() → spawn('opencode')
                                                    ↓
                                              stdout stream
                                                    ↓
                                          JSON line parser
                                                    ↓
                                          onData(chunk) callback
                                                    ↓
                                          webview.postMessage('stream')
```

### 3. LspProvider (lspProvider.ts)

Extracts semantic context from the current editor state.

**Responsibilities:**
- Reads VS Code diagnostic API for errors/warnings/info
- Spawns `simone-mcp symbols` for symbol extraction
- Combines cursor word, diagnostics, and symbols into a context string

### 4. SwarmCoordinator (swarmCoordinator.ts)

Dispatches tasks to specialized oh-my-opencode agents.

**Responsibilities:**
- Spawns `opencode run --agent=<type>` for each agent
- Tracks active tasks with unique IDs and status
- Supports parallel dispatch via `dispatchSwarm()` with `Promise.allSettled`

### 5. BuddySystem (buddyGamification.ts)

Gamification system with XP, levels, and moods.

**Responsibilities:**
- Status bar item showing `🤖 Buddy Lv.X`
- XP rewards for various actions (commits, responses, tests)
- Level-up system (level × 100 XP per level)
- Mood system with 30-second auto-decay to neutral

### 6. MemoryConsolidation (memoryConsolidation.ts)

Watches and consolidates project memory files.

**Responsibilities:**
- Scans for AGENTS.md, SIN-MEMORY.md, CLAUDE.md, .sincode-memory.md
- Watches for file changes and triggers context refresh
- Supports appending new memory entries with timestamps

### 7. InlineChatProvider (inlineChat.ts)

Provides ghost-text inline code completions.

**Responsibilities:**
- Registered as `InlineCompletionItemProvider` for all file patterns
- Sends code prefix (start of file to cursor) to AI
- Returns max 5 lines of completion as ghost text

### 8. SINCodeActionProvider (codeActions.ts)

Provides context-aware code actions via the lightbulb menu.

**Responsibilities:**
- QuickFix actions for diagnostic errors
- Refactor, Explain, and Generate Tests actions (always available)
- Applies AI suggestions as workspace edits

### 9. MarketplacePanel (agentMarketplace.ts)

Webview panel for browsing and installing agents.

**Responsibilities:**
- Displays 6 pre-loaded agents in a responsive grid
- Category filtering (Analysis, Research, Intelligence, Creative, Development, Vision)
- Install/remove with status tracking

## Extension Points

| Extension Point | Implementation | Scope |
|----------------|----------------|-------|
| `WebviewViewProvider` | `sincode.chatView` — main sidebar chat | Activity bar |
| `InlineCompletionItemProvider` | All file patterns (`**`) | Editor |
| `CodeActionProvider` | All file patterns (`**/*`) | Editor lightbulb |
| `StatusBarItem` (Left) | Mode selector (priority 100) | Status bar |
| `StatusBarItem` (Left) | Model selector (priority 99) | Status bar |
| `StatusBarItem` (Right) | BUDDY gamification (priority 100) | Status bar |
| `FileSystemWatcher` | `.git/HEAD` for commit detection | Workspace |
| `FileSystemWatcher` | Memory files for context refresh | Workspace |
| `onDidSaveTextDocument` | Proactive mode + auto test runner | Workspace |

## Webview Communication Protocol

The extension uses VS Code's `postMessage` API for bidirectional communication:

### Webview → Extension
| Message Type | Payload | Handler |
|-------------|---------|---------|
| `prompt` | `{ value: string }` | Send to AI via bridge |
| `cancel` | `{}` | Kill running process |
| `command` | `{ command: 'swarmDispatch' \| 'openMarketplace' }` | Execute command |

### Extension → Webview
| Message Type | Payload | Purpose |
|-------------|---------|---------|
| `stream` | `{ text: string }` | Streaming AI response chunk |
| `status` | `{ message: string }` | Status indicator text |
| `error` | `{ message: string }` | Error display |
| `mode-change` | `{ mode: string, message?: string }` | Mode badge update |

## Security Considerations

- **No external dependencies** — The extension has zero npm runtime dependencies
- **CLI sandboxing** — All AI calls go through the local `opencode` CLI, not direct API calls
- **Webview security** — `localResourceRoots` restricted to extension URI only
- **No telemetry** — No analytics or tracking code
