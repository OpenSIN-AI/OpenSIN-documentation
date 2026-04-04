# Observability & Monitoring Guide

Complete guide to monitoring OpenSIN agents in production.

## Overview

Observability in OpenSIN covers three pillars:
- **Metrics** — Quantitative measurements
- **Logs** — Detailed event records
- **Traces** — Request flow tracking

## Metrics

### Built-in Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `agent.requests.total` | Counter | Total requests |
| `agent.requests.success` | Counter | Successful requests |
| `agent.requests.failed` | Counter | Failed requests |
| `agent.latency.p50` | Histogram | 50th percentile latency |
| `agent.latency.p99` | Histogram | 99th percentile latency |
| `agent.tokens.input` | Counter | Input tokens used |
| `agent.tokens.output` | Counter | Output tokens used |
| `agent.cost.total` | Counter | Total cost in USD |
| `agent.cache.hit_rate` | Gauge | Cache hit percentage |
| `agent.memory.usage` | Gauge | Memory usage in MB |

### Prometheus Integration

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'opensin'
    static_configs:
      - targets: ['opensin:8000']
    metrics_path: '/metrics'
```

### Grafana Dashboard

```json
{
  "dashboard": {
    "title": "OpenSIN Agent Monitoring",
    "panels": [
      {
        "title": "Request Rate",
        "expr": "rate(agent_requests_total[5m])"
      },
      {
        "title": "Error Rate",
        "expr": "rate(agent_requests_failed[5m]) / rate(agent_requests_total[5m])"
      },
      {
        "title": "P99 Latency",
        "expr": "histogram_quantile(0.99, agent_latency_seconds_bucket)"
      },
      {
        "title": "Cost per Hour",
        "expr": "rate(agent_cost_total[1h])"
      }
    ]
  }
}
```

## Logging

### Log Configuration

```python
from opensin import Logger

logger = Logger(
    level="INFO",
    format="json",
    output="stdout",
    fields=["timestamp", "level", "agent", "event", "duration_ms"]
)
```

### Log Levels

| Level | When to Use |
|-------|-------------|
| DEBUG | Detailed debugging info |
| INFO | Normal operational events |
| WARNING | Unexpected but handled events |
| ERROR | Request failures |
| CRITICAL | System failures |

### Structured Logging

```python
logger.info("agent_request", extra={
    "agent_id": "researcher",
    "model": "gpt-4",
    "tokens_input": 150,
    "tokens_output": 300,
    "duration_ms": 2340,
    "cost": 0.015
})
```

## Distributed Tracing

### OpenTelemetry Integration

```python
from opentelemetry import trace
from opensin import OpenTelemetryExporter

exporter = OpenTelemetryExporter(
    endpoint="http://jaeger:14268/api/traces",
    service_name="opensin"
)

tracer = trace.get_tracer("opensin")

@tracer.start_as_current_span("agent.execute")
async def execute_agent(agent, prompt):
    with tracer.start_as_current_span("llm.generate"):
        response = await agent.generate(prompt)
    return response
```

### Trace Context

```
User Request → API Gateway → Orchestrator → Agent → LLM → Response
     ↓              ↓             ↓          ↓       ↓
  [trace_id]   [span_id]    [span_id]   [span_id] [span_id]
```

## Alerting

### Alert Rules

```yaml
# alerts.yml
groups:
  - name: opensin
    rules:
      - alert: HighErrorRate
        expr: rate(agent_requests_failed[5m]) / rate(agent_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Agent error rate above 5%"
          
      - alert: HighLatency
        expr: histogram_quantile(0.99, agent_latency_seconds_bucket) > 5
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "P99 latency above 5 seconds"
          
      - alert: BudgetExceeded
        expr: agent_cost_total > 100
        labels:
          severity: critical
        annotations:
          summary: "Daily budget exceeded"
```

### Notification Channels

| Channel | Configuration |
|---------|--------------|
| Slack | Webhook URL |
| PagerDuty | Integration key |
| Email | SMTP settings |
| Discord | Webhook URL |
| SMS | Twilio credentials |

## Health Checks

```python
from opensin import HealthCheck

health = HealthCheck()

@health.check("database")
async def check_database():
    return await db.ping()

@health.check("llm_api")
async def check_llm_api():
    return await agent.test_connection()

@health.check("cache")
async def check_cache():
    return await cache.ping()

# GET /health
# Returns: {"status": "healthy", "checks": {...}}
```

## Next Steps

- [Performance Benchmarking](/guide/performance-benchmarking)
- [Production Deployment](/guide/deployment-production)
- [Troubleshooting](/guide/troubleshooting)
