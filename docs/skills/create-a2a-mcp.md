# /create-a2a-mcp — Scaffold MCP Servers for A2A Agents

> **Trigger phrases**: "create MCP", "scaffold MCP server", "add MCP to agent", "create-a2a-mcp", "/create-a2a-mcp"
> **Works standalone** AND as an integration hook from `/create-a2a`.

## Purpose

Scaffold a complete, production-ready MCP (Model Context Protocol) server surface for any A2A agent or standalone project. Generates all required files, registers in opencode.json, and validates the result.

## When to Use

| Scenario | How |
|----------|-----|
| Building a new A2A agent | `/create-a2a` calls this skill automatically after base scaffold |
| Adding MCP to an existing agent | Call this skill directly on the agent root |
| Creating a standalone MCP server | Call this skill with a target directory |

## What Gets Scaffolded

```
<agent-root>/
├── src/mcp-server.ts          # MCP server with registerTool() pattern
├── mcp-config.json            # MCP config for local consumers
├── clients/opencode-mcp.json  # OpenCode client config
└── (cli.ts patched)           # serve-mcp command added if missing
```

Plus optionally:
- Global registration in `~/.config/opencode/opencode.json`
- Bin wrapper at `/Users/jeremy/dev/SIN-Solver/bin/sin-<slug>`

## SSOT Paths

| Asset | Path |
|-------|------|
| Template MCP server | `/Users/jeremy/dev/SIN-Solver/a2a/template-repo/A2A-SIN-Agent-Template/src/mcp-server.ts` |
| Template mcp-config | `/Users/jeremy/dev/SIN-Solver/a2a/template-repo/A2A-SIN-Agent-Template/mcp-config.json` |
| Template client config | `/Users/jeremy/dev/SIN-Solver/a2a/template-repo/A2A-SIN-Agent-Template/clients/opencode-mcp.json` |
| Template CLI | `/Users/jeremy/dev/SIN-Solver/a2a/template-repo/A2A-SIN-Agent-Template/src/cli.ts` |
| Global opencode config | `/Users/jeremy/.config/opencode/opencode.json` |
| SIN-Solver bin dir | `/Users/jeremy/dev/SIN-Solver/bin/` |
| Shared lib | `scripts/_mcp-lib.mjs` (this skill) |

## Built-in Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/_mcp-lib.mjs` | Shared helpers (arg parsing, slug normalization, file I/O) | Imported by other scripts |
| `scripts/mcp-scaffold.mjs` | Generate all MCP files from tool definitions | `node mcp-scaffold.mjs --agent-root <path> --slug <name> --tools '<json>'` |
| `scripts/mcp-register-global.mjs` | Register MCP in global opencode.json | `node mcp-register-global.mjs --slug <name> --agent-root <path> [--bin-wrapper]` |
| `scripts/mcp-verify.mjs` | Validate MCP setup completeness | `node mcp-verify.mjs --agent-root <path> --slug <name>` |

## Workflow

### Step 0 — Gather Input

Collect from user or from `/create-a2a` handoff:

| Parameter | Required | Description |
|-----------|----------|-------------|
| `agent-root` | ✅ | Absolute path to agent/project root |
| `slug` | ✅ | MCP slug (e.g. `sin-research`, `sin-server`) |
| `namespace` | ❌ | Tool namespace prefix (defaults to slug with `-` → `_`) |
| `tools` | ❌ | JSON array of tool definitions (see format below) |
| `register-global` | ❌ | Register in opencode.json (default: true) |
| `bin-wrapper` | ❌ | Create bin wrapper in SIN-Solver/bin/ (default: false) |
| `env-vars` | ❌ | JSON object of environment variables for MCP config |

### Step 1 — Run Scaffold

```bash
SCRIPTS=~/.config/opencode/skills/create-a2a-mcp/scripts
node $SCRIPTS/mcp-scaffold.mjs \
  --agent-root /path/to/agent \
  --slug sin-myagent \
  --tools '[{"name":"do_thing","description":"Does a thing","params":{"input":"string"},"action":"myagent.do_thing"}]'
```

This generates:
- `src/mcp-server.ts` — Full MCP server with all tools registered via `McpServer.registerTool()`
- `mcp-config.json` — Local MCP config
- `clients/opencode-mcp.json` — OpenCode client config
- Patches `src/cli.ts` to include `serve-mcp` command if missing

### Step 2 — Register Globally (Optional)

```bash
node $SCRIPTS/mcp-register-global.mjs \
  --slug sin-myagent \
  --agent-root /path/to/agent \
  --bin-wrapper
```

### Step 3 — Verify

```bash
node $SCRIPTS/mcp-verify.mjs \
  --agent-root /path/to/agent \
  --slug sin-myagent
```

Expected output: all checks green.

### Step 4 — Build & Smoke Test

```bash
npm --prefix <agent-root> run build
echo '{}' | node <agent-root>/dist/src/cli.js serve-mcp
# Should start without errors and respond to MCP protocol
```

## Tool Definition Format

Each tool in the `--tools` JSON array:

```json
{
  "name": "do_thing",
  "description": "Does a specific thing",
  "params": {
    "input": "string",
    "count": "number?",
    "confirm": "boolean?"
  },
  "action": "myagent.do_thing"
}
```

**Type mapping:**
- `string` → `z.string()` (required)
- `string?` → `z.string().optional()` (optional)
- `number` → `z.number()` (required)
- `number?` → `z.number().optional()` (optional)
- `boolean` → `z.boolean()` (required)
- `boolean?` → `z.boolean().optional()` (optional)
- `array` → `z.array(z.string())` (required)
- `array?` → `z.array(z.string()).optional()` (optional)

## Default Tools (Always Generated)

Every MCP server gets these baseline tools automatically:

1. `<namespace>_help` — Describe available agent actions
2. `<namespace>_health` — Check base agent readiness
3. `<namespace>_onboarding_status` — Read onboarding state
4. `<namespace>_onboarding_save` — Persist onboarding state (requires `confirm=true`)

## Integration with /create-a2a

When called from `/create-a2a`, the handoff contract is:

```json
{
  "agent-root": "/absolute/path/to/agent",
  "slug": "sin-agentname",
  "namespace": "sin_agentname",
  "tools": [...],
  "register-global": true,
  "bin-wrapper": true,
  "env-vars": { "KEY": "value" }
}
```

The `/create-a2a` SKILL.md should include this step after base scaffold:

```markdown
### MCP Surface Generation
After scaffolding the base agent, invoke skill `create-a2a-mcp` to generate the MCP server surface.
Pass the agent-root, slug, and domain-specific tool definitions.
```

## MCP Server Pattern Reference

### Production Pattern (McpServer.registerTool — PREFERRED)

```typescript
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';

const server = new McpServer({ name: 'sin-myagent', version: '0.1.0' });

server.registerTool('sin_myagent_help',
  { description: 'Describe available actions.' },
  async () => ({
    content: [{ type: 'text', text: JSON.stringify(result, null, 2) }],
  })
);

const transport = new StdioServerTransport();
await server.connect(transport);
```

### Transport Modes

| Mode | When | Config |
|------|------|--------|
| **stdio** | Local agents, opencode CLI | Default. Always use for A2A agents. |
| **streamable-http** | Remote/cloud agents | Only if agent runs on remote VM |
| **SSE** | Legacy | DEPRECATED. Never use for new agents. |

## Anti-Patterns

❌ Template name drift — always replace `template-a2a-sin-agent` with actual slug
❌ Missing `serve-mcp` in CLI — breaks opencode integration
❌ Business logic in mcp-server.ts — keep it thin, delegate to runtime.ts
❌ Hardcoded paths in mcp-config.json — use relative paths for portability
❌ SSE transport for new projects — use stdio or streamable-http
❌ Shared mutable server state across clients — fresh handler per call

## Checklist

- [ ] `src/mcp-server.ts` exists with all tools registered
- [ ] `mcp-config.json` exists with correct slug
- [ ] `clients/opencode-mcp.json` exists with correct slug
- [ ] `src/cli.ts` has `serve-mcp` command
- [ ] No template name drift (no `template-a2a-sin-agent` references)
- [ ] Global opencode.json registration (if requested)
- [ ] Bin wrapper created (if requested)
- [ ] `npm run build` succeeds
- [ ] `serve-mcp` starts without errors
- [ ] All default tools respond (help, health, onboarding)
