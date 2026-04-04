# Tutorial: Build a SaaS Customer Support Agent

Build a production-ready customer support agent in 30 minutes.

## What You'll Build

A multi-agent system that:
- Receives support tickets via Slack/Email
- Classifies and prioritizes automatically
- Resolves common issues without human intervention
- Escalates complex issues to the right team
- Tracks resolution metrics

## Step 1: Setup

```bash
# Install OpenSIN
pip install opensin-sdk

# Create project
mkdir support-agent && cd support-agent
opensin init
```

## Step 2: Create the Triage Agent

```python
from opensin import Agent

triage_agent = Agent(
    name="triage",
    model="gpt-4",
    system_prompt="""You are a support ticket triage specialist.

Your job:
1. Classify ticket type (bug, feature, billing, account, other)
2. Determine priority (P0-critical, P1-high, P2-medium, P3-low)
3. Route to the right team
4. Check if it's a known issue

Respond with JSON:
{"type": "...", "priority": "P0|P1|P2|P3", "team": "...", "known_issue": true|false, "response": "..."}""",
    tools=["json_output", "knowledge_base_search"]
)
```

## Step 3: Create the Response Agent

```python
response_agent = Agent(
    name="responder",
    model="gpt-4",
    system_prompt="""You are a friendly, professional support agent.

Rules:
- Always be empathetic
- Provide specific, actionable solutions
- Include links to documentation
- If you can't solve it, explain what you'll do next""",
    tools=["knowledge_base_search", "template_library"]
)
```

## Step 4: Create the Escalation Agent

```python
escalation_agent = Agent(
    name="escalation",
    model="gpt-4",
    system_prompt="""You determine when to escalate to humans.

Escalate if:
- Customer is frustrated (sentiment < 0.3)
- Issue requires account access changes
- Bug requires code fix
- Billing dispute > $100
- Customer requests human agent

When escalating, include:
- Summary of issue
- What was already tried
- Customer sentiment
- Recommended team for escalation""",
    tools=["sentiment_analysis", "slack_notify"]
)
```

## Step 5: Create the Support Team

```python
from opensin import Team

support_team = Team(
    name="customer-support",
    agents=[triage_agent, response_agent, escalation_agent],
    strategy="pipeline",  # triage → respond → escalate_if_needed
    max_iterations=3
)
```

## Step 6: Connect to Slack

```python
from opensin.integrations import Slack

slack = Slack(bot_token="xoxb-...")

@slack.on("message")
async def handle_support_request(event):
    if event.channel != "#support":
        return
    
    # Process ticket
    result = await support_team.execute({
        "ticket": event.text,
        "customer": event.user,
        "channel": event.channel
    })
    
    # Send response
    if result.escalated:
        await slack.post_message("#support-team", f"🚨 Escalated: {result.summary}")
    else:
        await slack.post_message(event.channel, result.response)
```

## Step 7: Add Knowledge Base

```python
# Load your documentation
from opensin import KnowledgeBase

kb = KnowledgeBase()
kb.load_directory("./docs")
kb.load_url("https://your-docs.com/api")
kb.index()

# Agents can now search the KB
```

## Step 8: Deploy

```bash
# Deploy to production
opensin deploy hf \
  --space your-org/support-agent \
  --sdk gradio \
  --hardware cpu-basic

# Or deploy to AWS
opensin deploy aws \
  --service lambda \
  --region us-east-1
```

## Step 9: Monitor

```python
from opensin import Metrics

metrics = Metrics()

# Track key metrics
metrics.track("tickets_resolved", count=1)
metrics.track("escalation_rate", value=result.escalated)
metrics.track("response_time", value=result.duration)
metrics.track("customer_satisfaction", value=result.sentiment)
```

## Next Steps

- [Real-World Use Cases](/examples/use-cases)
- [Advanced Agent Patterns](/guide/advanced-agent-patterns)
- [Production Deployment](/guide/deployment-production)
