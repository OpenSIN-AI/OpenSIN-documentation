# 🏛️ OpenSIN-AI — Master Documentation

> **Stand:** 2026-04-04 | **Version:** 2.0 | **Status:** ✅ ACTIVE

## 📋 Repository Overview

OpenSIN-AI ist die größte open-source AI Agent Organisation auf GitHub mit **156 Repositories**, **22 n8n Workflows**, und **21 A2A Agenten**.

| Komponente | Count | Status |
|------------|-------|--------|
| **Repositories** | 156 | ✅ All active |
| **n8n Workflows** | 22 | ✅ All active |
| **A2A Agents** | 21 | ✅ All configured |
| **OpenCode Skills** | 28 | ✅ All documented |
| **MCPs** | 27 | ✅ All configured |
| **Open Issues** | 200 | 📋 Labeled |
| **Open PRs** | 0 | ✅ Clean |

## 🏗️ Architektur

```
OpenSIN-AI Organization
├── Core Infrastructure
│   ├── OpenSIN-backend (Private) — Backend + A2A Fleet Control
│   ├── OpenSIN (Private) — 310+ packages across 25+ domains
│   └── OpenSIN-Code (Private) — Autonomous OpenSIN-Code CLI
│
├── A2A Agent Teams (130+ agents)
│   ├── Team Marketing — LinkedIn, Twitter, Medium, YouTube, etc.
│   ├── Team Coding — Frontend, Backend, DevOps, Security
│   ├── Team Infrastructure — Oracle Cloud, Cloudflare, Supabase
│   ├── Team Apple Apps — Shortcuts, Calendar, Notes, etc.
│   ├── Team Google Apps — Docs, Sheets, Drive, etc.
│   ├── Team Security — RedTeam, Forensics, Malware, etc.
│   └── Team Worker — Prolific, Mindrift, etc.
│
├── Infrastructure
│   ├── OCI VM (92.5.60.87) — n8n, Supabase, Token Factory
│   ├── HF Spaces — Agent Runtimes
│   └── Cloudflare — DNS, Workers, R2
│
└── Documentation
    ├── OpenSIN-documentation — Official docs (this repo)
    ├── Global-Dev-Docs-Standard — Dev documentation standard
    └── OpenSIN-Blueprints — Reusable blueprints
```

## 🔧 Development Guidelines

### Code Standards
- **TypeScript** für alle Agenten und Services
- **Python** für Scripts und Automation
- **JavaScript** für Web Components
- **Shell** für Infrastructure Scripts

### Documentation Standards
- Alle Repos folgen dem [Global-Dev-Docs-Standard](https://github.com/OpenSIN-AI/Global-Dev-Docs-Standard)
- Jedes Repo MUSS haben: `README.md`, `LICENSE`, `.gitignore`, `SECURITY.md`
- Agenten MÜSSEN haben: `agent.json`, `A2A-CARD.md`, `AGENTS.md`

### Git Workflow
- **Main Branch:** Protected, requires PR
- **Feature Branches:** `feature/description`
- **Commit Messages:** Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`)
- **PRs:** Require 1 approval, CI must pass

## 🚀 n8n CI/CD Pipeline

OpenSIN nutzt **niemals** GitHub Actions. Stattdessen:

| Workflow | Trigger | Zweck |
|----------|---------|-------|
| Global Fleet Self-Healing | Webhook | Automatisches Self-Healing |
| GitHub @opnsin-code Mention | GitHub Webhook | Auto-Delegation |
| Open Issues Auto-Processor | Schedule (1h) | Issue Processing |
| PR Watcher + Auto-Review | Schedule (15min) | PR Monitoring |
| Security Vulnerability Scanner | Schedule (24h) | Security Scanning |
| HF Spaces Health + Auto-Restart | Schedule (30min) | HF Spaces Health |
| GitHub Commit Monitor | Schedule (2h) | Commit Tracking |
| Token Pool Monitor | Schedule (30min) | Token Pool |
| Supabase Health Monitor | Schedule (15min) | Supabase Health |
| OCI VM Disk Space Monitor | Schedule (4h) | Infrastructure Health |

## 📁 Documentation Structure

```
OpenSIN-documentation/
├── docs/
│   ├── CLAW.md                    ← This file
│   ├── ops/                       ← Operations documentation
│   │   ├── opencode-config.md     ← OpenCode configuration SSOT
│   │   ├── n8n-setup.md           ← n8n setup and workflows
│   │   ├── omoc-swarm-bugs.md     ← OMOC Swarm bug registry
│   │   ├── disk-cleanup-2026-04-04.md
│   │   └── session-report-2026-04-04.md
│   ├── skills/                    ← OpenCode skills documentation (27 files)
│   ├── mcps/                      ← MCP documentation
│   ├── agents/                    ← A2A agent documentation
│   ├── commands/                  ← Command documentation
│   └── plugins/                   ← Plugin documentation
├── README.md
└── LICENSE
```

## 🔑 Key Resources

| Resource | URL | Purpose |
|----------|-----|---------|
| **Dashboard** | https://a2a.delqhi.com | A2A Fleet Dashboard |
| **n8n** | http://92.5.60.87:5678 | Workflow Automation |
| **Supabase** | http://92.5.60.87:54321 | Database |
| **OCI VM** | ubuntu@92.5.60.87 | Infrastructure Host |
| **GitHub Org** | https://github.com/OpenSIN-AI | Organization |

## ⚠️ Critical Rules

1. **NIEMALS** GitHub Actions nutzen — n8n + A2A only
2. **IMMER** `sin-sync` nach Änderungen an globaler Config
3. **NIEMALS** Auth-Dateien syncen — jede Maschine hat eigene Auth
4. **IMMER** Tests vor Commits
5. **NIEMALS** proprietären Code in public Repos

## 📊 Current Status

| Metric | Value |
|--------|-------|
| **Disk Space** | 92GB free |
| **n8n Workflows** | 22/22 active |
| **OCI VM Services** | 18/18 healthy |
| **Token Pool** | 12 Antigravity + 6 OpenAI |
| **Open Issues** | 200 (labeled) |
| **Open PRs** | 0 |

---

*Last updated: 2026-04-04 by SIN-Zeus*
