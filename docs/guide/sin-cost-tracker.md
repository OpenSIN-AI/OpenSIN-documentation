# SIN Cost Tracker — Real-time Cost Monitoring

> **OpenSIN's Cost Tracker** — Geklont aus Claude Code's cost-tracker.ts. Echtzeit-Kostenverfolgung für alle API-Calls.

## Architecture

```
API Call → Track Usage → Update Cost → Check Budget → Alert if exceeded
```

## Implementation

```python
from opensin.cost import CostTracker

tracker = CostTracker(
    models={
        "gpt-4": {"input": 0.03, "output": 0.06},  # per 1K tokens
        "gpt-3.5-turbo": {"input": 0.001, "output": 0.002},
        "claude-sonnet": {"input": 0.015, "output": 0.03},
    },
    budget={
        "daily": 50.00,
        "monthly": 1000.00
    }
)

# Track API usage
tracker.record_usage(
    model="gpt-4",
    input_tokens=1500,
    output_tokens=500
)

# Get current cost
print(f"Today: ${tracker.daily_cost:.2f}")
print(f"Month: ${tracker.monthly_cost:.2f}")

# Check budget
if tracker.is_daily_budget_exceeded():
    print("⚠️ Daily budget exceeded!")
```

## Model Usage Tracking

```python
from opensin.cost import ModelUsage

class ModelUsage:
    def __init__(self):
        self.models = {}
    
    def record(self, model: str, input_tokens: int, output_tokens: int):
        if model not in self.models:
            self.models[model] = {"input": 0, "output": 0, "cost": 0}
        
        self.models[model]["input"] += input_tokens
        self.models[model]["output"] += output_tokens
        self.models[model]["cost"] += self.calculate_cost(model, input_tokens, output_tokens)
    
    def get_total_cost(self) -> float:
        return sum(m["cost"] for m in self.models.values())
```

## Budget Alerts

```python
from opensin.cost import BudgetAlert

alerts = BudgetAlert(
    thresholds=[0.5, 0.75, 0.9, 1.0],
    channels=["slack", "email"]
)

# Check and alert
await alerts.check(tracker.daily_cost, tracker.daily_budget)
```

## Best Practices

1. **Track all models** — Every API call should be tracked
2. **Set budgets** — Daily and monthly limits
3. **Alert early** — Warn at 50%, 75%, 90%
4. **Hard stop** — Block calls when budget exceeded
5. **Report regularly** — Daily/weekly cost reports

## Next Steps

- [Cost Optimization](/guide/agent-cost-optimization)
- [SIN Token Estimation](/guide/sin-token-estimation)
