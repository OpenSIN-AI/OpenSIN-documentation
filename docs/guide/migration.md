# Migration Guide

## Migrating from v0.x to v1.0

### Breaking Changes

- Agent API has changed
- Team API has changed
- A2A protocol has changed

### Agent API Changes

**Before:**
```javascript
const agent = new Agent('my-agent', ['greet']);
```

**After:**
```javascript
const agent = new Agent({
  name: 'my-agent',
  capabilities: ['greet']
});
```

### Team API Changes

**Before:**
```javascript
const team = new Team('my-team', [agent1, agent2]);
```

**After:**
```javascript
const team = new Team({
  name: 'my-team',
  agents: [agent1, agent2]
});
```

### A2A Protocol Changes

**Before:**
```javascript
agent.sendTo('agent-b', 'Hello!');
```

**After:**
```javascript
agent.sendTo(agentB, {
  type: 'text',
  content: 'Hello!'
});
```

## Need Help?

- [Documentation](/guide/getting-started)
- [GitHub Issues](https://github.com/OpenSIN-AI/OpenSIN/issues)
- [Discord](https://discord.gg/opensin)
