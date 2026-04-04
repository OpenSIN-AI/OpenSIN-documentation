# sovereign-repo-governance (CEO & World Champion Edition)

(opencode - Skill) The March 2026 gold standard for autonomous repository management. This skill governs the entire lifecycle of a repository, divided into two primary pillars: **Internal Governance (Zeus & Hermes Control Plane)** for autonomous task orchestration, and **External Outreach (CEO Bug-Hunter Protocol)** for building global reputation by fixing upstream anomalies.

## Triggers
**MANDATORY USE:** Keywords "zeus", "bootstrap project", "roadmap to issues", "hermes dispatch", "github issue", "opencode issue", "hunt bugs", "fix upstream", "sync fixes", "report bug".

---

## PART 1: Internal Governance (Zeus & Hermes Control Plane)

The internal governance model converts high-level plans into highly structured, actionable GitHub Projects, Epics, and Sub-Issues, and then automatically dispatches them to the specialized A2A Coder Fleet.

### 0. GitHub Metadata Governance (Mandatory for OpenSIN-AI)
When creating or updating any A2A-SIN repository inside the GitHub organization `OpenSIN-AI`, agents MUST set the GitHub metadata correctly:
- **Required topic:** `opnsin-agent`
- **Required website field:** the public dashboard URL for that agent

Website host rules:
- Until the official domain cutover is explicitly released by the user, use the currently live dashboard host on `https://a2a.delqhi.com`
- After the official cutover/release, update the repo website to `https://opensin.ai/agents/<slug>`

Examples:
- before cutover: `https://a2a.delqhi.com/agents/sin-google-apps`
- after cutover: `https://opensin.ai/agents/sin-google-apps`

Fail-closed rule:
- a newly created A2A-SIN repo is **not governance-complete** until the required topic and the correct website URL are both set

### 1. The Zeus Bootstrap Flow
When an autonomous plan or roadmap is approved (e.g., via `/check-plan-done`), it MUST be persisted into a structured JSON roadmap (e.g., `Docs/operations/endgame-plan.json`).
- Use **`scripts/zeus/bootstrap-github-project.mjs`** to inject this plan into GitHub.
  - *Example:* `node scripts/zeus/bootstrap-github-project.mjs --owner Delqhi --repo SIN-Solver/OpenSIN --title "Phase 5 Endgame" --plan-file Docs/operations/endgame-plan.json`
- This script automatically:
  - Creates a new GitHub Project Board.
  - Converts the JSON plan into Epics and Sub-Issues.
  - Generates working branches linked to each issue (e.g., `zeus/01-phase-5-...`).
  - Applies color-coded labels and team/capability hints.

### 2. The Hermes Dispatch Flow
Once issues are in the GitHub/Supabase pool, they must be assigned to the A2A Coder workforce.
- Use **`scripts/zeus/hermes-pool-sync.mjs`** to poll the `sin_issues_pool` and dynamically route open tasks to the correct specialized agent (`A2A-SIN-Code-Database`, `A2A-SIN-Code-Integration`, `A2A-SIN-Code-AI`, `A2A-SIN-Frontend`, `A2A-SIN-Backend`, etc.) based on keywords and labels.
- Use **`scripts/zeus/hermes-dispatch.mjs`** to build capability routing artifacts for advanced topological assignments.
- Use **`scripts/zeus/hermes-intake.mjs`** to submit tasks directly to the `Room-13` FastAPI coordinator if executing in the legacy worker lane.

### 3. Inbound Work + PR Watcher Lane (Mandatory)
Every governed repo must separate ingress from review feedback:
- **Ingress:** n8n webhook/poller only
- **Normalization:** shared `work_item` contract only
- **Durable task state:** GitHub issue first
- **Review feedback:** PR watcher only after a PR exists

Required repo artifacts:
- `governance/repo-governance.json`
- `governance/pr-watcher.json`
- `governance/coder-dispatch-matrix.json` for coding/work repos
- `platforms/registry.json`
- `n8n-workflows/inbound-intake.json`
- `docs/03_ops/inbound-intake.md`
- `scripts/watch-pr-feedback.sh`

Fail-closed rules:
- no raw external payloads inside repos
- no accepted inbound work without GitHub issue creation/update
- no PR-based repo without watcher config + runnable watcher entrypoint
- no platform activation without registry entry, signature/cursor verification, dedupe, and issue mapping

Canonical shared references:
- `~/.config/opencode/INBOUND_WORK_ARCHITECTURE.md`
- `~/.config/opencode/templates/work-item.schema.json`
- `~/.config/opencode/templates/platform-registry.schema.json`
- `~/.config/opencode/templates/pr-watcher.schema.json`

---

## PART 2: External Outreach (CEO Bug-Hunter Protocol)

The external protocol dictates how the agent proactively hunts for bugs in upstream repositories, fixes them using SIN-Solver best practices, and publishes elite PRs/Issues.

### 1. Autonomous Reconnaissance
- Use `scripts/bug_hunter.mjs` to crawl upstreams like `anomalyco/opencode` and `code-yeongyu/oh-my-openagent`.
- Filter issues by complexity and local relevance.

### 2. The Fix-and-Vanish Loop
- Pick an issue, reproduce it in a local sandbox.
- Develop a structural fix following SIN-Solver's 2026 architecture standards.
- Add the bug to `repair-docs.md` with status ✅ GEFIXT.

### 3. Elite Publication & Visual Evidence
- Use `scripts/submit_sovereign_issue.mjs` to dual-file the fix.
- Public GitHub APIs do not expose first-class issue image uploads, so host screenshots on a stable public GitHub Release and embed them with Markdown.
- Generate premium code/error screenshots with `carbon-now-cli`.
- For issue evidence, capture three lanes when available: error state, changed code/diff state, successful post-fix state.
- Use `scripts/capture_diff_screenshot.mjs` to generate AIometrics-watermarked screenshots and upload them to the public `auto-screenshots` release.
- Ensure the PR/Issue comment includes a reference to our Sovereign Fleet.

---

## Automation Tools

**Internal (Zeus & Hermes):**
- **`scripts/zeus/bootstrap-github-project.mjs`**: Converts JSON roadmaps into full GitHub Project Boards, Epics, and working branches.
- **`scripts/zeus/hermes-pool-sync.mjs`**: Polls the Supabase issue pool and dispatches tasks to specific A2A Coder Agents.
- **`scripts/zeus/hermes-dispatch.mjs`**: Generates capability-routed executor jobs.
- **`scripts/zeus/hermes-intake.mjs`**: Submits capability payloads to the Room-13 coordinator.

**External (Bug Hunter):**
- **`scripts/bug_hunter.mjs`**: Crawls upstreams for candidates.
- **`scripts/sync_all_local_fixes.mjs`**: Deep-scans docs and reports un-published local fixes.
- **`scripts/capture_diff_screenshot.mjs`**: Generates and hosts premium code/error screenshots.
- **`scripts/submit_sovereign_issue.mjs`**: Dual-files issues with CEO formatting and optional visual evidence (`--error-file`, `--diff-file`, `--success-file`).
- **`scripts/remediate_workspace_docs.mjs`**: Idempotent documentation sync for Google Workspace.

> **FLEET SYNC MANDATE:** Any modifications to this skill or its scripts MUST be pushed to all runtimes via `sin-sync`.

---

## PART 3: Automated Wiki Governance (Best Practices)

In enterprise and private environments, standard GitHub Wikis easily become disorganized dumping grounds. To maintain technical excellence, all A2A agents MUST autonomously initialize and structure the GitHub Wiki of a new or existing repository using strict best practices based on the repository's use case.

### Core Enterprise Wiki Rules
1. **Wiki as Code:** A GitHub Wiki is just a secondary Git repository (`https://github.com/<org>/<repo>.wiki.git`). Agents must interact with it via `git clone`, generate the structure locally, and `git push`.
2. **Mandatory Navigation:** Every wiki MUST have a `_Sidebar.md` to force a strict, hierarchical navigation menu. Do not rely on GitHub's default alphabetical sorting.
3. **Logical Folders:** Use slash-separated filenames to mimic folders (e.g., `Architecture/System-Design.md`).
4. **Image Persistence:** Create an `assets/` folder inside the `.wiki.git` repository to host images. Never link to ephemeral external image hosts.

### Standard Templates per Use Case
Use the `scripts/zeus/wiki-bootstrap.mjs` script to automatically generate the correct structure based on the repo type:

- **Frontend (`--type frontend`)**:
  - `Home.md` (Project Overview, Setup)
  - `Architecture/State-Management.md`
  - `Architecture/Component-Library.md`
  - `Guides/Styling-Conventions.md`
- **Backend/Service (`--type backend`)**:
  - `Home.md` (Project Overview, Setup)
  - `Architecture/System-Design.md`
  - `Architecture/Database-Schema.md`
  - `API/Endpoints.md`
  - `Operations/Runbooks.md`
- **Library/Package (`--type library`)**:
  - `Home.md` (Overview, Installation)
  - `Usage/Quickstart.md`
  - `API/Reference.md`
  - `Guides/Contributing.md`
- **Monorepo (`--type monorepo`)**:
  - `Home.md` (Ecosystem Overview, Setup)
  - `Architecture/Package-Boundaries.md`
  - `Operations/CI-CD-Pipelines.md`
  - `Guides/Tooling.md`

### Execution
Whenever a new repo is created or an agent is tasked with documentation:
```bash
node scripts/zeus/wiki-bootstrap.mjs --org OpenSIN-AI --repo my-new-service --type backend
```
This clones the wiki, scaffolds the correct `.md` files and the `_Sidebar.md`, and pushes it to the repository.
