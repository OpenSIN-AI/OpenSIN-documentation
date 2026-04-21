# Dynamic Input Commands — Quick Reference

**Erstellt:** 2026-04-16
**Status:** ✅ Aktiv und synchronisiert (OCI VM + Mac)

---

## Browser-Automation Commands (mit Vision-Gate)

### Navigation
```bash
/browser-goto $ARGUMENTS
# Beispiel: /browser-goto https://github.com/OpenSIN-AI
# Substituiert zu: webauto-nodriver_goto({ url: "https://github.com/OpenSIN-AI" })
# + AUTOMATISCH: Screenshot + Vision-Gate
```

### Koordinaten-Klick
```bash
/click-at $1 $2
# Beispiel: /click-at 512 384
# Substituiert zu: webauto-nodriver_click({ x: 512, y: 384 })
# + AUTOMATISCH: Screenshot + Vision-Gate
```

### Element-Klick (Safe)
```bash
/click-element-safe $ARGUMENTS
# Beispiel: /click-element-safe "a[data-tab-item='i1issues-tab']"
# Versucht erst Selector, dann Koordinaten-Fallback
# + AUTOMATISCH: Screenshot + Vision-Gate
```

### Vision-Gate (MANDATORY nach jeder Aktion)
```bash
/vision-gate-check $ARGUMENTS
# Beispiel: /vision-gate-check "Klick auf Issues-Tab"
# Macht: Screenshot → Vision-Modell → PROCEED/STOP/RETRY
```

## Dynamic Input Variablen

| Variable | Bedeutung | Beispiel |
|----------|-----------|----------|
| `$ARGUMENTS` | Alle Argumente | `/browser-goto URL` → URL = $ARGUMENTS |
| `$1` | Erstes positional | `/click-at X Y` → X = $1 |
| `$2` | Zweites positional | `/click-at X Y` → Y = $2 |

## Message Commands

### WhatsApp
```bash
/whatsapp-send $1 $ARGUMENTS
# Beispiel: /whatsapp-send +49123456789 "Hallo Welt!"
# $1 = Nummer, $ARGUMENTS = Nachricht
```

### SMS
```bash
/send-sms $1 $ARGUMENTS
# Beispiel: /send-sms +49123456789 "Dein Code: 123456"
```

## macOS Commands

### Kalender
```bash
/mac-calendar-create $ARGUMENTS
# Beispiel: /mac-calendar-create {"calendar": "Arbeit", "title": "Meeting", "start_time": "2026-04-16T14:00", "end_time": "2026-04-16T15:00"}
```

### Notes
```bash
/mac-notes-create $ARGUMENTS
# Beispiel: /mac-notes-create {"folder": "Arbeit", "title": "Meeting Notes", "body": "Besprechung um 14 Uhr"}
```

## Alle Commands anzeigen
```bash
opencode debug config 2>&1 | grep '"description": "Navigate'
# Oder:
grep -A1 '"browser-goto":' ~/.config/opencode/opencode.json
```

## Sync-Status
- ✅ **Mac:** Commands aktiv
- ✅ **OCI VM:** Synchronisiert via `sin-sync` (see canonical infra repo for host details)
- ⚠️ **HF VMs:** Noch nicht synchronisiert (Optional)

---

**Regel:** Jede Browser-Aktion MUSS mit Vision-Gate enden. NIE blind klicken!
