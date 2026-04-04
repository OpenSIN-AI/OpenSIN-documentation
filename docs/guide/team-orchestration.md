# Team Orchestration

OpenSIN teams enable multiple agents to work together on complex tasks.

## Creating a Team

```bash
opensin team create research-team --agents researcher,writer,reviewer --strategy sequential
```

## Team Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| sequential | Agents work one after another | Pipeline workflows |
| parallel | Agents work simultaneously | Independent tasks |
| consensus | Agents vote on outcomes | Decision making |
| leader | One agent coordinates others | Complex coordination |
| pipeline | Output of one feeds input of next | Data processing |

## Executing a Team Task

```bash
opensin team exec research-team --task "Research AI trends and write a report"
```

## Next Steps

- [Agent Basics](/guide/agent-basics)
- [A2A Protocol](/guide/a2a-protocol)
