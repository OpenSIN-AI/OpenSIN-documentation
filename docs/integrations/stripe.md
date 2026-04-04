# Stripe Integration

Connect OpenSIN agents to Stripe for payment automation.

## Overview

The Stripe integration enables agents to:
- Process payments and subscriptions
- Generate invoices automatically
- Handle refunds and disputes
- Monitor revenue metrics
- Send payment notifications

## Setup

```bash
opensin integration create stripe \
  --api-key sk_live_YOUR_KEY \
  --webhook-secret whsec_YOUR_SECRET
```

## Agent Configuration

```python
from opensin import Agent
from opensin.integrations import Stripe

stripe = Stripe(api_key="sk_live_...")

payment_agent = Agent(
    name="payment-processor",
    model="gpt-4",
    system_prompt="You handle payment processing and billing.",
    tools=["stripe_create_charge", "stripe_create_subscription", "stripe_generate_invoice"]
)
```

## Common Workflows

### Automated Billing

```
[Subscription Due] → [Generate Invoice] → [Process Payment] → [Send Receipt]
```

### Payment Notifications

```python
@stripe.on("invoice.payment_succeeded")
async def handle_payment(event):
    await payment_agent.send(f"Payment received: {event.amount}")
    await notify_customer(event.customer_email, "payment_success")
```

## Next Steps

- [Webhooks & Events](/guide/webhooks-events)
- [n8n Workflows](/guide/n8n-workflows)
