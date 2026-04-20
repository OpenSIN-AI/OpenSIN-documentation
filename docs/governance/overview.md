# Governance Overview — OpenSIN-AI Fleet Governance

**Status:** Active
**Owner:** SIN-Zeus (control-plane)

---

## What Is Governance?

Governance defines the rules, processes, and automated checks that keep the OpenSIN-AI fleet operating safely, consistently, and in alignment with organizational standards. Governance is not optional — it is enforced through automated checks, PR-watcher hooks, and fleet-wide mandates.

---

## Governance Layers

### 1. Repo Governance
Every repository in the OpenSIN-AI organization must comply with minimum standards:
- `README.md` with project description
- `AGENTS.md` with agent operating manual
- `LICENSE` file
- `.gitignore` configuration
- GitHub Topics (at least 1)
- No hardcoded secrets

Enforced by: [Repo Health Check](/governance/repo-health-check) GitHub Action

### 2. Code Governance
- **PR-Watcher**: Every PR is automatically reviewed by 5 parallel sub-agents
- **Commit Hooks**: `.opencode/opencode.json` hooks inject Global Brain context
- **Code Quality**: LSP diagnostics, AST-grep patterns, test coverage gates

### 3. Fleet Governance
- **Agent Mandates**: Priority-ranked rules in `AGENTS.md` (P-100 to P0)
- **Technology Bans**: Camoufox, Playwright, Puppeteer, Selenium permanently banned
- **Package Manager**: Bun only — npm is permanently banned
- **LLM Routing**: Only approved models via `opencode` CLI

### 4. Auth Governance
- **Antigravity Plugin**: Must never be removed from opencode.json
- **Token Rotation**: Automated via OCI VM token factory
- **Supabase Pool**: Centralized token management with `is_active` boolean

---

## Key Governance Agents

| Agent | Role | Mandate |
|-------|------|---------|
| **SIN-Zeus** | Fleet Commander | Top-level orchestration, audit, compliance |
| **SIN-Hermes** | Task Dispatcher | Routes tasks, monitors fleet health |
| **SIN-Herakles** | Backend/Infra | Heavy lifting, system operations |
| **PR-Watcher** | Code Review | Automated PR analysis (5 parallel agents) |
| **Box Storage Agent** | Artifact Management | Uploads logs/screenshots to Box.com, auto-creates issues |

---

## Governance Documents

| Document | Purpose |
|----------|---------|
| [Repo Health Check](/governance/repo-health-check) | Automated compliance checks |
| [Domain Registry](/governance/domain-registry) | Evidence-based public / gated / internal surface map |
| [Zeus — Fleet Commander](/governance/zeus) | Zeus operating manual |
| [Hermes — Task Dispatcher](/governance/hermes) | Hermes operating manual |

---

## Violation Consequences

| Violation | Consequence |
|-----------|-------------|
| Banned technology usage | Immediate permanent ban |
| npm instead of bun | Immediate ban |
| Gemini API direct calls | Permanent ban |
| Web actions without Vision Gate | Permanent ban |
| Code without comments | Protocol violation |
| Assumptions without proof | Immediate ban |
| Bugs without GitHub Issues | Protocol violation |

---

## Related

- [Fleet Overview](/fleet/overview)
- [Repo Health Check](/governance/repo-health-check)
- [Domain Registry](/governance/domain-registry)
- [Agent Design Best Practices](/best-practices/agent-design)
- [Security Architecture](/architecture/security)

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Immediate Bug Registry** | -4.0 | JEDER Bug SOFORT als GitHub Issue |
| **PR-Watcher** | 0.0 | Alle Repos brauchen PR-Watcher |
| **Zeus/Hermes** | 0.0 | Fleet-Kommando via SIN-Zeus |

→ [Alle Mandate](/best-practices/error-handling)
