# Passwordmanager (A2A-SIN-Passwordmanager)

The **A2A-SIN-Passwordmanager** is the central secrets authority for the OpenSIN ecosystem. Every agent, extension, and service retrieves credentials through it.

## Architecture

```
┌──────────────────────┐
│   A2A Agent / CLI    │
│   "spm run-action"   │
└──────────┬───────────┘
           │ JSON action
           ▼
┌──────────────────────┐
│  SIN-Passwordmanager │
│  (Node.js TypeScript)│
│                      │
│  Backends:           │
│  ├── gcloud ────────→│ Google Cloud Secret Manager
│  ├── keychain ──────→│ macOS Keychain
│  └── file ──────────→│ AES-256-GCM encrypted file
└──────────────────────┘
```

## Backend: Google Cloud Secrets (Default)

| Property | Value |
|----------|-------|
| **Secret naming** | `spm-{lowercase_name}` (dots replaced with dashes) |
| **Encryption** | AES-256 at rest (Google-managed) |
| **Replication** | Automatic multi-region |
| **Free tier** | 6 active secret versions, 10,000 access ops/month |
| **Auth** | Service account with `roles/secretmanager.admin` |

## Actions Reference

| Action | Parameters | Description |
|--------|-----------|-------------|
| `sin.passwordmanager.health` | — | Health check (backend, state, sample surface) |
| `sin.passwordmanager.secret.put` | `name`, `value`, `description?`, `tags?` | Store or update a secret |
| `sin.passwordmanager.secret.get` | `name`, `reveal?` | Retrieve a secret (masked or revealed) |
| `sin.passwordmanager.secret.delete` | `name` | Delete a secret |
| `sin.passwordmanager.secret.list` | — | List all secrets (metadata only) |
| `sin.passwordmanager.target.bind` | `name`, `target` | Bind a sync target to a secret |
| `sin.passwordmanager.target.list` | `name?` | List sync targets |
| `sin.passwordmanager.secret.sync` | `name`, `targetIds?` | Sync secret to bound targets |
| `sin.passwordmanager.secret.sync_all` | — | Sync all secrets to all targets |

## Sync Targets

The Passwordmanager can fan out secrets to external systems:

| Target Kind | Description |
|------------|-------------|
| `huggingface_space_secret` | Sets a secret on a Hugging Face Space |
| `github_actions_repo` | Sets a GitHub Actions secret on a repo |

## CLI

```bash
export SPM_SECRET_BACKEND=gcloud

spm run-action '{"action":"sin.passwordmanager.secret.put","name":"MY_KEY","value":"<DEIN_API_KEY>","description":"My API key","tags":["auth"]}'

spm run-action '{"action":"sin.passwordmanager.secret.get","name":"MY_KEY","reveal":true}'
```

## Setup

See [Onboarding Guide](/guide/onboarding) for automated setup, or the [OpenSIN-onboarding repo](https://github.com/OpenSIN-AI/OpenSIN-onboarding) for manual installation.

## Source Code

[OpenSIN-backend/a2a/team-infrastructure/A2A-SIN-Passwordmanager](https://github.com/OpenSIN-AI/OpenSIN-backend/tree/main/a2a/team-infrastructure/A2A-SIN-Passwordmanager)

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
