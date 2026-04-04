# 🏗️ OpenSIN-AI Infrastructure

> **Stand:** 2026-04-04 | **Status:** ✅ All systems operational

## OCI VM (92.5.60.87)

### Services

| Service | Port | Status | Purpose |
|---------|------|--------|---------|
| **n8n** | 5678 | ✅ Active | Workflow automation |
| **Supabase** | 54321 | ✅ Active | Database |
| **Supabase Studio** | 3004 | ✅ Active | DB management UI |
| **Aurora** | 8080 | ✅ Active | LLM proxy |
| **sin-room13** | — | ✅ Active | Chat room |
| **Redis Cache** | — | ✅ Active | Caching layer |
| **LLM Tunnel** | — | ✅ Active | Cloudflare tunnel |

### Resource Usage

| Resource | Usage | Limit |
|----------|-------|-------|
| **CPU** | ~30% | 4 cores (A1.Flex) |
| **RAM** | ~6GB | 24GB |
| **Disk** | ~50GB | 200GB |
| **Network** | ~100Mbps | 480Mbps |

### Docker Containers

```
n8n-n8n-1: Up (healthy)
supabase-db: Up (healthy)
supabase-studio: Up (healthy)
supabase-auth: Up (healthy)
supabase-rest: Up (healthy)
supabase-realtime: Up (healthy)
supabase-storage: Up (healthy)
supabase-analytics: Up (healthy)
supabase-pooler: Up (healthy)
supabase-kong: Up (healthy)
supabase-meta: Up (healthy)
supabase-edge-functions: Up
supabase-vector: Up (healthy)
supabase-imgproxy: Up (healthy)
aurora: Up
llm-tunnel: Up
sin-room13: Up (healthy)
room-04-redis-cache: Up (healthy)
```

## HF Spaces

| Space | Status | Purpose |
|-------|--------|---------|
| delqhi/sin-solver | ❌ Not deployed | Main solver interface |
| delqhi/sin-chatroom | ❌ Not deployed | Chat interface |
| delqhi/sin-platform-auth | ❌ Not deployed | Auth service |

## Cloudflare

| Resource | Purpose |
|----------|---------|
| **DNS** | Domain management |
| **Workers** | Edge computing |
| **R2** | Object storage |
| **Tunnels** | Secure access to OCI VM |

---

*Last updated: 2026-04-04 by SIN-Zeus*
