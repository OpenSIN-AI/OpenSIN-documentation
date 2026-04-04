# Authentication Architecture

> **Status:** ✅ Active | **Type:** Security Design

## Overview

Authentication flow for OpenSIN-AI services.

## Auth Flow

```
User → OpenCode → OAuth Provider → Token → API Access
                        ↓
                  Antigravity Plugin
                        ↓
                  Token Rotation
```

## Auth Methods

| Service | Method | Provider |
|---------|--------|----------|
| OpenCode | OAuth | Google/Antigravity |
| n8n | JWT | Local |
| Supabase | API Key | Supabase |
| GitHub | OAuth | GitHub |

---

*Last updated: 2026-04-04 by SIN-Zeus*
