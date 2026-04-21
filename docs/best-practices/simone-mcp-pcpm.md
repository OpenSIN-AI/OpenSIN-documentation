---
title: Simone MCP + PCPM — Mandatory Agent Intelligence Layer
description: Every OpenSIN agent must use Simone MCP for symbolic code intelligence and PCPM for persistent project memory before implementation work begins.
---

# Simone MCP + PCPM — Mandatory Agent Intelligence Layer

> **Mandate (Priority -9.5):** Every OpenSIN coder, worker, and implementation agent must activate Simone MCP and load PCPM context before code navigation, symbol editing, structural change, or implementation work begins.

## At a glance

| Area | Standard |
|---|---|
| Required before coding | Global-Brain / PCPM hooks installed, Simone MCP reachable, repo config wired |
| Required tooling | Simone MCP for symbol search, references, structural edits, and semantic memory |
| Forbidden behavior | Blind grep-led refactors, raw search/replace symbol edits, editing without context hydration |
| Proof | Passing health check, visible MCP config, and Simone-backed code navigation for structural work |

## 1. Why Simone MCP exists

Agents that edit code without semantic structure are guessing. Simone MCP gives the fleet a reliable way to navigate symbols, understand references, and make structural changes without treating the repository like plain text.

It provides:

- **Symbol navigation** for exact definitions
- **Reference discovery** before rename or refactor work
- **Structural editing** through LSP-grade operations
- **Project overview** for language-aware workspace mapping
- **Hybrid memory** across sessions through vector + graph storage
- **A2A + MCP endpoints** for shared automation surfaces

## 2. Why PCPM exists

Persistent context keeps sessions from starting cold every time. PCPM and Global Brain preserve prior decisions, bug history, active plans, and evidence, so the next agent continues the work instead of rediscovering it.

It protects:

- continuity between sessions
- shared knowledge across the fleet
- plan handoff quality
- evidence-first decision making

## 3. Required activation flow

### Step 1 — Couple the project to Global Brain / PCPM

```bash
node /path/to/Infra-SIN-Global-Brain/src/cli.js setup-hooks   --project $(basename "$PWD")   --project-root "$PWD"   --agents-directive
```

If `.pcpm/` already exists and `.opencode/opencode.json` already contains the hooks, keep the existing coupling.

### Step 2 — Verify Simone MCP health

```bash
# Local
curl -s http://localhost:8765/health | python3 -m json.tool

# HF Space
curl -s https://openjerro-simone-mcp.hf.space/health | python3 -m json.tool
```

Expected shape:

```json
{
  "status": "ok",
  "service": "simone-mcp",
  "version": "1.0.0",
  "transports": ["stdio", "streamable-http"],
  "tools": 10,
  "capabilities": ["symbol_navigation", "references", "structural_edit", "memory"]
}
```

### Step 3 — Use Simone MCP for structural work

| Task | Correct approach | Forbidden approach |
|------|------------------|--------------------|
| Find where `UserService` is defined | Use Simone symbol search | Grep blindly through files |
| Rename `getUser` everywhere | Use Simone-backed rename / structural edit flow | `sed` or manual repo-wide replacement |
| Understand a codebase before editing | Ask for a project overview | Read random files and guess |
| Find all callers of `processPayment` | Use reference discovery | Manual search only |
| Insert a new method into a class | Use structural edit primitives | Raw file append |

## 4. OpenCode integration

Add Simone MCP to `.opencode/opencode.json`:

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

## 5. Tool reference

| Tool | Description |
|------|-------------|
| `find_symbol` | Find all definitions of a symbol by name or path pattern |
| `find_references` | Find all usages and call sites |
| `replace_symbol_body` | Replace a symbol body with structural safety |
| `insert_after_symbol` | Insert code immediately after a symbol definition |
| `get_project_overview` | Return a language-aware map of the repository |
| `execute_simone_action` | Run a named high-level action such as refactor or validate |
| `process_lsp_task` | Submit an async LSP task |
| `memory_store` | Persist a knowledge item to hybrid memory |
| `memory_query` | Retrieve relevant stored context |
| `health_check` | Verify Simone MCP responsiveness |

## 6. Verification checklist

- [ ] Global-Brain / PCPM hooks are installed for this project
- [ ] Simone MCP health check returns `"status": "ok"`
- [ ] `.opencode/opencode.json` includes the `simone-mcp` entry
- [ ] Symbol edits use Simone-backed navigation or structural operations
- [ ] Cross-session context was loaded before major implementation work

## Related docs

- [Best-Practice Page Pattern](/best-practices/page-pattern)
- [MCP Integration](/best-practices/mcp-integration)
- [Team Orchestration](/best-practices/team-orchestration)
- [Simone MCP repository](https://github.com/OpenSIN-AI/Simone-MCP)
- [Simone MCP HF Space](https://huggingface.co/spaces/openjerro/simone-mcp)

---

*Last updated:* 2026-04-21  
*Status:* **ACTIVE & MANDATORY**  
*Maintainer:* sin-zeus  
*Mandate reference:* MANDATE-0.34.md

---

## Enforcement signals

This mandate is enforced through the global AGENTS stack, installer coupling, worker instructions, and template inheritance. Code changes made without Simone MCP + PCPM active should be treated as unverified until reviewed.

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Simone MCP + PCPM** | -9.5 | VOR jedem Code-Task aktivieren |
| **Global Brain Init** | -100.0 | setup-hooks VOR jeder Arbeit |
