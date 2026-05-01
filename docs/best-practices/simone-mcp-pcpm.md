---
title: Simone MCP + PCPM — Mandatory Agent Intelligence Layer
description: Every OpenSIN agent MUST use Simone MCP for symbolic code intelligence and PCPM for persistent project memory. No exceptions.
---

# Simone MCP + PCPM — Mandatory Agent Intelligence Layer

> **MANDATE (PRIORITY -9.5):** Every OpenSIN agent, every worker, every coder must activate Simone MCP and load PCPM context **before** any code navigation, symbol editing, structural change, or implementation task begins. This is not optional.

---

## Why Simone MCP?

AI coding agents that operate without semantic code understanding are blind. They guess file locations, copy-paste symbols without understanding call graphs, and create regressions by editing in the dark.

**Simone MCP** is the OpenSIN semantic intelligence server that gives every agent:

- **Symbol navigation** — find exactly where a function, class, or variable is defined across the entire workspace
- **Reference discovery** — know every call site before you rename or refactor
- **Structural editing** — replace symbol bodies via LSP, not fragile regex hacks
- **Project overview** — language-aware codebase map for any directory
- **Hybrid memory** — Qdrant + Neo4j vector/graph store for cross-session knowledge
- **A2A + MCP surface** — streamable HTTP MCP at `/mcp`, A2A JSON-RPC at `/a2a/v1`, health at `/health`, metrics at `/metrics`

---

## Why PCPM?

Without persistent context, every agent session starts from scratch. The Global-Brain DPMA v4 / PCPM system ensures:

- **No amnesia between sessions** — architectural decisions, bug history, and coding conventions survive restarts
- **Hive mind synchronization** — all agents share the same knowledge base
- **Plan continuity** — active tasks are resumed, not restarted
- **Evidence-first audit** — every decision is backed by stored context, not hallucination

---

## Activation Protocol (MANDATORY before any coding task)

### Step 1 — Check PCPM / Global-Brain coupling

```bash
# In every project root, before any other work:
node /Users/jeremy/dev/global-brain/src/cli.js setup-hooks \
  --project $(basename "$PWD") \
  --project-root "$PWD" \
  --agents-directive
```

If `.pcpm/` or `.opencode/opencode.json` with hooks already exists → skip, already coupled.

### Step 2 — Verify Simone MCP is reachable

```bash
# Health check (local):
curl -s http://localhost:8765/health | python3 -m json.tool

# Health check (HF Space — production):
curl -s https://openjerro-simone-mcp.hf.space/health | python3 -m json.tool
```

Expected response:

```json
{
  "status": "ok",
  "service": "simone-mcp",
  "version": "1.0.0",
  "transports": ["stdio", "streamable-http"],
  "tools": 10,
  "capabilities": [
    "symbol_navigation",
    "references",
    "structural_edit",
    "memory"
  ]
}
```

### Step 3 — Use Simone MCP for ALL code operations

| Task                                   | Correct approach                                   | Forbidden approach                |
| -------------------------------------- | -------------------------------------------------- | --------------------------------- |
| Find where `UserService` is defined    | `find_symbol("UserService")` via Simone MCP        | Grepping blindly through files    |
| Rename `getUser` everywhere            | `replace_symbol_body` + LSP rename via Simone MCP  | sed/awk across the repo           |
| Understand the codebase before editing | `get_project_overview()` via Simone MCP            | Reading random files and guessing |
| Find all callers of `processPayment`   | `find_references("processPayment")` via Simone MCP | Manual grep                       |
| Insert a new method into a class       | `insert_after_symbol` via Simone MCP               | Raw file append                   |

---

## OpenCode Integration

Add Simone MCP to your project's OpenCode config (`.opencode/opencode.json`):

```json
{
  "mcp": {
    "simone-mcp": {
      "type": "streamable-http",
      "url": "https://openjerro-simone-mcp.hf.space/mcp",
      "description": "Semantic code intelligence — symbol navigation, references, structural editing, hybrid memory"
    }
  }
}
```

For local development, replace the URL with `http://localhost:8765/mcp`.

---

## Simone MCP Tool Reference

| Tool                    | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| `find_symbol`           | Find all definitions of a symbol by name path pattern     |
| `find_references`       | Find all usages/call sites of a symbol                    |
| `replace_symbol_body`   | Replace a symbol's full body (LSP-grade)                  |
| `insert_after_symbol`   | Insert code immediately after a symbol definition         |
| `get_project_overview`  | Get a language-aware overview of the codebase structure   |
| `execute_simone_action` | Run a named high-level action (refactor, validate, audit) |
| `process_lsp_task`      | Submit an LSP task for async processing                   |
| `memory_store`          | Persist a knowledge item to hybrid vector/graph memory    |
| `memory_query`          | Retrieve relevant knowledge from hybrid memory            |
| `health_check`          | Verify Simone MCP is alive and responsive                 |

---

## Repository

- **GitHub:** [https://github.com/OpenSIN-AI/Simone-MCP](https://github.com/OpenSIN-AI/Simone-MCP)
- **HF Space:** [https://huggingface.co/spaces/openjerro/simone-mcp](https://huggingface.co/spaces/openjerro/simone-mcp)
- **MCP endpoint:** `https://openjerro-simone-mcp.hf.space/mcp`
- **A2A endpoint:** `https://openjerro-simone-mcp.hf.space/a2a/v1`
- **Dashboard:** `https://openjerro-simone-mcp.hf.space/dashboard`

---

## Enforcement

This mandate is enforced at multiple levels:

1. **Global AGENTS.md** (`~/.config/opencode/AGENTS.md`) — Priority -9.5 rule
2. **upgraded-opencode-stack installer** — checks for Simone MCP coupling on install
3. **MANDATE-0.34.md** — canonical blueprint mandate file in `upgraded-opencode-stack`
4. **worker-code.md** — explicit `<orchestration_mandate>` block in every worker instruction
5. **Template-A2A-SIN-Agent AGENTS.md** — every new agent inherits this requirement

**Violation = architectural failure.** If an agent edits code without Simone MCP + PCPM active, its changes are considered unverified and must be reviewed before merge.

---

## Quick Checklist

Before starting any coding task:

- [ ] PCPM / Global-Brain hooks are installed in this project (`.opencode/opencode.json` exists with `beforeRun`/`afterRun` hooks)
- [ ] Simone MCP health check returns `"status": "ok"`
- [ ] OpenCode MCP config includes `simone-mcp` entry
- [ ] No symbol edits are made via raw file search/replace without first running `find_symbol` or `find_references`

---

_Last updated:_ 2026-04-12
_Status:_ **ACTIVE & MANDATORY**
_Maintainer:_ sin-zeus
_Mandate reference:_ MANDATE-0.34.md

---

## Relevante Mandate

| Mandat                | Priority | Regel                          |
| --------------------- | -------- | ------------------------------ |
| **Simone MCP + PCPM** | -9.5     | VOR jedem Code-Task aktivieren |
| **Global Brain Init** | -100.0   | setup-hooks VOR jeder Arbeit   |
