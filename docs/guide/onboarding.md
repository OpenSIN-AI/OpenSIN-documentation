# Onboarding & First-Run Setup

When a new user runs OpenSIN for the first time, the autonomous onboarding system handles all setup automatically.

## What Gets Configured

| Component | Description |
|-----------|-------------|
| **A2A-SIN-Passwordmanager** | Central secrets authority backed by Google Cloud Secret Manager |
| **Google Cloud Project** | GCP project with Secret Manager API and service account |
| **OpenSIN Bridge** | Chrome extension with CDP vision + multi-provider AI analysis |
| **Platform API Keys** | Groq, NVIDIA NIM, Hugging Face — free-tier accounts registered |

## Quick Start

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN-onboarding.git
cd OpenSIN-onboarding
./scripts/onboard.sh
```

## The 6 Phases

### Phase 1: System Bootstrap

Verifies all prerequisites: Node.js 18+, Python 3.11+, Chrome, gcloud CLI, GitHub CLI. Installs missing tools via Homebrew.

### Phase 2: GCP Project + Service Account

1. Authenticates with Google (browser-based OAuth via CDP)
2. Creates or reuses a GCP project
3. Enables the Secret Manager API
4. Creates `opensin-agent` service account with `secretmanager.admin` role
5. Generates JSON key file (stored at `~/.config/opencode/auth/google/service-account.json`)

### Phase 3: Passwordmanager

1. Clones and builds A2A-SIN-Passwordmanager from source (sparse checkout)
2. Configures `gcloud` as the default backend
3. Creates `spm` CLI at `~/.local/bin/spm`
4. Runs health check to verify connectivity

### Phase 4: Chrome Extension

1. Copies OpenSIN Bridge extension to `~/.config/sin/opensin-bridge/`
2. Provides instructions for loading in Chrome
3. Detects existing Chrome CDP sessions

### Phase 5: Platform Registration

Autonomously registers on free-tier AI platforms:

| Platform | Free Tier | Key Name |
|----------|-----------|----------|
| Groq | 14,400 req/day (vision) | `GROQ_API_KEY` |
| NVIDIA NIM | 1,000 calls/month | `NVIDIA_API_KEY` |
| Hugging Face | Unlimited CPU Spaces | `HUGGINGFACE_TOKEN` |
| GitHub | Auto-detected from `gh` CLI | `GITHUB_TOKEN` |

### Phase 6: Verification

Runs end-to-end checks: gcloud auth, Secret Manager access, PM health, spm CLI, extension files, key file permissions.

## Passwordmanager Architecture

The Passwordmanager supports 3 backends:

| Backend | Storage | Best For |
|---------|---------|----------|
| **gcloud** (default) | Google Cloud Secret Manager | Production, multi-machine |
| **keychain** | macOS Keychain | Local-only, single machine |
| **file** | AES-256-GCM encrypted file | Offline, portable |

### CLI Usage

```bash
export SPM_SECRET_BACKEND=gcloud

# Store a secret
spm run-action '{"action":"sin.passwordmanager.secret.put","name":"MY_KEY","value":"<DEIN_API_KEY>","description":"My API key","tags":["auth"]}'

# Retrieve (masked)
spm run-action '{"action":"sin.passwordmanager.secret.get","name":"MY_KEY"}'

# Retrieve (revealed)
spm run-action '{"action":"sin.passwordmanager.secret.get","name":"MY_KEY","reveal":true}'

# List all
spm run-action '{"action":"sin.passwordmanager.secret.list"}'

# Health check
spm run-action '{"action":"sin.passwordmanager.health"}'
```

### Security

- Secret **values** stored exclusively in Google Cloud Secret Manager (AES-256 encrypted)
- Service account key at `~/.config/opencode/auth/google/service-account.json` (permissions `600`)
- Local catalog contains metadata only (names, tags, targets — never values)
- Pre-commit hooks prevent accidental key commits

## Key Rotation

If a service account key is compromised:

```bash
gcloud auth login --no-launch-browser
gcloud iam service-accounts keys create /tmp/new-key.json \
  --iam-account=opensin-agent@YOUR_PROJECT.iam.gserviceaccount.com
cp /tmp/new-key.json ~/.config/opencode/auth/google/service-account.json
chmod 600 ~/.config/opencode/auth/google/service-account.json
gcloud auth activate-service-account --key-file=~/.config/opencode/auth/google/service-account.json
rm /tmp/new-key.json
```

## Further Reading

- [OpenSIN-onboarding repository](https://github.com/OpenSIN-AI/OpenSIN-onboarding)
- [Passwordmanager source](https://github.com/OpenSIN-AI/OpenSIN-backend/tree/main/a2a/team-infrastructure/A2A-SIN-Passwordmanager)
- [OpenSIN Bridge extension](https://github.com/OpenSIN-AI/OpenSIN-backend/tree/main/services/sin-chrome-extension)

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` — npm/pnpm sind verboten |
| **Antigravity-Only** | -10.0 | KEIN gemini-api Provider — nur `google/antigravity-*` |
| **Kommentar-Pflicht** | -6.0 | EXTREM umfangreiche Kommentare in ALLEN Code-Dateien |

→ [Alle Mandate](/best-practices/code-quality)
