# SIN Cost Tracking

> **OpenSIN's Cost Management** — Transparenz über API-Kosten in Echtzeit.

## Overview

Verfolge Kosten pro Agent, Session, und Tool-Call mit detaillierten Breakdowns.

## Echtzeit Cost Display

```
Session: research-2026-04-04
┌─────────────────────────────────────────────┐
│ Tokens: 12,450 | Cost: $0.37 | Time: 2:34  │
├─────────────────────────────────────────────┤
│ Model          | Tokens | Cost   | Cache    │
│ gpt-4          | 8,200  | $0.25  | 15% hit  │
│ gpt-3.5-turbo  | 4,250  | $0.12  | 32% hit  │
└─────────────────────────────────────────────┘
```

## Cost Tracking API

```python
from opensin import CostTracker

tracker = CostTracker()

# Kosten pro Agent
agent_cost = tracker.get_agent_cost("researcher")
print(f"Researcher: ${agent_cost.total:.4f}")

# Kosten pro Session
session_cost = tracker.get_session_cost("session-123")
print(f"Session: ${session_cost.total:.4f}")

# Kosten pro Tool
tool_costs = tracker.get_tool_costs()
for tool, cost in tool_costs.items():
    print(f"{tool}: ${cost:.4f}")
```

## Budget Limits

```python
from opensin import BudgetManager

budget = BudgetManager(
    daily_limit=10.00,
    monthly_limit=200.00,
    alert_threshold=0.8,  # 80% Warnung
    hard_stop=True        # Stop bei Limit
)

# Vor jeder API-Call prüfen
if budget.would_exceed_limit(estimated_cost):
    raise BudgetExceededError(f"Would exceed daily limit")
```

## Cost Alerts

```bash
# Budget Warnung bei 80%
⚠️ 80% des täglichen Budgets erreicht ($8.00/$10.00)

# Hard Stop bei 100%
🛑 Tägliches Budget erschöpft. Weitere Calls blockiert.
```

## Cost Optimization Tips

1. **Cache nutzen** — Prompt Caching spart 50-80%
2. **Modell-Mix** — Günstige Modelle für einfache Tasks
3. **Streaming** — Weniger Tokens durch early stop
4. **Compaction** — Weniger Context = weniger Tokens
5. **Batching** — Mehrere Requests zusammenfassen

## Cost Reports

```bash
# Täglicher Report
/sin cost --period daily

# Wöchentlicher Report
/sin cost --period weekly

# Detaillierter Report
/sin cost --detailed --format json
```

## Next Steps

- [Performance Optimization](/guide/performance-optimization)
- [SIN.md System](/guide/sin-md-system)
