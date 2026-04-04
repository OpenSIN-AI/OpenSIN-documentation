# Best Practices: Performance

## Overview

Performance best practices for OpenSIN agents.

## 1. Use Appropriate Models

Choose models based on task complexity:
- Simple tasks: Use smaller, faster models
- Complex tasks: Use larger, more capable models

## 2. Implement Caching

```javascript
const cache = new Map();

async function getCachedResponse(key) {
  if (cache.has(key)) {
    return cache.get(key);
  }

  const response = await generateResponse();
  cache.set(key, response);
  return response;
}
```

## 3. Optimize Prompts

Keep prompts concise and focused.

## 4. Monitor Performance

```javascript
agent.on('response', (response) => {
  console.log(`Response time: ${response.time}ms`);
  console.log(`Tokens used: ${response.tokens}`);
});
```

## 5. Use Connection Pooling

For database and API connections, use connection pooling.

## Next Steps
- [Testing](/best-practices/testing)
- [Agent Design](/best-practices/agent-design)
