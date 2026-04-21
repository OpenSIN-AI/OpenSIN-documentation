import{_ as a,o as n,c as e,a2 as i}from"./chunks/framework.ufzXw1qY.js";const d=JSON.parse('{"title":"Fleet Overview — A2A Agent Fleet","description":"","frontmatter":{},"headers":[],"relativePath":"fleet/overview.md","filePath":"fleet/overview.md"}'),p={name:"fleet/overview.md"};function t(l,s,r,o,h,c){return n(),e("div",null,[...s[0]||(s[0]=[i(`<h1 id="fleet-overview-—-a2a-agent-fleet" tabindex="-1">Fleet Overview — A2A Agent Fleet <a class="header-anchor" href="#fleet-overview-—-a2a-agent-fleet" aria-label="Permalink to &quot;Fleet Overview — A2A Agent Fleet&quot;">​</a></h1><p><strong>Status:</strong> Active <strong>Owner:</strong> SIN-Zeus (Fleet Commander)</p><hr><h2 id="what-is-the-fleet" tabindex="-1">What Is The Fleet? <a class="header-anchor" href="#what-is-the-fleet" aria-label="Permalink to &quot;What Is The Fleet?&quot;">​</a></h2><p>The OpenSIN-AI Fleet is a network of autonomous A2A (Agent-to-Agent) agents that collaborate across repositories, platforms, and services. Each agent is a self-contained process with its own tools, skills, and Telegram bot — coordinated by Team Managers and the global orchestrator SIN-Zeus.</p><hr><h2 id="fleet-architecture-hub-spoke" tabindex="-1">Fleet Architecture (Hub &amp; Spoke) <a class="header-anchor" href="#fleet-architecture-hub-spoke" aria-label="Permalink to &quot;Fleet Architecture (Hub &amp; Spoke)&quot;">​</a></h2><p>As defined in the <code>OpenSIN-overview</code> SSOT, the fleet follows a strict <strong>Hub &amp; Spoke</strong> model to ensure massive scalability and governance.</p><div class="language-mermaid vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">mermaid</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">graph TD;</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    User[Operator / Mobile] --&gt;|Task| TeamManager[Team-SIN-* Orchestrator];</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    NeuralBus[OpenSIN Neural-Bus] &lt;--&gt;|Event Mesh| TeamManager;</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    </span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    subgraph Team Monorepo</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">        TeamManager --&gt;|Delegate| WorkerA[A2A-SIN-Worker-A];</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">        TeamManager --&gt;|Delegate| WorkerB[A2A-SIN-Worker-B];</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    end</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    </span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    TeamManager --&gt;|Register| Registry[Domain Registry / Global Brain];</span></span></code></pre></div><h3 id="key-principles" tabindex="-1">Key Principles <a class="header-anchor" href="#key-principles" aria-label="Permalink to &quot;Key Principles&quot;">​</a></h3><ol><li><strong>Managers Orchestrate:</strong> Only <code>Team-SIN-*</code> agents are authorized to manage multi-step workflows and communicate with the Neural-Bus Hub.</li><li><strong>Workers Execute:</strong> <code>A2A-SIN-*</code> worker agents are specialists. They do not talk to workers from other teams; they only report to their designated Manager.</li><li><strong>Registry Truth:</strong> An agent does not exist until it is verified in the <a href="/governance/domain-registry.html">Domain Registry</a>. ┌──────────────────────────────────────────────┐ │ SIN-Zeus │ │ (Fleet Commander) │ ├──────────────────┬───────────────────────────┤ │ Team Managers │ Global Agents │ │ ───────────── │ ───────────── │ │ Team Coding │ SIN-Hermes (Dispatcher) │ │ Team Worker │ SIN-Herakles (Backend) │ │ Team Infra │ SIN-Solver (Web App) │ │ Team Google │ SIN-Research │ │ Team Media │ SIN-Patents │ │ Team Microsoft │ ... │ └──────────────────┴───────────────────────────┘</li></ol><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span></span></span>
<span class="line"><span>---</span></span>
<span class="line"><span></span></span>
<span class="line"><span>## Agent Categories</span></span>
<span class="line"><span></span></span>
<span class="line"><span>| Category | Count | Examples |</span></span>
<span class="line"><span>|----------|-------|----------|</span></span>
<span class="line"><span>| **Team Managers** | 5+ | Team Coding, Team Worker, Team Infra, Team Google Apps, Team Microsoft |</span></span>
<span class="line"><span>| **Coding Agents** | 10+ | Simone-MCP, Frontend, Backend, DevOps, DataScience, GitLab-LogsCenter |</span></span>
<span class="line"><span>| **Platform Agents** | 30+ | Prolific, HeyPiggy, Mindrift, Instagram, TikTok, YouTube, LinkedIn |</span></span>
<span class="line"><span>| **Messaging Agents** | 15+ | WhatsApp, Telegram, Discord, Signal, Slack, Teams, WeChat, LINE |</span></span>
<span class="line"><span>| **Apple Agents** | 10+ | Mail, Notes, Calendar, Safari, Shortcuts, Photos, FaceTime |</span></span>
<span class="line"><span>| **Infrastructure** | 6+ | A2A-SIN-Box-Storage (Room 09), Stripe, Chrome Extension, Computer Use, Memory, N8N |</span></span>
<span class="line"><span></span></span>
<span class="line"><span>---</span></span>
<span class="line"><span></span></span>
<span class="line"><span>## Fleet Communication</span></span>
<span class="line"><span></span></span>
<span class="line"><span>- **A2A Protocol**: Agent-to-Agent JSON-RPC over HTTP</span></span>
<span class="line"><span>- **Telegram**: Fleet-wide alerts, operator chat, incident escalation</span></span>
<span class="line"><span>- **Neural-Bus**: NATS JetStream event mesh (WIP — see [Neural-Bus docs](/architecture/global-brain-neural-bus))</span></span>
<span class="line"><span>- **GitHub**: Issues, PRs, and the Fleet Operations project board</span></span>
<span class="line"><span></span></span>
<span class="line"><span>---</span></span>
<span class="line"><span></span></span>
<span class="line"><span>## Agent Lifecycle</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. **Create**: Generated from \`Template-SIN-Agent\` via \`/create-a2a-sin-agent\` skill</span></span>
<span class="line"><span>2. **Deploy**: Pushed to GitHub, Cloudflare Workers, or HF Space</span></span>
<span class="line"><span>3. **Register**: Added to fleet registry and team configuration</span></span>
<span class="line"><span>4. **Operate**: Autonomous task execution, self-healing via GitHub Issues</span></span>
<span class="line"><span>5. **Monitor**: Box.com Storage collects artifacts, errors trigger auto-issues</span></span>
<span class="line"><span></span></span>
<span class="line"><span>---</span></span>
<span class="line"><span></span></span>
<span class="line"><span>## Key Repositories</span></span>
<span class="line"><span></span></span>
<span class="line"><span>| Repo | Purpose |</span></span>
<span class="line"><span>|------|---------|</span></span>
<span class="line"><span>| [Template-SIN-Agent](https://github.com/OpenSIN-AI/Template-SIN-Agent) | Blueprint for all agents |</span></span>
<span class="line"><span>| [Template-SIN-Team](https://github.com/OpenSIN-AI/Template-SIN-Team) | Blueprint for team managers |</span></span>
<span class="line"><span>| [OpenSIN-documentation](https://github.com/OpenSIN-AI/OpenSIN-documentation) | Fleet docs (this repo) |</span></span>
<span class="line"><span>| [OpenSIN-Code](https://github.com/OpenSIN-AI/OpenSIN-Code) | CLI core, plugins, engine |</span></span>
<span class="line"><span>| [OpenSIN-Neural-Bus](https://github.com/OpenSIN-AI/OpenSIN-Neural-Bus) | Event-sourcing mesh |</span></span>
<span class="line"><span>| [Fleet Operations Project](https://github.com/orgs/OpenSIN-AI/projects/21) | Tracking board |</span></span>
<span class="line"><span></span></span>
<span class="line"><span>---</span></span>
<span class="line"><span></span></span>
<span class="line"><span>## Infrastructure Agent Details</span></span>
<span class="line"><span></span></span>
<span class="line"><span>### A2A-SIN-Box-Storage (Room 09)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>**Box.com Storage API Agent** — Central file upload service for the entire OpenSIN fleet. Replaces deprecated GitLab Storage.</span></span>
<span class="line"><span></span></span>
<span class="line"><span>| Property | Value |</span></span>
<span class="line"><span>|:---|:---|</span></span>
<span class="line"><span>| **Room** | 09 |</span></span>
<span class="line"><span>| **Static IP** | \`&lt;canonical-box-storage-ip&gt;:3000\` |</span></span>
<span class="line"><span>| **Internal Endpoint** | \`http://room-09-box-storage:3000\` |</span></span>
<span class="line"><span>| **Public A2A** | \`Unverified in public docs — verify in owning repo before external use\` |</span></span>
<span class="line"><span>| **Health** | \`GET /health\` |</span></span>
<span class="line"><span>| **Upload** | \`POST /api/v1/upload\` |</span></span>
<span class="line"><span>| **Validate** | \`POST /api/v1/validate\` |</span></span>
<span class="line"><span>| **Auth** | \`X-Box-Storage-Key\` header |</span></span>
<span class="line"><span>| **Team** | Team Infrastructure |</span></span>
<span class="line"><span>| **Agent Repo** | [A2A-SIN-Box-Storage](https://github.com/OpenSIN-AI/A2A-SIN-Box-Storage) |</span></span>
<span class="line"><span></span></span>
<span class="line"><span>#### Capabilities</span></span>
<span class="line"><span>- \`storage_upload\` — Upload files to Box.com public folder</span></span>
<span class="line"><span>- \`storage_public_url\` — Return shareable CDN URLs  </span></span>
<span class="line"><span>- \`file_validation\` — Enforce size, type, extension whitelist</span></span>
<span class="line"><span>- \`cdn_distribution\` — Box edge cache integration</span></span>
<span class="line"><span>- \`cache_management\` — ETag, cache-control headers</span></span>
<span class="line"><span></span></span>
<span class="line"><span>#### Box.com Folders</span></span>
<span class="line"><span>| Folder | Shared Link | Folder ID |</span></span>
<span class="line"><span>|--------|-------------|-----------|</span></span>
<span class="line"><span>| \`/Public\` | https://app.box.com/s/1st624o9eb5xdistusew5w0erb8offc7 | \`1st624o9eb5xdistusew5w0erb8offc7\` |</span></span>
<span class="line"><span>| \`/Cache\` | https://app.box.com/s/9s5htoefw1ux9ajaqj656v9a02h7z7x1 | \`9s5htoefw1ux9ajaqj656v9a02h7z7x1\` |</span></span>
<span class="line"><span></span></span>
<span class="line"><span>#### Usage Example</span></span>
<span class="line"><span>\`\`\`bash</span></span>
<span class="line"><span># Upload file via agent</span></span>
<span class="line"><span>curl -X POST &quot;http://room-09-box-storage:3000/api/v1/upload&quot; \\</span></span>
<span class="line"><span>  -H &quot;X-Box-Storage-Key: $BOX_STORAGE_API_KEY&quot; \\</span></span>
<span class="line"><span>  -F &quot;file=@screenshot.png&quot;</span></span>
<span class="line"><span></span></span>
<span class="line"><span># Preflight validation</span></span>
<span class="line"><span>curl -X POST &quot;http://room-09-box-storage:3000/api/v1/validate&quot; \\</span></span>
<span class="line"><span>  -H &quot;Content-Type: application/json&quot; \\</span></span>
<span class="line"><span>  -d &#39;{&quot;filename&quot;:&quot;report.pdf&quot;,&quot;size&quot;:5242880}&#39;</span></span>
<span class="line"><span></span></span>
<span class="line"><span># Health check</span></span>
<span class="line"><span>curl &quot;http://room-09-box-storage:3000/health&quot;</span></span></code></pre></div><h4 id="mcp-integration" tabindex="-1">MCP Integration <a class="header-anchor" href="#mcp-integration" aria-label="Permalink to &quot;MCP Integration&quot;">​</a></h4><p>Agents can access Box Storage via MCP using the <code>sin-box-storage</code> interface:</p><div class="language-json vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">json</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#6A737D;--shiki-dark:#6A737D;">// In opencode.json MCP config</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">{</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">  &quot;mcpServers&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: {</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">    &quot;sin-box-storage&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: {</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">      &quot;command&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&quot;bun&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">,</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">      &quot;args&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: [</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&quot;x&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&quot;@sin-docker/sin-box-storage-mcp&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">]</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    }</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">  }</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">}</span></span></code></pre></div><h4 id="docker-deployment-infra-sin-docker-empire" tabindex="-1">Docker Deployment (Infra-SIN-Docker-Empire) <a class="header-anchor" href="#docker-deployment-infra-sin-docker-empire" aria-label="Permalink to &quot;Docker Deployment (Infra-SIN-Docker-Empire)&quot;">​</a></h4><div class="language-yaml vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">yaml</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">room-09-box-storage</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">  build</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">./services/box-storage</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">  image</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">a2a-sin-box-storage:latest</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">  container_name</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">room-09-box-storage</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">  restart</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">unless-stopped</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">  environment</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    - </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">BOX_DEVELOPER_TOKEN=\${BOX_DEVELOPER_TOKEN}</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    - </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">BOX_PUBLIC_FOLDER_ID=\${BOX_PUBLIC_FOLDER_ID}</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    - </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">BOX_CACHE_FOLDER_ID=\${BOX_CACHE_FOLDER_ID}</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    - </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">API_KEY=\${BOX_STORAGE_API_KEY}</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    - </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">PORT=3000</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">  networks</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">    haus-netzwerk</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">      ipv4_address</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&lt;canonical-box-storage-ip&gt;</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">  ports</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    - </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&quot;3000:3000&quot;</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">  healthcheck</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">    test</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: [</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&quot;CMD&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&quot;curl&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&quot;-f&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&quot;http://127.0.0.1:3000/health&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">]</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">    interval</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">30s</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">    timeout</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">10s</span></span>
<span class="line"><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">    retries</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">3</span></span></code></pre></div><blockquote><p><strong>Migration Note:</strong> A2A-SIN-Box-Storage replaces <code>room-07-gitlab-storage</code>. All agents MUST migrate from <code>gitlab_logcenter.py</code> to Box Storage API. See <a href="/storage/box-cloud-storage.html">Box Cloud Storage Docs</a> for full migration guide.</p></blockquote><hr><h2 id="related" tabindex="-1">Related <a class="header-anchor" href="#related" aria-label="Permalink to &quot;Related&quot;">​</a></h2><ul><li><a href="/governance/overview.html">Governance Overview</a></li><li><a href="/architecture/a2a.html">A2A Architecture</a></li><li><a href="/guide/team-orchestration.html">Team Orchestration</a></li><li><a href="/guide/agent-configuration.html">Agent Configuration</a></li></ul><hr><h2 id="relevante-mandate" tabindex="-1">Relevante Mandate <a class="header-anchor" href="#relevante-mandate" aria-label="Permalink to &quot;Relevante Mandate&quot;">​</a></h2><table tabindex="0"><thead><tr><th>Mandat</th><th>Priority</th><th>Regel</th></tr></thead><tbody><tr><td><strong>A2A-First</strong></td><td>-200.0</td><td>SELBST MACHEN via A2A-Agenten</td></tr><tr><td><strong>LLM via opencode CLI</strong></td><td>-2.5</td><td><code>opencode run --format json</code></td></tr><tr><td><strong>Fleet Architecture V2</strong></td><td>0.0</td><td>marketplace metadata in agent.json</td></tr></tbody></table><p>→ <a href="/best-practices/a2a-communication.html">Alle Mandate</a></p>`,25)])])}const g=a(p,[["render",t]]);export{d as __pageData,g as default};
