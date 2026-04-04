# Token Pool Architecture

> **Status:** ✅ Active | **Type:** Resource Management

## Overview

Token pool manages LLM API tokens across the OpenSIN fleet.

## Architecture

```
Agent → Token Pool → Select Token → LLM API
              ↓
         Supabase DB
              ↓
        Rotation Logic
```

## Providers

| Provider | Tokens | Status |
|----------|--------|--------|
| Antigravity | 12 | ✅ Active |
| OpenAI | 6 | ✅ Active |

---

*Last updated: 2026-04-04 by SIN-Zeus*
