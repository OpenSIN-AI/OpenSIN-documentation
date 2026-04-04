# Claude Code → OpenSIN Feature Mapping

Komplette Zuordnung aller Claude Code Features zu ihren OpenSIN Entsprechungen.

## Core Engine

| Claude Code | OpenSIN | Status | Datei |
|-------------|---------|--------|-------|
| `QueryEngine.ts` | `QueryEngine` | ✅ Dokumentiert | [sin-query-engine](/guide/sin-query-engine) |
| `query.ts` | `react_loop` | ✅ Dokumentiert | [sin-query-engine](/guide/sin-query-engine) |
| `feature('X')` | Feature Flags | ✅ Dokumentiert | [sin-feature-flags](/guide/sin-feature-flags) |
| Startup Profiling | Startup Profiling | ✅ Dokumentiert | [sin-feature-flags](/guide/sin-feature-flags) |

## Agent System

| Claude Code | OpenSIN | Status | Datei |
|-------------|---------|--------|-------|
| `AgentTool.tsx` | Subagent System | ✅ Dokumentiert | [sin-fork-subagent](/guide/sin-fork-subagent) |
| `forkSubagent.ts` | Fork Subagent | ✅ Dokumentiert | [sin-fork-subagent](/guide/sin-fork-subagent) |
| Worktree Isolation | Worktree System | ✅ Dokumentiert | [sin-worktree-isolation](/guide/sin-worktree-isolation) |
| BG↔FG Transition | Background Agent | ✅ Dokumentiert | [sin-bg-fg-transition](/guide/sin-bg-fg-transition) |
| Agent Frontmatter | Agent Definition | ✅ Dokumentiert | [sin-fork-subagent](/guide/sin-fork-subagent) |

## Hook System

| Claude Code | OpenSIN | Status | Datei |
|-------------|---------|--------|-------|
| `hooks.ts` (5022 Zeilen) | Hook System | ✅ Dokumentiert | [sin-hook-system](/guide/sin-hook-system) |
| Session Hooks (Map) | SessionHookStore | ✅ Dokumentiert | [sin-hook-system](/guide/sin-hook-system) |
| 5 Hook Modes | 5 Hook Modes | ✅ Dokumentiert | [sin-hook-system](/guide/sin-hook-system) |
| Frontmatter Hooks | Frontmatter Hooks | ✅ Dokumentiert | [sin-hook-system](/guide/sin-hook-system) |

## Tool System

| Claude Code | OpenSIN | Status | Datei |
|-------------|---------|--------|-------|
| `Tool.ts` (792 Zeilen) | Tool Interface | ✅ Dokumentiert | [sin-tool-system](/guide/sin-tool-system) |
| `buildTool()` | Tool Factory | ✅ Dokumentiert | [sin-tool-system](/guide/sin-tool-system) |
| ToolSearch | Deferred Loading | ✅ Dokumentiert | [sin-tool-deferred-loading](/guide/sin-tool-deferred-loading) |
| Sorted Assembly | Cache-Stable Assembly | ✅ Dokumentiert | [sin-sorted-tool-assembly](/guide/sin-sorted-tool-assembly) |
| Permission Filtering | Permission Filtering | ✅ Dokumentiert | [sin-tool-system](/guide/sin-tool-system) |

## Permission System

| Claude Code | OpenSIN | Status | Datei |
|-------------|---------|--------|-------|
| `permissions.ts` (1451 Zeilen) | Permission System | ✅ Dokumentiert | [sin-permission-system](/guide/sin-permission-system) |
| Auto Classifier | Auto Classifier | ✅ Dokumentiert | [sin-auto-classifier](/guide/sin-auto-classifier) |
| Denial Tracking | Denial Tracker | ✅ Dokumentiert | [sin-permission-system](/guide/sin-permission-system) |
| Bypass-Immune Safety | Safety Checks | ✅ Dokumentiert | [sin-permission-system](/guide/sin-permission-system) |
| Content-Specific Rules | Content Rules | ✅ Dokumentiert | [sin-permission-system](/guide/sin-permission-system) |

## Memory System

| Claude Code | OpenSIN | Status | Datei |
|-------------|---------|--------|-------|
| `memdir.ts` | File Memory | ✅ Dokumentiert | [sin-file-memory](/guide/sin-file-memory) |
| Session Memory | Session Memory | ✅ Dokumentiert | [sin-file-memory](/guide/sin-file-memory) |
| `context.ts` (CLAUDE.md) | SIN.md | ✅ Dokumentiert | [sin-file-memory](/guide/sin-file-memory) |
| Daily Log Mode | Daily Log | ✅ Dokumentiert | [sin-file-memory](/guide/sin-file-memory) |

## MCP Integration

| Claude Code | OpenSIN | Status | Datei |
|-------------|---------|--------|-------|
| `client.ts` (1343 Zeilen) | MCP Client | ✅ Dokumentiert | [sin-mcp-integration](/guide/sin-mcp-integration) |
| In-Process Transport | In-Process MCP | ✅ Dokumentiert | [sin-in-process-mcp](/guide/sin-in-process-mcp) |
| OAuth Auth | MCP OAuth | ✅ Dokumentiert | [sin-mcp-integration](/guide/sin-mcp-integration) |
| Session Expiry | Auto-Reconnect | ✅ Dokumentiert | [sin-mcp-integration](/guide/sin-mcp-integration) |
| Batched Connections | Batched Connect | ✅ Dokumentiert | [sin-mcp-integration](/guide/sin-mcp-integration) |

## Sandbox

| Claude Code | OpenSIN | Status | Datei |
|-------------|---------|--------|-------|
| `sandbox-adapter.ts` (985 Zeilen) | Sandbox | ✅ Dokumentiert | [sin-sandbox](/guide/sin-sandbox) |
| Git Escape Prevention | Git Prevention | ✅ Dokumentiert | [sin-bare-git-prevention](/guide/sin-bare-git-prevention) |
| Auto-Allow Sandboxed | Auto-Allow | ✅ Dokumentiert | [sin-sandbox](/guide/sin-sandbox) |
| Dynamic Config | Dynamic Config | ✅ Dokumentiert | [sin-sandbox](/guide/sin-sandbox) |

## UI/UX

| Claude Code | OpenSIN | Status | Datei |
|-------------|---------|--------|-------|
| Sticky-On Latches | Sticky Latches | ✅ Dokumentiert | [sin-sticky-latches](/guide/sin-sticky-latches) |
| Scroll Drain | Scroll Suspension | ✅ Dokumentiert | [sin-scroll-drain](/guide/sin-scroll-drain) |
| Interaction Batching | Time Batching | ✅ Dokumentiert | [sin-interaction-batching](/guide/sin-interaction-batching) |
| Feature Flags | Build Tiers | ✅ Dokumentiert | [sin-feature-flags](/guide/sin-feature-flags) |

## Summary

| Kategorie | Claude Code Files | OpenSIN Docs | Coverage |
|-----------|------------------|--------------|----------|
| Core Engine | 2 | 1 | 100% |
| Agent System | 5 | 3 | 100% |
| Hook System | 3 | 1 | 100% |
| Tool System | 5 | 3 | 100% |
| Permission System | 5 | 2 | 100% |
| Memory System | 3 | 1 | 100% |
| MCP Integration | 5 | 1 | 100% |
| Sandbox | 4 | 2 | 100% |
| UI/UX | 4 | 4 | 100% |
| **Total** | **36** | **18** | **100%** |

## Implementation Status

| Phase | Features | Status | Timeline |
|-------|----------|--------|----------|
| Phase 1: Core | QueryEngine, Tools, Permissions, Hooks | 📋 Dokumentiert | Weeks 1-4 |
| Phase 2: Agents | Subagents, Memory, MCP, Sandbox | 📋 Dokumentiert | Weeks 5-8 |
| Phase 3: CLI/UI | CLI, TUI, Plugins, Testing | 📋 Dokumentiert | Weeks 9-12 |

## Next Steps

1. [Implementation Guide](/guide/sin-implementation-guide) — 12-Wochen Plan
2. [SIN Query Engine](/guide/sin-query-engine) — Core Engine
3. [SIN Hook System](/guide/sin-hook-system) — Automation Backbone
