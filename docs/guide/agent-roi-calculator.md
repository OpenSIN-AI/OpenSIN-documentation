# Agent ROI Calculator

Calculate and demonstrate the return on investment for OpenSIN agents.

## ROI Formula

```
ROI = (Value Generated - Cost) / Cost × 100
```

## Cost Components

### Direct Costs

| Component | Calculation | Example |
|-----------|-------------|---------|
| API Costs | Tokens × Price/1K | $500/month |
| Infrastructure | Server costs | $200/month |
| Development | Hours × Rate | $2,000/month |
| Maintenance | Ongoing support | $500/month |
| **Total** | | **$3,200/month** |

### Indirect Costs

| Component | Calculation | Example |
|-----------|-------------|---------|
| Training | Team training time | $500/month |
| Integration | Setup and config | $300/month |
| Monitoring | Tools and alerts | $200/month |
| **Total** | | **$1,000/month** |

## Value Components

### Time Savings

```python
# Calculate time savings
hours_saved_per_task = 2  # Hours saved per task
tasks_per_month = 500     # Tasks per month
hourly_rate = 75          # Average hourly rate

time_savings = hours_saved_per_task * tasks_per_month * hourly_rate
print(f"Time savings: ${time_savings:,}/month")  # $75,000/month
```

### Quality Improvement

```python
# Calculate quality improvement
error_rate_before = 0.10    # 10% error rate
error_rate_after = 0.02     # 2% error rate
cost_per_error = 500        # Cost per error
tasks_per_month = 500

error_cost_before = error_rate_before * tasks_per_month * cost_per_error
error_cost_after = error_rate_after * tasks_per_month * cost_per_error
quality_savings = error_cost_before - error_cost_after
print(f"Quality savings: ${quality_savings:,}/month")  # $40,000/month
```

### Revenue Impact

```python
# Calculate revenue impact
conversion_rate_before = 0.05   # 5% conversion
conversion_rate_after = 0.07    # 7% conversion
visitors_per_month = 10000
average_order_value = 100

revenue_before = conversion_rate_before * visitors_per_month * average_order_value
revenue_after = conversion_rate_after * visitors_per_month * average_order_value
revenue_increase = revenue_after - revenue_before
print(f"Revenue increase: ${revenue_increase:,}/month")  # $20,000/month
```

## ROI Calculation

```python
total_costs = 3200 + 1000  # Direct + Indirect
total_value = 75000 + 40000 + 20000  # Time + Quality + Revenue

roi = (total_value - total_costs) / total_costs * 100
payback_period = total_costs / (total_value - total_costs)

print(f"Monthly ROI: {roi:.0f}%")
print(f"Payback period: {payback_period:.1f} months")
print(f"Annual ROI: {roi * 12:.0f}%")
```

## ROI Dashboard

```python
from opensin.analytics import ROIDashboard

dashboard = ROIDashboard(
    costs=cost_tracker,
    value=value_tracker,
    period="monthly"
)

# Generate report
report = dashboard.generate_report()
print(report.markdown())

# Export
dashboard.export_csv("roi-report.csv")
dashboard.export_pdf("roi-report.pdf")
```

## Best Practices

1. **Track everything** — Measure all costs and benefits
2. **Be conservative** — Under-promise, over-deliver
3. **Update regularly** — Recalculate monthly
4. **Share results** — Show stakeholders the value
5. **Optimize continuously** — Find ways to improve ROI

## Next Steps

- [Cost Tracking](/guide/sin-cost-tracking)
- [Agent Economics](/guide/agent-economics)
