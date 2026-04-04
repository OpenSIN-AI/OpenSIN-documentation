# Agent Observability

Complete observability stack for OpenSIN agents.

## Three Pillars

### 1. Metrics

```python
from opensin.observability import MetricsCollector

metrics = MetricsCollector()

# Track custom metrics
metrics.counter("requests.total").increment()
metrics.histogram("request.duration").observe(duration_ms)
metrics.gauge("memory.usage").set(memory_mb)
metrics.counter("tokens.input").add(tokens_in)
metrics.counter("tokens.output").add(tokens_out)
metrics.counter("cost.total").add(cost_usd)
```

### 2. Logging

```python
from opensin.observability import Logger

logger = Logger(
    service="opensin-agent",
    level="INFO",
    format="json",
    fields=["timestamp", "level", "agent", "session", "event"]
)

logger.info("agent.request", extra={
    "agent_id": "researcher",
    "model": "gpt-4",
    "prompt_length": len(prompt),
    "session_id": session_id
})
```

### 3. Tracing

```python
from opensin.observability import Tracer

tracer = Tracer(service_name="opensin")

@tracer.span("agent.execute")
async def execute_agent(agent, prompt):
    with tracer.span("llm.generate"):
        response = await agent.generate(prompt)
    return response
```

## Dashboards

### Grafana Dashboard

```json
{
  "dashboard": {
    "title": "OpenSIN Agent Overview",
    "panels": [
      {"title": "Request Rate", "expr": "rate(opensin_requests_total[5m])"},
      {"title": "Error Rate", "expr": "rate(opensin_errors_total[5m]) / rate(opensin_requests_total[5m])"},
      {"title": "P99 Latency", "expr": "histogram_quantile(0.99, opensin_request_duration_seconds_bucket)"},
      {"title": "Token Usage", "expr": "rate(opensin_tokens_total[5m])"},
      {"title": "Cost per Hour", "expr": "rate(opensin_cost_total[1h])"},
      {"title": "Cache Hit Rate", "expr": "rate(opensin_cache_hits_total[5m]) / rate(opensin_cache_lookups_total[5m])"}
    ]
  }
}
```

## Alerting

```yaml
# alerts.yml
groups:
  - name: opensin-agents
    rules:
      - alert: HighErrorRate
        expr: rate(opensin_errors_total[5m]) / rate(opensin_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        
      - alert: HighLatency
        expr: histogram_quantile(0.99, opensin_request_duration_seconds_bucket) > 5
        for: 10m
        labels:
          severity: warning
        
      - alert: BudgetExceeded
        expr: opensin_cost_total > 100
        labels:
          severity: critical
          
      - alert: LowCacheHitRate
        expr: rate(opensin_cache_hits_total[5m]) / rate(opensin_cache_lookups_total[5m]) < 0.3
        for: 15m
        labels:
          severity: warning
```

## Distributed Tracing

```
User Request → API Gateway → Orchestrator → Agent → LLM → Response
     ↓              ↓             ↓          ↓       ↓
  [trace_id]   [span_id]    [span_id]   [span_id] [span_id]
```

## Best Practices

1. **Instrument everything** — Track all key metrics
2. **Set meaningful alerts** — Alert on symptoms, not causes
3. **Use structured logging** — JSON format for easy parsing
4. **Correlate traces** — Link requests across services
5. **Monitor costs** — Track token usage and spending
6. **Dashboard everything** — Visual dashboards for quick insights

## Next Steps

- [Monitoring Guide](/guide/monitoring)
- [Performance Benchmarking](/guide/performance-benchmarking)
