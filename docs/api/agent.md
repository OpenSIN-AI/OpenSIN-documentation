# Agent API

## Agent Class

### Constructor

```javascript
new Agent(options: AgentOptions)
```

### AgentOptions

| Property | Type | Description | Required |
|----------|------|-------------|----------|
| `name` | string | Unique agent identifier | Yes |
| `description` | string | Agent description | No |
| `capabilities` | string[] | What the agent can do | Yes |
| `model` | string | AI model to use | Yes |
| `systemPrompt` | string | Instructions for the agent | No |

### Methods

#### `start()`

Start the agent.

```javascript
await agent.start();
```

#### `stop()`

Stop the agent.

```javascript
await agent.stop();
```

#### `send(message: string)`

Send a message to the agent.

```javascript
const response = await agent.send('Hello!');
```

#### `respond(message: string)`

Respond to a message.

```javascript
await agent.respond('Hello back!');
```

#### `on(event: string, handler: Function)`

Register an event handler.

```javascript
agent.on('message', async (msg) => {
  console.log('Received:', msg.text);
});
```
