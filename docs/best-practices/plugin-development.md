---
title: "Plugin Development Best Practices"
---

# Plugin Development Best Practices

Guidelines for building robust, maintainable OpenSIN plugins that extend the CLI with commands, agents, skills, and hooks.

## Plugin Structure

### Standard Layout

```
opencode-plugin-my-plugin/
├── package.json
├── tsconfig.json
├── src/
│   ├── index.ts           # Main entry point
│   ├── commands/          # Slash commands
│   │   ├── index.ts       # Command exports
│   │   └── my-command.ts  # Individual command
│   ├── agents/            # Agent definitions
│   │   └── index.ts
│   ├── skills/            # Skill definitions
│   │   └── index.ts
│   └── hooks/             # Lifecycle hooks
│       └── index.ts
├── tests/
│   └── plugin.test.ts
└── README.md
```

### Package.json

```json
{
  "name": "opencode-plugin-my-plugin",
  "version": "1.0.0",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "opencode": {
    "plugin": true,
    "commands": ["./dist/commands/index.js"],
    "agents": ["./dist/agents/index.js"],
    "skills": ["./dist/skills/index.js"],
    "hooks": ["./dist/hooks/index.js"]
  },
  "peerDependencies": {
    "opencode": ">=1.0.0"
  }
}
```

## Commands

### Command Definition

```typescript
import { defineCommand } from 'opencode/plugin'

export const myCommand = defineCommand({
  name: 'my-command',
  description: 'Execute my custom operation',
  parameters: {
    target: {
      type: 'string',
      description: 'Target to process',
      required: true,
    },
    verbose: {
      type: 'boolean',
      description: 'Enable verbose output',
      default: false,
    },
  },
  handler: async (context, args) => {
    const { target, verbose } = args

    if (verbose) {
      context.log(`Processing target: ${target}`)
    }

    const result = await processTarget(target)

    return {
      status: 'success',
      result,
    }
  },
})
```

### Command Best Practices

- **Validate inputs early** — Fail fast with clear error messages
- **Provide progress feedback** — Use `context.log()` for long operations
- **Return structured output** — Always return objects, not raw strings
- **Handle errors gracefully** — Catch and format errors for the user

## Agents

### Agent Definition

```typescript
import { defineAgent } from 'opencode/plugin'

export const researcherAgent = defineAgent({
  name: 'researcher',
  description: 'Expert research agent with web search capabilities',
  model: 'claude-sonnet-4-6',
  systemPrompt: `You are an expert researcher. Provide detailed, well-sourced reports with citations. Always verify facts from multiple sources.`,
  tools: ['read', 'write', 'bash', 'web_search', 'web_fetch'],
  maxTurns: 30,
  contextWindow: 128_000,
})
```

### Agent Best Practices

- **Single responsibility** — One agent, one purpose
- **Specific system prompts** — Avoid generic "helpful assistant" prompts
- **Minimal tool set** — Only enable necessary tools
- **Appropriate model** — Match model capability to task complexity

## Skills

### Skill Definition

```typescript
import { defineSkill } from 'opencode/plugin'

export const codeReviewSkill = defineSkill({
  name: 'code-review',
  description: 'Review code for quality, security, and best practices',
  trigger: /review|code quality|lint/i,
  instructions: `When reviewing code:
1. Check for security vulnerabilities
2. Verify error handling
3. Assess performance implications
4. Check naming and style consistency
5. Suggest improvements with examples`,
  context: {
    files: ['*.ts', '*.tsx', '*.js', '*.jsx'],
    scope: 'document',
  },
})
```

## Hooks

### Lifecycle Hooks

```typescript
import { defineHook } from 'opencode/plugin'

export const securityHook = defineHook({
  name: 'security-guidance',
  events: ['PreToolUse'],
  handler: async (event) => {
    if (event.tool === 'bash') {
      const dangerous = [
        'rm -rf /',
        'sudo',
        'chmod 777',
        'curl | bash',
      ]
      const cmd = event.args.command || ''

      if (dangerous.some((d) => cmd.includes(d))) {
        return {
          approved: false,
          reason: `Potentially dangerous command: ${cmd}`,
          suggestion: 'Review this command carefully before executing.',
        }
      }
    }

    return { approved: true }
  },
})
```

### Available Hook Events

| Event | Trigger | Use Case |
|-------|---------|----------|
| `PreToolUse` | Before tool execution | Security gates, validation |
| `PostToolUse` | After tool execution | Logging, cleanup |
| `UserPromptSubmit` | Before prompt sent | Prompt enhancement, filtering |
| `Stop` | Session ends | Cleanup, summary |

## Testing Plugins

```typescript
import { describe, it, expect } from 'vitest'
import { myCommand } from '../src/commands/my-command'

describe('my-command', () => {
  it('should process target successfully', async () => {
    const context = createMockContext()
    const result = await myCommand.handler(context, {
      target: 'test-input',
      verbose: false,
    })

    expect(result.status).toBe('success')
    expect(result.result).toBeDefined()
  })

  it('should reject invalid input', async () => {
    const context = createMockContext()

    await expect(
      myCommand.handler(context, { target: '', verbose: false })
    ).rejects.toThrow(/invalid target/)
  })
})
```

## Publishing

1. **Version semantically** — Follow semver (major.minor.patch)
2. **Document thoroughly** — README with installation, usage, examples
3. **Test across environments** — macOS, Linux, CI
4. **Namespace properly** — Use `opencode-plugin-*` prefix
5. **Peer dependencies** — Declare opencode version requirement

## Checklist

- [ ] Plugin follows standard structure
- [ ] All commands have descriptions and parameter docs
- [ ] Agents have specific system prompts
- [ ] Skills have clear trigger patterns
- [ ] Hooks handle edge cases
- [ ] Tests cover happy path and error cases
- [ ] README includes installation and usage examples
- [ ] Package.json has correct opencode configuration
