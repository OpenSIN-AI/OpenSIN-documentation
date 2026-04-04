# A2A-SIN-Team-Google-Apps — Setup Guide

> **Repository:** A2A-SIN-Team-Google-Apps | **Organization:** OpenSIN-AI | **Status:** ✅ Active

## Prerequisites

- Node.js 18+ or Python 3.11+
- Git 2.30+
- OpenCode CLI
- Docker (for local development)
- Access to OpenSIN-AI organization

## Installation

```bash
# Clone the repository
git clone git@github.com:OpenSIN-AI/A2A-SIN-Team-Google-Apps.git
cd A2A-SIN-Team-Google-Apps

# Install dependencies
npm install  # or pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your credentials
```

## Configuration

```bash
# Link to OpenCode
ln -s ~/.config/opencode .opencode

# Configure local settings
cp .opencode/settings.example.json .opencode/settings.local.json
```

## Running

```bash
# Development mode
npm run dev  # or python -m a2a_sin_team_google_apps

# Production mode
npm run build
npm start
```

## Testing

```bash
# Run all tests
npm test  # or pytest

# Run specific test suite
npm run test:unit
npm run test:integration
npm run test:e2e
```

## Deployment

```bash
# Deploy to staging
npm run deploy:staging

# Deploy to production
npm run deploy:production
```

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Dependencies fail to install | Clear cache: `npm cache clean --force` |
| Tests fail locally | Check environment variables |
| Deployment fails | Verify CI/CD pipeline configuration |

## Related Repositories

- [OpenSIN-backend](./OpenSIN-backend.md)
- [OpenSIN-documentation](./OpenSIN-documentation.md)

---

*Last updated: 2026-04-04 by SIN-Zeus*
