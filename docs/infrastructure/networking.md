# Networking Configuration

> **Status:** ✅ Active | **Type:** Network Setup

## Overview

OpenSIN networking configuration for secure communication between services.

## Network Topology

```
Internet → Cloudflare Tunnel → OCI VM → Docker Network → Services
```

## Ports

| Service | Port | Access |
|---------|------|--------|
| n8n | 5678 | Public (via tunnel) |
| Supabase | 54321 | Public (via tunnel) |
| Supabase Studio | 3004 | Private |
| Aurora | 8080 | Private |

## Security

- All public access via Cloudflare tunnel
- Internal services on private network
- Firewall rules restrict access

---

*Last updated: 2026-04-04 by SIN-Zeus*
