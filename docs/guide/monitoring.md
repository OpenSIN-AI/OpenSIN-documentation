# Monitoring Guide

## Overview

This guide covers monitoring OpenSIN in production.

## Metrics

OpenSIN exposes the following metrics:

| Metric | Description |
|--------|-------------|
| `agent_count` | Number of active agents |
| `team_count` | Number of active teams |
| `message_count` | Total messages processed |
| `error_count` | Total errors |
| `response_time` | Average response time |

## Prometheus

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'opensin'
    static_configs:
      - targets: ['localhost:3000']
```

## Grafana

Import the OpenSIN dashboard from Grafana marketplace.

## Alerting

Configure alerts for:
- High error rate
- High response time
- Low agent count
- High memory usage

## Logging

OpenSIN logs to stdout by default. Configure log aggregation with:

- ELK Stack
- Loki
- CloudWatch

## Next Steps
- [Scaling](/guide/scaling)
- [Troubleshooting](/guide/troubleshooting)
