# API Reference

OpenCode provides a comprehensive CLI API for programmatic access.

## CLI Commands

### `opencode run [message]`

Run OpenCode with a message.

```bash
opencode run "Create a REST API with Express"
opencode run --agent researcher "Research AI trends"
opencode run --model openai/gpt-5.4 "Write unit tests"
```

**Options:**
| Flag | Description | Default |
|------|-------------|---------|
| `--agent` | Agent to use | `general` |
| `--model` | Model to use | Config default |
| `--format` | Output format (text, json) | `text` |
| `--pure` | Run without external plugins | `false` |

### `opencode session list`

List all sessions.

```bash
opencode session list -n 10
```

### `opencode export [sessionID]`

Export session data as JSON.

```bash
opencode export ses_abc123 > session.json
```

### `opencode import <file>`

Import session data.

```bash
opencode import session.json
```

### `opencode agent create <name>`

Create a new agent.

```bash
opencode agent create researcher --model openai/gpt-5.4
opencode agent list
```

### `opencode providers`

Manage AI providers.

```bash
opencode providers
opencode providers add openai
```

### `opencode mcp`

Manage MCP servers.

```bash
opencode mcp list
opencode mcp add filesystem --command bunx @modelcontextprotocol/server-filesystem /path
```

### `opencode stats`

Show token usage and cost statistics.

```bash
opencode stats
```

### `opencode upgrade [target]`

Upgrade OpenCode.

```bash
opencode upgrade
opencode upgrade 1.2.3
```

### `opencode github`

Manage GitHub integration.

```bash
opencode github setup
opencode pr 42
```

### `opencode serve`

Start headless server.

```bash
opencode serve --port 3000
```

### `opencode web`

Start web interface.

```bash
opencode web
```

### `opencode debug`

Debugging tools.

```bash
opencode debug
```

### `opencode uninstall`

Uninstall OpenCode.

```bash
opencode uninstall
opencode uninstall --keep-config
opencode uninstall --keep-data
```

## ACP (Agent Client Protocol)

```bash
opencode acp
```

Start the ACP server for programmatic agent interaction.

## Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENCODE_MODEL` | Default model |
| `OPENCODE_AGENT` | Default agent |
| `OPENCODE_HOME` | Custom home directory |
| `OPENCODE_CONFIG_DIR` | Custom config directory |
| `OPENCODE_CACHE_DIR` | Custom cache directory |

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
