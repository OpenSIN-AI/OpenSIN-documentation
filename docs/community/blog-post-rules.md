# 📝 Blog Post Regeln

Jeder Blog Post auf blog.opensin.ai MUSS folgende Standards erfüllen.

## Struktur

| Element | Anforderung |
|---------|-------------|
| **Titel** | Prägnant, Keyword-optimiert, < 60 Zeichen |
| **Einleitung** | Problem → Lösung in 2-3 Sätzen |
| **TL;DR** | Zusammenfassung in 1 Satz am Anfang |
| **Hauptteil** | Code-Beispiele, Screenshots, Architektur-Diagramme |
| **Fazit** | Zusammenfassung + Call-to-Action |
| **Metadaten** | Author, Datum, Tags, Featured Image |

## SEO-Anforderungen

| Metrik | Ziel |
|--------|------|
| Meta Description | < 160 Zeichen |
| Open Graph Tags | Erforderlich (og:title, og:description, og:image) |
| Canonical URL | Erforderlich |
| Tags | Mindestens 3, maximal 8 |
| Interne Links | Mindestens 2 Links zu eigenen Docs/Repos |

## Content-Qualität

- **Code-Beispiele** müssen ausführbar und getestet sein
- **Screenshots** müssen aktuell und annotiert sein
- **Architektur-Diagramme** müssen ASCII oder SVG sein
- **Externe Quellen** müssen verlinkt und aktuell sein
- **Sprache:** Deutsch für Core-Docs, Englisch für Blog Posts

## Publishing-Prozess

1. **Draft** in `docs/02_marketing/blog-posts/` erstellen
2. **Review** durch Core Team (mindestens 1 Approval)
3. **SEO-Check** (Meta Description, OG Tags, Canonical)
4. **Publish** via n8n CI/CD Pipeline
5. **Promote** auf Twitter/X, Discord, LinkedIn

## Beispiel Frontmatter

```markdown
---
title: "Why 100 AI Agents Beat 1 Super-Agent"
published: 2026-04-03
tags: [ai, agents, opensource, openai, claude]
canonical: https://github.com/OpenSIN-AI/OpenSIN
---
```

## 🔗 Verknüpfte Dokumentation

- [Marketing-Strategie](./governance-marketing.md) – Marketing-Übersicht
- [Contributing](./contributing.md) – Beitragsrichtlinien
