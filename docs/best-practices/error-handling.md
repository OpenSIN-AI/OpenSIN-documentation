# Error Handling Best Practices

> **Status:** ✅ Active | **Type:** Quality

## Overview

Error handling guidelines for OpenSIN-AI projects.

## Principles

1. **Fail fast** — detect errors early
2. **Fail safe** — graceful degradation
3. **Log everything** — structured logging
4. **Alert on critical** — Telegram notifications

## Patterns

```typescript
try {
  await riskyOperation();
} catch (error) {
  logger.error("Operation failed", { error, context });
  await notifyTelegram(`Error: ${error.message}`);
  throw new OperationalError("Failed", { cause: error });
}
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
