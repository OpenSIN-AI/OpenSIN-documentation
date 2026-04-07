---
title: "Monitoring & Observability Best Practices"
---

# Monitoring & Observability Best Practices

Guidelines for monitoring OpenSIN agents, tracking performance, and maintaining operational visibility.

## Key Metrics

### Agent Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| Request Rate | Requests per second | > 100 req/s |
| Error Rate | Percentage of failed requests | > 5% |
| Latency (p50) | Median response time | > 5s |
| Latency (p99) | 99th percentile response time | > 30s |
| Token Usage | Input + output tokens per session | > 100K/session |
| Cost | API costs per hour | > $10/hour |
| Active Sessions | Concurrent agent sessions | > 50 |
| Turn Count | Average turns per task | > 20 |

### Infrastructure Metrics

| Component | Metric | Threshold |
|-----------|--------|-----------|
| n8n (OCI VM) | CPU usage | > 80% |
| n8n (OCI VM) | Memory usage | > 90% |
| Supabase | Connection pool usage | > 80% |
| Supabase | Storage usage | > 80% of 200GB |
| HF Spaces | Uptime | < 99% |
| MCP Servers | Response time | > 5s |

## Health Checks

### Agent Health

```typescript
interface AgentHealth {
  status: 'healthy' | 'degraded' | 'unhealthy'
  lastActivity: Date
  activeSessions: number
  errorRate: number
  avgResponseTime: number
  modelAvailability: boolean
}

async function checkAgentHealth(agentId: string): Promise<AgentHealth> {
  const metrics = await metricsService.getAgentMetrics(agentId)
  const modelStatus = await checkModelAvailability()

  return {
    status: determineHealthStatus(metrics, modelStatus),
    lastActivity: metrics.lastActivity,
    activeSessions: metrics.activeSessions,
    errorRate: metrics.errorRate,
    avgResponseTime: metrics.avgResponseTime,
    modelAvailability: modelStatus.available,
  }
}
```

### Infrastructure Health

```bash
# Run health checks
npm run health

# Check specific components
npm run health:agents
npm run health:infrastructure
npm run health:mcp
npm run health:a2a
```

## Logging

### Log Levels

| Level | Use Case |
|-------|----------|
| `ERROR` | Failures requiring immediate attention |
| `WARN` | Recoverable issues, degraded performance |
| `INFO` | Significant events (session start, delegation) |
| `DEBUG` | Detailed execution flow |
| `TRACE` | Every tool call, every LLM response |

### Structured Logging

```typescript
import { createLogger } from '@opensin/sdk'

const logger = createLogger({
  level: 'INFO',
  format: 'json',
  destination: 'logcenter',
  redaction: ['apiKey', 'token', 'password'],
})

logger.info('Session started', {
  sessionId: 'ses_abc123',
  agentId: 'researcher',
  model: 'claude-sonnet-4-6',
})

logger.error('Tool execution failed', {
  tool: 'bash',
  error: 'Command timeout',
  sessionId: 'ses_abc123',
})
```

## Alerting

### Alert Rules

```typescript
const alertRules = [
  {
    name: 'high_error_rate',
    condition: (metrics) => metrics.errorRate > 0.05,
    severity: 'critical',
    channels: ['telegram', 'email'],
    message: 'Agent error rate exceeds 5%',
  },
  {
    name: 'model_unavailable',
    condition: (metrics) => !metrics.modelAvailability,
    severity: 'high',
    channels: ['telegram'],
    message: 'Primary model is unavailable',
  },
  {
    name: 'cost_spike',
    condition: (metrics) => metrics.hourlyCost > 10,
    severity: 'warning',
    channels: ['telegram'],
    message: 'Hourly cost exceeds $10',
  },
]
```

## Dashboards

### Agent Fleet Dashboard

```
┌─────────────────────────────────────────────────┐
│              OpenSIN Fleet Status                │
├─────────────────────────────────────────────────┤
│ Total Agents: 92    Active: 45    Idle: 47      │
│                                                 │
│ Success Rate: 98.2%    Avg Latency: 2.1s        │
│ Hourly Cost: $4.23    Tokens/min: 12,450        │
│                                                 │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐            │
│ │  Teams  │ │  MCPs   │ │  A2A    │            │
│ │  17/17  │ │  6/7    │ │ 92/92   │            │
│ │   ✅    │ │  ⚠️     │ │   ✅    │            │
│ └─────────┘ └─────────┘ └─────────┘            │
└─────────────────────────────────────────────────┘
```

## Cost Monitoring

```typescript
import { UsagePricing } from '@opensin/sdk'

const pricing = new UsagePricing({
  models: {
    'gpt-4o-mini': { input: 0.15, output: 0.6 },
    'gpt-4o': { input: 2.5, output: 10 },
    'claude-sonnet-4-6': { input: 3, output: 15 },
    'claude-opus-4-6': { input: 15, output: 75 },
  },
})

// Track per session
pricing.trackSession('ses_abc123', {
  model: 'claude-sonnet-4-6',
  inputTokens: 25000,
  outputTokens: 8000,
})

// Get cost report
const report = pricing.getReport('ses_abc123')
// { totalCost: 0.195, totalTokens: 33000, calls: 12 }
```

## Checklist

- [ ] All key metrics collected
- [ ] Health checks configured
- [ ] Log levels set appropriately
- [ ] Alert rules defined
- [ ] Cost monitoring enabled
- [ ] Dashboards created
- [ ] Log redaction active
- [ ] GitLab LogCenter integration working
