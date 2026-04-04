# Google Workspace Integration

Connect OpenSIN agents to Google Workspace for productivity automation.

## Overview

The Google Workspace integration enables agents to:
- Read and send emails via Gmail
- Create and manage Calendar events
- Access and edit Google Docs, Sheets, Slides
- Manage Google Drive files
- Send Chat messages

## Setup

### 1. Create Google Cloud Project

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create new project
3. Enable APIs:
   - Gmail API
   - Google Calendar API
   - Google Drive API
   - Google Docs API
   - Google Sheets API
4. Create OAuth 2.0 credentials
5. Configure consent screen

### 2. Configure OpenSIN

```bash
opensin integration create google-workspace \
  --client-id YOUR_CLIENT_ID \
  --client-secret YOUR_CLIENT_SECRET \
  --refresh-token YOUR_REFRESH_TOKEN
```

## Agent Configuration

```python
from opensin import Agent
from opensin.integrations import GoogleWorkspace

gws = GoogleWorkspace(
    client_id="...",
    client_secret="...",
    refresh_token="..."
)

assistant = Agent(
    name="workspace-assistant",
    model="gpt-4",
    system_prompt="You manage Google Workspace tasks.",
    tools=["gmail_send", "calendar_create", "drive_upload", "docs_create"]
)
```

## Common Workflows

### Email Triage

```python
@gws.on("gmail:new_email")
async def triage_email(event):
    email = await gws.gmail.get(event.message_id)
    priority = await assistant.send(f"Prioritize: {email.subject}\n{email.body}")
    if priority == "high":
        await assistant.send(f"Draft response to {email.from_address}")
```

### Meeting Preparation

```python
# Before each meeting
async def prepare_for_meeting(event_id):
    event = await gws.calendar.get(event_id)
    attendees = event.attendees
    agenda = await assistant.send(f"Create agenda for {event.title}")
    doc = await gws.docs.create(title=f"Agenda: {event.title}", content=agenda)
    await gws.calendar.update(event_id, attachments=[doc.url])
```

### Document Analysis

```python
# Analyze spreadsheet
data = await gws.sheets.read(spreadsheet_id, range="A1:Z100")
insights = await assistant.send(f"Analyze this data: {data}")
report = await gws.docs.create(title="Analysis Report", content=insights)
```

## Next Steps

- [n8n Workflows](/guide/n8n-workflows)
- [Webhooks & Events](/guide/webhooks-events)
