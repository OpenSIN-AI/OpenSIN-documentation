# 📋 Issue Phases 1-3

Vom internen Tool zur globalen A2A Supervisor Platform.

## Phase 1: Narrative Architecture

**Ziel:** Fundamentale Trennung von Public Marketing und authenticated Operational Surfaces.

### Host Policy

| Surface | Domain | Indexierung |
|---------|--------|-------------|
| **Public/Marketing** | `sin-solver.delqhi.com` | ✅ Indexierbar |
| **Product/Dashboard** | `a2a.delqhi.com` | ❌ Noindex |

### Proof SSOT (Single Source of Truth)

Alle Trust-Claims werden extrahiert in `proofRegistry.ts`:
- Aktive Agenten → Runtime Endpoint
- Uptime → Deployment Signal
- Security Posture → Verified Registry Fact

### Narrative: Supervisor Agent

**Kern-Positionierung:** "One agent to orchestrate your entire A2A workforce."

**Mental Model:**
```
Request → Solver → Workflows/Agents → Control Plane → Output
```

### Definition of Done

- [ ] Public Routes emit indexable Headers, Product Routes bleiben noindex
- [ ] Keine hardcodierten Metrics in React Components
- [ ] Separated Content Schemas (`components/site/content/*`)
- [ ] Core Narrative dokumentiert und approved

---

## Phase 2: Visual System Buildout

**Ziel:** Jedes Issue braucht visuelle Dokumentation.

### Anforderungen

| Element | Format | Zweck |
|---------|--------|-------|
| **Screenshots** | PNG/WebP | UI-Zustände zeigen |
| **Diagramme** | ASCII oder SVG | Architektur veranschaulichen |
| **Videos** | MP4/GIF (max 30s) | Workflows demonstrieren |
| **Before/After** | Side-by-side | Veränderungen dokumentieren |

### Regeln

- Kein Issue ohne visuellen Kontext
- Alle Screenshots müssen annotiert sein
- Diagramme müssen lesbar sein (mindestens 800px Breite)
- Videos müssen Untertitel haben

---

## Phase 3: Hardening

**Ziel:** Alle Issues gegen Production-Standards härten.

### Checklist

| Bereich | Check |
|---------|-------|
| **Error Handling** | Alle Error Cases abgedeckt, sinnvolle Error Messages |
| **Security** | Keine Secrets, Input Validation, Guardrails |
| **Performance** | Keine N+1 Queries, Caching wo sinnvoll, Memory-Leaks geprüft |
| **Monitoring** | Health Endpoints, Metrics, Logging, Alerting |
| **Documentation** | README aktualisiert, API-Docs aktuell, CHANGELOG gepflegt |
| **Testing** | Unit Tests, Integration Tests, E2E Tests, Coverage > 80% |

### Production-Readiness Gate

```
Error Handling ✅ → Security ✅ → Performance ✅ → Monitoring ✅ → Docs ✅ → Tests ✅ → MERGE
```

## 🔗 Verknüpfte Dokumentation

- [Architektur](./architecture.md) – Gesamtübersicht
- [Best Practices](./best-practices.md) – Entwicklungsstandards
- [Testing](./testing-environment-database.md) – Testing Guide
