# Best Practices: Testing

## Overview

Testing best practices for OpenSIN agents.

## 1. Write Unit Tests

```javascript
describe('My Agent', () => {
  it('should respond to greetings', async () => {
    const response = await agent.send('Hello!');
    expect(response).toContain('Hello');
  });

  it('should handle errors gracefully', async () => {
    const response = await agent.send('');
    expect(response.error).toBeDefined();
  });
});
```

## 2. Write Integration Tests

```javascript
describe('Team Integration', () => {
  it('should complete tasks', async () => {
    const result = await team.assign({
      task: 'Write a blog post',
      workflow: [
        { agent: 'researcher', task: 'Research' },
        { agent: 'writer', task: 'Write' }
      ]
    });
    expect(result.status).toBe('completed');
  });
});
```

## 3. Write End-to-End Tests

```javascript
describe('End-to-End', () => {
  it('should handle complete workflow', async () => {
    const response = await fetch('http://localhost:3000/api/message', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: 'Hello!' })
    });
    expect(response.status).toBe(200);
  });
});
```

## 4. Use Test Fixtures

```javascript
const testMessages = [
  'Hello!',
  'What is AI?',
  'Write a poem'
];
```

## 5. Mock External Services

```javascript
jest.mock('@opensin/core', () => ({
  Agent: jest.fn().mockImplementation(() => ({
    send: jest.fn().mockResolvedValue('Mock response'),
    start: jest.fn(),
    stop: jest.fn()
  }))
}));
```

## 6. Test Coverage

Aim for at least 80% code coverage.

```bash
npm test -- --coverage
```

## Next Steps
- [Agent Design](/best-practices/agent-design)
- [Security](/best-practices/security)
