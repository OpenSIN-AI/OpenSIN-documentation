---
title: "Vercel Deployment"
---

# Vercel Deployment

OpenSIN nutzt Vercel für das Hosting der User WebApp (`chat.opensin.ai`).

## 🌐 Domains & Projekte

| Domain                                     | Vercel Projekt          | Framework  | Status         |
| ------------------------------------------ | ----------------------- | ---------- | -------------- |
| [chat.opensin.ai](https://chat.opensin.ai) | `dashboard-enterprise`  | Next.js 15 | ✅ Deployed    |
| [opensin.ai](https://opensin.ai)           | `website-opensin`       | Vite       | 🔄 In Progress |
| [docs.opensin.ai](https://docs.opensin.ai) | `OpenSIN-documentation` | VitePress  | ✅ Deployed    |

## 🚀 OpenSIN-WebApp Deployment

### Projekt-Details

- **Vercel Projekt:** `dashboard-enterprise` (ID: `prj_YtbTDMo1Tse8EM9iWtQ1wFtPtOvX`)
- **Domain:** `chat.opensin.ai` ✅ Verified
- **Framework:** Next.js 15 (App Router)
- **Repo:** [OpenSIN-AI/OpenSIN-WebApp](https://github.com/OpenSIN-AI/OpenSIN-WebApp)

### Environment Variables

| Variable                  | Wert                          | Zweck                   |
| ------------------------- | ----------------------------- | ----------------------- |
| `NEXT_PUBLIC_BACKEND_URL` | `https://api.opensin.ai`      | OpenSIN-backend API URL |
| `NEXT_PUBLIC_AUTH_URL`    | `https://api.opensin.ai/auth` | Auth Endpoint           |
| `AUTH_SECRET`             | _(generiert)_                 | JWT Session Secret      |

### Deployment Flow

```
git push origin main → Vercel erkennt Push → Auto Build → Production Deploy
```

### Landing Page Redirect

Die `vercel.json` konfiguriert automatische Redirects:

- `/` → `https://opensin.ai` (Landing Page)
- `/landing` → `https://opensin.ai`
- `/dashboard` → User Dashboard (nach Login)

## 🔧 Vercel API Setup

```bash
# Projekt erstellen
curl -X POST "https://api.vercel.com/v9/projects" \
  -H "Authorization: Bearer $VERCEL_TOKEN" \
  -d '{"name": "opensin-webapp", "framework": "nextjs"}'

# Domain hinzufügen
curl -X POST "https://api.vercel.com/v9/projects/opensin-webapp/domains" \
  -H "Authorization: Bearer $VERCEL_TOKEN" \
  -d '{"name": "chat.opensin.ai"}'

# Env Var setzen
curl -X POST "https://api.vercel.com/v9/projects/opensin-webapp/env" \
  -H "Authorization: Bearer $VERCEL_TOKEN" \
  -d '{"key": "NEXT_PUBLIC_BACKEND_URL", "value": "https://api.opensin.ai"}'
```

## 📊 Aktuell deployte Projekte (48 total)

Die Vercel-Organisation enthält 48 Projekte, darunter:

- **OpenSIN:** `dashboard-enterprise`, `website-opensin`, `sin-solver-dashboard`
- **AIOMETRICS:** `mindsafeguardian`, `humanpulse`, `aquawild`, etc.
- **Andere:** `afd-portal`, `delqhi-website`, `singularity-web-app`
