# Fleet Overview — A2A Agent Fleet

**Status:** Active
**Owner:** SIN-Zeus (Fleet Commander)

---

## What Is The Fleet?

The OpenSIN-AI Fleet is a network of autonomous A2A (Agent-to-Agent) agents that collaborate across repositories, platforms, and services. Each agent is a self-contained process with its own tools, skills, and Telegram bot — coordinated by Team Managers and the global orchestrator SIN-Zeus.

---

## Fleet Architecture

```
┌──────────────────────────────────────────────┐
│               SIN-Zeus                        │
│          (Fleet Commander)                    │
├──────────────────┬───────────────────────────┤
│  Team Managers   │   Global Agents           │
│  ─────────────   │   ─────────────           │
│  Team Coding     │   SIN-Hermes (Dispatcher) │
│  Team Worker     │   SIN-Herakles (Backend)  │
│  Team Infra      │   SIN-Solver (Web App)    │
│  Team Google     │   SIN-Research            │
│  Team Media      │   SIN-Patents             │
│  Team Microsoft  │   ...                     │
└──────────────────┴───────────────────────────┘
```

---

## Agent Categories

| Category | Count | Examples |
|----------|-------|----------|
| **Team Managers** | 5+ | Team Coding, Team Worker, Team Infra, Team Google Apps, Team Microsoft |
| **Coding Agents** | 10+ | Simone-MCP, Frontend, Backend, DevOps, DataScience, GitLab-LogsCenter |
| **Platform Agents** | 30+ | Prolific, HeyPiggy, Mindrift, Instagram, TikTok, YouTube, LinkedIn |
| **Messaging Agents** | 15+ | WhatsApp, Telegram, Discord, Signal, Slack, Teams, WeChat, LINE |
| **Apple Agents** | 10+ | Mail, Notes, Calendar, Safari, Shortcuts, Photos, FaceTime |
| **Infrastructure** | 5+ | Storage, Stripe, Chrome Extension, Computer Use, Memory |

---

## Fleet Communication

- **A2A Protocol**: Agent-to-Agent JSON-RPC over HTTP
- **Telegram**: Fleet-wide alerts, operator chat, incident escalation
- **Neural-Bus**: NATS JetStream event mesh (WIP — see [Neural-Bus docs](/architecture/global-brain-neural-bus))
- **GitHub**: Issues, PRs, and the Fleet Operations project board

---

## Agent Lifecycle

1. **Create**: Generated from `Template-SIN-Agent` via `/create-a2a-sin-agent` skill
2. **Deploy**: Pushed to GitHub, Cloudflare Workers, or HF Space
3. **Register**: Added to fleet registry and team configuration
4. **Operate**: Autonomous task execution, self-healing via GitHub Issues
5. **Monitor**: Box.com Storage collects artifacts, errors trigger auto-issues

---

## Key Repositories

| Repo | Purpose |
|------|---------|
| [Template-SIN-Agent](https://github.com/OpenSIN-AI/Template-SIN-Agent) | Blueprint for all agents |
| [Template-SIN-Team](https://github.com/OpenSIN-AI/Template-SIN-Team) | Blueprint for team managers |
| [OpenSIN-documentation](https://github.com/OpenSIN-AI/OpenSIN-documentation) | Fleet docs (this repo) |
| [OpenSIN-Code](https://github.com/OpenSIN-AI/OpenSIN-Code) | CLI core, plugins, engine |
| [OpenSIN-Neural-Bus](https://github.com/OpenSIN-AI/OpenSIN-Neural-Bus) | Event-sourcing mesh |
| [Fleet Operations Project](https://github.com/orgs/OpenSIN-AI/projects/21) | Tracking board |

---

## Related

- [Governance Overview](/governance/overview)
- [A2A Architecture](/architecture/a2a)
- [Team Orchestration](/guide/team-orchestration)
- [Agent Configuration](/guide/agent-configuration)
