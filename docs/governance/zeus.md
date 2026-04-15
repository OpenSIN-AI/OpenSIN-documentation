# SIN-Zeus — Fleet Commander

**Role:** Fleet Commander & Control-Plane Orchestrator
**Model:** `qwen/coder-model` (primary), `claude-opus-4.6-thinking` (fallback)
**Status:** Active
**Owner:** Jeremy Schulze (Delqhi)

---

## Overview

SIN-Zeus is the top-level orchestrator of the OpenSIN-AI fleet. It conducts organization-wide audits, dispatches tasks to team managers, enforces governance compliance, and maintains the SSOT (Single Source of Truth) across all repositories.

---

## Responsibilities

### 1. Organization Audits
- Scans all repos for stale branches, open issues, fake PRs
- Creates tracking projects on GitHub
- Generates audit reports with findings and action items
- Closes resolved issues and stale PRs

### 2. Task Dispatch
- Delegates work to Team Managers (Coding, Worker, Infra, Google, Microsoft)
- Uses background agents for parallel execution
- Monitors task completion and retries on failure

### 3. Governance Enforcement
- Runs Repo Health Check compliance audits
- Monitors PR-Watcher results
- Enforces mandate priorities (P-100 to P0)
- Bans and flags protocol violations

### 4. Fleet Coordination
- Maintains fleet registry and team configurations
- Coordinates cross-team collaboration
- Manages the Fleet Operations project board
- Handles incident escalation

---

## Architecture

```
┌─────────────────────────────────────┐
│           SIN-Zeus                   │
│     (Fleet Commander)                │
├──────────────┬──────────────────────┤
│   Scan       │  Audit               │
│   ├──repos   │  ├──issues           │
│   ├──branches│  ├──PRs              │
│   └──config  │  └──compliance       │
│              │                      │
│   Dispatch   │  Report              │
│   ├──teams   │  ├──GitHub Issues    │
│   ├──agents  │  ├──Project Boards   │
│   └──tasks   │  └──Audit Reports    │
└──────────────┴──────────────────────┘
```

---

## Commands

| Command | Description |
|---------|-------------|
| `zeus.audit` | Full organization audit across all repos |
| `zeus.dispatch` | Delegate task to team fleet |
| `zeus.compliance` | Run governance compliance check |
| `zeus.health` | Fleet health status report |
| `zeus.cleanup` | Prune stale branches, close resolved issues |

---

## Recent Actions

| Date | Action | Result |
|------|--------|--------|
| 2026-04-14 | Org-wide audit | 22 stale branches pruned, 1 fake PR closed, 3 zombie issues closed |
| 2026-04-14 | Fleet Project #21 created | 19 issues tracked |
| 2026-04-14 | Audit Issue #99 created | Complete findings documented |

---

## Related

- [Hermes — Task Dispatcher](/governance/hermes)
- [Governance Overview](/governance/overview)
- [Fleet Overview](/fleet/overview)
- [Repo Health Check](/governance/repo-health-check)

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Immediate Bug Registry** | -4.0 | JEDER Bug SOFORT als GitHub Issue |
| **PR-Watcher** | 0.0 | Alle Repos brauchen PR-Watcher |
| **Zeus/Hermes** | 0.0 | Fleet-Kommando via SIN-Zeus |

→ [Alle Mandate](/best-practices/error-handling)
