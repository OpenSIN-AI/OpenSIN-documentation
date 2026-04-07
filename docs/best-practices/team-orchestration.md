---
title: "Team Orchestration Best Practices"
---

# Team Orchestration Best Practices

Patterns for coordinating multiple agents to work together effectively on complex tasks.

## Team Structure

### Naming Convention

All teams follow the `[Type]-SIN-[Name]` schema:

- `Team-SIN-*` — Orchestrators, Hubs, Managers
- `A2A-SIN-*` — Worker Agents

### Team Composition

```
Team-SIN-Infrastructure
├── Manager (delegation, lexicon RAG, retry)
├── A2A-SIN-Storage (worker)
├── A2A-SIN-Supabase (worker)
├── A2A-SIN-N8N (worker)
├── A2A-SIN-CI-CD (worker)
└── ...
```

## Delegation Strategies

### Parallel Delegation

```typescript
// Independent tasks — run simultaneously
const results = await Promise.allSettled([
  delegate({
    to: 'A2A-SIN-Research',
    task: 'Research market trends',
    timeout: 300_000,
  }),
  delegate({
    to: 'A2A-SIN-Code-AI',
    task: 'Analyze code architecture',
    timeout: 300_000,
  }),
  delegate({
    to: 'A2A-SIN-Summary',
    task: 'Prepare executive summary',
    timeout: 120_000,
  }),
])
```

### Sequential Delegation

```typescript
// Dependent tasks — output feeds next input
const research = await delegate({
  to: 'A2A-SIN-Research',
  task: 'Gather requirements',
})

const design = await delegate({
  to: 'A2A-SIN-Code-AI',
  task: 'Design architecture',
  context: research.result,
})

const implementation = await delegate({
  to: 'A2A-SIN-Code-DevOps',
  task: 'Implement and deploy',
  context: design.result,
})
```

## Team Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| `parallel` | Agents work simultaneously | Independent tasks |
| `sequential` | Agents work one after another | Pipeline workflows |
| `consensus` | Agents vote on outcomes | Decision making |
| `leader` | One agent coordinates others | Complex coordination |
| `pipeline` | Output feeds next input | Data processing |

## Retry and Recovery

### Automatic Retry

```typescript
async function delegateWithRetry(
  config: DelegationConfig,
  maxRetries = 3
): Promise<DelegationResult> {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await delegate(config)
    } catch (error) {
      if (i === maxRetries - 1) {
        await notifyOperator({
          type: 'delegation_failure',
          agent: config.to,
          attempts: maxRetries,
          error,
        })
        throw error
      }
      await sleep(Math.pow(2, i) * 2000)
    }
  }
}
```

### Fallback Agents

```typescript
async function delegateWithFallback(config: DelegationConfig) {
  try {
    return await delegate(config)
  } catch {
    // Fallback to general-purpose agent
    return await delegate({
      ...config,
      to: 'A2A-SIN-Summary',
      task: `${config.task} (delegated as fallback)`,
    })
  }
}
```

## Monitoring

### Team Metrics

```typescript
interface TeamMetrics {
  totalDelegations: number
  successfulDelegations: number
  failedDelegations: number
  averageResponseTime: number
  activeAgents: number
  idleAgents: number
}

function getTeamMetrics(team: string): TeamMetrics {
  // Query team metrics from n8n or database
  return metricsService.query({ team })
}
```

### Health Dashboard

```
Team-SIN-Infrastructure
├── Status: ✅ Healthy
├── Active Workers: 8/15
├── Avg Response Time: 2.3s
├── Success Rate: 98.5%
└── Last Activity: 2 min ago
```

## Checklist

- [ ] Team follows naming conventions
- [ ] Delegation strategy chosen per task
- [ ] Timeouts configured for all delegations
- [ ] Retry logic implemented
- [ ] Error notifications configured
- [ ] Metrics collection enabled
- [ ] Fallback agents defined
