---
title: "Telegram Bot Agent"
---

# Telegram Bot Agent Example

Build an A2A agent that operates a Telegram bot for automated notifications, command handling, and fleet monitoring.

## Overview

Every OpenSIN agent should have its own Telegram bot for:
- Receiving commands from operators
- Sending alerts and status updates
- Delivering task results
- Escalation notifications

## Setup

### 1. Create the Bot with BotFather

```
/newbot
Bot name: SIN Code Analyzer Bot
Username: sin_code_analyzer_bot
```

Save the token you receive.

### 2. Register with OpenSIN

```bash
# Register the bot
sin-telegrambot register \
  --token "7123456789:AAH..." \
  --name "sin-code-analyzer"

# Bootstrap chat_id (auto-sends /start)
sin-telegrambot bootstrap --name "sin-code-analyzer"

# Set command menu
sin-telegrambot set-commands \
  --bot "sin-code-analyzer" \
  --commands '[
    {"command":"status","description":"Show agent health status"},
    {"command":"analyze","description":"Analyze a GitHub repo"},
    {"command":"report","description":"Get daily summary report"},
    {"command":"help","description":"Show available commands"}
  ]'
```

### 3. Implement Command Handlers

```typescript
import { SINTelegramBot } from '@opensin/agent-sdk'

const bot = new SINTelegramBot({
  name: 'sin-code-analyzer',
  commands: {
    '/status': async (msg) => {
      const health = await checkHealth()
      return `Agent Status: ${health.status}\n` +
             `Uptime: ${health.uptime}\n` +
             `Tasks completed: ${health.tasksCompleted}`
    },

    '/analyze': async (msg) => {
      const repo = msg.text.split(' ')[1]
      if (!repo) return 'Usage: /analyze owner/repo'

      await bot.reply(msg, 'Starting analysis...')
      const results = await analyzeRepo(repo)

      return `Analysis complete for ${repo}:\n\n` +
             `Files: ${results.files}\n` +
             `Issues found: ${results.issues}\n` +
             `Score: ${results.score}/100`
    },

    '/report': async (msg) => {
      const report = await generateDailyReport()
      return report
    },
  },
})
```

### 4. Send Proactive Notifications

```typescript
// Alert on task completion
agent.on('task:complete', async (task) => {
  await bot.send(
    `Task completed: ${task.title}\n` +
    `Duration: ${task.duration}ms\n` +
    `Result: ${task.status}`
  )
})

// Alert on errors
agent.on('task:error', async (task, error) => {
  await bot.send(
    `Task FAILED: ${task.title}\n` +
    `Error: ${error.message}\n` +
    `Auto-creating GitHub issue...`
  )
})

// Send with inline keyboard buttons
await bot.send(
  'New PR requires review',
  {
    buttons: [[
      { text: 'Approve', callback_data: 'pr_approve_123' },
      { text: 'Reject', callback_data: 'pr_reject_123' },
    ]]
  }
)
```

### 5. Integrate with n8n

Create an n8n workflow that routes Telegram messages to your agent:

```bash
sin-n8n create telegram-notify \
  --name "Code-Analyzer-Telegram" \
  --vars BOT_TOKEN=7123456789:AAH... \
         CHAT_ID=your_chat_id \
  --activate
```

## Using the MCP Tools

The `sin-telegrambot` MCP provides these tools:

| Tool | Description |
|------|-------------|
| `sin_telegrambot_send` | Send a message (HTML formatting supported) |
| `sin_telegrambot_send_document` | Send a file/document |
| `sin_telegrambot_status` | Check bot identity and webhook info |
| `sin_telegrambot_updates` | Fetch recent messages (polling) |
| `sin_telegrambot_set_webhook` | Set webhook URL |
| `sin_telegrambot_set_commands` | Set the command menu |

### Example: Send a Formatted Report

```typescript
await sinTelegramBot.send({
  bot: 'sin-code-analyzer',
  message: `
<b>Daily Code Analysis Report</b>

<pre>
Repository    Issues  Score
──────────────────────────
opensin-code  3       92/100
opensin-sdk   0       98/100
agent-sdk     1       95/100
</pre>

<i>Generated at ${new Date().toISOString()}</i>
  `,
  parse_mode: 'HTML',
})
```

### Example: Send a File

```typescript
await sinTelegramBot.sendDocument({
  bot: 'sin-code-analyzer',
  file: '/tmp/analysis-report.pdf',
  caption: 'Full analysis report for Q2 2026',
})
```

## Fleet Monitoring Pattern

The `A2A-SIN-TelegramBot` agent acts as fleet-wide incident monitor:

```
Agent Error → A2A-SIN-TelegramBot detects
            → Creates GitHub Issue (via SIN-GitHub-Issues)
            → Dispatches fix task (via SIN-Hermes)
            → Notifies operator via Telegram
            → Monitors fix progress
            → Closes issue when resolved
```

This creates a fully autonomous self-healing loop with human visibility through Telegram.

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
