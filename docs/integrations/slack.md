# Slack Integration

Connect OpenSIN agents to Slack for team automation.

## Overview

The Slack integration enables agents to:
- Respond to messages in channels
- Create and manage workflows
- Send notifications and alerts
- Handle slash commands
- Post formatted messages with blocks

## Setup

### 1. Create Slack App

1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Create new app with Bot Token Scopes:
   - `chat:write`
   - `channels:read`
   - `im:read`
3. Install app to workspace

### 2. Configure OpenSIN

```bash
opensin integration create slack \
  --bot-token xoxb-YOUR_TOKEN \
  --signing-secret YOUR_SECRET
```

## Agent Configuration

```python
from opensin import Agent
from opensin.integrations import Slack

slack = Slack(bot_token="xoxb-...", signing_secret="...")

assistant = Agent(
    name="slack-assistant",
    model="gpt-4",
    system_prompt="You are a helpful Slack assistant.",
    tools=["slack_post_message", "slack_get_channel", "slack_react"]
)
```

## Common Workflows

### Channel Monitoring

```python
@slack.on("message")
async def handle_message(event):
    if event.channel == "#support":
        response = await assistant.send(event.text)
        await slack.post_message(event.channel, response.content)
```

### Alert Notifications

```python
# Send alerts to channel
await slack.post_message(
    channel="#alerts",
    text="🚨 Production issue detected",
    blocks=[alert_block]
)
```

## Next Steps

- [Webhooks & Events](/guide/webhooks-events)
- [Team Orchestration](/guide/team-orchestration)
