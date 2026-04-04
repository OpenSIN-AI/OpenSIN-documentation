# Cloudflare Workers Deployment

> **Status:** ✅ Active | **Type:** Edge Deployment

## Overview

Cloudflare Workers deploy OpenSIN edge functions for low-latency API processing.

## Configuration

```toml
name = "opensin-worker"
main = "src/index.ts"
compatibility_date = "2026-04-04"

[vars]
API_URL = "http://92.5.60.87:5678"
```

## Deployment

```bash
wrangler deploy
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
