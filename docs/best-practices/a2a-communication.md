---
title: "A2A Communication Best Practices"
---

# A2A Communication Best Practices

Guidelines for reliable, secure, and efficient Agent-to-Agent communication in the OpenSIN ecosystem.

## Protocol Fundamentals

### Message Structure

Every A2A message must follow this structure:

```typescript
interface A2AMessage {
  id: string              // UUID for tracking
  from: string            // Sender agent ID
  to: string              // Target agent ID
  type: 'request' | 'response' | 'notification' | 'error'
  content: unknown        // Task payload or response data
  metadata?: {
    priority: 'low' | 'normal' | 'high' | 'critical'
    timeout?: number      // ms until message expires
    correlationId?: string // Link related request/response
    retryCount?: number   // Current retry attempt
  }
}
```

### Communication Patterns

| Pattern | Use Case | Example |
|---------|----------|---------|
| Request/Response | Task delegation | Research agent → Data agent |
| Fire-and-Forget | Notifications | Status updates, logging |
| Pub/Sub | Broadcast | Fleet-wide announcements |
| Pipeline | Sequential processing | Data → Analysis → Report |

## Reliability

### Retry Strategy

Implement exponential backoff for failed deliveries:

```typescript
async function sendWithRetry(message: A2AMessage, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await a2aClient.send(message)
    } catch (error) {
      if (i === maxRetries - 1) throw error
      const delay = Math.pow(2, i) * 1000 // 1s, 2s, 4s
      await sleep(delay)
    }
  }
}
```

### Dead Letter Queue

Messages that fail after all retries go to a dead letter queue:

```typescript
interface DeadLetterEntry {
  originalMessage: A2AMessage
  failureReason: string
  failedAt: Date
  retryCount: number
}
```

### Idempotency

All A2A operations must be idempotent — processing the same message twice must not cause duplicate side effects:

```typescript
// Use correlationId to detect duplicates
const processed = await checkProcessed(message.correlationId)
if (processed) return { status: 'duplicate', id: message.correlationId }

// Process the message
const result = await handleMessage(message)

// Mark as processed
await markProcessed(message.correlationId)
```

## Security

### Authentication

All inter-agent communication requires JWT authentication:

```typescript
const response = await fetch('https://agent-b.opensin.ai/a2a/v1', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${jwt}`,
    'X-Agent-ID': 'sin-hermes',
    'X-Fleet-ID': 'production',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(taskPayload),
})
```

### Transport Encryption

- **Production**: HTTPS (TLS 1.3) required for all external communication
- **Internal**: Cloudflare Tunnels for zero-trust networking
- **Never** transmit credentials over plaintext HTTP

### Payload Validation

Validate all incoming messages before processing:

```typescript
function validateMessage(msg: unknown): A2AMessage {
  const schema = z.object({
    id: z.string().uuid(),
    from: z.string().min(1),
    to: z.string().min(1),
    type: z.enum(['request', 'response', 'notification', 'error']),
    content: z.unknown(),
    metadata: z.object({
      priority: z.enum(['low', 'normal', 'high', 'critical']).optional(),
      timeout: z.number().positive().optional(),
    }).optional(),
  })

  return schema.parse(msg)
}
```

## Performance

### Connection Pooling

Reuse connections to avoid handshake overhead:

```typescript
const pool = new A2AConnectionPool({
  size: 10,
  idleTimeout: 60_000,
  healthCheckInterval: 30_000,
})

// Get connection from pool
const conn = await pool.acquire()
try {
  await conn.send(message)
} finally {
  pool.release(conn)
}
```

### Message Batching

Batch independent messages to reduce network overhead:

```typescript
// Instead of sending individually
messages.forEach(msg => a2aClient.send(msg))

// Batch them
await a2aClient.sendBatch(messages)
```

### Timeout Configuration

Set appropriate timeouts based on message priority:

| Priority | Timeout | Retry Count |
|----------|---------|-------------|
| Critical | 30s | 5 |
| High | 60s | 3 |
| Normal | 120s | 2 |
| Low | 300s | 1 |

## Error Handling

### Error Response Format

Standardize error responses:

```typescript
interface A2AError {
  type: 'error'
  code: 'AGENT_UNAVAILABLE' | 'TIMEOUT' | 'INVALID_PAYLOAD' | 'RATE_LIMITED' | 'INTERNAL_ERROR'
  message: string
  details?: unknown
  retryable: boolean
}
```

### Circuit Breaker

Prevent cascading failures with circuit breakers:

```typescript
const circuit = new CircuitBreaker({
  failureThreshold: 5,
  resetTimeout: 30_000,
  halfOpenMaxCalls: 1,
})

circuit.execute(() => a2aClient.send(message))
```

## Monitoring

### Message Tracking

Track all messages for debugging and auditing:

```typescript
interface MessageLog {
  messageId: string
  correlationId?: string
  from: string
  to: string
  type: string
  status: 'sent' | 'delivered' | 'processed' | 'failed' | 'expired'
  timestamp: Date
  latency?: number
}
```

### Key Metrics

| Metric | Alert Threshold |
|--------|----------------|
| Message delivery rate | < 99% |
| Average latency | > 5s |
| Dead letter queue size | > 100 |
| Circuit breaker trips | > 3/hour |

## Checklist

Before deploying A2A communication:

- [ ] Message schema validated with Zod/JSON Schema
- [ ] JWT authentication configured
- [ ] Retry logic with exponential backoff implemented
- [ ] Idempotency handling via correlation IDs
- [ ] Circuit breaker for external agent calls
- [ ] Dead letter queue configured
- [ ] Timeout values set per priority level
- [ ] Error responses follow standard format
- [ ] Message logging enabled for debugging
- [ ] Transport uses HTTPS/TLS 1.3
