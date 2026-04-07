---
title: "Error Handling Best Practices"
---

# Error Handling Best Practices

Patterns for robust error handling, recovery, and resilience in OpenSIN agents and workflows.

## Error Classification

### Error Types

```typescript
enum ErrorType {
  // Recoverable
  RateLimit = 'rate_limit',
  Timeout = 'timeout',
  ConnectionLost = 'connection_lost',
  ModelUnavailable = 'model_unavailable',

  // Retryable
  TransientFailure = 'transient_failure',
  ServiceDegraded = 'service_degraded',

  // Fatal
  InvalidConfiguration = 'invalid_config',
  AuthenticationFailed = 'auth_failed',
  PermissionDenied = 'permission_denied',
  InvalidInput = 'invalid_input',
}

interface OpenSINError extends Error {
  type: ErrorType
  recoverable: boolean
  retryable: boolean
  context?: Record<string, unknown>
  timestamp: number
}
```

## Retry Patterns

### Exponential Backoff

```typescript
async function withRetry<T>(
  fn: () => Promise<T>,
  options: RetryOptions = {}
): Promise<T> {
  const {
    maxRetries = 3,
    baseDelay = 1000,
    maxDelay = 30_000,
    jitter = true,
  } = options

  let lastError: Error | undefined

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn()
    } catch (error) {
      lastError = error as Error

      if (!isRetryable(error)) {
        throw error
      }

      if (attempt === maxRetries) {
        break
      }

      const delay = Math.min(
        baseDelay * Math.pow(2, attempt),
        maxDelay
      )
      const jitteredDelay = jitter
        ? delay * (0.5 + Math.random())
        : delay

      await sleep(jitteredDelay)
    }
  }

  throw new Error(
    `Operation failed after ${maxRetries + 1} attempts: ${lastError?.message}`
  )
}
```

### Circuit Breaker

```typescript
class CircuitBreaker {
  private failures = 0
  private state: 'closed' | 'open' | 'half-open' = 'closed'
  private readonly threshold: number
  private readonly resetTimeout: number

  constructor(threshold = 5, resetTimeout = 60_000) {
    this.threshold = threshold
    this.resetTimeout = resetTimeout
  }

  async execute<T>(fn: () => Promise<T>): Promise<T> {
    if (this.state === 'open') {
      throw new Error('Circuit breaker is open — request blocked')
    }

    try {
      const result = await fn()
      this.onSuccess()
      return result
    } catch (error) {
      this.onFailure()
      throw error
    }
  }

  private onSuccess() {
    this.failures = 0
    this.state = 'closed'
  }

  private onFailure() {
    this.failures++
    if (this.failures >= this.threshold) {
      this.state = 'open'
      setTimeout(() => {
        this.state = 'half-open'
      }, this.resetTimeout)
    }
  }
}
```

## Agent Loop Error Handling

### Graceful Degradation

```typescript
const agent = new AgentLoop({
  maxTurns: 20,
  errorHandling: {
    onToolError: 'retry', // retry | skip | abort
    maxRetries: 3,
    onModelTimeout: 'retry',
    modelTimeoutMs: 60_000,
    onContextOverflow: 'compress',
  },
})

try {
  const result = await agent.run('Complex task')
} catch (error) {
  if (error.type === ErrorType.RateLimit) {
    // Wait and retry
    await sleep(error.retryAfter || 60_000)
    return await agent.run('Complex task')
  }

  if (error.type === ErrorType.ModelUnavailable) {
    // Switch to fallback model
    agent.setModel('gpt-4o-mini')
    return await agent.run('Complex task')
  }

  // Log and notify
  await logError(error)
  await notifyOperator({ type: 'agent_failure', error })
  throw error
}
```

## Input Validation

### Schema Validation

```typescript
import { z } from 'zod'

const ToolArgsSchema = z.object({
  path: z
    .string()
    .min(1)
    .refine((p) => !p.includes('..'), 'Path traversal not allowed')
    .refine((p) => p.startsWith('/workspace/'), 'Path must be in workspace'),
  command: z.string().optional(),
  timeout: z.number().max(30_000).optional(),
})

function validateToolArgs(raw: unknown) {
  const result = ToolArgsSchema.safeParse(raw)
  if (!result.success) {
    throw new ValidationError(
      `Invalid tool arguments: ${result.error.message}`
    )
  }
  return result.data
}
```

## Logging

### Structured Error Logging

```typescript
function logError(error: OpenSINError, context: LogContext) {
  const entry = {
    timestamp: new Date().toISOString(),
    level: error.recoverable ? 'warn' : 'error',
    type: error.type,
    message: error.message,
    stack: error.stack,
    context,
    agentId: context.agentId,
    sessionId: context.sessionId,
  }

  // Redact sensitive data
  const sanitized = sanitizeLogEntry(entry)

  // Send to LogCenter
  logClient.send(sanitized)
}

function sanitizeLogEntry(entry: Record<string, unknown>) {
  const sensitive = ['apiKey', 'token', 'password', 'secret', 'auth']
  const sanitized = { ...entry }

  for (const key of sensitive) {
    if (sanitized[key]) {
      sanitized[key] = '***REDACTED***'
    }
  }

  if (sanitized.context) {
    sanitized.context = sanitizeLogEntry(
      sanitized.context as Record<string, unknown>
    )
  }

  return sanitized
}
```

## Recovery Strategies

| Error Type | Strategy | Action |
|------------|----------|--------|
| Rate limit | Wait + retry | Sleep for `retryAfter`, then retry |
| Timeout | Retry with smaller context | Compress context, retry |
| Connection lost | Reconnect | Re-establish connection, retry |
| Model unavailable | Fallback model | Switch to cheaper model |
| Context overflow | Compress | Use ContextCompressor |
| Invalid input | Reject | Return clear error message |
| Permission denied | Escalate | Notify operator |

## Checklist

- [ ] All errors classified (recoverable/retryable/fatal)
- [ ] Retry logic with exponential backoff
- [ ] Circuit breakers for external services
- [ ] Input validation on all tool arguments
- [ ] Structured error logging with redaction
- [ ] Fallback models configured
- [ ] Operator notifications for fatal errors
- [ ] Recovery strategies documented per error type
