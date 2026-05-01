# OpenSIN Code Rust Engine

Die Rust Engine (`opensin-engine`) ist das performante Backend von OpenSIN-Code.

> **Pfad:** `packages/opensin-engine/`
> **Umfang:** 71 Dateien | 48 Rust-Files | 37.731 Zeilen

---

## Struktur

```
packages/opensin-engine/
├── Cargo.toml              # Workspace Definition
├── Cargo.lock              # Dependency Lockfile
├── SIN.md                  # OpenSIN Code Dokumentation
├── PARITY.md               # Feature Parity mit TypeScript
├── README.md               # Engine Dokumentation
├── CONTRIBUTING.md         # Contributing Guidelines
└── crates/
    ├── api/                # API Layer (7 Dateien)
    │   └── src/
    │       ├── lib.rs      # Module Exports
    │       ├── client.rs   # ProviderClient Abstraction
    │       ├── types.rs    # StreamEvent, MessageRequest
    │       ├── error.rs    # ApiError Enum
    │       ├── sse.rs      # SSE Parser
    │       └── providers/
    │           ├── mod.rs          # Provider Trait, Model Registry
    │           ├── openai_provider.rs  # OpenAI API Client
    │           └── openai_compat.rs    # OpenAI/xAI via OCI Proxy
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
    ├── tools/              # Tools Layer (1 Datei, ~2.500 Zeilen)
    │   └── src/
    │       └── lib.rs      # 19 Built-in Tools
    ├── commands/           # Commands Layer (1 Datei, ~1.800 Zeilen)
    │   └── src/
    │       └── lib.rs      # 27+ Slash Commands
    ├── sin-cli/            # CLI Layer (6 Dateien)
    │   └── src/
    │       ├── main.rs     # CLI Entry, REPL, OAuth Login
    │       ├── app.rs      # SessionApp, Slash Command Handling
    │       ├── args.rs     # Clap Argument Parsing
    │       ├── render.rs   # Terminal Renderer, Markdown, Spinners
    │       ├── init.rs     # Repo Initialization, Auto-detection
    │       └── input.rs    # Vim-mode Terminal Line Editor
    ├── plugins/            # Plugin System (2 Dateien + bundled)
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
    ├── server/             # Server Layer (1 Datei)
    │   └── src/
    │       └── lib.rs      # Axum HTTP API, SSE Streaming
    └── compat-harness/     # Compat-Harness (1 Datei)
        └── src/
            └── lib.rs      # Upstream TS Source Extraction
```

---

## API Layer

Der API Layer abstrahiert den Zugriff auf verschiedene LLM-Provider:

```rust
// Provider Trait
pub trait Provider {
    async fn stream(&self, request: MessageRequest) -> Result<StreamEvent>;
    fn models(&self) -> Vec<ModelInfo>;
}

// OpenAI Provider
let client = OpenSinApiClient::new(api_key, base_url);
let events = client.stream(request).await?;
```

### Unterstützte Provider

- **OpenSinApi** — OpenAI API via OCI Proxy
- **OpenAICompat** — OpenAI/xAI kompatible Endpunkte

---

## Runtime Layer

### Core Agent Loop

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

### Session Compaction

Der Compaction-Algorithmus reduziert den Kontext wenn das Token-Limit erreicht wird:

1. **Micro-Compact** — Einzelne Tool-Aufrufe zusammenfassen
2. **Session Memory Compact** — Ältere Nachrichten komprimieren
3. **Full Compact** — Gesamte Konversation zusammenfassen

---

## Built-in Tools (19)

| Tool                 | Beschreibung                       |
| -------------------- | ---------------------------------- |
| BashTool             | Shell Command Execution            |
| ReadFileTool         | Datei lesen                        |
| WriteFileTool        | Datei schreiben                    |
| EditFileTool         | Datei bearbeiten (Suchen/Ersetzen) |
| GlobSearchTool       | Datei-Globbing                     |
| GrepSearchTool       | Text-Suche                         |
| WebFetchTool         | URL-Inhalte abrufen                |
| WebSearchTool        | Websuche                           |
| TodoWriteTool        | Todo-Liste verwalten               |
| SkillTool            | Skill-Ausführung                   |
| AgentTool            | Sub-Agent spawnen                  |
| ToolSearchTool       | Deferred Tool Discovery            |
| NotebookEditTool     | Jupyter Notebook bearbeiten        |
| SleepTool            | Verzögerung                        |
| BriefTool            | Session-Zusammenfassung            |
| ConfigTool           | Konfiguration (internal)           |
| StructuredOutputTool | Strukturierte Ausgabe              |
| REPLTool             | REPL VM (internal)                 |
| PowerShellTool       | PowerShell Execution               |

---

## CLI Layer

Der Rust CLI (`sin-cli`) bietet einen vollständigen REPL-Modus:

```bash
# Interaktiver Modus
sin

# Mit Prompt
sin "Erkläre die Codebasis"

# Non-interactive
sin --print "Review this file"

# Mit Model
sin --model opus "Analyse this"
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
  "name": "sin-mein-plugin",
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

## Bauen

```bash
cd packages/opensin-engine
cargo build --release
cargo test
```

---

_Zuletzt aktualisiert: 2026-04-07 | OpenSIN-AI_
