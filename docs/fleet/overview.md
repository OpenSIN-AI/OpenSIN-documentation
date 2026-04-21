# Fleet Overview — A2A Agent Fleet

**Status:** Active
**Owner:** SIN-Zeus (Fleet Commander)

---

## What Is The Fleet?

The OpenSIN-AI Fleet is a network of autonomous A2A (Agent-to-Agent) agents that collaborate across repositories, platforms, and services. Each agent is a self-contained process with its own tools, skills, and Telegram bot — coordinated by Team Managers and the global orchestrator SIN-Zeus.

---

## Fleet Architecture (Hub & Spoke)

As defined in the `OpenSIN-overview` SSOT, the fleet follows a strict **Hub & Spoke** model to ensure massive scalability and governance.

```mermaid
graph TD;
    User[Operator / Mobile] -->|Task| TeamManager[Team-SIN-* Orchestrator];
    NeuralBus[OpenSIN Neural-Bus] <-->|Event Mesh| TeamManager;
    
    subgraph Team Monorepo
        TeamManager -->|Delegate| WorkerA[A2A-SIN-Worker-A];
        TeamManager -->|Delegate| WorkerB[A2A-SIN-Worker-B];
    end
    
    TeamManager -->|Register| Registry[Domain Registry / Global Brain];
```

### Key Principles

1. **Managers Orchestrate:** Only `Team-SIN-*` agents are authorized to manage multi-step workflows and communicate with the Neural-Bus Hub.
2. **Workers Execute:** `A2A-SIN-*` worker agents are specialists. They do not talk to workers from other teams; they only report to their designated Manager.
3. **Registry Truth:** An agent does not exist until it is verified in the [Domain Registry](/governance/domain-registry).
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
| **Infrastructure** | 6+ | A2A-SIN-Box-Storage (Room 09), Stripe, Chrome Extension, Computer Use, Memory, N8N |

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

## Infrastructure Agent Details

### A2A-SIN-Box-Storage (Room 09)

**Box.com Storage API Agent** — Central file upload service for the entire OpenSIN fleet. Replaces deprecated GitLab Storage.

| Property | Value |
|:---|:---|
| **Room** | 09 |
| **Static IP** | `<canonical-box-storage-ip>:3000` |
| **Internal Endpoint** | `http://room-09-box-storage:3000` |
| **Public A2A** | `Unverified in public docs — verify in owning repo before external use` |
| **Health** | `GET /health` |
| **Upload** | `POST /api/v1/upload` |
| **Validate** | `POST /api/v1/validate` |
| **Auth** | `X-Box-Storage-Key` header |
| **Team** | Team Infrastructure |
| **Agent Repo** | [A2A-SIN-Box-Storage](https://github.com/OpenSIN-AI/A2A-SIN-Box-Storage) |

#### Capabilities
- `storage_upload` — Upload files to Box.com public folder
- `storage_public_url` — Return shareable CDN URLs  
- `file_validation` — Enforce size, type, extension whitelist
- `cdn_distribution` — Box edge cache integration
- `cache_management` — ETag, cache-control headers

#### Box.com Folders
| Folder | Shared Link | Folder ID |
|--------|-------------|-----------|
| `/Public` | https://app.box.com/s/1st624o9eb5xdistusew5w0erb8offc7 | `1st624o9eb5xdistusew5w0erb8offc7` |
| `/Cache` | https://app.box.com/s/9s5htoefw1ux9ajaqj656v9a02h7z7x1 | `9s5htoefw1ux9ajaqj656v9a02h7z7x1` |

#### Usage Example
```bash
# Upload file via agent
curl -X POST "http://room-09-box-storage:3000/api/v1/upload" \
  -H "X-Box-Storage-Key: $BOX_STORAGE_API_KEY" \
  -F "file=@screenshot.png"

# Preflight validation
curl -X POST "http://room-09-box-storage:3000/api/v1/validate" \
  -H "Content-Type: application/json" \
  -d '{"filename":"report.pdf","size":5242880}'

# Health check
curl "http://room-09-box-storage:3000/health"
```

#### MCP Integration
Agents can access Box Storage via MCP using the `sin-box-storage` interface:

```json
// In opencode.json MCP config
{
  "mcpServers": {
    "sin-box-storage": {
      "command": "bun",
      "args": ["x", "@sin-docker/sin-box-storage-mcp"]
    }
  }
}
```

#### Docker Deployment (Infra-SIN-Docker-Empire)
```yaml
room-09-box-storage:
  build: ./services/box-storage
  image: a2a-sin-box-storage:latest
  container_name: room-09-box-storage
  restart: unless-stopped
  environment:
    - BOX_DEVELOPER_TOKEN=${BOX_DEVELOPER_TOKEN}
    - BOX_PUBLIC_FOLDER_ID=${BOX_PUBLIC_FOLDER_ID}
    - BOX_CACHE_FOLDER_ID=${BOX_CACHE_FOLDER_ID}
    - API_KEY=${BOX_STORAGE_API_KEY}
    - PORT=3000
  networks:
    haus-netzwerk:
      ipv4_address: <canonical-box-storage-ip>
  ports:
    - "3000:3000"
  healthcheck:
    test: ["CMD", "curl", "-f", "http://127.0.0.1:3000/health"]
    interval: 30s
    timeout: 10s
    retries: 3
```

> **Migration Note:** A2A-SIN-Box-Storage replaces `room-07-gitlab-storage`. All agents MUST migrate from `gitlab_logcenter.py` to Box Storage API. See [Box Cloud Storage Docs](/storage/box-cloud-storage) for full migration guide.

---

## Related

- [Governance Overview](/governance/overview)
- [A2A Architecture](/architecture/a2a)
- [Team Orchestration](/guide/team-orchestration)
- [Agent Configuration](/guide/agent-configuration)

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **A2A-First** | -200.0 | SELBST MACHEN via A2A-Agenten |
| **LLM via opencode CLI** | -2.5 | `opencode run --format json` |
| **Fleet Architecture V2** | 0.0 | marketplace metadata in agent.json |

→ [Alle Mandate](/best-practices/a2a-communication)
