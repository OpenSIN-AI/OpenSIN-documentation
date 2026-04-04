# 🚀 Deployment Guide

> **Stand:** 2026-04-04

## n8n Workflows

### Import Workflows

```bash
# Copy workflow JSONs to OCI VM
scp n8n-workflows/*.json ubuntu@92.5.60.87:/tmp/n8n-import/

# Import via n8n CLI
ssh ubuntu@92.5.60.87 "docker exec n8n-n8n-1 n8n import:workflow --separate --input=/tmp/n8n-import/"
```

### Activate Workflows

```bash
# Via sin-n8n CLI
sin-n8n activate "workflow-name"

# Via API
curl -X POST http://92.5.60.87:5678/api/v1/workflows/{id}/activate   -H "X-N8N-API-KEY: $N8N_API_KEY"
```

## HF Spaces Deployment

```bash
# Create space via API
curl -X POST "https://huggingface.co/api/repos/create"   -H "Authorization: Bearer $HF_TOKEN"   -H "Content-Type: application/json"   -d '{"name": "sin-solver", "type": "space", "organization": "delqhi", "sdk": "docker"}'

# Note: Rate limited to 20 spaces per day
```

## OpenCode Sync

```bash
# Sync config to OCI VM
sin-sync

# Verify sync
ssh ubuntu@92.5.60.87 "python3 -c "import json; print(json.load(open('/home/ubuntu/.config/opencode/opencode.json'))['model'])""
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
