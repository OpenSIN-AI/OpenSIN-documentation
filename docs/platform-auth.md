# SIN Platform Auth — Browser Session Management

**Datum:** 2026-04-04  
**Version:** 1.0.0  
**Status:** ✅ Production Ready  
**Repo:** `OpenSIN-backend/services/sin-platform-auth`

## Übersicht

**SIN Platform Auth** ist das autonome Cookie-Extraktions- und Injection-System für alle SIN Platform Agents und Platform Workers. Es extrahiert Browser-Sessions direkt aus dem Chrome Default Profil des Users, entschlüsselt die Cookies mit dem macOS Keychain "Chrome Safe Storage" Key, und speichert sie im sin-passwordmanager für die Nutzung durch HF Space Agenten und Platform Workers.

**Zero Human Intervention:** Der User surft normal in Chrome — sin-platform-auth erkennt und extrahiert alle Sessions automatisch.

## Architektur

```
Chrome Default Profil (Cookies.db)
  ↓
sin-platform-auth (Cookie-Export)
  ↓
macOS Keychain (Chrome Safe Storage Key)
  ↓
PBKDF2-SHA1 + AES-128-CBC Entschlüsselung
  ↓
sin-passwordmanager (catalog.json + Keychain)
  ↓
Platform Workers (13) + HF Space Agents (20)
```

## Unterstützte Plattformen (17)

| Plattform | Login URL | Handle |
|-----------|-----------|--------|
| X (Twitter) | https://x.com/login | @opnsin |
| YouTube | https://youtube.com | @opnsin |
| Instagram | https://instagram.com/accounts/login | @opnsin |
| Reddit | https://reddit.com/login | opnsin |
| Discord | https://discord.com/login | opnsin |
| Medium | https://medium.com/m/signin | @opnsin |
| TikTok | https://tiktok.com/login | @opnsin |
| HuggingFace | https://huggingface.co/login | delqhi |
| LinkedIn | https://linkedin.com/login | opnsin |
| Telegram | https://web.telegram.org | @opnsin |
| Google-Apps | https://accounts.google.com | opnsin |
| GitHub (Community) | https://github.com/login | opnsin |
| DevTo | https://dev.to/enter | @opnsin |
| ProductHunt | https://www.producthunt.com/login | opnsin |
| StackOverflow | https://stackoverflow.com/users/login | opnsin |
| Quora | https://www.quora.com/login | opnsin |
| IndieHackers | https://www.indiehackers.com/signin | opnsin |

## CLI Usage

```bash
sin-platform-auth status          # Session Status aller Plattformen
sin-platform-auth export youtube  # Cookies exportieren
sin-platform-auth save            # Alle Cookies speichern
sin-platform-auth list            # Unterstützte Plattformen
```

## Cookie-Entschlüsselung

Chrome v10 Format: `v10` + AES-128-CBC(PBKDF2-SHA1(key, "saltysalt", 1003), IV=" "*16, data)

**Key:** Chrome Safe Storage String aus macOS Keychain (als UTF-8, NICHT base64-decoded!)

**BUG-091 Fix:** Chrome 146 verwendet inkonsistentes PKCS7 Padding → Fallback auf longest printable ASCII extraction.

## Integration mit Platform Workers

Alle 13 Platform Workers nutzen sin-platform-auth für automatische Session-Injection:
- Prolific, Outlier, Clickworker, Appen, Scale AI, Mindrift, OneForma
- DataAnnotation, YouGov, Freecash, Karya, Meinungsstudie, Surge AI

## MCP Tools

| Tool | Beschreibung |
|------|-------------|
| `platform_auth_status` | Login-Status für alle/spezifische Plattformen |
| `platform_auth_export` | Cookies für Plattform exportieren |
| `platform_auth_save` | Cookies exportieren und speichern |
| `platform_auth_load` | Gespeicherte Cookies laden |
| `platform_auth_list` | Alle unterstützten Plattformen |
| `platform_auth_inject_script` | Cookie-Injection Script für Browser generieren |
