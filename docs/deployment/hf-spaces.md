# HF Spaces Deployment Guide

## Quick Deploy
```bash
python3 ~/.config/opencode/skills/create-hf-space-vm/scripts/create_hf_space.py \
  --slug sin-my-agent \
  --namespace easeeeclip \
  --hardware cpu-basic
```

## Available HF Accounts
| Account | Token Source | Status |
|---------|-------------|--------|
| easeeeclip | sin-passwordmanager (HF_API_9) | ✅ Available |
| OpenJerro | sin-passwordmanager (HF_TOKEN_1) | ❌ Rate Limited |
| mazingaimaze | sin-passwordmanager (HF_TOKEN_2) | ❌ Rate Limited |
| funviral | sin-passwordmanager (HF_TOKEN_3) | ❌ Rate Limited |
| lolitaexibabe | sin-passwordmanager (HF_TOKEN_4) | ❌ Rate Limited |
| Mulimul | sin-passwordmanager (HF_TOKEN_5) | ❌ Rate Limited |
| appimepp | sin-passwordmanager (HF_TOKEN_6) | ❌ Rate Limited |
| account7 | sin-passwordmanager (HF_TOKEN_7) | ❌ Rate Limited |
| delqhi | sin-passwordmanager (HUGGINGFACE_TOKEN) | ❌ Auth Error |

## Rate Limits
- **20 space creations per day per account**
- Resets every 24 hours
- Use different accounts to bypass limit

## Hardware Options
| Hardware | Cost | Use Case |
|----------|------|----------|
| cpu-basic | FREE | All A2A agents |
| cpu-upgrade | $21.60/mo | Heavy workloads |
| gpu-t4-small | Paid | ML inference |

**Rule:** ALWAYS use cpu-basic for A2A agents ($0/month)
