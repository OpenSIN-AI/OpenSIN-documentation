# Agent Monitoring Dashboard

Build comprehensive monitoring dashboards for OpenSIN agents.

## Dashboard Components

### 1. Health Overview

```
┌─────────────────────────────────────────────────────────┐
│                  OpenSIN Health Overview                 │
├─────────────────────────────────────────────────────────┤
│  Status: 🟢 Healthy    Uptime: 99.97%    Agents: 24/24  │
├─────────────────────────────────────────────────────────┤
│  Agent              Status   Latency   Errors   Cost/h  │
│  researcher         🟢       1.2s      0.01%    $0.45   │
│  writer             🟢       0.8s      0.00%    $0.32   │
│  reviewer           🟢       1.5s      0.02%    $0.51   │
│  triage             🟡       3.2s      0.05%    $0.28   │
└─────────────────────────────────────────────────────────┘
```

### 2. Metrics Dashboard

```python
from opensin.monitoring import Dashboard

dashboard = Dashboard(
    title="OpenSIN Agent Monitoring",
    refresh_interval=30,
    panels=[
        {"type": "timeseries", "title": "Request Rate", "metric": "requests_per_second"},
        {"type": "timeseries", "title": "Error Rate", "metric": "error_rate"},
        {"type": "timeseries", "title": "P99 Latency", "metric": "latency_p99"},
        {"type": "gauge", "title": "Cache Hit Rate", "metric": "cache_hit_rate"},
        {"type": "stat", "title": "Total Cost Today", "metric": "cost_total"},
        {"type": "table", "title": "Agent Status", "metric": "agent_status"},
    ]
)
```

### 3. Alert Configuration

```yaml
alerts:
  - name: HighErrorRate
    condition: error_rate > 0.05
    duration: 5m
    severity: critical
    channels: [slack, pagerduty]
    
  - name: HighLatency
    condition: latency_p99 > 5000
    duration: 10m
    severity: warning
    channels: [slack]
    
  - name: BudgetExceeded
    condition: cost_daily > budget_daily * 0.9
    duration: 0m
    severity: critical
    channels: [slack, email]
    
  - name: LowCacheHitRate
    condition: cache_hit_rate < 0.3
    duration: 15m
    severity: warning
    channels: [slack]
```

### 4. Log Viewer

```python
from opensin.monitoring import LogViewer

viewer = LogViewer(
    source="elasticsearch",
    index="opensin-logs-*",
    filters={
        "level": ["ERROR", "WARN"],
        "agent": ["researcher", "writer"]
    },
    refresh=10
)
```

### 5. Trace Viewer

```python
from opensin.monitoring import TraceViewer

traces = TraceViewer(
    source="jaeger",
    service="opensin",
    limit=50,
    sort="duration_desc"
)
```

## Grafana Integration

### Import Dashboard

```bash
# Import pre-built dashboard
opensin monitoring import grafana-dashboard.json

# Or use Grafana API
curl -X POST http://grafana:3000/api/dashboards/db \
  -H "Authorization: Bearer $GRAFANA_TOKEN" \
  -d @grafana-dashboard.json
```

### Data Sources

```yaml
# datasources.yml
apiVersion: 1
datasources:
  - name: Prometheus
    type: prometheus
    url: http://prometheus:9090
    
  - name: Elasticsearch
    type: elasticsearch
    url: http://elasticsearch:9200
    
  - name: Jaeger
    type: jaeger
    url: http://jaeger:16686
```

## Best Practices

1. **Single pane of glass** — All metrics in one dashboard
2. **Set meaningful alerts** — Alert on symptoms, not causes
3. **Use runbooks** — Link alerts to runbooks
4. **Review regularly** — Weekly dashboard review
5. **Iterate** — Improve dashboards based on incidents

## Next Steps

- [Observability Guide](/guide/agent-observability)
- [Monitoring Guide](/guide/monitoring)
