# Monitoring Guide

## Metrics

| Metric | Description |
|--------|-------------|
| `agent_count` | Active agents |
| `team_count` | Active teams |
| `message_count` | Messages processed |
| `error_count` | Total errors |
| `response_time` | Avg response time |

## Prometheus

```yaml
scrape_configs:
  - job_name: 'opensin'
    static_configs:
      - targets: ['localhost:3000']
```

## Grafana

Import the OpenSIN dashboard from Grafana marketplace.

## Alerting

Configure alerts for high error rate, high response time, low agent count.

## Next Steps
- [Scaling](/guide/scaling)
- [Troubleshooting](/guide/troubleshooting)
