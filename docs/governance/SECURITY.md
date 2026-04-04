# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| Latest | ✅ |

## Reporting a Vulnerability

**Please do NOT open a public issue.**

Email: security@opensin.ai

We respond within 48 hours.

## Security Practices

### Secrets Management

- All credentials managed via environment variables or `sin-passwordmanager`
- No secrets in code or documentation
- `.env` files in `.gitignore`
- GitHub Secrets for CI/CD pipelines
- Regular secret rotation via auth-rotator systems

### Input Validation & Guardrails

- All agent inputs validated with Zod schemas
- Prompt injection detection on all inputs
- Jailbreak pattern detection
- PII detection (SSN, credit cards, API keys)
- Toxicity scoring on all outputs
- Hallucination detection for AI-generated content
- Invisible Unicode detection

### Agent Security

- All A2A agent operations logged to OpenSIN-Ledger
- Authorization token required for all agent actions
- Guardrails enforced on all inputs/outputs
- Sandboxing for untrusted code execution
- Allowlist for agent capabilities
- DM Pairing for unauthorized users

### Browser Automation Security

- Isolated Chrome profiles per rotation (fresh profile each run)
- No Playwright/Docker containers for auth flows (nodriver only)
- Singleton lock cleanup before Chrome launch
- Visible mode for development (no headless during testing)
- Separate profiles for work vs. personal use

### Network Security

- HTTPS for all external connections
- TLS certificate validation
- Allowlists for outbound connections
- No internal ports exposed publicly
- Rate limiting on all API endpoints
- CORS headers configured correctly

### Dependency Security

- Regular `npm audit` / `bun audit` scans
- A2A Dependency Agent replaces Dependabot (weekly checks)
- Pinned dependency versions
- `--frozen-lockfile` in CI/CD
- New dependencies reviewed before adding

### Container Security

- Non-root user in all Dockerfiles
- Image vulnerability scanning (trivy, grype)
- Minimal base images (alpine, distroless)
- Resource limits (CPU, memory) set
- Read-only filesystem where possible
- No host filesystem mounts

### Audit & Compliance

- All operations logged to OpenSIN-Ledger
- A2A Governance Agent enforces branch protection
- No force pushes to `main`
- PR required before merging to `main`
- CI/CD pipeline must pass before merge
- Minimum 1 approval required
