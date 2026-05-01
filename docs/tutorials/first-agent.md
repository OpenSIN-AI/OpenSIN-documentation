# Tutorial: Create Your First Agent

## Prerequisites

- Node.js 20+
- OpenCode CLI installed
- GitHub account

## Step 1: Install OpenCode

```bash
curl -fsSL https://opencode.ai/install | bash
```

## Step 2: Install the Upgraded Stack

```bash
git clone https://github.com/Delqhi/upgraded-opencode-stack.git
cd upgraded-opencode-stack
./install.sh
```

## Step 3: Create an Agent

```bash
opencode agent create my-agent --model openai/gpt-5.4
```

## Step 4: Run Your Agent

```bash
opencode run --agent my-agent "Hello, world!"
```

## Step 5: Add Tools

```bash
# Install plugins
bun add -g @opensin/plugin-context-pruning
bun add -g @opensin/plugin-envsitter
bun add -g @opensin/plugin-safety-net
```

## Next Steps

- Read the [Plugin System Guide](../guide/plugin-system.md)
- Explore the [A2A Protocol](../guide/a2a-protocol.md)
- Check the [API Reference](../api/index.md)

---

## Relevante Mandate

| Mandat                   | Priority | Doku                                                    |
| ------------------------ | -------- | ------------------------------------------------------- |
| **Bun-Only**             | -1.5     | `bun install` / `bun run` statt npm                     |
| **LLM via opencode CLI** | -2.5     | `opencode run --format json` — KEINE direkten API-Calls |
| **A2A-Agenten-Pflicht**  | -200.0   | SELBST MACHEN via `create-a2a-sin-agent`                |
| **Kommentar-Pflicht**    | -6.0     | EXTREM umfangreiche Kommentare                          |

→ [Alle Mandate](/best-practices/a2a-communication)
