# Best Practices: Agent Design

## 1. Clear Purpose

Every agent should have a clear, focused purpose.

```javascript
// ✅ Good: Focused agent
const agent = new Agent({ name: 'researcher', capabilities: ['research', 'analyze'] });
```

## 2. Clear System Prompt

```javascript
const agent = new Agent({
  systemPrompt: 'You are a research assistant. Find relevant information and present it clearly.'
});
```

## 3. Error Handling

```javascript
agent.on('error', async (error) => {
  console.error('Agent error:', error);
  await agent.respond('I encountered an error. Please try again.');
});
```

## 4. Rate Limiting

```javascript
const agent = new Agent({ rateLimit: { messagesPerMinute: 60, tokensPerMinute: 10000 } });
```

## 5. Logging

```javascript
const agent = new Agent({ logging: { level: 'info', destination: 'file', path: './logs/agent.log' } });
```

## Next Steps
- [Security](/best-practices/security)
- [Performance](/best-practices/performance)
