# OpenSIN-AI Code — Python Agent Development Platform

OpenSIN-AI Code ist die Python-basierte Agent Development Platform der OpenSIN-AI Organisation. Metadata-driven Architektur für schnellen Prototyping und Porting.

> **Repository:** [OpenSIN-AI/opensin-ai-code](https://github.com/OpenSIN-AI/opensin-ai-code)
>
> **Umfang:** 100 Dateien | 2.386 Zeilen Python-Code | 26 Subsystem-Pakete

## OpenSIN-AI Agent Roadmap

- Feature spec: [OpenSIN-overview/docs/opensin-ai-agent-feature-spec.md](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/opensin-ai-agent-feature-spec.md)
- Comparison guide: [OpenSIN-AI Agent Features](opensin-ai-agent-features.md)
- This repo maps the Python agent development surface to the same OpenSIN-AI Agent roadmap.

---

## Architektur

OpenSIN-AI Code ist als metadata-driven Python Workspace organisiert:

```
opensin-ai-code/
├── README.md               # Projektdokumentation
├── LICENSE                 # Apache 2.0
├── src/
│   ├── main.py             # CLI Entry Point (argparse)
│   ├── runtime.py          # PortRuntime: Routing, Bootstrap, Turn Loops
│   ├── query_engine.py     # QueryEnginePort: Message Submission, Streaming
│   ├── QueryEngine.py      # QueryEngineRuntime Wrapper
│   ├── commands.py         # Command Surface (207 entries)
│   ├── tools.py            # Tool Surface (184 entries)
│   ├── session_store.py    # Session Persistence
│   ├── transcript.py       # Transcript Buffer
│   ├── port_manifest.py    # Workspace Manifest
│   ├── parity_audit.py     # Python vs TypeScript Coverage
│   ├── command_graph.py    # Command Segmentation
│   ├── bootstrap_graph.py  # Bootstrap Stages
│   ├── tool_pool.py        # Tool Pool Assembly
│   ├── permissions.py      # Tool Permission Context
│   ├── execution_registry.py  # Mirrored Command/Tool Wrappers
│   ├── setup.py            # Setup Report
│   ├── prefetch.py         # Simulated Prefetches
│   ├── deferred_init.py    # Trust-gated Init
│   ├── system_init.py      # System Init Message Builder
│   ├── models.py           # Core Dataclasses
│   ├── context.py          # Port Context
│   ├── history.py          # Event Log
│   ├── cost_tracker.py     # Cost Tracking
│   ├── costHook.py         # Cost Hook Application
│   ├── remote_runtime.py   # Remote Mode Simulation
│   ├── direct_modes.py     # Direct-connect Modes
│   ├── task.py             # Task Stub
│   ├── tasks.py            # Default Tasks
│   ├── Tool.py             # Tool Definitions
│   ├── query.py            # Query DTOs
│   ├── replLauncher.py     # REPL Banner
│   ├── dialogLaunchers.py  # Dialog Launchers
│   ├── ink.py              # Markdown Rendering
│   ├── interactiveHelpers.py  # Utility Helpers
│   ├── projectOnboardingState.py  # Onboarding State
│   └── [26 subdirectories] # Placeholder packages loading JSON metadata
└── tests/
    └── test_porting_workspace.py
```

---

## Core Components

### CLI Entry Point (`main.py`)

Argparse-basierter Router mit 25+ Subcommands:

- `summary` — Porting-Zusammenfassung
- `manifest` — Workspace Manifest
- `parity-audit` — Coverage-Vergleich
- `route`, `bootstrap`, `turn-loop` — Runtime-Simulation
- `remote-mode`, `ssh-mode` — Remote-Modi

### QueryEngine (`query_engine.py`)

`QueryEnginePort` Klasse:

- Message Submission
- Turn Loop Execution
- Streaming Support
- Session Persistence
- Structured Output
- Context Compacting

### PortRuntime (`runtime.py`)

`PortRuntime` Klasse:

- Prompt Routing zu Commands/Tools
- Session Bootstrap
- Multi-Turn Loop Execution
- Permission Denial Inference

### Reference Data

JSON Snapshots in `reference_data/`:

- `archive_surface_snapshot.json` — 1902 TS-Dateien, 207 Commands, 184 Tools
- `commands_snapshot.json` — 207 Command Entries
- `tools_snapshot.json` — 184 Tool Entries
- `subsystems/*.json` — 29 Subsystem Metadata Files

---

## Subsystem Packages

| Subsystem        | Beschreibung             |
| ---------------- | ------------------------ |
| `assistant/`     | Assistant Module         |
| `bootstrap/`     | Bootstrap Module         |
| `bridge/`        | Bridge Module            |
| `buddy/`         | Buddy Companion          |
| `cli/`           | CLI Module               |
| `components/`    | UI Components            |
| `constants/`     | Constants                |
| `coordinator/`   | Task Coordinator         |
| `entrypoints/`   | Entry Points             |
| `hooks/`         | Hook System              |
| `keybindings/`   | Keybindings              |
| `memdir/`        | Memory Directory         |
| `migrations/`    | Migrations               |
| `moreright/`     | MoreRight Module         |
| `native_ts/`     | Native TypeScript Bridge |
| `outputStyles/`  | Output Styles            |
| `plugins/`       | Plugin System            |
| `remote/`        | Remote Module            |
| `schemas/`       | Data Schemas             |
| `screens/`       | Screen Definitions       |
| `server/`        | Server Module            |
| `services/`      | Services                 |
| `skills/`        | Skills System            |
| `state/`         | State Management         |
| `types/`         | Type Definitions         |
| `upstreamproxy/` | Upstream Proxy           |
| `utils/`         | Utilities                |
| `vim/`           | Vim Integration          |
| `voice/`         | Voice Module             |

---

## Schnellstart

```bash
# Repository klonen
git clone https://github.com/OpenSIN-AI/opensin-ai-code.git
cd opensin-ai-code

# Porting-Zusammenfassung
python3 -m src.main summary

# Workspace Manifest
python3 -m src.main manifest

# Subsysteme auflisten
python3 -m src.main subsystems --limit 16

# Tests ausführen
python3 -m unittest discover -s tests -v
```

---

_Zuletzt aktualisiert: 2026-04-07 | OpenSIN-AI_
