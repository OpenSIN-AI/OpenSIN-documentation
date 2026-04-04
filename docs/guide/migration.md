# Migration Guide

## v0.x to v1.0

### Agent API

**Before:** `new Agent('name', ['cap'])`
**After:** `new Agent({ name: 'name', capabilities: ['cap'] })`

### Team API

**Before:** `new Team('name', [agents])`
**After:** `new Team({ name: 'name', agents: [agents] })`

### A2A Protocol

**Before:** `agent.sendTo('name', 'msg')`
**After:** `agent.sendTo(agent, { type: 'text', content: 'msg' })`
