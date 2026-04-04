# Webhooks & Events Guide

Integrate OpenSIN with external systems using webhooks and the event system.

## Event Types

OpenSIN emits events for all significant actions:

| Event | Trigger | Payload |
|-------|---------|---------|
| `agent.created` | New agent created | Agent details |
| `agent.started` | Agent begins processing | Agent ID, input |
| `agent.completed` | Agent finishes task | Agent ID, output |
| `agent.failed` | Agent encounters error | Agent ID, error |
| `team.created` | New team created | Team details |
| `team.started` | Team begins execution | Team ID, task |
| `team.completed` | Team finishes task | Team ID, results |
| `team.failed` | Team encounters error | Team ID, error |
| `message.sent` | Message sent via A2A | Message details |
| `message.received` | Message received | Message details |
| `deployment.started` | Deployment begins | Deployment details |
| `deployment.completed` | Deployment succeeds | Deployment details |
| `deployment.failed` | Deployment fails | Deployment details |
| `error.occurred` | System error occurs | Error details |

## Webhook Configuration

### Create Webhook

```bash
opensin webhook create \
  --url https://your-server.com/webhook \
  --events agent.completed,agent.failed,team.completed \
  --secret your-webhook-secret
```

### List Webhooks

```bash
opensin webhook list
```

### Delete Webhook

```bash
opensin webhook delete <webhook-id>
```

## Receiving Webhooks

### Python Example (FastAPI)

```python
from fastapi import FastAPI, Request, HTTPException
import hashlib
import hmac

app = FastAPI()

WEBHOOK_SECRET = "your-webhook-secret"

def verify_signature(payload: bytes, signature: str) -> bool:
    expected = hmac.new(
        WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)

@app.post("/webhook")
async def handle_webhook(request: Request):
    # Verify signature
    signature = request.headers.get("X-OpenSIN-Signature")
    body = await request.body()
    
    if not verify_signature(body, signature):
        raise HTTPException(status_code=401, detail="Invalid signature")
    
    # Process event
    event = await request.json()
    
    if event["type"] == "agent.completed":
        await handle_agent_completed(event["data"])
    elif event["type"] == "agent.failed":
        await handle_agent_failed(event["data"])
    elif event["type"] == "team.completed":
        await handle_team_completed(event["data"])
    
    return {"status": "ok"}
```

### Node.js Example (Express)

```javascript
const express = require('express');
const crypto = require('crypto');

const app = express();
app.use(express.json({ verify: (req, res, buf) => { req.rawBody = buf } }));

const WEBHOOK_SECRET = 'your-webhook-secret';

app.post('/webhook', (req, res) => {
  const signature = req.headers['x-opensin-signature'];
  const expected = crypto
    .createHmac('sha256', WEBHOOK_SECRET)
    .update(req.rawBody)
    .digest('hex');
  
  if (signature !== expected) {
    return res.status(401).json({ error: 'Invalid signature' });
  }
  
  const event = req.body;
  
  switch (event.type) {
    case 'agent.completed':
      handleAgentCompleted(event.data);
      break;
    case 'agent.failed':
      handleAgentFailed(event.data);
      break;
    case 'team.completed':
      handleTeamCompleted(event.data);
      break;
  }
  
  res.json({ status: 'ok' });
});
```

## Event Subscription (In-App)

Subscribe to events directly in your code:

```python
from opensin import EventSubscriber

subscriber = EventSubscriber()

@subscriber.on("agent.completed")
async def on_agent_completed(event):
    print(f"Agent {event.data['agent_id']} completed task")
    await notify_user(event.data)

@subscriber.on("agent.failed")
async def on_agent_failed(event):
    print(f"Agent {event.data['agent_id']} failed: {event.data['error']}")
    await alert_team(event.data)

@subscriber.on("team.completed")
async def on_team_completed(event):
    print(f"Team {event.data['team_id']} completed: {event.data['results']}")
    await save_results(event.data)

# Start listening
await subscriber.start()
```

## Event Filtering

Filter events by agent, team, or type:

```python
# Only events from specific agent
subscriber.filter(agent_id="researcher")

# Only events from specific team
subscriber.filter(team_id="research-team")

# Only specific event types
subscriber.filter(event_types=["agent.completed", "agent.failed"])

# Combine filters
subscriber.filter(
    agent_id="researcher",
    event_types=["agent.completed"]
)
```

## Retry Policy

Webhooks are retried on failure:

| Attempt | Delay | Max Attempts |
|---------|-------|--------------|
| 1 | Immediate | - |
| 2 | 1 minute | - |
| 3 | 5 minutes | - |
| 4 | 30 minutes | - |
| 5 | 2 hours | Final attempt |

## Security

### Signature Verification

All webhook payloads are signed with HMAC-SHA256:

```
X-OpenSIN-Signature: sha256=<hex-signature>
X-OpenSIN-Timestamp: 1712217600
X-OpenSIN-Event: agent.completed
```

### Best Practices

1. Always verify signatures
2. Check timestamps (reject old events)
3. Use HTTPS endpoints
4. Implement idempotency
5. Log all webhook deliveries

## Monitoring

### Webhook Dashboard

```bash
# View webhook delivery status
opensin webhook status <webhook-id>

# View recent deliveries
opensin webhook deliveries <webhook-id> --limit 50

# Retry failed delivery
opensin webhook retry <delivery-id>
```

### Metrics

| Metric | Description |
|--------|-------------|
| `webhook.deliveries.total` | Total deliveries |
| `webhook.deliveries.success` | Successful deliveries |
| `webhook.deliveries.failed` | Failed deliveries |
| `webhook.latency.p99` | 99th percentile latency |
| `webhook.retries.total` | Total retries |

## Next Steps

- [Events API](/api/events)
- [Monitoring Guide](/guide/monitoring)
- [Integration Guides](/integrations/telegram)
