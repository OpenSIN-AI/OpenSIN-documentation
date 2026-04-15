# @sin/plugin-sdk

> Plugin SDK for SIN Code CLI — TypeScript-based OpenCode fork with plugins

## Installation

```bash
bun add @sin/plugin-sdk
```

## Quick Start

### Create a Plugin

```typescript
import { definePlugin, createTool, createHook } from '@sin/plugin-sdk';

export default definePlugin({
  name: '@sin/my-plugin',
  version: '1.0.0',
  type: 'tool',
  description: 'My awesome plugin',

  async activate(ctx) {
    // Register a tool
    ctx.tools.register(createTool({
      name: 'hello',
      description: 'Say hello',
      parameters: {
        name: { type: 'string', required: true }
      },
      execute: async ({ name }) => ({
        content: `Hello, ${name}!`
      })
    }));

    // Register a hook
    ctx.events.on('session:start', async (data) => {
      ctx.logger.info('Session started!');
    });
  }
});
```

### Plugin Manifest

Create `sin-plugin.json`:

```json
{
  "name": "@sin/my-plugin",
  "version": "1.0.0",
  "type": "tool",
  "main": "dist/index.js",
  "sinPlugin": {
    "minVersion": "1.0.0",
    "capabilities": ["tool"],
    "config": {
      "apiKey": {
        "type": "string",
        "required": true,
        "description": "API Key for the service"
      }
    }
  }
}
```

## Testing

```typescript
import { testPlugin, mockContext } from '@sin/plugin-sdk/test';

describe('My Plugin', () => {
  it('should activate successfully', async () => {
    const result = await testPlugin(myPlugin, {
      config: { apiKey: 'test-key' }
    });

    expect(result.success).toBe(true);
  });
});
```

## API Reference

### Plugin Types
- `tool` — New tools for the agent
- `hook` — Event-based automation
- `agent` — Specialized agent configurations
- `command` — New slash commands
- `auth` — Model authentication providers
- `theme` — Visual themes
- `memory` — Persistent memory systems
- `mcp` — Model Context Protocol servers

### Core APIs
- `definePlugin()` — Create a plugin
- `createTool()` — Create a tool
- `createHook()` — Create a hook
- `createCommand()` — Create a command
- `defineAuthProvider()` — Create an auth provider

### Context APIs
- `ctx.config` — Plugin configuration
- `ctx.session` — Current session info
- `ctx.tools` — Tool registry
- `ctx.events` — Event bus
- `ctx.logger` — Logging interface
- `ctx.sin` — SIN Core API (memory, a2a, permissions)

## Examples

See the [Examples section](/examples/hello-world) for complete plugin implementations.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

Apache 2.0