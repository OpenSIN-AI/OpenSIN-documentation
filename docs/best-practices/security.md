# 🔒 Security Guide

> **Stand:** 2026-04-04

## Authentication

### OpenCode Auth

| Method | Status | Notes |
|--------|--------|-------|
| **OpenRouter API Key** | ✅ Configured | Free models (qwen3.6-plus:free) |
| **Antigravity OAuth** | ✅ Configured | Claude, Gemini via OAuth |
| **Google Service Account** | ✅ Configured | Google Docs/Drive access |

### n8n Auth

| Method | Status | Notes |
|--------|--------|-------|
| **JWT API Key** | ✅ Active | Created via REST API |
| **Owner Account** | ✅ Active | zukunftsorientierte.energie@gmail.com |

### Supabase Auth

| Method | Status | Notes |
|--------|--------|-------|
| **Service Role Key** | ✅ Active | Full database access |
| **Anon Key** | ✅ Active | Public API access |

## Token Management

### Token Pool

| Provider | Count | Status |
|----------|-------|--------|
| **Antigravity** | 12 | ✅ Active |
| **OpenAI** | 6 | ✅ Active |

### Token Rotation

- Automatic rotation via `opencode-antigravity-auth` plugin
- Manual rotation: `sin-rotator`
- Fallback: `nemotron-3-super-free`

## Secrets Management

| Secret | Location | Access |
|--------|----------|--------|
| **OpenRouter API Key** | opencode.json | Local only |
| **n8n API Key** | n8n.env | Local + OCI VM |
| **HF Token** | ~/.huggingface/token | Local only |
| **GitHub Token** | gh CLI config | Local only |
| **Google SA Key** | auth/google/ | Local only |

## Security Best Practices

1. **Never commit secrets** to git repositories
2. **Use environment variables** for API keys
3. **Rotate tokens regularly** via sin-rotator
4. **Use separate auth per machine** — never sync auth files
5. **Enable 2FA** on all accounts where possible

---

*Last updated: 2026-04-04 by SIN-Zeus*
