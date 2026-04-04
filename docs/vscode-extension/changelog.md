# Changelog

All notable changes to the SIN Code VS Code Extension will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [0.1.0] - 2026-04-03

Initial release of the SIN Code VS Code Extension — an agentic AI coding assistant for OpenSIN.

### Phase 1: Core AI Assistant

#### Added
- **Sidebar Chat Panel** — Full-featured AI chat in the VS Code sidebar with streaming responses, mode badge, cancel button, and Swarm/Marketplace quick-access buttons
- **5 Agent Modes** — Switch between specialized modes with distinct system prompts:
  - **Architect** (🏗️) — System architecture planning and project roadmaps
  - **Code** (💻) — Production-ready code implementation (default mode)
  - **Debug** (🐛) — Root cause analysis with log reading and evidence-based fixes
  - **Ask** (❓) — Code explanation and Q&A without modifying code
  - **Proactive** (⚡) — Always-on background analysis on file saves
- **Mode Selector** — Status bar item (left) for quick mode switching via Quick Pick
- **Model Selector** — Status bar item (left) for choosing the underlying LLM; auto-fetches models from `~/.config/opencode/` config
- **Memory Consolidation** — Automatic loading and watching of `AGENTS.md`, `SIN-MEMORY.md`, `CLAUDE.md`, and `.sincode-memory.md` with live context refresh on file changes
- **LSP Integration** — Semantic context extraction including real-time diagnostics (errors/warnings), symbol extraction via `simone-mcp`, and cursor-aware word context
- **File Context Management** — Add files to conversation context via command palette or editor context menu
- **CLI Bridge** — Robust `opencode run --format json` integration with streaming JSON parsing, stderr forwarding, and process cancellation

### Phase 2: Intelligence Layer

#### Added
- **Swarm Coordinator** — Multi-agent task dispatch to specialized oh-my-opencode agents:
  - **Explore** (🔍) — Codebase patterns, file structures, ast-grep
  - **Librarian** (📚) — Documentation research, GitHub examples
  - **Oracle** (🔮) — Architecture, debugging, complex logic
  - **Artistry** (🎨) — Creative problem solving, non-conventional approaches
  - Parallel dispatch via `dispatchSwarm()` with `Promise.allSettled`
  - Task tracking with unique IDs and status (pending/running/completed/failed)
  - VS Code progress notifications during dispatch
- **BUDDY Gamification System** — Status bar pet companion that reacts to coding activity:
  - XP rewards: +25 commits, +20 swarm tasks, +15 test passes, +10 responses, +5 context files/analysis
  - Level-up system (level x 100 XP per level) with celebration notifications
  - Mood system: happy/sad/excited/neutral/sleeping with 30-second auto-decay
  - Event reactions: commits (🚀), test passes (✅), errors (💥), failures (😢)
  - Clickable status bar item with detailed tooltip (mood, level, XP, last action)
- **Auto Test Runner** — Automatically runs `npm test` in a dedicated terminal when `.test.` or `.spec.` files are saved
- **Git Commit Detection** — Watches `.git/HEAD` for changes and triggers Buddy XP rewards on every commit

### Phase 3: Advanced Capabilities

#### Added
- **Inline Chat / Completions** — AI-powered ghost-text code completions:
  - Triggered via `Cmd+Shift+I` (Mac) / `Ctrl+Shift+I` (Win/Linux)
  - Registered as `InlineCompletionItemProvider` for all file patterns
  - Sends code prefix to AI, requests max 5 lines of completion
  - Graceful error fallback
- **AI Code Actions** — Context-aware actions via lightbulb menu and command palette:
  - **Fix Error** (🔮) — QuickFix for diagnostic errors using Debug mode
  - **Refactor Selection** (🤖) — Refactor selected code using Code mode
  - **Explain Code** (📖) — Plain-English explanation in a side panel using Ask mode
  - **Generate Tests** (✅) — Generate unit tests and create `.test.` file using Code mode
- **Agent Marketplace** — Built-in webview panel for discovering and installing agents:
  - 6 pre-loaded agents across 6 categories (Analysis, Research, Intelligence, Creative, Development, Vision)
  - Category filtering with toggle buttons
  - One-click install/remove with status tracking
  - Installed count badge in header
  - Responsive grid layout with version display
  - Triggered via `Cmd+Shift+M` (Mac) / `Ctrl+Shift+M` (Win/Linux)

### Keybindings

| Shortcut | Command |
|----------|---------|
| `Cmd+Shift+I` / `Ctrl+Shift+I` | Trigger Inline Suggestion |
| `Cmd+Shift+M` / `Ctrl+Shift+M` | Open Agent Marketplace |

### Commands

| Command | Description |
|---------|-------------|
| `sincode.start` | Open the SIN Code sidebar |
| `sincode.selectMode` | Switch between agent modes |
| `sincode.selectModel` | Choose the underlying LLM |
| `sincode.addFileToContext` | Add current file to conversation context |
| `sincode.inlineChat.trigger` | Trigger inline code completion |
| `sincode.openMarketplace` | Open Agent Marketplace panel |
| `sincode.swarmDispatch` | Dispatch task to swarm agent |
| `sincode.buddyInfo` | Show BUDDY status |
| `sincode.fixError` | Fix error with AI |
| `sincode.refactorSelection` | Refactor selection with AI |
| `sincode.explainCode` | Explain code in side panel |
| `sincode.generateTests` | Generate tests for selection |

### Architecture

- **10 source files** across `src/`: extension, cliBridge, modes, lspProvider, swarmCoordinator, buddyGamification, memoryConsolidation, inlineChat, codeActions, agentMarketplace
- **WebviewViewProvider** for sidebar chat with full HTML/CSS/JS UI
- **InlineCompletionItemProvider** for ghost-text completions
- **CodeActionProvider** for QuickFix and Refactor actions
- **StatusBarItems** for mode, model, and BUDDY status
- **FileSystemWatchers** for git commits and memory file changes
- **Event listeners** for document saves (proactive mode + auto test runner)

### Requirements

- VS Code >= 1.85.0
- `opencode` CLI installed and in PATH
- (Optional) `simone-mcp` for LSP symbol extraction
