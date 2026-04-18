---
title: "Advanced Orchestration"
---

# Advanced Orchestration

Learn how to build complex multi-agent workflows with task delegation, parallel execution, and fault-tolerant orchestration.

## Orchestrator Pattern

The orchestrator pattern uses a central agent to decompose complex tasks and delegate subtasks to specialized agents:

```typescript
import { AgentBuilder, Orchestrator } from '@opensin/agent-sdk'

const orchestrator = new Orchestrator({
  agents: {
    'frontend': AgentBuilder.create('sin-frontend')
      .withSkills(['react', 'tailwind', 'accessibility'])
      .build(),
    'backend': AgentBuilder.create('sin-herakles')
      .withSkills(['api-design', 'database', 'auth'])
      .build(),
    'tester': AgentBuilder.create('sin-tester')
      .withSkills(['unit-tests', 'integration', 'e2e'])
      .build(),
  },
  strategy: 'parallel-when-possible',
})

// The orchestrator breaks down the task and delegates
const result = await orchestrator.execute(
  'Build a user registration feature with email verification'
)
```

## Task Decomposition

Break complex tasks into a dependency graph:

```typescript
const taskGraph = {
  'design-api': {
    agent: 'backend',
    prompt: 'Design REST API for user registration',
    depends: [],
  },
  'design-ui': {
    agent: 'frontend',
    prompt: 'Design registration form UI',
    depends: [],
  },
  'implement-api': {
    agent: 'backend',
    prompt: 'Implement the registration API endpoints',
    depends: ['design-api'],
  },
  'implement-ui': {
    agent: 'frontend',
    prompt: 'Build the registration form component',
    depends: ['design-ui', 'design-api'],
  },
  'write-tests': {
    agent: 'tester',
    prompt: 'Write tests for registration flow',
    depends: ['implement-api', 'implement-ui'],
  },
}

// Execute with automatic dependency resolution
const results = await orchestrator.executeGraph(taskGraph)
```

Independent tasks (`design-api` and `design-ui`) run in parallel. Dependent tasks wait for their prerequisites.

## Fault Tolerance

### Retry with Backoff

```typescript
const orchestrator = new Orchestrator({
  retry: {
    maxAttempts: 3,
    backoff: 'exponential',  // 1s, 2s, 4s
    retryableErrors: ['timeout', 'rate_limit', 'connection_error'],
  },
})
```

### Fallback Agents

If the primary agent fails, route to a fallback:

```typescript
const orchestrator = new Orchestrator({
  agents: {
    'primary-coder': {
      agent: 'sin-herakles',
      fallback: 'sin-solver',  // use if primary fails
    },
  },
})
```

### Circuit Breaker

Prevent cascading failures by stopping delegation to unhealthy agents:

```typescript
const circuitBreaker = {
  failureThreshold: 3,     // open circuit after 3 failures
  resetTimeout: 60_000,    // try again after 60 seconds
  halfOpenMax: 1,           // allow 1 test request
}
```

## Event-Driven Orchestration

Use n8n workflows for event-driven orchestration that doesn't require a running agent:

```bash
# Create a workflow that triggers on GitHub webhook
sin-n8n create http-poller \
  --name "PR-Review-Pipeline" \
  --vars POLL_URL=https://api.github.com/repos/OpenSIN-AI/OpenSIN-Code/pulls \
         CRON_EXPR="*/5 * * * *" \
  --activate
```

### Workflow Chaining

Chain n8n workflows for complex pipelines:

```
GitHub PR Created
    → n8n: Extract PR diff
    → A2A-SIN-Herakles: Code review
    → A2A-SIN-Tester: Run test suite
    → n8n: Post review comment
    → Telegram: Notify team
```

## Monitoring Orchestration

Track task execution across the fleet:

```typescript
orchestrator.on('task:start', (event) => {
  console.log(`[${event.agent}] Starting: ${event.task.id}`)
})

orchestrator.on('task:complete', (event) => {
  console.log(`[${event.agent}] Completed in ${event.duration}ms`)
})

orchestrator.on('task:error', (event) => {
  console.error(`[${event.agent}] Failed: ${event.error.message}`)
  // Auto-creates GitHub issue via SIN-GitHub-Issues
})
```

## Best Practices

1. **Keep agents focused** -- each agent should have a clear, narrow responsibility
2. **Design for failure** -- every delegation should have a retry and fallback path
3. **Minimize coupling** -- agents communicate through structured task artifacts, not shared state
4. **Log everything** -- task execution traces are essential for debugging multi-agent workflows
5. **Test in isolation** -- verify each agent works independently before composing

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Vision-Gate** | -7.0 | KEINE Browser-Aktion ohne Screenshot + Vision-Check |
| **DevTools-First** | -1.0 | JEDER CSS-Selektor via DevTools verifizieren |
| **Bun-Only** | -1.5 | `bun install` / `bun run` — npm ist verboten |
| **Technologie-Souveränität** | -2.0 | nodriver + Chrome Profil — Playwright/etc. verboten |

→ [Alle Mandate](/best-practices/browser-automation)
