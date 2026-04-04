# Hugging Face Spaces Deployment

> **Status:** ⏸️ Planned | **Type:** Cloud Deployment

## Overview

HF Spaces provide free GPU-enabled hosting for OpenSIN agent interfaces.

## Creating a Space

```bash
curl -X POST "https://huggingface.co/api/repos/create"   -H "Authorization: Bearer $HF_TOKEN"   -H "Content-Type: application/json"   -d '{"name": "sin-solver", "type": "space", "organization": "delqhi", "sdk": "docker"}'
```

## Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## Rate Limits

- 20 spaces per day creation limit
- Free tier: CPU only, 16GB RAM
- Paid tier: GPU available

---

*Last updated: 2026-04-04 by SIN-Zeus*
