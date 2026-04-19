---
title: OpenSIN-Code CLI Reference
description: Canonical V1 reference for the TypeScript OpenSIN CLI surface.
---

# OpenSIN-Code CLI Reference

`OpenSIN-Code` is the **canonical TypeScript CLI** in the OpenSIN-AI organization.

- Canonical owner: [OpenSIN-AI/OpenSIN-Code](https://github.com/OpenSIN-AI/OpenSIN-Code)
- Org role: [Canonical Repos → Autonomous coding surface](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CANONICAL-REPOS.md#2-autonomous-coding-surface-typescript)
- Launch gate: [OpenSIN-Code#1117](https://github.com/OpenSIN-AI/OpenSIN-Code/issues/1117)

## What this page covers

This page documents the **V1 user-facing command surface** as it exists in the current source tree and the V1 launch gate.

It intentionally separates:

1. the commands an OSS user should actually learn first,
2. the larger source-derived command inventory that still exists in the repo,
3. experimental or internal modules that are **not** the first thing docs should teach.

## Quick orientation

| Topic | Current truth |
|---|---|
| Product role | TypeScript fork of the autonomous coding CLI surface |
| Verified install path today | Clone `OpenSIN-Code`, `bun install`, `bun run build`, start locally |
| Launch target | Public `opensin` install flow tracked in `OpenSIN-Code#1117` |
| Biggest blocker | [R1 merge/split decision](https://github.com/OpenSIN-AI/OpenSIN-Code/issues/1116) |

## Core V1 workflows

### 1. Start or resume work

These are the commands a new user should hit first:

| Command | Purpose |
|---|---|
| `/help` | Show the active command surface |
| `/resume` | Re-open a previous session |
| `/status` | Inspect current runtime status |
| `/session` | Work with saved sessions |
| `/compact` | Reduce context size without losing the thread |
| `/rewind` | Step back in the active conversation |
| `/export` | Export a session or result for later use |
| `/clear` | Clear conversation state or caches |

### 2. Configure the runtime

| Command | Purpose |
|---|---|
| `/config` | Inspect or change CLI configuration |
| `/model` | Change the active model |
| `/permissions` | Review or change tool permission behavior |
| `/mcp` | Manage MCP servers and connections |
| `/plugin` | Browse, install, or manage plugins |
| `/skills` | Discover and execute skills |
| `/hooks` | Review hook behavior |
| `/memory` | Inspect persistent memory surfaces |
| `/privacy-settings` | Control privacy / telemetry preferences |

### 3. Do actual code work

| Command | Purpose |
|---|---|
| `/plan` | Build an execution plan before coding |
| `/review` | Run post-implementation review workflow |
| `/doctor` | Diagnose local environment problems |
| `/branch` | Start a focused git workstream |
| `/diff` | Review current code changes |
| `/agents` | Manage agent surfaces and agent-mode routing |
| `/files` | Inspect file-oriented workspace state |
| `/tasks` | Inspect task execution state |

## Source-derived command inventory

The current `OpenSIN-Code` source tree contains a broader command inventory under:

- `packages/opensin-sdk/src/core/commands/`

That inventory includes the following top-level modules.

### Primary user-facing groups

- `add-dir`, `agents`, `branch`, `clear`, `compact`, `config`, `context`, `copy`, `cost`, `diff`, `doctor`, `export`, `files`, `help`, `hooks`, `install`, `login`, `logout`, `mcp`, `memory`, `model`, `permissions`, `plan`, `plugin`, `privacy-settings`, `resume`, `review`, `rewind`, `session`, `skills`, `stats`, `status`, `tasks`, `theme`, `upgrade`, `usage`

### Platform and setup commands

- `chrome`, `desktop`, `install-github-app`, `install-slack-app`, `mobile`, `remote-env`, `remote-setup`, `sandbox-toggle`, `terminalSetup`, `voice`, `vim`

### Advanced, experimental, or maintenance modules in the tree

- `advisor`, `ant-trace`, `autofix-pr`, `backfill-sessions`, `break-cache`, `bridge`, `btw`, `bughunter`, `ctx_viz`, `debug-tool-call`, `effort`, `env`, `extra-usage`, `fast`, `feedback`, `good-opensin`, `heapdump`, `issue`, `keybindings`, `mock-limits`, `oauth-refresh`, `onboarding`, `output-style`, `passes`, `perf-issue`, `pr_comments`, `rate-limit-options`, `release-notes`, `reload-plugins`, `rename`, `reset-limits`, `share`, `stickers`, `summary`, `tag`, `teleport`, `thinkback`, `thinkback-play`

## What is still not fully finished for launch

The docs gate in [OpenSIN-documentation#135](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/135) and the CLI gate in [OpenSIN-Code#1117](https://github.com/OpenSIN-AI/OpenSIN-Code/issues/1117) still require:

- a final public installer story from the marketing site,
- a stable `opensin --help` experience with no broken entries,
- support URLs and error strings that reference the right canonical repos,
- a command reference that is generated or at least maintained from one source.

This page closes the "no canonical reference at all" gap, but the launch-gate work in the CLI repo is still the source of truth for final polish.

## Recommended learning path

1. [Getting Started](/guide/getting-started)
2. This CLI reference
3. [OpenSIN backend V1 API](/api/backend-v1)
4. [Agent author guide](/guide/how-to-configure-agents)

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `OpenSIN-Code` uses Bun for the TypeScript workspace |
| **Annahmen-Verbot** | -5.0 | V1 command claims must track real modules or live issues |
| **Test-Beweis-Pflicht** | 0.0 | Launch docs must be backed by successful build / runtime validation |

→ [Alle Mandate](/best-practices/code-quality)
