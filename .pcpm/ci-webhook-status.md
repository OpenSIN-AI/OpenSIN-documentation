# CI/CD Webhook Templates

## Status: PENDING

9 Repos benötigen n8n Webhook-Trigger:

### Repos die den Webhook brauchen:

| Repo | Status | PR |
|------|--------|-----|
| A2A-SIN-Teams | ⏳ Pending | - |
| A2A-SIN-WhatsApp | ⏳ Pending | - |
| A2A-SIN-Email | ⏳ Pending | - |
| A2A-SIN-Google-Chat | ⏳ Pending | - |
| A2A-SIN-LinkedIn | ⏳ Pending | - |
| A2A-SIN-DevTo | ⏳ Pending | - |
| A2A-SIN-StackOverflow | ⏳ Pending | - |
| A2A-SIN-Quora | ⏳ Pending | - |
| A2A-SIN-Community | ⏳ Pending | - |

### Template Datei:

Siehe `.github/workflows/n8n-webhook.yml`

### Manuelle Schritte pro Repo:

1. Branch erstellen: `git checkout -b feat/add-n8n-webhook`
2. Datei erstellen: `.github/workflows/n8n-webhook.yml` (siehe Template)
3. Commit & Push: `git commit -m "ci: add n8n webhook trigger"`
4. PR erstellen: `gh pr create --title "ci: add n8n webhook trigger"`

### WICHTIG:

- KEINE direkten GitHub Actions für Build/Test/Deploy!
- NUR der minimale Webhook-Trigger zu n8n!
- n8N Secret `N8N_WEBHOOK_URL` muss in jedem Repo gesetzt sein
