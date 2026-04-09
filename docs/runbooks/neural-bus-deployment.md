# Neural-Bus OCI Deployment Runbook

**Status:** LIVE ✅  
**Deployed:** 2026-04-09  
**Host:** OCI VM `ubuntu@92.5.60.87`

---

## Infrastructure

| Service | Container | Host Port | Container Port | Status |
|---------|-----------|-----------|----------------|--------|
| NATS JetStream | `opensin-neural-bus-nats-1` | 4222 (client), 8222 (dashboard) | 4222, 8222 | ✅ RUNNING |
| Redis | `opensin-neural-bus-redis-1` | 6380 | 6379 | ✅ RUNNING |
| pgvector (Ouroboros DNA) | `opensin-neural-bus-pgvector-1` | 5435 | 5432 | ✅ RUNNING |

**Port mapping rationale:**
- Redis remapped `6379→6380`: avoids conflict with `room-04-redis-cache` container on OCI
- pgvector remapped `5432→5435`: avoids conflict with `supabase-db` (5433) and `supabase-pooler` (5434)
- NATS ports 4222 and 8222 were free — no remapping needed

---

## Verified Endpoints

```bash
# NATS client (JetStream enabled)
nats://92.5.60.87:4222

# NATS monitoring dashboard
http://92.5.60.87:8222/varz

# Redis (password required)
redis://:${REDIS_PASSWORD}@92.5.60.87:6380

# pgvector / Ouroboros DNA DB
postgresql://opensin:${PG_PASSWORD}@92.5.60.87:5435/ouroboros_dna
```

---

## Connection Strings for Agents

In any A2A agent, inject via environment or `opencode` secrets:

```python
NATS_URL = "nats://92.5.60.87:4222"
REDIS_URL = "redis://:REDIS_PASSWORD@92.5.60.87:6380"
PG_DSN   = "postgresql://opensin:PG_PASSWORD@92.5.60.87:5435/ouroboros_dna"
```

Credentials are stored in `~/OpenSIN-Neural-Bus/.env` on the OCI VM. **Never commit `.env` to the repo.**

---

## Management Commands (run on OCI via SSH)

```bash
ssh ubuntu@92.5.60.87

# Status
cd ~/OpenSIN-Neural-Bus && docker compose ps

# Logs
docker compose logs -f nats
docker compose logs -f redis
docker compose logs -f pgvector

# Restart single service
docker compose restart nats

# Full teardown (data preserved in ./data/)
docker compose down

# Full teardown + wipe data
docker compose down -v && rm -rf data/
```

---

## Disk Space Note

OCI VM disk was 100% full on 2026-04-09 due to `/tmp/` accumulation:
- Deleted-but-open files from previous runs
- Stale Docker images (3.1GB reclaimed via `docker image prune -a`)
- Stale `.sqlite` / `.tar.gz` test artifacts in `/tmp/`

**Action taken:** `docker image prune -a -f` freed 3.1GB. Neural-Bus images required ~600MB of that space.

**Monitor disk:** `df -h /` should stay below 95% to allow Docker operations.

---

## NATS Subject Topology

| Subject | Publisher | Subscriber | Purpose |
|---------|-----------|------------|---------|
| `opensin.capability.gap` | Any agent detecting a missing tool | A2A-SIN-Medusa | Trigger MCP synthesis |
| `opensin.capability.resolved` | A2A-SIN-Medusa | Fleet registry, Zeus | New MCP server is ready |
| `opensin.capability.failed` | A2A-SIN-Medusa | Zeus, Telegram alert | Synthesis failed after 3 retries |
| `opensin.fleet.heartbeat` | All A2A agents | SIN-Monitor (planned) | Fleet liveness tracking |

---

## Ouroboros DNA Database

The `ouroboros_dna` PostgreSQL database stores:
- **Capability Registry**: All synthesized MCP servers (name, version, manifest, code hash)
- **Procedural Lessons**: Successful and failed synthesis patterns for few-shot recall
- **pgvector extension**: Enables semantic similarity search over lesson embeddings

To enable pgvector extension after first boot:
```sql
-- Run once inside pgvector container
CREATE EXTENSION IF NOT EXISTS vector;
```

```bash
docker exec -it opensin-neural-bus-pgvector-1 \
  psql -U opensin -d ouroboros_dna -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

---

## Related Repos

| Repo | Purpose |
|------|---------|
| [OpenSIN-AI/OpenSIN-Neural-Bus](https://github.com/OpenSIN-AI/OpenSIN-Neural-Bus) | Infrastructure + TypeScript SDK + Python Ouroboros SDK |
| [OpenSIN-AI/A2A-SIN-Medusa](https://github.com/OpenSIN-AI/A2A-SIN-Medusa) | Self-Extender agent that synthesizes new MCP servers |

**Open Issues:**
- [Medusa #1](https://github.com/OpenSIN-AI/A2A-SIN-Medusa/issues/1): Wire Medusa to Neural-Bus NATS event mesh
- [Medusa #2](https://github.com/OpenSIN-AI/A2A-SIN-Medusa/issues/2): Integrate Ouroboros Memory into Medusa synthesis loop
- [Neural-Bus #1](https://github.com/OpenSIN-AI/OpenSIN-Neural-Bus/issues/1): Initialize the Decentralized Event-Sourcing Mesh (NATS/Redis)
