# 🚨 AGENTS.md Mandate — Full Audit & Remediation Plan

**Issue:** [#95](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/95)
**Date:** 2026-04-14
**Severity:** CRITICAL
**Status:** In Progress

---

## Executive Summary

**20 of 100 repositories** (20%) in the OpenSIN-AI organization are missing `AGENTS.md` — the fundamental operating manual for every A2A agent. This is a **critical compliance violation** of the Global Agentic Paradigm.

Without `AGENTS.md`, agents are **dead endpoints**: other agents cannot discover their capabilities, understand their auth model, or know how to interact with them.

---

## Full Audit Table

| # | Repo | README | AGENTS.md | Priority | Action Required |
|---|------|--------|-----------|----------|-----------------|
| 1 | MCP-SIN-chrome-extension | ❌ | ❌ | **CRITICAL** | Create README + AGENTS.md |
| 2 | MCP-SIN-computer-use | ❌ | ❌ | **CRITICAL** | Create README + AGENTS.md |
| 3 | MCP-SIN-mcp-gateway | ❌ | ❌ | **CRITICAL** | Create README + AGENTS.md |
| 4 | MCP-SIN-in-chrome | ❌ | ❌ | **CRITICAL** | Create README + AGENTS.md |
| 5 | MCP-SIN-memory | ❌ | ❌ | **CRITICAL** | Create README + AGENTS.md |
| 6 | MCP-SIN-platform-auth | ❌ | ❌ | **CRITICAL** | Create README + AGENTS.md |
| 7 | MCP-SIN-usebrowser | ❌ | ❌ | **CRITICAL** | Create README + AGENTS.md |
| 8 | OpenSIN-Neural-Bus | ✅ | ❌ | **HIGH** | Create AGENTS.md |
| 9 | opensin-ai-code | ✅ | ❌ | **HIGH** | Create AGENTS.md |
| 10 | opensin-ai-platform | ✅ | ❌ | **HIGH** | Create AGENTS.md |
| 11 | sin-github-action | ✅ | ❌ | **MEDIUM** | Create AGENTS.md |
| 12 | A2A-SIN-Worker-heypiggy | ✅ | ❌ | **MEDIUM** | Create AGENTS.md |
| 13 | A2A-SIN-Medusa | ✅ | ❌ | **MEDIUM** | Create AGENTS.md |
| 14 | Template-SIN-Team | ✅ | ❌ | **MEDIUM** | Create AGENTS.md |
| 15 | OpenSIN-overview | ✅ | ❌ | **MEDIUM** | Create AGENTS.md |
| 16 | SIN-InkogniFlow | ✅ | ❌ | **MEDIUM** | Create AGENTS.md |
| 17 | Biz-SIN-Marketing | ✅ | ❌ | **MEDIUM** | Create AGENTS.md |
| 18 | A2A-SIN-Storage | ✅ | ❌ | **LOW** | Create AGENTS.md |
| 19 | A2A-SIN-Medium | ✅ | ❌ | **LOW** | Create AGENTS.md |
| 20 | A2A-SIN-YouTube | ✅ | ❌ | **LOW** | Create AGENTS.md |
| 21 | A2A-SIN-TikTok | ✅ | ❌ | **LOW** | Create AGENTS.md |

---

## CRITICAL: AGENTS.md Drafts for MCP Servers

### 1. MCP-SIN-chrome-extension

```markdown
# MCP-SIN-chrome-extension

## Identity
- **Name:** MCP-SIN-chrome-extension
- **Type:** MCP Server
- **Organization:** OpenSIN-AI
- **Namespace:** sin-chrome-extension

## Purpose
Chrome Extension bridge for browser automation. Provides tools to interact with Chrome extensions, manage extension state, and bridge between MCP clients and Chrome DevTools Protocol (CDP). This server acts as the gateway between AI agents and Chrome extension APIs.

## Auth Model
- **Local:** localhost CDP connection (port 9335 default)
- **Remote:** streamable-http with optional API key
- **Chrome Profile:** Uses user's default Chrome profile with existing sessions
- **Security:** Extension permission model enforced by Chrome

## Available Tools
| Tool | Parameters | Description |
|------|-----------|-------------|
| `get_extension_state` | `extension_id: string` | Get current state of a Chrome extension |
| `list_extensions` | `enabled_only?: boolean` | List all installed Chrome extensions |
| `execute_extension_action` | `extension_id: string, action: string, args?: object` | Execute an action on a Chrome extension |
| `inject_content_script` | `extension_id: string, script: string, matches: string[]` | Inject content script via extension |
| `get_extension_permissions` | `extension_id: string` | Get permissions granted to an extension |
| `bridge_cdp_command` | `command: string, params?: object` | Send CDP command through extension bridge |

## Commands
```bash
# Start MCP server (stdio mode)
node dist/index.js

# Start MCP server (streamable-http mode)
node dist/index.js --port 8765

# Health check
curl http://localhost:8765/health
```

## Endpoints
- **stdio:** Standard input/output (default)
- **streamable-http:** `http://localhost:8765/mcp`

## Dependencies
- Chrome browser with remote debugging enabled
- OpenSIN Chrome extension installed
- Node.js >= 18

## Lifecycle
- **Start:** Connects to Chrome via CDP on configured port
- **Running:** Listens for MCP tool calls, forwards to Chrome extension API
- **Error:** Chrome disconnected → auto-reconnect with exponential backoff
- **Shutdown:** Graceful CDP disconnect, cleanup

## Observability
- Health endpoint: `GET /health`
- Logs: stdout with JSON structured logging
- Metrics: CDP connection status, tool call counts, error rates
```

### 2. MCP-SIN-computer-use

```markdown
# MCP-SIN-computer-use

## Identity
- **Name:** MCP-SIN-computer-use
- **Type:** MCP Server
- **Organization:** OpenSIN-AI
- **Namespace:** sin-computer-use

## Purpose
Desktop computer control and automation. Provides screen capture, mouse/keyboard control, window management, and file system operations for full computer automation. Enables AI agents to interact with the desktop environment like a human user.

## Auth Model
- **Local:** Direct OS access (requires accessibility permissions on macOS)
- **Remote:** NOT recommended for security reasons
- **Permissions:** macOS Accessibility + Screen Recording permissions required

## Available Tools
| Tool | Parameters | Description |
|------|-----------|-------------|
| `screenshot` | `region?: {x,y,width,height}, format?: "png"|"jpeg"` | Capture screen or region |
| `mouse_move` | `x: number, y: number` | Move mouse to coordinates |
| `mouse_click` | `x: number, y: number, button?: "left"|"right"` | Click at coordinates |
| `mouse_drag` | `from: {x,y}, to: {x,y}` | Drag from one point to another |
| `keyboard_type` | `text: string` | Type text via keyboard |
| `keyboard_press` | `key: string` | Press a specific key (Enter, Tab, etc.) |
| `keyboard_shortcut` | `keys: string[]` | Press keyboard shortcut (Cmd+C, etc.) |
| `get_window_list` | `include_hidden?: boolean` | List all open windows |
| `focus_window` | `window_id: string \| title: string` | Bring window to foreground |
| `get_clipboard` | - | Get clipboard content |
| `set_clipboard` | `text: string` | Set clipboard content |
| `file_read` | `path: string` | Read file from filesystem |
| `file_write` | `path: string, content: string` | Write file to filesystem |

## Commands
```bash
# Start MCP server
node dist/index.js

# Health check
curl http://localhost:PORT/health
```

## Endpoints
- **stdio:** Standard input/output (default)
- **streamable-http:** `http://localhost:PORT/mcp`

## Dependencies
- macOS Accessibility permission granted
- macOS Screen Recording permission granted
- Node.js >= 18
- puppeteer/screen-capture-capture (platform-specific)

## Lifecycle
- **Start:** Verifies OS permissions, initializes input controllers
- **Running:** Processes tool calls for screen/keyboard/mouse operations
- **Error:** Permission denied → halt and report to operator
- **Shutdown:** Release input controllers, cleanup

## Observability
- Health endpoint: `GET /health`
- Logs: All screen/mouse/keyboard actions logged with timestamps
- Security: All file operations logged for audit trail
```

### 3. MCP-SIN-mcp-gateway

```markdown
# MCP-SIN-mcp-gateway

## Identity
- **Name:** MCP-SIN-mcp-gateway
- **Type:** MCP Server
- **Organization:** OpenSIN-AI
- **Namespace:** sin-mcp-gateway

## Purpose
Multi-MCP server gateway and router. Aggregates multiple MCP servers behind a single unified endpoint, provides load balancing, service discovery, and intelligent request routing. Acts as the central nervous system for MCP communication in the OpenSIN ecosystem.

## Auth Model
- **Local:** No auth (localhost only)
- **Remote:** Bearer token authentication configurable per upstream
- **Upstream Auth:** Passes through auth headers to target MCP servers

## Available Tools
| Tool | Parameters | Description |
|------|-----------|-------------|
| `list_servers` | - | List all registered MCP servers |
| `register_server` | `name: string, url: string, tools?: string[]` | Register a new MCP server |
| `unregister_server` | `name: string` | Remove an MCP server from the gateway |
| `route_tool_call` | `server: string, tool: string, args: object` | Route a tool call to specific server |
| `broadcast_tool_call` | `tool: string, args: object` | Send tool call to all registered servers |
| `get_server_health` | `name: string` | Check health of a specific MCP server |
| `get_server_tools` | `name: string` | List available tools for a specific server |
| `discover_servers` | `network?: string` | Auto-discover MCP servers on network |

## Commands
```bash
# Start gateway
node dist/index.js --port 8765

# With config file
node dist/index.js --config gateway-config.json

# Health check
curl http://localhost:8765/health
```

## Endpoints
- **Main:** `http://localhost:8765/mcp`
- **Health:** `http://localhost:8765/health`
- **Admin:** `http://localhost:8765/admin`

## Dependencies
- Node.js >= 18
- MCP servers to route to (registered at startup or runtime)
- Optional: etcd/Redis for service discovery

## Lifecycle
- **Start:** Load registered servers from config, health check all upstreams
- **Running:** Route tool calls, monitor upstream health, auto-discover new servers
- **Error:** Upstream down → mark unhealthy, reroute if possible, alert operator
- **Shutdown:** Graceful drain, close all upstream connections

## Observability
- Health endpoint: `GET /health`
- Admin panel: `GET /admin` (server list, health status, tool catalog)
- Metrics: Request routing stats, upstream latency, error rates per server
```

### 4. MCP-SIN-in-chrome

```markdown
# MCP-SIN-in-chrome

## Identity
- **Name:** MCP-SIN-in-chrome
- **Type:** MCP Server
- **Organization:** OpenSIN-AI
- **Namespace:** sin-in-chrome

## Purpose
MCP server running inside Chrome browser context via content script / extension. Provides direct DOM access, JavaScript execution, page state monitoring, and browser-internal automation. Unlike CDP-based tools, this runs AS the page, giving native access to the DOM and JavaScript runtime.

## Auth Model
- **Browser:** Runs as Chrome extension content script (inherits extension permissions)
- **External:** Communicates via Chrome extension messaging API
- **Security:** Origin-restricted by extension manifest

## Available Tools
| Tool | Parameters | Description |
|------|-----------|-------------|
| `get_dom` | `selector?: string, include_styles?: boolean` | Get DOM structure |
| `execute_js` | `script: string` | Execute JavaScript in page context |
| `get_page_state` | - | Get current page URL, title, load state |
| `get_cookies` | `domain?: string` | Get cookies for current domain |
| `set_cookies` | `cookies: [{name, value, domain, path}]` | Set cookies in browser |
| `get_local_storage` | `key?: string` | Get localStorage entries |
| `get_session_storage` | `key?: string` | Get sessionStorage entries |
| `wait_for_element` | `selector: string, timeout?: number` | Wait for element to appear |
| `get_accessibility_tree` | - | Get accessibility tree for screen reader |
| `intercept_network` | `pattern: string` | Intercept and log network requests |
| `fill_form` | `selector: string, value: string` | Fill form field by selector |
| `get_text_content` | `selector: string` | Get text content of element |

## Commands
```bash
# This MCP runs inside Chrome as an extension
# Start via Chrome extension loading:
# 1. chrome://extensions → Developer mode
# 2. Load unpacked → point to extension directory
# 3. Extension connects to local MCP bridge automatically
```

## Endpoints
- **Internal:** Chrome extension messaging (no external endpoint)
- **Bridge:** Connects to local MCP bridge via native messaging host

## Dependencies
- Chrome browser
- OpenSIN Chrome Extension loaded
- Native messaging host configured

## Lifecycle
- **Start:** Extension loads, injects content script, connects to bridge
- **Running:** Receives tool calls via messaging, executes in page context, returns results
- **Error:** Page navigated → re-inject content script, reconnect
- **Shutdown:** Extension unloaded, cleanup listeners

## Observability
- Console logging via extension background page
- Network interception logs
- DOM mutation tracking
```

### 5. MCP-SIN-memory

```markdown
# MCP-SIN-memory

## Identity
- **Name:** MCP-SIN-memory
- **Type:** MCP Server
- **Organization:** OpenSIN-AI
- **Namespace:** sin-memory

## Purpose
Persistent memory and context storage for AI agents. Provides long-term memory, semantic search over stored context, conversation history, knowledge retrieval, and cross-session context sharing. This is the "hippocampus" of the OpenSIN agent fleet.

## Auth Model
- **Local:** File-based storage with user-scoped directories
- **Remote:** Supabase-backed with JWT authentication
- **Encryption:** AES-256 for sensitive memory entries
- **Access:** Agent-scoped — each agent can only access its own memory namespace

## Available Tools
| Tool | Parameters | Description |
|------|-----------|-------------|
| `store_memory` | `namespace: string, key: string, value: string, tags?: string[]` | Store a memory entry |
| `retrieve_memory` | `namespace: string, key: string` | Retrieve a specific memory |
| `search_memory` | `namespace: string, query: string, limit?: number` | Semantic search in memory |
| `list_memories` | `namespace: string, tags?: string[]` | List all memories in namespace |
| `delete_memory` | `namespace: string, key: string` | Delete a memory entry |
| `update_memory` | `namespace: string, key: string, value: string` | Update existing memory |
| `get_conversation_history` | `session_id: string, limit?: number` | Get conversation history |
| `store_conversation` | `session_id: string, messages: array` | Store conversation messages |
| `get_agent_context` | `agent_name: string` | Get all context for an agent |
| `cross_reference` | `query: string, namespaces: string[]` | Search across multiple namespaces |

## Commands
```bash
# Start with local storage
node dist/index.js --storage local --path ~/.opensin/memory

# Start with Supabase storage
node dist/index.js --storage supabase --url SUPABASE_URL --key SUPABASE_KEY

# Health check
curl http://localhost:PORT/health
```

## Endpoints
- **stdio:** Standard input/output (default)
- **streamable-http:** `http://localhost:PORT/mcp`

## Dependencies
- Node.js >= 18
- Local: filesystem access
- Supabase (optional): Supabase project with memory tables
- Embedding model (for semantic search): OpenAI or local model

## Lifecycle
- **Start:** Initialize storage backend, load indexes, warm cache
- **Running:** Process store/retrieve/search operations, maintain indexes
- **Error:** Storage unavailable → fallback to local cache, alert operator
- **Shutdown:** Flush pending writes, close connections

## Observability
- Health endpoint: `GET /health`
- Metrics: Storage operations/sec, search latency, cache hit rate
- Memory usage: Track total stored entries per namespace
```

### 6. MCP-SIN-platform-auth

```markdown
# MCP-SIN-platform-auth

## Identity
- **Name:** MCP-SIN-platform-auth
- **Type:** MCP Server
- **Organization:** OpenSIN-AI
- **Namespace:** sin-platform-auth

## Purpose
Platform authentication bridge for OAuth flows, token rotation, credential management, and secure auth state across multiple platforms (Google, OpenAI, GitHub, etc.). Centralizes authentication logic so individual agents don't need to implement auth themselves.

## Auth Model
- **Master Auth:** Encrypted credential store (keychain / encrypted file)
- **Platform Auth:** Per-platform OAuth2/OIDC flows
- **Token Rotation:** Automatic token refresh before expiry
- **Secrets:** Never logs or exposes raw tokens

## Available Tools
| Tool | Parameters | Description |
|------|-----------|-------------|
| `authenticate` | `platform: string, method?: "oauth"|"api_key"` | Initiate auth for a platform |
| `get_token` | `platform: string` | Get valid access token (auto-refreshes) |
| `refresh_token` | `platform: string` | Manually refresh a token |
| `revoke_token` | `platform: string` | Revoke access for a platform |
| `list_platforms` | - | List all configured platforms |
| `add_platform` | `platform: string, config: object` | Add new platform credentials |
| `remove_platform` | `platform: string` | Remove platform configuration |
| `get_auth_status` | `platform: string` | Check auth status for a platform |
| `oauth_callback` | `code: string, state: string` | Handle OAuth callback |
| `validate_token` | `platform: string, token: string` | Validate a token's freshness |

## Commands
```bash
# Start auth server
node dist/index.js --port 8765

# Initialize credential store
node dist/index.js --init-store

# Health check
curl http://localhost:8765/health
```

## Endpoints
- **Main:** `http://localhost:8765/mcp`
- **OAuth Callback:** `http://localhost:8765/oauth/callback`
- **Health:** `http://localhost:8765/health`

## Dependencies
- Node.js >= 18
- Encrypted credential store (keychain or encrypted file)
- Platform-specific OAuth client IDs/secrets
- Browser automation (for OAuth flows without headless)

## Lifecycle
- **Start:** Load credential store, check token freshness, schedule refresh jobs
- **Running:** Handle auth requests, auto-refresh tokens before expiry
- **Error:** Token expired + refresh failed → mark platform as auth_required, alert operator
- **Shutdown:** Cancel refresh timers, save state

## Observability
- Health endpoint: `GET /health`
- Auth status: `GET /health` includes per-platform auth status
- Audit log: All token operations logged (without exposing token values)
- Alerts: Refresh failures, auth expirations
```

### 7. MCP-SIN-usebrowser

```markdown
# MCP-SIN-usebrowser

## Identity
- **Name:** MCP-SIN-usebrowser
- **Type:** MCP Server
- **Organization:** OpenSIN-AI
- **Namespace:** sin-usebrowser

## Purpose
High-level browser automation wrapper providing simplified API over nodriver/CDP. Offers navigation, clicking, typing, screenshot capture, and form filling through an intuitive tool interface. Abstracts away the complexity of direct CDP/nodriver interaction for AI agents.

## Auth Model
- **Local:** Uses Chrome's default profile with existing sessions
- **CDP Port:** 9335 (default, configurable)
- **Profile:** `/Users/jeremy/Library/Application Support/Google/Chrome/Default`
- **Sessions:** Inherits all logged-in sessions from Chrome profile

## Available Tools
| Tool | Parameters | Description |
|------|-----------|-------------|
| `navigate` | `url: string` | Navigate to URL |
| `screenshot` | `full_page?: boolean, path?: string` | Take screenshot |
| `click_element` | `selector: string \| x: number, y: number` | Click element |
| `type_text` | `selector: string, text: string` | Type text into element |
| `get_text` | `selector: string` | Get text content of element |
| `get_html` | `selector?: string` | Get HTML of element or page |
| `get_links` | `include_hidden?: boolean` | Get all links on page |
| `fill_form` | `fields: {selector: string, value: string}[]` | Fill multiple form fields |
| `submit_form` | `selector?: string` | Submit form |
| `wait_for` | `selector: string, timeout?: number` | Wait for element |
| `execute_js` | `script: string` | Execute JavaScript on page |
| `get_cookies` | `domain?: string` | Get browser cookies |
| `scroll` | `direction: "up"|"down", amount?: number` | Scroll page |
| `select_option` | `selector: string, value: string` | Select dropdown option |

## Commands
```bash
# Start browser automation server
node dist/index.js --cdp-port 9335

# With custom Chrome profile
node dist/index.js --profile "Default" --cdp-port 9335

# Health check
curl http://localhost:PORT/health
```

## Endpoints
- **stdio:** Standard input/output (default)
- **streamable-http:** `http://localhost:PORT/mcp`

## Dependencies
- Chrome browser with remote debugging (`--remote-debugging-port=9335`)
- nodriver Python package (for browser control)
- Node.js >= 18

## Lifecycle
- **Start:** Launch Chrome with CDP, initialize browser context
- **Running:** Process automation tool calls, maintain browser state
- **Error:** Browser crashed → restart Chrome, restore session if possible
- **Shutdown:** Close browser, cleanup temp files

## Observability
- Health endpoint: `GET /health` (includes browser status)
- Logs: All automation actions logged with before/after state
- Screenshots: Auto-captured on errors for debugging
- Performance: Action timing, page load times
```

---

## Step-by-Step Remediation Plan

### Phase 1: CRITICAL — MCP Servers (Week 1)
1. Create AGENTS.md for all 7 MCP servers (drafts above)
2. Create README.md for all 7 MCP servers (see separate MCP README audit)
3. Add GitHub topics: `opnsin-mcp` to all MCP repos
4. Verify each MCP server can be started and health-checked

### Phase 2: HIGH — Core Infrastructure (Week 2)
1. Create AGENTS.md for OpenSIN-Neural-Bus
2. Create AGENTS.md for opensin-ai-code
3. Create AGENTS.md for opensin-ai-platform
4. Add GitHub topics: `opnsin-agent` to all agent repos

### Phase 3: MEDIUM — Worker & Team Agents (Week 3)
1. Create AGENTS.md for remaining 7 medium-priority repos
2. Verify A2A card and `.well-known` endpoints where applicable
3. Sync all changes via `sin-sync` to OCI VM and HF VMs

### Phase 4: LOW — Utility Agents (Week 4)
1. Create AGENTS.md for remaining 3 low-priority repos
2. Final audit: verify 0 repos missing AGENTS.md
3. Enable automated repo health check (Issue #98)

---

## Compliance Checklist

- [ ] All 20 repos have AGENTS.md
- [ ] All 7 MCP servers have README.md + AGENTS.md
- [ ] All agent repos have `opnsin-agent` topic
- [ ] All MCP repos have `opnsin-mcp` topic
- [ ] All changes synced via `sin-sync`
- [ ] Automated health check enabled (Issue #98)

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
