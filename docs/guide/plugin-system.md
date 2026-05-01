# Plugin System

OpenCode's plugin system extends the CLI with custom commands, agents, skills, and hooks.

## Plugin Architecture

```
my-plugin/
├── package.json          # Plugin metadata and dependencies
├── src/
│   ├── index.ts          # Plugin entry point
│   ├── commands/         # Custom slash commands
│   ├── agents/           # Custom agent definitions
│   ├── skills/           # Custom skill definitions
│   └── hooks/            # Lifecycle hooks
└── README.md
```

## Creating a Plugin

### 1. Initialize

```bash
mkdir my-plugin && cd my-plugin
npm init -y
npm install opencode
```

### 2. package.json

```json
{
  "name": "opencode-plugin-my-plugin",
  "version": "0.1.0",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "opencode": {
    "plugin": true,
    "commands": ["./dist/commands/index.js"],
    "agents": ["./dist/agents/index.js"],
    "skills": ["./dist/skills/index.js"]
  }
}
```

### 3. Install

```bash
npm install -g opencode-plugin-my-plugin
```

Or add to `opencode.json`:

```json
{
  "plugin": ["opencode-plugin-my-plugin"]
}
```

## Available Hooks

| Hook               | Trigger                             |
| ------------------ | ----------------------------------- |
| `PreToolUse`       | Before a tool is executed           |
| `PostToolUse`      | After a tool is executed            |
| `UserPromptSubmit` | Before user prompt is sent to model |
| `Stop`             | When session ends                   |

## Example: Custom Command

```typescript
import { defineCommand } from "opencode/plugin";

export const myCommand = defineCommand({
  name: "my-command",
  description: "My custom command",
  handler: async (context, args) => {
    // Command logic
    return { output: "Result" };
  },
});
```

## Example: Custom Agent

```typescript
import { defineAgent } from "opencode/plugin";

export const myAgent = defineAgent({
  name: "my-agent",
  description: "My custom agent",
  model: "openai/gpt-5.4",
  systemPrompt: "You are a helpful assistant.",
  tools: ["read", "write", "bash"],
});
```

## Plugin Registry

| Plugin                      | Description                                      | Install                                         |
| --------------------------- | ------------------------------------------------ | ----------------------------------------------- |
| `oh-my-opencode`            | Multi-agent orchestration framework              | `npm i -g oh-my-opencode`                       |
| `opencode-antigravity-auth` | OAuth token rotation for Claude/Gemini           | `npm i -g opencode-antigravity-auth`            |
| `opencode-qwen-proxy`       | OpenCode-Qwen-Proxy (Qwen OAuth with throttling) | `npm i -g github:RunMintOn/OpenCode-Qwen-Proxy` |
| `opencode-openrouter-auth`  | OpenRouter auth with local proxy                 | Local source in upgraded-opencode-stack         |

## Best Practices

1. **Namespace your plugin** — Use `opencode-plugin-*` prefix
2. **Keep it focused** — One plugin, one responsibility
3. **Document everything** — Include README with usage examples
4. **Test thoroughly** — Include unit tests for commands and agents
5. **Version properly** — Use semantic versioning
