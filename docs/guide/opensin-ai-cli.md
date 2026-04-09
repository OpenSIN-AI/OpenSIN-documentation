# OpenSIN-AI CLI — AI Coding Assistant in Rust

OpenSIN-AI CLI ist der hochperformante, speicher-sichere AI Coding Assistant der OpenSIN-AI Organisation. Komplett in Rust implementiert für maximale Geschwindigkeit und Sicherheit.

> **Repository:** [OpenSIN-AI/opensin-ai-cli](https://github.com/OpenSIN-AI/opensin-ai-cli)
>
> **Umfang:** 70 Dateien | 34.601 Zeilen Rust-Code | 9 Crates

## OpenSIN-AI Agent Roadmap

- Feature spec: [OpenSIN-overview/docs/opensin-ai-agent-feature-spec.md](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/opensin-ai-agent-feature-spec.md)
- Comparison guide: [OpenSIN-AI Agent Features](opensin-ai-agent-features.md)
- Verified runtime: heartbeat, cron, failover, approval hooks, and orchestrator-aware CLI routing

---

## Architektur

OpenSIN-AI CLI ist als Rust Workspace mit Cargo organisiert:

```
opensin-ai-cli/
├── Cargo.toml              # Workspace Definition
├── Cargo.lock              # Dependency Lockfile
├── README.md               # Projektdokumentation
├── CONTRIBUTING.md         # Contributing Guidelines
├── LICENSE                 # Apache 2.0
└── crates/
    ├── opensin-cli/        # CLI Entry Point (6 Dateien)
    │   └── src/
    │       ├── main.rs     # CLI Entry, REPL, OAuth Login
    │       ├── app.rs      # SessionApp, Slash Command Handling
    │       ├── args.rs     # Clap Argument Parsing
    │       ├── render.rs   # Terminal Renderer, Markdown, Spinners
    │       ├── init.rs     # Repo Initialization, Auto-detection
    │       └── input.rs    # Vim-mode Terminal Line Editor
    ├── api/                # API Layer (11 Dateien)
    │   └── src/
    │       ├── lib.rs      # Module Exports
    │       ├── client.rs   # ProviderClient Abstraction
    │       ├── types.rs    # StreamEvent, MessageRequest
    │       ├── error.rs    # ApiError Enum
    │       ├── sse.rs      # SSE Parser
    │       └── providers/
    │           ├── mod.rs          # Provider Trait, Model Registry
    │           ├── opensin_provider.rs  # OpenSIN API Client
    │           └── openai_compat.rs    # OpenAI/xAI kompatible Endpunkte
    ├── runtime/            # Runtime Layer (18 Dateien)
    │   └── src/
    │       ├── lib.rs          # Module Exports
    │       ├── conversation.rs # Core Agent Loop
    │       ├── config.rs       # Multi-source Config Loading
    │       ├── session.rs      # Session Persistence
    │       ├── compact.rs      # Session Compaction Algorithm
    │       ├── bash.rs         # Bash Execution with Sandbox
    │       ├── file_ops.rs     # Read/Write/Edit/Glob/Grep
    │       ├── oauth.rs        # OAuth Flow with PKCE
    │       ├── sandbox.rs      # Linux Namespace Isolation
    │       ├── hooks.rs        # Pre/Post Tool Hooks
    │       ├── prompt.rs       # System Prompt Building
    │       ├── mcp.rs          # MCP Tool Naming
    │       ├── mcp_client.rs   # Transport Abstraction
    │       ├── mcp_stdio.rs    # JSON-RPC over stdio
    │       ├── permissions.rs  # Permission Mode Enforcement
    │       ├── remote.rs       # Upstream Proxy Support
    │       ├── usage.rs        # Token Usage Tracking
    │       ├── sse.rs          # SSE Event Parsing
    │       ├── bootstrap.rs    # Bootstrap Phases
    │       └── json.rs         # Custom JSON Parser/Renderer
    ├── tools/              # Tools Layer
    │   └── src/lib.rs      # 19 Built-in Tools
    ├── commands/           # Commands Layer
    │   └── src/lib.rs      # 27+ Slash Commands
    ├── plugins/            # Plugin System
    │   └── src/
    │       ├── lib.rs      # Full Plugin System
    │       └── hooks.rs    # Hook Execution
    ├── lsp/                # LSP Layer (5 Dateien)
    │   └── src/
    │       ├── lib.rs      # LSP Re-exports
    │       ├── client.rs   # JSON-RPC over stdio
    │       ├── manager.rs  # Multi-server Manager
    │       ├── types.rs    # LSP Context Enrichment
    │       └── error.rs    # LSP Error Types
    ├── server/             # Server Layer
    │   └── src/lib.rs      # Axum HTTP API, SSE Streaming
    └── compat-harness/     # Compat-Harness
        └── src/lib.rs      # Upstream Source Extraction
```

---

## Core Engine

### API Layer

Der API Layer abstrahiert den Zugriff auf verschiedene LLM-Provider:

```rust
// Provider Trait
pub trait Provider {
    async fn stream(&self, request: MessageRequest) -> Result<StreamEvent>;
    fn models(&self) -> Vec<ModelInfo>;
}

// OpenSIN Provider
let client = OpenSinApiClient::new(api_key, base_url);
let events = client.stream(request).await?;
```

### Unterstützte Provider

- **OpenSinApi** — OpenSIN API via OCI Proxy
- **OpenAICompat** — OpenAI/xAI kompatible Endpunkte

### Runtime Layer

#### Core Agent Loop

```rust
let mut conversation = Conversation::new(config);
loop {
    let response = client.stream(conversation.messages()).await?;
    conversation.add_assistant(response);
    
    for tool_call in response.tool_calls {
        let result = tools.execute(&tool_call).await?;
        conversation.add_tool_result(tool_call.id, result);
    }
}
```

#### Session Compaction

Der Compaction-Algorithmus reduziert den Kontext wenn das Token-Limit erreicht wird:

1. **Micro-Compact** — Einzelne Tool-Aufrufe zusammenfassen
2. **Session Memory Compact** — Ältere Nachrichten komprimieren
3. **Full Compact** — Gesamte Konversation zusammenfassen

---

## Built-in Tools (19)

| Tool | Beschreibung |
|------|-------------|
| BashTool | Shell Command Execution |
| ReadFileTool | Datei lesen |
| WriteFileTool | Datei schreiben |
| EditFileTool | Datei bearbeiten (Suchen/Ersetzen) |
| GlobSearchTool | Datei-Globbing |
| GrepSearchTool | Text-Suche |
| WebFetchTool | URL-Inhalte abrufen |
| WebSearchTool | Websuche |
| TodoWriteTool | Todo-Liste verwalten |
| SkillTool | Skill-Ausführung |
| AgentTool | Sub-Agent spawnen |
| ToolSearchTool | Deferred Tool Discovery |
| NotebookEditTool | Jupyter Notebook bearbeiten |
| SleepTool | Verzögerung |
| BriefTool | Session-Zusammenfassung |
| ConfigTool | Konfiguration (internal) |
| StructuredOutputTool | Strukturierte Ausgabe |
| REPLTool | REPL VM (internal) |
| PowerShellTool | PowerShell Execution |

---

## CLI Layer

Der Rust CLI bietet einen vollständigen REPL-Modus:

```bash
# Interaktiver Modus
opensin-ai

# Mit Prompt
opensin-ai "Erkläre die Codebasis"

# Non-interactive
opensin-ai --print "Review this file"

# Mit Model
opensin-ai --model opus "Analyse this"
```

### Features

- **REPL** — Interaktive Eingabe mit History
- **Vim-Mode** — Vim-style Line Editor
- **Markdown Rendering** — Syntax Highlighting, Code Blocks
- **Spinner** — Animierte Ladeanzeige
- **Slash Commands** — 27+ integrierte Befehle

---

## Plugin System

Plugins können Hooks, Commands, Agents und Skills registrieren:

```json
{
  "name": "opensin-mein-plugin",
  "version": "1.0.0",
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "python3 ${OPENSIN_PLUGIN_ROOT}/hooks/validate.py"
      }
    ]
  }
}
```

---

## Schnellstart

```bash
# Repository klonen
git clone https://github.com/OpenSIN-AI/opensin-ai-cli.git
cd opensin-ai-cli

# Bauen
cargo build --release

# Tests ausführen
cargo test

# CLI starten
cargo run --bin opensin-ai
```

---

## Installation

### Von Source
```bash
cargo install --path crates/opensin-cli --locked
```

### Pre-built Binary
```bash
./target/release/opensin-ai
```

---

*Zuletzt aktualisiert: 2026-04-07 | OpenSIN-AI*
