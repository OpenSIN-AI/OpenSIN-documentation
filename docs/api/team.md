# Team API

## Team Class

### Constructor

```javascript
new Team(options: TeamOptions)
```

### TeamOptions

| Property | Type | Description | Required |
|----------|------|-------------|----------|
| `name` | string | Team name | Yes |
| `agents` | Agent[] | Team agents | Yes |
| `orchestrator` | string | Orchestration strategy | Yes |

### Methods

#### `start()`

Start the team.

```javascript
await team.start();
```

#### `assign(task: Task)`

Assign a task to the team.

```javascript
await team.assign({
  task: 'Write a blog post',
  workflow: [
    { agent: 'researcher', task: 'Research' },
    { agent: 'writer', task: 'Write' }
  ]
});
```

#### `on(event: string, handler: Function)`

Register an event handler.

```javascript
team.on('task-complete', (result) => {
  console.log('Task completed:', result);
});
```
