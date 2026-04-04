# Best Practices: Security

## Overview

Security best practices for OpenSIN agents.

## 1. Never Hardcode Credentials

```javascript
// ❌ Bad
const agent = new Agent({
  apiKey: 'sk-1234567890'
});

// ✅ Good
const agent = new Agent({
  apiKey: process.env.OPENAI_API_KEY
});
```

## 2. Validate All Inputs

```javascript
agent.on('message', async (msg) => {
  // Validate input
  if (!msg.text || typeof msg.text !== 'string') {
    await agent.respond('Invalid input');
    return;
  }

  // Process message
  const response = await processMessage(msg.text);
  await agent.respond(response);
});
```

## 3. Implement Rate Limiting

```javascript
const agent = new Agent({
  name: 'my-agent',
  rateLimit: {
    messagesPerMinute: 60,
    tokensPerMinute: 10000
  }
});
```

## 4. Log All Actions

```javascript
const agent = new Agent({
  name: 'my-agent',
  logging: {
    level: 'info',
    destination: 'file',
    path: './logs/agent.log'
  }
});
```

## 5. Use HTTPS

Always use HTTPS for API communications.

## 6. Regular Security Audits

Regularly audit your agents for security vulnerabilities.

## Next Steps
- [Performance](/best-practices/performance)
- [Testing](/best-practices/testing)
