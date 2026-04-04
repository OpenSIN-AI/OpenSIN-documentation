# Backup and Restore

> **Status:** ✅ Active | **Type:** Data Protection

## Overview

Backup and restore procedures for OpenSIN infrastructure.

## Backup Schedule

| Component | Frequency | Retention |
|-----------|-----------|-----------|
| n8n workflows | Daily | 30 days |
| Supabase database | Hourly | 7 days |
| OpenCode config | On change | Unlimited |

## Backup Commands

```bash
# n8n backup
docker cp n8n-n8n-1:/home/node/.n8n/database.sqlite /backup/n8n.db

# Supabase backup
docker exec supabase-db pg_dump -U postgres > /backup/supabase.sql
```

## Restore

```bash
# n8n restore
docker cp /backup/n8n.db n8n-n8n-1:/home/node/.n8n/database.sqlite

# Supabase restore
cat /backup/supabase.sql | docker exec -i supabase-db psql -U postgres
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
