#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
A2A-SIN-Worker-HeyPiggy — Vision Gate Edition v3.0 (EXAKTE TAB-BINDUNG)
================================================================================
ARCHITEKTUR:
  Bridge Extension (Chrome) ←WebSocket→ HF MCP Server ←HTTP→ Dieser Worker
  Jede einzelne Aktion wird von Gemini 3 Flash visuell verifiziert.

KERNPRINZIP — EXAKTE TAB-BINDUNG (PRIORITY -7.85):
  Der Worker öffnet genau EINEN Tab (tabs_create) und speichert dessen
  tabId + windowId als CURRENT_TAB_ID / CURRENT_WINDOW_ID.
  AB DIESEM MOMENT wird JEDER Bridge-Call mit dem exakten tabId geschickt.
  Es gibt KEINEN Fallback auf den "aktiven Tab" oder "currentWindow".
  Wenn CURRENT_TAB_ID nicht gesetzt ist, crasht der Call absichtlich laut,
  statt still auf einen fremden Tab zu fallen.

  Benutzer können parallel andere Tabs öffnen oder bedienen —
  das DARF den Worker NIEMALS beeinflussen.

SICHERHEITSLAYER:
  1. Exakte Tab-Bindung: CURRENT_TAB_ID ist nach Init immer gesetzt (nie None)
  2. Click-Eskalationskette: click_element → ghost_click → keyboard → vision_click → coordinates
  3. DOM-Verifikation NACH JEDER Aktion (nicht nur Screenshot-Hash)
  4. Screenshot-Hash-Tracking: Erkennt Stillstand automatisch
  5. Audit-Log auf Disk: Jede Aktion, jeder Screenshot, jedes Vision-Ergebnis
  6. Session-Backup: Cookies werden vor Crash gesichert
  7. Bridge-Reconnect: Automatischer Reconnect bei Verbindungsverlust
  8. Credential-Isolation: Passwörter werden NIEMALS an die AI gesendet
  9. Human-Delays: Zufällige Pausen zwischen 1.5-4.5 Sekunden
  10. Try/Except um JEDE einzelne Operation: Kein unbehandelter Crash möglich
  11. Page-State-Klassifikation: Erkennt Login, Dashboard, Survey, Error
  12. Proof-Collection: Screenshots mit Zeitstempel für Nachvollziehbarkeit
================================================================================
"""

import asyncio
import base64
import hashlib
import json
import os
import random
import re
import time
import traceback
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# ============================================================================
# USER PROFIL — Jeremy Schulze
# WHY: Der Worker muss Profil-Fragen (Region, Wohnort, Geschlecht, Name etc.)
#      korrekt mit den echten Daten des Users beantworten.
#      Das Profil wird in den Vision-Prompt injiziert damit Gemini die richtigen
#      Antworten wählt — ohne raten, ohne falsche Klicks.
# CONSEQUENCES: Ohne Profil würde Gemini zufällig antworten → falsche Daten,
#               Umfragen brechen ab, Account könnte gesperrt werden.
# ============================================================================

PROFILE_PATH = Path("/Users/jeremy/.config/opencode/profiles/jeremy_schulze.json")


def _load_user_profile() -> dict:
    """
    Lädt das Benutzerprofil von Disk.
    WHY: Profil-Fragen in Umfragen (Region, Name, Wohnort etc.) müssen mit
         echten User-Daten beantwortet werden, nicht zufällig geraten.
    CONSEQUENCES: Fehlt die Datei, wird ein leeres Profil verwendet (kein Crash).
    """
    if PROFILE_PATH.exists():
        try:
            with open(PROFILE_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[PROFIL] Warnung: Profil konnte nicht geladen werden: {e}")
    return {}


USER_PROFILE = _load_user_profile()


def _build_profile_context() -> str:
    """
    Baut einen lesbaren Profil-Kontext-String für den Vision-Prompt.
    WHY: Gemini muss die genauen Profil-Antworten kennen damit es beim
         Ankreuzen von Radio-Buttons (Region, Geschlecht etc.) die richtigen
         Optionen wählt.
    CONSEQUENCES: Leerer String wenn kein Profil vorhanden — Vision fällt auf
                  generische Antwortlogik zurück.
    """
    if not USER_PROFILE:
        return ""

    lines = ["BENUTZERPROFIL (nutze diese Daten für Profil-Fragen):"]

    # Direkte Felder
    field_map = {
        "name": "Name",
        "first_name": "Vorname",
        "last_name": "Nachname",
        "gender": "Geschlecht (male=Männlich)",
        "city": "Wohnort/Stadt",
        "region": "Region in Deutschland",
        "country": "Land",
    }
    for key, label in field_map.items():
        val = USER_PROFILE.get(key)
        if val:
            lines.append(f"- {label}: {val}")

    # Explizite Profil-Antworten (Frage → Antwort Mapping)
    profile_answers = USER_PROFILE.get("profile_answers", {})
    if profile_answers:
        lines.append("KONKRETE ANTWORTEN FÜR HÄUFIGE FRAGEN:")
        for question, answer in profile_answers.items():
            lines.append(f"  - '{question}' → '{answer}'")

    region_note = USER_PROFILE.get("region_note")
    if region_note:
        lines.append(f"HINWEIS: {region_note}")

    return "\n".join(lines)


# ============================================================================
# KONFIGURATION
# ============================================================================

# Bridge-Endpunkte
BRIDGE_MCP_URL = "https://openjerro-opensin-bridge-mcp.hf.space/mcp"
BRIDGE_HEALTH_URL = "https://openjerro-opensin-bridge-mcp.hf.space/health"

# Vision Gate Limits (aus AGENTS.md PRIORITY -7.0)
# WHY MAX_STEPS=120: Umfragen haben oft 20-40 Fragen, jede Frage braucht
#   Screenshot + Vision + Klick + DOM-Verify = 4 Aktionen. 40 Fragen * 4 = 160.
#   120 ist ein sicherer Wert der auch lange Surveys komplett abschließt.
MAX_STEPS = 120
# WHY MAX_RETRIES=5: 3 war zu aggressiv — manchmal braucht eine Seite länger zum laden.
MAX_RETRIES = 5
# WHY MAX_NO_PROGRESS=15: Survey-Seiten sehen Frage-für-Frage fast identisch aus.
#   Screenshot-Hash-Vergleich erkennt das fälschlich als 'kein Fortschritt'.
#   15 Schritte gibt dem Worker genug Spielraum um durch mehrseitige Surveys zu kommen.
#   Außerdem wird no_progress_count bei page_state='survey_active' NICHT hochgezählt.
MAX_NO_PROGRESS = 15
MAX_CLICK_ESCALATIONS = 5  # 5 Klick-Methoden bevor aufgegeben wird
VISION_MODEL = "google/antigravity-gemini-3-flash"
CLICK_ACTIONS = (
    "click_element",
    "click_ref",
    "ghost_click",
    "vision_click",
    "click_coordinates",
)

# 1x1 PNG als lokaler Vision-Probe. WHY: Die Preflight-Prüfung muss die
# screenshot-basierte Vision-Authentifizierung testen, BEVOR irgendeine Browser-
# Mutation stattfindet. Dafür reicht ein minimales gültiges PNG als sicherer Probe.
VISION_AUTH_PROBE_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO5wZuoAAAAASUVORK5CYII="
)

# Verzeichnisse für Artefakte
RUN_ID = datetime.now().strftime("%Y%m%d_%H%M%S")
ARTIFACT_DIR = Path(f"/tmp/heypiggy_run_{RUN_ID}")
SCREENSHOT_DIR = ARTIFACT_DIR / "screenshots"
AUDIT_DIR = ARTIFACT_DIR / "audit"
SESSION_DIR = ARTIFACT_DIR / "sessions"

# Erstelle alle Verzeichnisse beim Start
for d in [ARTIFACT_DIR, SCREENSHOT_DIR, AUDIT_DIR, SESSION_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# ============================================================================
# EXAKTE TAB-BINDUNG — GLOBAL STATE (PRIORITY -7.85)
# ============================================================================
# CURRENT_TAB_ID und CURRENT_WINDOW_ID werden beim ersten tabs_create gesetzt
# und DANACH niemals mehr auf None zurückgesetzt.
# Alle Bridge-Calls MÜSSEN tabId enthalten — kein Fallback auf aktiven Tab!
# WHY: Parallele User-Tabs dürfen den Worker NIEMALS beeinflussen.
# CONSEQUENCES: Wenn tabId nicht gesetzt ist, schlägt der Call laut fehl.
CURRENT_TAB_ID: int | None = None  # Wird nach init() IMMER gesetzt sein
CURRENT_WINDOW_ID: int | None = None  # Wird nach init() IMMER gesetzt sein
WORKER_HOST_HINT = "heypiggy.com"  # Host-Teil der Worker-URL zur Recovery-Prüfung
request_id_counter = 0


def _require_tab_id() -> int:
    """
    Gibt CURRENT_TAB_ID zurück oder wirft einen Fehler wenn nicht gesetzt.
    WHY: Nach dem initialen Tab-Erstellen MUSS tabId immer bekannt sein.
         Ein leerer Fallback würde auf einen beliebigen aktiven Tab fallen —
         das ist das exakte Problem das wir eliminieren wollen.
    CONSEQUENCES: Laut fehlschlagen ist besser als still falschen Tab steuern.
    """
    global CURRENT_TAB_ID
    if CURRENT_TAB_ID is None:
        raise RuntimeError(
            "CURRENT_TAB_ID ist nicht gesetzt! "
            "Worker darf keine Bridge-Calls senden bevor tabs_create erfolgreich war."
        )
    return CURRENT_TAB_ID


def _tab_params() -> dict:
    """
    Gibt ein Dict mit dem exakten tabId zurück.
    WHY: Convenience-Wrapper damit alle Funktionen einheitlich tabId übergeben.
    CONSEQUENCES: Wirft RuntimeError wenn tabId nicht gesetzt — kein stiller Fallback.
    """
    return {"tabId": _require_tab_id()}


# ============================================================================
# AUDIT-LOG — Jede einzelne Aktion wird auf Disk geloggt
# ============================================================================

AUDIT_LOG_PATH = AUDIT_DIR / "audit.jsonl"


def audit(event_type: str, **data):
    """
    Schreibt einen Audit-Eintrag ins Log.
    WHY: Damit wir bei JEDEM Fehler exakt nachvollziehen können was passiert ist.
    CONSEQUENCES: Ohne Audit-Log ist Debugging unmöglich.
    """
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event_type,
        "run_id": RUN_ID,
        **data,
    }
    try:
        with open(AUDIT_LOG_PATH, "a") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception:
        pass  # Audit-Fehler darf den Worker NIEMALS crashen

    # Auch auf stdout für Live-Monitoring
    emoji_map = {
        "screenshot": "📸",
        "vision_check": "🧠",
        "action": "⚡",
        "ghost_click": "👻",
        "coord_click": "🎯",
        "vision_click": "🔭",
        "click_escalation": "🔺",
        "error": "❌",
        "success": "✅",
        "bridge_health": "📡",
        "session_save": "💾",
        "state_change": "🔄",
        "navigate": "🌐",
        "stop": "🛑",
        "start": "🚀",
    }
    emoji = emoji_map.get(event_type, "📝")
    print(f"{emoji} [{event_type}] {json.dumps(data, ensure_ascii=False)[:200]}")


def missing_required_credentials() -> list[str]:
    """
    Liefert fehlende Pflicht-Env-Variablen für den Worker.
    WHY: Der Worker darf ohne echte Zugangsdaten niemals in Login-/Survey-Flow laufen.
    CONSEQUENCES: Die Preflight-Kontrolle stoppt fail-closed vor jeder Browser-Mutation.
    """
    missing = []
    if not os.environ.get("HEYPIGGY_EMAIL"):
        missing.append("HEYPIGGY_EMAIL")
    if not os.environ.get("HEYPIGGY_PASSWORD"):
        missing.append("HEYPIGGY_PASSWORD")
    return missing


def ensure_vision_probe_screenshot() -> str:
    """
    Schreibt ein minimales Screenshot-PNG für den Vision-Auth-Probe auf Disk.
    WHY: Der Auth-Check soll denselben screenshot-basierten OpenSIN-Vision-Pfad nutzen
    wie der echte Worker, aber ohne vorher einen Browser-Tab zu mutieren.
    CONSEQUENCES: Gibt immer einen stabilen lokalen PNG-Pfad für den Probe zurück.
    """
    probe_path = SCREENSHOT_DIR / "vision_auth_probe.png"
    if not probe_path.exists():
        probe_path.write_bytes(VISION_AUTH_PROBE_PNG)
    return str(probe_path)


def collect_opencode_text(stdout: bytes) -> str:
    """
    Extrahiert Text-Events aus `opencode run --format json`.
    WHY: OpenSIN/sincode liefert JSONL-Ereignisse statt einer einzigen Text-Antwort.
    CONSEQUENCES: Alle Vision-Call-Sites können denselben robusten Parser wiederverwenden.
    """
    full_text = ""
    for line in stdout.decode("utf-8", errors="replace").splitlines():
        try:
            event = json.loads(line)
        except Exception:
            continue
        if event.get("type") == "text":
            full_text += event.get("part", {}).get("text", "")
    return full_text.strip()


def detect_vision_auth_failure(raw_text: str) -> str | None:
    """
    Erkennt harte Vision-Authentifizierungsfehler im kombinierten Output.
    WHY: Issue #86 verlangt ein fail-closed Verhalten bei 401 / invalid credentials.
    CONSEQUENCES: Sobald dieses Pattern auftaucht, darf der Worker nicht weiterlaufen.
    """
    lowered = (raw_text or "").lower()
    if "401" in lowered and "invalid authentication credentials" in lowered:
        return "401 invalid authentication credentials"
    if "invalid authentication credentials" in lowered:
        return "invalid authentication credentials"
    if "authentication credentials" in lowered and "invalid" in lowered:
        return "invalid authentication credentials"
    return None


async def run_vision_model(
    prompt: str,
    screenshot_path: str,
    *,
    timeout: int = 120,
    step_num: int = 0,
    purpose: str = "vision",
) -> dict:
    """
    Führt einen screenshot-basierten OpenSIN-Vision-Call über `opencode run` aus.
    WHY: Preflight-Probe und reguläre Vision-Entscheidungen müssen denselben CLI-Pfad
    nutzen, damit Auth-Fehler zentral erkannt und fail-closed behandelt werden.
    CONSEQUENCES: Gibt strukturierte Resultate mit `ok` und `auth_failure` zurück.
    """
    cmd = [
        "opencode",
        "run",
        prompt,
        "-f",
        screenshot_path,
        "--model",
        VISION_MODEL,
        "--format",
        "json",
    ]

    try:
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout)
        full_text = collect_opencode_text(stdout)
        stderr_text = stderr.decode("utf-8", errors="replace").strip()
        combined = "\n".join(part for part in [full_text, stderr_text] if part)
        auth_error = detect_vision_auth_failure(combined)

        if process.returncode != 0:
            error_message = stderr_text or full_text or f"opencode exit {process.returncode}"
            if auth_error:
                audit(
                    "error",
                    message=f"Vision auth failure ({purpose}): {auth_error}",
                    step=step_num,
                )
                return {
                    "ok": False,
                    "auth_failure": True,
                    "error": auth_error,
                    "stdout_text": full_text,
                    "stderr_text": stderr_text,
                    "returncode": process.returncode,
                }
            audit(
                "error",
                message=f"Vision command failed ({purpose}): {error_message[:200]}",
                step=step_num,
            )
            return {
                "ok": False,
                "auth_failure": False,
                "error": error_message,
                "stdout_text": full_text,
                "stderr_text": stderr_text,
                "returncode": process.returncode,
            }

        if auth_error:
            audit(
                "error",
                message=f"Vision auth failure ({purpose}): {auth_error}",
                step=step_num,
            )
            return {
                "ok": False,
                "auth_failure": True,
                "error": auth_error,
                "stdout_text": full_text,
                "stderr_text": stderr_text,
                "returncode": process.returncode,
            }

        return {
            "ok": True,
            "auth_failure": False,
            "text": full_text,
            "stderr_text": stderr_text,
            "returncode": process.returncode,
        }

    except asyncio.TimeoutError:
        audit("error", message=f"Vision Timeout ({purpose})", step=step_num)
        return {
            "ok": False,
            "auth_failure": False,
            "error": f"Vision Timeout ({purpose})",
            "stdout_text": "",
            "stderr_text": "",
            "returncode": None,
        }

    except Exception as e:
        auth_error = detect_vision_auth_failure(str(e))
        if auth_error:
            audit(
                "error",
                message=f"Vision auth failure ({purpose}): {auth_error}",
                step=step_num,
            )
            return {
                "ok": False,
                "auth_failure": True,
                "error": auth_error,
                "stdout_text": "",
                "stderr_text": str(e),
                "returncode": None,
            }
        audit("error", message=f"Vision Exception ({purpose}): {e}", step=step_num)
        return {
            "ok": False,
            "auth_failure": False,
            "error": str(e),
            "stdout_text": "",
            "stderr_text": str(e),
            "returncode": None,
        }


async def ensure_worker_preflight() -> dict:
    """
    Prüft die komplette Control-Plane vor der ersten Browser-Mutation.
    WHY: Issue #86 verlangt ein fail-closed Gate vor tabs_create/navigation/login.
    CONSEQUENCES: Fehlt Env oder Vision-Auth, stoppt der Worker bevor ein Tab erstellt wird.
    """
    missing = missing_required_credentials()
    if missing:
        reason = f"Pflicht-Env fehlt: {', '.join(missing)}"
        audit("stop", reason=reason)
        return {"ok": False, "reason": reason}

    if not await check_bridge_alive():
        reason = "Bridge nicht erreichbar während Preflight"
        audit("stop", reason=reason)
        return {"ok": False, "reason": reason}

    probe_path = ensure_vision_probe_screenshot()
    probe_prompt = (
        "Antworte ausschließlich mit gültigem JSON im Format "
        '{"status":"ok"}. Keine Erklärungen.'
    )
    probe_result = await run_vision_model(
        probe_prompt,
        probe_path,
        timeout=60,
        step_num=0,
        purpose="preflight_auth_probe",
    )
    if not probe_result.get("ok"):
        reason = probe_result.get("error", "Vision-Probe fehlgeschlagen")
        audit("stop", reason=f"Vision-Preflight fehlgeschlagen: {reason}")
        return {"ok": False, "reason": reason}

    probe_text = probe_result.get("text", "")
    try:
        probe_json = json.loads(probe_text)
    except Exception as e:
        reason = f"Vision-Preflight lieferte kein JSON: {e}"
        audit("stop", reason=reason)
        return {"ok": False, "reason": reason}

    if probe_json.get("status") != "ok":
        reason = f"Vision-Preflight nicht healthy genug: {probe_text[:120]}"
        audit("stop", reason=reason)
        return {"ok": False, "reason": reason}

    audit("success", message="Worker-Preflight bestanden: Env + Vision auth healthy")
    return {"ok": True, "reason": "ready"}


# ============================================================================
# BRIDGE-KOMMUNIKATION — Extrem robustes HTTP mit Retry und Reconnect
# ============================================================================


def fetch_health():
    """
    Holt den Bridge-Health-Status.
    WHY: Vor JEDER Aktion muss die Bridge erreichbar sein.
    CONSEQUENCES: Bei Timeout wird gewartet, nicht gecrasht.
    """
    try:
        req = urllib.request.Request(BRIDGE_HEALTH_URL)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        return {"error": str(e), "extensionConnected": False}


async def wait_for_extension(timeout=600):
    """
    Wartet robust auf die Extension-Verbindung.
    WHY: Ohne Extension sind alle Bridge-Calls sinnlos.
    CONSEQUENCES: 600s Timeout, danach harter Abbruch mit klarer Fehlermeldung.
    """
    audit("start", message="Warte auf Bridge Extension", timeout=timeout)
    start = time.time()
    last_status = None

    while time.time() - start < timeout:
        health = await asyncio.to_thread(fetch_health)
        current = health.get("extensionConnected")

        # Nur loggen bei Statusänderung, um Spam zu vermeiden
        if current != last_status:
            audit(
                "bridge_health",
                connected=current,
                version=health.get("version", "?"),
                tools=health.get("toolsCount", 0),
                pending=health.get("pendingRequests", 0),
            )
            last_status = current

        if current is True:
            audit("success", message="Extension verbunden")
            return True

        await asyncio.sleep(5)

    raise RuntimeError(f"Timeout ({timeout}s): Bridge Extension nicht verbunden.")


def post_mcp(method: str, params: dict = None):
    """
    Sendet einen MCP-Request an die Bridge mit 3x Retry und Error-Body-Parsing.
    WHY: Die Bridge kann kurzzeitig 500er liefern, das darf nicht zum Crash führen.
    CONSEQUENCES: Nach 3 Fehlversuchen wird eine RuntimeError geworfen (wird oben gefangen).
    """
    global request_id_counter
    request_id_counter += 1

    body = {"jsonrpc": "2.0", "method": method, "id": request_id_counter}
    if params:
        body["params"] = params

    last_err = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(
                BRIDGE_MCP_URL,
                data=json.dumps(body).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                decoded = json.loads(resp.read().decode("utf-8"))
                if "error" in decoded:
                    last_err = f"MCP Protocol Error: {decoded['error']}"
                    audit("error", message=last_err, attempt=attempt + 1)
                    time.sleep(2 * (attempt + 1))
                    continue
                return decoded.get("result", {})

        except urllib.error.HTTPError as e:
            # Echten Error-Body extrahieren statt nur Status-Code
            try:
                error_body = e.read().decode("utf-8")
                error_json = json.loads(error_body)
                last_err = f"HTTP {e.code}: {json.dumps(error_json)}"
            except Exception:
                last_err = f"HTTP {e.code}: {e.reason}"
            audit("error", message=last_err, attempt=attempt + 1)
            time.sleep(2 * (attempt + 1))

        except Exception as e:
            last_err = str(e)
            audit("error", message=last_err, attempt=attempt + 1)
            time.sleep(2 * (attempt + 1))

    raise RuntimeError(f"MCP fehlgeschlagen nach 3 Versuchen: {last_err}")


def decode_mcp_result(raw):
    """
    Decodiert das MCP-Result aus der verschachtelten JSON-RPC Struktur.
    WHY: Die Bridge gibt content[0].text zurück, das muss entpackt werden.
    """
    if isinstance(raw, dict) and "content" in raw:
        txt = raw["content"][0].get("text", "")
        try:
            return json.loads(txt)
        except Exception:
            return txt
    return raw


def normalize_selector(selector: str) -> str:
    """
    Bereinigt einen Vision-Selector in gültiges CSS.
    WHY: Vision-Modelle erzeugen manchmal Playwright-artige Pseudo-Selektoren
    wie :contains(...) oder :has-text(...). Diese sind im Browser-QuerySelector
    nicht gültig und müssen deshalb vor der Ausführung repariert werden.
    """
    if not selector:
        return selector

    cleaned = selector
    cleaned = re.sub(r":contains\((?:[^()]+|\([^()]*\))*\)", "", cleaned)
    cleaned = re.sub(r":has-text\((?:[^()]+|\([^()]*\))*\)", "", cleaned)
    cleaned = re.sub(r":text\((?:[^()]+|\([^()]*\))*\)", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


async def click_visible_button_with_text(text_hint: str):
    """
    Klicke einen sichtbaren Button anhand seines Textinhalts.
    WHY: Vision kann dashboard-blockierende Gate-Buttons wie
    "Starte die erste Umfrage!" übersehen. Dieser DOM-basierte
    Gate-Klick verhindert, dass wir Survey-Karten zu früh anklicken.
    """
    global CURRENT_TAB_ID, CURRENT_WINDOW_ID
    tab_params = _tab_params()
    js_code = f"""
    (function() {{
      const hint = {json.dumps(text_hint.lower())};
      const candidates = Array.from(document.querySelectorAll('button, a, [role="button"]'));
      const el = candidates.find((node) => {{
        const text = (node.textContent || '').trim().toLowerCase();
        const visible = node.offsetParent !== null;
        return visible && text.includes(hint);
      }});
      if (!el) return {{ clicked: false, reason: 'not found', hint: hint }};
      if (typeof el.focus === 'function') el.focus();
      if (typeof el.click === 'function') el.click();
      else el.dispatchEvent(new MouseEvent('click', {{ bubbles: true, cancelable: true, view: window }}));
      return {{
        clicked: true,
        text: (el.textContent || '').trim().substring(0, 120),
        tag: el.tagName,
        id: el.id || '',
        cls: (el.className || '').toString().substring(0, 120)
      }};
    }})();
    """
    return await execute_bridge("execute_javascript", {"script": js_code, **tab_params})


async def resolve_survey_selector(selector: str, description: str = "") -> str:
    """
    Wandelt generische Survey-Selektoren in die echte #survey-... ID um.
    WHY: Vision liefert auf HeyPiggy oft nur "div.survey-item" statt der
    konkreten ID. Damit wir nicht blind die erste Karte anklicken, lesen wir
    die sichtbaren Survey-Karten aus dem DOM und wählen die beste Karte über
    Preis-Hinweis oder höchste vergütete Karte.
    """
    if not selector:
        return selector

    lowered = selector.lower()
    if "survey-item" not in lowered and "survey" not in lowered:
        return selector

    global CURRENT_TAB_ID, CURRENT_WINDOW_ID
    tab_params = _tab_params()
    js_code = """
    (function() {
      const cards = Array.from(document.querySelectorAll('div.survey-item')).map((el) => {
        const r = el.getBoundingClientRect();
        return {
          id: el.id || '',
          text: (el.textContent || '').replace(/\\s+/g, ' ').trim(),
          visible: el.offsetParent !== null,
          x: Math.round(r.left + r.width / 2),
          y: Math.round(r.top + r.height / 2),
          w: Math.round(r.width),
          h: Math.round(r.height),
        };
      });
      return cards.filter((card) => card.visible && card.id);
    })();
    """
    scan = await execute_bridge("execute_javascript", {"script": js_code, **tab_params})
    cards = []
    if isinstance(scan, dict):
        cards = scan.get("result", []) or []
    elif isinstance(scan, list):
        cards = scan

    if not isinstance(cards, list) or not cards:
        return selector

    price_hint = None
    for source in (description or "", selector):
        m = re.search(r"(\d+[.,]\d+)\s*€", source)
        if m:
            price_hint = m.group(1).replace(",", ".")
            break

    def _card_price(card):
        text = str(card.get("text", ""))
        m = re.search(r"(\d+[.,]\d+)\s*€", text)
        if not m:
            return None
        try:
            return float(m.group(1).replace(",", "."))
        except Exception:
            return None

    chosen = None
    if price_hint is not None:
        for card in cards:
            text = str(card.get("text", ""))
            if price_hint in text.replace(",", "."):
                chosen = card
                break

    if chosen is None:
        priced_cards = []
        for card in cards:
            price = _card_price(card)
            if price is not None:
                priced_cards.append((price, card))
        if priced_cards:
            priced_cards.sort(key=lambda item: item[0], reverse=True)
            chosen = priced_cards[0][1]

    if chosen and chosen.get("id"):
        resolved = f"#{chosen['id']}"
        if resolved != selector:
            audit(
                "state_change",
                message=(
                    f"Survey-Selector auf echte ID aufgelöst: {selector[:80]} -> {resolved}"
                ),
            )
        return resolved

    return selector


async def recover_worker_tab_id() -> int | None:
    """
    Stellt die exakt bekannte Worker-Tab-ID wieder her.
    WHY: Parallel geöffnete Browser-Tabs dürfen den Worker nie beeinflussen.
    Wir akzeptieren deshalb nur die vorher gespeicherte Tab-ID oder genau eine
    eindeutige HeyPiggy-Tab-Instanz im gespeicherten Fenster.
    """
    global CURRENT_TAB_ID, CURRENT_WINDOW_ID

    query = {}
    if CURRENT_WINDOW_ID is not None:
        query["windowId"] = CURRENT_WINDOW_ID

    tabs_raw = await asyncio.to_thread(
        post_mcp, "tools/call", {"name": "tabs_list", "arguments": {"query": query}}
    )
    tabs_result = decode_mcp_result(tabs_raw)
    tabs = []
    if isinstance(tabs_result, dict):
        tabs = tabs_result.get("tabs", []) or []

    if CURRENT_TAB_ID is not None:
        for tab in tabs:
            if isinstance(tab, dict) and tab.get("id") == CURRENT_TAB_ID:
                return CURRENT_TAB_ID

    candidates = [
        tab
        for tab in tabs
        if isinstance(tab, dict) and WORKER_HOST_HINT in str(tab.get("url", "")).lower()
    ]

    if len(candidates) == 1:
        CURRENT_TAB_ID = candidates[0].get("id")
        audit(
            "state_change",
            message=(
                f"Worker-Tab wiederhergestellt: tabId={CURRENT_TAB_ID}, "
                f"windowId={CURRENT_WINDOW_ID}"
            ),
        )
        return CURRENT_TAB_ID

    if not candidates and CURRENT_WINDOW_ID is None:
        # Letzter Versuch: alle Tabs im Browser durchsuchen, aber nur wenn wir
        # noch keinen eigenen Fenster-Kontext haben. Das bleibt trotzdem streng
        # auf den HeyPiggy-Host begrenzt.
        tabs_raw = await asyncio.to_thread(
            post_mcp, "tools/call", {"name": "tabs_list", "arguments": {}}
        )
        tabs_result = decode_mcp_result(tabs_raw)
        if isinstance(tabs_result, dict):
            all_tabs = tabs_result.get("tabs", []) or []
            candidates = [
                tab
                for tab in all_tabs
                if isinstance(tab, dict)
                and WORKER_HOST_HINT in str(tab.get("url", "")).lower()
            ]
            if len(candidates) == 1:
                CURRENT_TAB_ID = candidates[0].get("id")
                audit(
                    "state_change",
                    message=f"Worker-Tab global wiedergefunden: tabId={CURRENT_TAB_ID}",
                )
                return CURRENT_TAB_ID

    if candidates:
        audit(
            "error",
            message=(
                f"Worker-Tab-Recovery mehrdeutig: {len(candidates)} HeyPiggy-Tabs "
                "im gleichen Kontext gefunden"
            ),
        )
    else:
        audit(
            "error",
            message="Worker-Tab-Recovery fehlgeschlagen: kein HeyPiggy-Tab gefunden",
        )
    return None


async def execute_bridge(method: str, params: dict = None):
    """
    Führt einen Bridge-Tool-Call aus und decodiert das Ergebnis.
    WHY: Zentraler Wrapper der JEDEN Bridge-Call absichert.
    CONSEQUENCES: Fängt alle Exceptions und gibt ein Error-Dict zurück statt zu crashen.
    """
    try:
        call_params = params or {}
        raw = await asyncio.to_thread(
            post_mcp, "tools/call", {"name": method, "arguments": call_params}
        )
        result = decode_mcp_result(raw)

        # Wenn ein explizit gesetzter tabId-Wert stale ist, niemals blind auf den
        # aktiven Tab ausweichen. Stattdessen nur die exakt bekannte Worker-Tab-
        # Zuordnung wiederherstellen.
        if (
            isinstance(result, dict)
            and result.get("error")
            and call_params.get("tabId") is not None
        ):
            error_text = str(result.get("error", ""))
            if "No tab with id" in error_text or "No tab with given id" in error_text:
                audit(
                    "state_change",
                    message=f"Stale tabId für {method} erkannt; versuche Worker-Tab-Recovery",
                )
                recovered_tab_id = await recover_worker_tab_id()
                if recovered_tab_id is not None:
                    retry_params = dict(call_params)
                    retry_params["tabId"] = recovered_tab_id
                    retry_raw = await asyncio.to_thread(
                        post_mcp,
                        "tools/call",
                        {"name": method, "arguments": retry_params},
                    )
                    result = decode_mcp_result(retry_raw)

        return result
    except Exception as e:
        audit("error", message=f"execute_bridge({method}) failed: {e}")
        return {"error": str(e)}


async def check_bridge_alive():
    """
    Prüft ob die Bridge noch lebt, und wartet ggf. auf Reconnect.
    WHY: Mitten im Lauf kann die Extension disconnecten (Tab-Crash, Sleep, etc.)
    CONSEQUENCES: Bis zu 60s Reconnect-Versuch bevor aufgegeben wird.
    """
    health = await asyncio.to_thread(fetch_health)
    if health.get("extensionConnected") is True:
        return True

    audit("state_change", message="Bridge disconnected! Versuche Reconnect...")
    start = time.time()
    while time.time() - start < 60:
        await asyncio.sleep(5)
        health = await asyncio.to_thread(fetch_health)
        if health.get("extensionConnected") is True:
            audit("success", message="Bridge reconnected!")
            return True

    audit("error", message="Bridge Reconnect fehlgeschlagen nach 60s")
    return False


# ============================================================================
# SCREENSHOT-ENGINE — Mit Hash-Tracking für Fortschrittserkennung
# ============================================================================


async def take_screenshot(step_num: int, label: str = ""):
    """
    Macht einen Screenshot der exakt bekannten Worker-Tab-Instanz und speichert ihn als PNG.
    WHY: Jeder einzelne Schritt muss visuell dokumentiert werden (PRIORITY -7.0).
    CONSEQUENCES: Gibt (path, hash) zurück für Fortschrittserkennung.
    """
    try:
        params = _tab_params()
        # `screenshot_full` hängt an der sichtbaren Browser-Instanz und wäre bei
        # parallelen Tabs unsicher. `observe` liefert ein tabgebundenes Screenshot
        # für genau die Worker-Instanz.
        res = await execute_bridge("observe", params)

        if isinstance(res, dict) and "screenshot" in res:
            screenshot = res.get("screenshot") or {}
            if isinstance(screenshot, dict) and "dataUrl" in screenshot:
                res = screenshot["dataUrl"]
        elif isinstance(res, dict) and "dataUrl" in res:
            # Fallback für ältere Bridge-Implementierungen.
            res = res["dataUrl"]

        if not isinstance(res, str) or not res.startswith("data:"):
            audit(
                "error",
                message="Screenshot fehlgeschlagen",
                step=step_num,
                result_type=type(res).__name__,
            )
            return None, None

        # Base64 decodieren und speichern
        _, payload = res.split(",", 1)
        # Padding korrigieren (Bridge liefert manchmal ohne Padding)
        payload += "=" * ((4 - len(payload) % 4) % 4)
        img_bytes = base64.b64decode(payload)

        # Hash für Fortschrittserkennung berechnen
        img_hash = hashlib.md5(img_bytes).hexdigest()

        # Dateiname mit Zeitstempel und Label für Nachvollziehbarkeit
        safe_label = re.sub(r"[^a-zA-Z0-9_-]", "", label.replace(" ", "_"))[:30]
        filename = f"step_{step_num:03d}_{safe_label}_{img_hash[:8]}.png"
        path = SCREENSHOT_DIR / filename
        path.write_bytes(img_bytes)

        audit(
            "screenshot",
            step=step_num,
            path=str(path),
            hash=img_hash,
            size=len(img_bytes),
        )
        return str(path), img_hash

    except Exception as e:
        audit("error", message=f"Screenshot Exception: {e}", step=step_num)
        return None, None


# ============================================================================
# DOM PRE-SCAN — Holt ECHTE Selektoren von der Seite vor jedem Vision-Call
# ============================================================================


async def dom_prescan():
    """
    Scannt die aktuelle Seite nach klickbaren Elementen und liefert echte Selektoren.
    WHY: Gemini DARF NIEMALS CSS-Selektoren raten! Es muss die echten kennen.
    CONSEQUENCES: Ohne Pre-Scan schlägt Gemini Fantasie-Selektoren wie :has-text() vor.
    """
    global CURRENT_TAB_ID, CURRENT_WINDOW_ID
    tab_params = _tab_params()

    # 1. Accessibility-Tree-Snapshot mit Refs holen (für click_ref)
    snapshot_info = ""
    try:
        snapshot = await execute_bridge(
            "snapshot", {**tab_params, "includeScreenshot": False}
        )
        if isinstance(snapshot, dict) and "tree" in snapshot:
            tree = snapshot["tree"]
            # Nur interaktive Elemente (mit @eX Refs) extrahieren
            interactive = [l.strip() for l in tree.splitlines() if "@e" in l]
            if interactive:
                snapshot_info = (
                    "ACCESSIBILITY-TREE REFS (nutzbar mit click_ref):\n"
                    + "\n".join(interactive[:20])
                )
            audit(
                "action",
                message=f"DOM Pre-Scan: {len(interactive)} interactive refs, {snapshot.get('refCount', 0)} total refs",
            )
    except Exception as e:
        audit("error", message=f"Snapshot fehlgeschlagen: {e}")

    # 2. Echte HTML-Elemente mit Klick-Potential scannen
    clickable_info = ""
    try:
        js_scan = """
        (function() {
            var results = [];
            var all = document.querySelectorAll('[onclick], [role="button"], a[href], button, input[type="submit"], [style*="cursor: pointer"], .survey-item, .survey-card, [class*="card"], [class*="survey"]');
            for (var i = 0; i < Math.min(all.length, 25); i++) {
                var el = all[i];
                var r = el.getBoundingClientRect();
                if (r.width < 5 || r.height < 5) continue;
                var sel = '';
                if (el.id) sel = '#' + el.id;
                else if (el.className && typeof el.className === 'string') {
                    var cls = el.className.split(' ').filter(function(c) { return c.length > 0; })[0];
                    if (cls) sel = el.tagName.toLowerCase() + '.' + cls;
                }
                if (!sel) sel = el.tagName.toLowerCase();
                results.push({
                    sel: sel,
                    tag: el.tagName,
                    id: el.id || '',
                    cls: (el.className + '').substring(0, 80),
                    text: (el.textContent || '').substring(0, 60).replace(/\\n/g, ' ').trim(),
                    x: Math.round(r.x + r.width/2),
                    y: Math.round(r.y + r.height/2),
                    w: Math.round(r.width),
                    h: Math.round(r.height),
                    cursor: getComputedStyle(el).cursor
                });
            }
            return results;
        })();
        """
        scan_result = await execute_bridge(
            "execute_javascript", {"script": js_scan, **tab_params}
        )
        if isinstance(scan_result, dict) and "result" in scan_result:
            elements = scan_result["result"]
            if isinstance(elements, list) and elements:
                lines = []
                for el in elements:
                    selector = el.get("sel", "?")
                    if el.get("id"):
                        selector = f"#{el['id']}"
                    text = el.get("text", "")[:40]
                    lines.append(
                        f'  - selector="{selector}" text="{text}" pos=({el.get("x")},{el.get("y")}) size={el.get("w")}x{el.get("h")} cursor={el.get("cursor")}'
                    )
                clickable_info = (
                    "KLICKBARE ELEMENTE AUF DER SEITE (ECHTE CSS-Selektoren!):\n"
                    + "\n".join(lines)
                )
                audit(
                    "action",
                    message=f"DOM Pre-Scan: {len(elements)} clickable elements found",
                )
    except Exception as e:
        audit("error", message=f"Clickable scan fehlgeschlagen: {e}")

    # 3. Seiten-URL und Titel
    page_context = ""
    try:
        page_info = await execute_bridge("get_page_info", tab_params)
        if isinstance(page_info, dict):
            page_context = f"AKTUELLE SEITE: URL={page_info.get('url', '?')} Title={page_info.get('title', '?')}"
    except Exception:
        pass

    return "\n\n".join(filter(None, [page_context, snapshot_info, clickable_info]))


# ============================================================================
# VISION GATE — Gemini 3 Flash Analyse mit gehärtetem Prompt + DOM-Kontext
# ============================================================================


async def ask_vision(
    screenshot_path: str, action_desc: str, expected: str, step_num: int
):
    """
    Sendet einen Screenshot + DOM-Kontext an Gemini 3 Flash.
    WHY: KEIN EINZIGER KLICK ohne dass das Vision-Modell den Bildschirm gesehen hat.
    CONSEQUENCES: Bei Parse-Fehler wird RETRY zurückgegeben (nie ein Crash).
    """
    # DOM Pre-Scan: Echte Selektoren VOR dem Vision-Call holen!
    dom_context = await dom_prescan()

    # Profil-Kontext aus gespeichertem User-Profil laden
    # WHY: Gemini muss wissen wer der User ist um Profil-Fragen korrekt zu beantworten.
    #      Ohne Profil würde Gemini zufällig wählen → falsche Region, falscher Name etc.
    profile_context = _build_profile_context()

    prompt = f"""Du bist der Vision Gate Controller der OpenSIN-Bridge.

KONTEXT:
- Letzte Aktion: '{action_desc}'
- Erwartetes Ergebnis: '{expected}'
- Schritt Nummer: {step_num} von maximal {MAX_STEPS}

{profile_context}

{dom_context}

AUFGABE — Analysiere den Screenshot UND die DOM-Daten oben PRÄZISE:

1. BLOCKIERUNGEN: Sind Captchas, Cookie-Banner, Consent-Modals, Login-Dialoge, Popups, Overlays oder Error-Messages sichtbar?
   → Wenn ja: Diese ZUERST schliessen/akzeptieren!

2. AKTUELLER STATUS: Was zeigt die Seite GENAU an?

3. FORTSCHRITT: Hat sich gegenüber der letzten Aktion etwas verändert?

4. NÄCHSTE AKTION: Was muss als nächstes passieren?

VERFÜGBARE AKTIONEN (wähle GENAU EINE):
- "click_element" — Standard CSS-Selektor Klick. Params: {{"selector": "#id-oder-.klasse"}}
- "click_ref" — Klick per Accessibility-Tree-Ref (z.B. @e9). BEVORZUGT für Radio-Buttons, Checkboxen, Links ohne ID! Params: {{"ref": "@e9"}}
- "ghost_click" — Voller Pointer+Mouse Event-Stack für SPA/React-Elemente. Params: {{"selector": "#echte-id"}}
- "vision_click" — Beschreibungsbasierter Klick. Params: {{"description": "Text des Elements"}}
- "click_coordinates" — Absoluter Pixel-Klick. Params: {{"x": 100, "y": 200}}
- "keyboard" — Tastatur verwenden (z.B. Tab, Enter). Params: {{"keys": ["Enter"], "selector": "#optional-id"}}
- "type_text" — Text eingeben. Params: {{"selector": "css", "text": "wert"}}
- "navigate" — URL aufrufen. Params: {{"url": "https://..."}}
- "scroll_down" — Seite nach unten scrollen
- "scroll_up" — Seite nach oben scrollen
- "none" — Aufgabe erledigt, nichts mehr zu tun

ABSOLUTE PFLICHT-REGELN FÜR SELEKTOREN:
- NUTZE NUR Selektoren aus der DOM-Analyse oben! NIEMALS raten!
- Pseudo-Selektoren wie :has-text(), :contains(), :has() sind VERBOTEN (existieren nicht in CSS)!
- Bevorzuge #id Selektoren (z.B. #survey-65076903) — die sind IMMER eindeutig!
- WICHTIG: input[type='radio'][value='X'] NIEMALS nutzen — HeyPiggy Radio-Buttons haben KEINE value= Attribute!
- Für Radio-Buttons → IMMER click_ref mit dem @eX Ref aus dem ACCESSIBILITY-TREE oben nutzen!
- Für Survey-Karten auf HeyPiggy: Die Klasse ist .survey-item (NICHT .survey-card!), jede Karte hat eine eindeutige ID wie #survey-XXXXXXXX
- Nutze ghost_click für alle div-basierten Karten (cursor: pointer)
- Playwright-only Texte-Selektoren wie :contains(), :has-text() oder :text() sind VERBOTEN.
- Wenn du Textreferenz brauchst, nenne den echten CSS-Selektor aus dem DOM-Pre-Scan oder eine eindeutige #id.

KLICK-STRATEGIE:
- Für Radio-Buttons ([radio @eX] im Accessibility-Tree) → click_ref mit {{"ref": "@eX"}} — das ist PFLICHT!
- Für <button>, <a>, <input> → click_element
- Für div.survey-item / div[cursor=pointer] → ghost_click mit #id-Selektor
- Für Elemente ohne CSS-Selektor → vision_click mit Beschreibung
- Letzter Ausweg → click_coordinates mit x,y aus der DOM-Analyse

PAGE STATE REGELN — KRITISCH:
- "dashboard" → HeyPiggy Startseite mit Survey-Liste, noch keine Umfrage gestartet
- "login" → Login-Formular sichtbar
- "onboarding" → Profil-Modal/Onboarding-Fragen (Region, Name, etc.) — VOR dem eigentlichen Dashboard!
- "survey_active" → UMFRAGE LÄUFT GERADE! Fragen werden angezeigt (Radio-Buttons, Dropdowns, Textfelder, Skalen). NIEMALS "none" zurückgeben solange Fragen sichtbar sind!
- "survey" → Survey-Auswahl / Übergangsseite (zwischen Dashboard und aktiver Umfrage)
- "survey_done" → Umfrage erfolgreich abgeschlossen, Bestätigungsseite
- "error" → Fehlermeldung, Timeout oder unbekannter Zustand
- "unknown" → Seite nicht klar erkennbar

PROFIL-FRAGEN REGELN — KRITISCH:
- Wenn ein Modal mit Profil-Fragen sichtbar ist (Region, Wohnort, Geschlecht, Name, Alter etc.):
  page_state="onboarding" setzen!
- Nutze IMMER das BENUTZERPROFIL oben um die korrekte Antwort zu wählen!
- Region-Frage ("In welcher Region wohnst du?"): IMMER "Norden" wählen (Jeremy wohnt in Berlin, wählt Norden)
- Nach Auswahl der Antwort → "Nächste"/"Weiter" Button klicken!
- Profil-Modals MÜSSEN vollständig ausgefüllt werden bevor Umfragen gestartet werden!

UMFRAGE-REGELN — ÄUSSERST WICHTIG:
- Wenn page_state="survey_active": BEENDE DIE UMFRAGE VOLLSTÄNDIG! Klicke ALLE Fragen durch bis zur Bestätigungsseite!
- Wenn eine Frage sichtbar ist → IMMER beantworten und "Weiter"/"Next"/"Submit" klicken!
- NIEMALS next_action="none" wenn noch Fragen offen sind!
- Radio-Button Fragen → click_ref mit dem @eX Ref aus dem Accessibility-Tree (NICHT click_element mit value=!)
- Dropdown-Fragen → click_element auf die gewünschte Option
- Freitext-Fragen → type_text mit einer sinnvollen Antwort
- Skalen-Fragen (1-5, 1-7, etc.) → click_element auf mittlere oder positive Option
- "Weiter"/"Next"/"Fortfahren"/"Continue"/"Submit" Buttons → IMMER klicken nach einer Antwort!
- Fortschrittsbalken sichtbar? → Umfrage läuft noch, page_state="survey_active"!

REGELN:
- Antworte AUSSCHLIESSLICH mit gültigem JSON! Kein Markdown, kein Text!
- Bei Captchas oder unlösbaren Blockierungen: verdict="STOP"
- Bei unveränderter Seite: verdict="RETRY" und schlage eine ANDERE Methode vor!
- Credentials NIEMALS ausgeben! Nutze "<EMAIL>" und "<PASSWORD>" als Platzhalter.
- Wähle IMMER die lukrativste verfügbare Umfrage (höchster €-Betrag)!

ANTWORT-FORMAT (NUR dieses JSON, NICHTS anderes):
{{
  "verdict": "PROCEED",
  "page_state": "dashboard|login|onboarding|survey|survey_active|survey_done|error|unknown",
  "reason": "Kurze Analyse...",
  "progress": true,
  "next_action": "click_ref",
  "next_params": {{"ref": "@e9"}}
}}"""

    run_result = await run_vision_model(
        prompt,
        screenshot_path,
        timeout=120,
        step_num=step_num,
        purpose="main_loop",
    )
    if not run_result.get("ok"):
        error_reason = run_result.get("error", "Vision call failed")
        if run_result.get("auth_failure"):
            return {
                "verdict": "STOP",
                "reason": f"Vision auth failed: {error_reason}",
                "next_action": "none",
                "page_state": "error",
                "progress": False,
            }
        return {
            "verdict": "RETRY",
            "reason": error_reason,
            "next_action": "none",
            "page_state": "unknown",
            "progress": False,
        }

    full_text = run_result.get("text", "")

    try:
        # Markdown-Block entfernen falls vorhanden
        if "```json" in full_text:
            full_text = full_text.split("```json")[1].split("```")[0].strip()
        elif "```" in full_text:
            parts = full_text.split("```")
            if len(parts) >= 3:
                full_text = parts[1].strip()
                # Falls der erste Teil nach ``` mit "json" beginnt, entfernen
                if full_text.startswith("json"):
                    full_text = full_text[4:].strip()

        result = json.loads(full_text)
        audit(
            "vision_check",
            step=step_num,
            verdict=result.get("verdict"),
            page_state=result.get("page_state"),
            reason=result.get("reason", "")[:150],
            next_action=result.get("next_action"),
        )
        return result

    except json.JSONDecodeError as e:
        audit(
            "error",
            message=f"Vision JSON Parse Error: {e}",
            step=step_num,
            raw_output=full_text[:500],
        )
        return {
            "verdict": "RETRY",
            "reason": f"JSON Parse Error: {e}",
            "next_action": "none",
            "page_state": "unknown",
            "progress": False,
        }

    except Exception as e:
        audit("error", message=f"Vision Exception: {e}", step=step_num)
        return {
            "verdict": "RETRY",
            "reason": str(e),
            "next_action": "none",
            "page_state": "unknown",
            "progress": False,
        }


# ============================================================================
# KEYBOARD NAVIGATION — Tab, Enter, Arrow Keys als ultimative Bypass-Methode
# ============================================================================


async def keyboard_action(keys: list, selector: str = ""):
    """
    Führt Tastatur-Aktionen aus via JavaScript KeyboardEvent Dispatch.
    WHY: Wenn ALLE Klick-Methoden scheitern, funktionieren Tastatur-Events IMMER,
    weil sie auf OS-Level durchgehen und von keinem Framework blockiert werden.
    CONSEQUENCES: Die allerbeste Umgehung für störrische SPAs.

    Unterstützte Keys: Tab, Enter, Space, ArrowDown, ArrowUp, ArrowLeft, ArrowRight, Escape
    """
    global CURRENT_TAB_ID, CURRENT_WINDOW_ID
    tab_params = _tab_params()
    selector = normalize_selector(selector)

    # Mapping von Key-Namen zu KeyboardEvent-Properties
    key_map = {
        "Tab": {"key": "Tab", "code": "Tab", "keyCode": 9},
        "Enter": {"key": "Enter", "code": "Enter", "keyCode": 13},
        "Space": {"key": " ", "code": "Space", "keyCode": 32},
        "Escape": {"key": "Escape", "code": "Escape", "keyCode": 27},
        "ArrowDown": {"key": "ArrowDown", "code": "ArrowDown", "keyCode": 40},
        "ArrowUp": {"key": "ArrowUp", "code": "ArrowUp", "keyCode": 38},
        "ArrowLeft": {"key": "ArrowLeft", "code": "ArrowLeft", "keyCode": 37},
        "ArrowRight": {"key": "ArrowRight", "code": "ArrowRight", "keyCode": 39},
    }

    results = []
    for key_name in keys:
        kp = key_map.get(key_name, {"key": key_name, "code": key_name, "keyCode": 0})

        # Wenn ein Selektor angegeben ist, erst auf das Element fokussieren
        focus_part = ""
        if selector:
            focus_part = f"""
                var target = document.querySelector("{selector}");
                if (target && typeof target.focus === 'function') {{
                    target.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                    target.focus();
                }}
            """

        js_code = f"""
        (function() {{
            {focus_part}
            var el = document.activeElement || document.body;
            var opts = {{
                key: "{kp["key"]}", code: "{kp["code"]}",
                keyCode: {kp["keyCode"]}, which: {kp["keyCode"]},
                bubbles: true, cancelable: true, composed: true,
                view: window
            }};
            el.dispatchEvent(new KeyboardEvent('keydown', opts));
            el.dispatchEvent(new KeyboardEvent('keypress', opts));
            el.dispatchEvent(new KeyboardEvent('keyup', opts));
            return {{
                success: true, key: "{key_name}",
                target: el.tagName + (el.id ? '#' + el.id : '') + (el.className ? '.' + (el.className + '').split(' ')[0] : ''),
                focused: el === document.activeElement
            }};
        }})();
        """
        try:
            result = await execute_bridge(
                "execute_javascript", {"script": js_code, **tab_params}
            )
            audit("keyboard", key=key_name, result=str(result)[:150])
            results.append(result)
            # Kurze Pause zwischen Tasten wie ein Mensch
            await asyncio.sleep(0.15 + random.random() * 0.25)
        except Exception as e:
            audit("error", message=f"Keyboard {key_name} failed: {e}")
            results.append({"error": str(e)})

    return results


# ============================================================================
# DOM-VERIFIKATION — Prüft ob sich die Seite WIRKLICH verändert hat
# ============================================================================


async def dom_verify_change(before_url: str, before_title: str):
    """
    Prüft via DOM ob die Seite sich nach einer Aktion verändert hat.
    WHY: Vision allein kann täuschen (gleicher Screenshot, aber DOM hat sich geändert).
         DOM allein kann täuschen (URL gleich, aber visuell komplett anders).
         NUR BEIDES ZUSAMMEN gibt Sicherheit!
    CONSEQUENCES: Gibt ein Dict mit changed=True/False und Details zurück.
    """
    tab_params = _tab_params()

    try:
        page_info = await execute_bridge("get_page_info", tab_params)
        current_url = page_info.get("url", "") if isinstance(page_info, dict) else ""
        current_title = (
            page_info.get("title", "") if isinstance(page_info, dict) else ""
        )

        if not current_url and not current_title:
            # Tab may still be loading — wait briefly and retry once with same tabId
            # NEVER switch to a different tab or recover to a new one here
            await asyncio.sleep(1.5)
            page_info = await execute_bridge("get_page_info", tab_params)
            current_url = (
                page_info.get("url", "") if isinstance(page_info, dict) else ""
            )
            current_title = (
                page_info.get("title", "") if isinstance(page_info, dict) else ""
            )

        url_changed = current_url != before_url
        title_changed = current_title != before_title

        # Auch DOM-Diff via Bridge page_diff abfragen (vergleicht Accessibility Trees)
        dom_diff = None
        try:
            diff_result = await execute_bridge("page_diff", tab_params)
            if isinstance(diff_result, dict):
                dom_diff = {
                    "added": diff_result.get("addedCount", 0),
                    "removed": diff_result.get("removedCount", 0),
                    "changed": diff_result.get("changedCount", 0),
                }
        except Exception:
            pass

        changed = (
            url_changed
            or title_changed
            or (
                dom_diff
                and (
                    dom_diff["added"] > 0
                    or dom_diff["removed"] > 0
                    or dom_diff["changed"] > 0
                )
            )
        )

        result = {
            "changed": bool(changed),
            "url_changed": url_changed,
            "title_changed": title_changed,
            "current_url": current_url,
            "current_title": current_title,
            "dom_diff": dom_diff,
        }
        audit("dom_verify", **result)
        return result

    except Exception as e:
        audit("error", message=f"DOM-Verifikation fehlgeschlagen: {e}")
        return {"changed": False, "error": str(e)}


# ============================================================================
# KLICK-ESKALATIONSKETTE — 5 Methoden mit Keyboard-Bypass, automatisch eskalierend
# ============================================================================

MAX_CLICK_ESCALATIONS = 5  # click → ghost → KEYBOARD → vision → coords

# Globaler Schritt-Zähler für Vision-Screenshots innerhalb der Eskalation.
# WHY: take_screenshot() braucht eine step_num — wir verwenden einen eigenen
# Zähler damit Eskalations-Screenshots im Audit-Log klar von Hauptloop-Schritten
# unterscheidbar sind (Format: "esc_NNN").
_ESC_STEP = 0


async def _vision_gate_inside_escalation(
    step_label: str, action_done: str, expected: str
) -> dict:
    """
    Macht Screenshot + Vision-Check INNERHALB der Eskalationskette.
    Gibt das volle Vision-Decision-Dict zurück (verdict, next_action, next_params, page_state).
    WHY: Das Mandat verlangt Vision VOR JEDER AKTION — auch vor jeder Eskalationsstufe.
    CONSEQUENCES: Ohne diesen Gate kann die Eskalation blind 5 Aktionen hintereinander
    feuern ohne zu wissen ob der Klick überhaupt sinnvoll war.
    """
    global _ESC_STEP
    _ESC_STEP += 1
    img_path, _ = await take_screenshot(_ESC_STEP * 1000, label=f"esc_{step_label}")
    if not img_path:
        # Screenshot fehlgeschlagen → pessimistisch RETRY zurückgeben
        return {
            "verdict": "RETRY",
            "next_action": "none",
            "next_params": {},
            "page_state": "unknown",
        }
    return await ask_vision(img_path, action_done, expected, _ESC_STEP * 1000)


async def escalating_click(
    selector: str = "",
    description: str = "",
    x: int = None,
    y: int = None,
    step_num: int = 0,
    ref: str = "",
):
    """
    Versucht einen Klick mit bis zu 5 Methoden — JEDE durch Vision-Gate abgesichert.
    WHY: Verschiedene Webseiten-Technologien brauchen verschiedene Interaktionsmethoden.
    Vision entscheidet nach JEDEM Klickversuch ob die nächste Stufe nötig ist.
    CONSEQUENCES: Kein blinder Auto-Eskalations-Loop mehr — Vision sieht jede Stufe.

    Eskalationskette (vision-gesteuert):
    1. click_ref (Accessibility-Ref, falls vorhanden) → Vision-Check
    2. click_element (Standard CSS-Selektor) → Vision-Check
    3. ghost_click (Voller Pointer+Mouse Event-Stack via JS) → Vision-Check
    4. KEYBOARD (Tab zum Element navigieren + Enter drücken) → Vision-Check
    5. vision_click / click_coordinates als letzte Auswege → Vision-Check
    """
    tab_params = _tab_params()
    selector = normalize_selector(selector)
    selector = await resolve_survey_selector(selector, description)
    if not selector and description:
        desc_lower = description.lower()
        if "umfrage" in desc_lower or "survey" in desc_lower or "€" in desc_lower:
            selector = await resolve_survey_selector("div.survey-item", description)

    methods = []
    if ref:
        methods.append(("click_ref", {**tab_params, "ref": ref}))
    if selector:
        methods.append(("click_element", {**tab_params, "selector": selector}))
    if selector:
        methods.append(("ghost_click_js", selector))
    if selector:
        methods.append(("keyboard_focus_enter", selector))
    if description:
        methods.append(("vision_click", {**tab_params, "description": description}))
    if x is not None and y is not None:
        methods.append(("click_coordinates_js", (x, y)))

    before_url, before_title = "", ""
    try:
        pi = await execute_bridge("get_page_info", tab_params)
        if isinstance(pi, dict):
            before_url = pi.get("url", "")
            before_title = pi.get("title", "")
    except Exception:
        pass

    for i, method_info in enumerate(methods):
        if i >= MAX_CLICK_ESCALATIONS:
            break

        method_name = method_info[0]
        audit(
            "click_escalation",
            level=i + 1,
            method=method_name,
            selector=selector[:80] if selector else "",
        )

        try:
            if method_name == "click_ref":
                result = await execute_bridge("click_ref", method_info[1])
                if isinstance(result, dict) and result.get("error"):
                    audit("error", message=f"click_ref failed: {result['error']}")
                else:
                    await asyncio.sleep(0.8)
                    esc_decision = await _vision_gate_inside_escalation(
                        f"after_click_ref_{i}",
                        f"click_ref auf {ref[:60]}",
                        "Seite hat reagiert",
                    )
                    audit(
                        "vision_check",
                        method="click_ref",
                        verdict=esc_decision.get("verdict"),
                        page_state=esc_decision.get("page_state"),
                    )
                    if esc_decision.get("verdict") == "PROCEED":
                        return True
                continue

            if method_name == "click_element":
                result = await execute_bridge("click_element", method_info[1])
                if isinstance(result, dict) and result.get("error"):
                    audit("error", message=f"click_element failed: {result['error']}")
                else:
                    await asyncio.sleep(0.8)
                    esc_decision = await _vision_gate_inside_escalation(
                        f"after_click_element_{i}",
                        f"click_element auf {selector[:60]}",
                        "Seite hat reagiert",
                    )
                    audit(
                        "vision_check",
                        method="click_element",
                        verdict=esc_decision.get("verdict"),
                        page_state=esc_decision.get("page_state"),
                    )
                    if esc_decision.get("verdict") == "PROCEED":
                        return True
                continue

            elif method_name == "ghost_click_js":
                sel = method_info[1]
                js_code = f"""
                (function() {{
                    const el = document.querySelector("{sel}");
                    if (!el) return {{ error: "Element not found", selector: "{sel}" }};
                    el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                    const rect = el.getBoundingClientRect();
                    const x = rect.left + rect.width / 2;
                    const y = rect.top + rect.height / 2;
                    if (typeof el.focus === 'function') el.focus();
                    const opts = {{
                        bubbles: true, cancelable: true,
                        clientX: x, clientY: y, screenX: x, screenY: y,
                        view: window, detail: 1, button: 0, buttons: 1
                    }};
                    el.dispatchEvent(new PointerEvent('pointerover', opts));
                    el.dispatchEvent(new PointerEvent('pointerenter', {{...opts, bubbles: false}}));
                    el.dispatchEvent(new MouseEvent('mouseover', opts));
                    el.dispatchEvent(new MouseEvent('mouseenter', {{...opts, bubbles: false}}));
                    el.dispatchEvent(new PointerEvent('pointerdown', opts));
                    el.dispatchEvent(new MouseEvent('mousedown', opts));
                    el.dispatchEvent(new PointerEvent('pointerup', {{...opts, buttons: 0}}));
                    el.dispatchEvent(new MouseEvent('mouseup', {{...opts, buttons: 0}}));
                    el.dispatchEvent(new MouseEvent('click', {{...opts, buttons: 0}}));
                    if (typeof el.click === 'function') el.click();
                    return {{ success: true, tag: el.tagName, text: (el.textContent || '').substring(0, 60) }};
                }})();
                """
                result = await execute_bridge(
                    "execute_javascript", {"script": js_code, **tab_params}
                )
                if isinstance(result, dict) and result.get("error"):
                    audit("error", message=f"ghost_click failed: {result['error']}")
                else:
                    await asyncio.sleep(0.8)
                    esc_decision = await _vision_gate_inside_escalation(
                        f"after_ghost_click_{i}",
                        f"ghost_click auf {sel[:60]}",
                        "Seite hat reagiert",
                    )
                    audit(
                        "vision_check",
                        method="ghost_click",
                        verdict=esc_decision.get("verdict"),
                        page_state=esc_decision.get("page_state"),
                    )
                    if esc_decision.get("verdict") == "PROCEED":
                        return True
                continue

            elif method_name == "keyboard_focus_enter":
                sel = method_info[1]
                focus_js = f"""
                (function() {{
                    var el = document.querySelector("{sel}");
                    if (!el) return {{ error: "Element not found" }};
                    el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                    el.setAttribute('tabindex', '0');
                    el.focus();
                    return {{
                        success: true, focused: document.activeElement === el,
                        tag: el.tagName, id: el.id || '', text: (el.textContent || '').substring(0, 40)
                    }};
                }})();
                """
                focus_result = await execute_bridge(
                    "execute_javascript", {"script": focus_js, **tab_params}
                )
                audit("keyboard", action="focus", result=str(focus_result)[:150])
                await asyncio.sleep(0.3)
                await keyboard_action(["Enter"], selector=sel)
                await asyncio.sleep(0.8)
                esc_decision = await _vision_gate_inside_escalation(
                    f"after_keyboard_enter_{i}",
                    f"keyboard Enter auf {sel[:60]}",
                    "Seite hat reagiert",
                )
                audit(
                    "vision_check",
                    method="keyboard_enter",
                    verdict=esc_decision.get("verdict"),
                    page_state=esc_decision.get("page_state"),
                )
                if esc_decision.get("verdict") == "PROCEED":
                    return True
                await keyboard_action(["Space"], selector=sel)
                await asyncio.sleep(0.8)
                esc_decision2 = await _vision_gate_inside_escalation(
                    f"after_keyboard_space_{i}",
                    f"keyboard Space auf {sel[:60]}",
                    "Seite hat reagiert",
                )
                audit(
                    "vision_check",
                    method="keyboard_space",
                    verdict=esc_decision2.get("verdict"),
                    page_state=esc_decision2.get("page_state"),
                )
                if esc_decision2.get("verdict") == "PROCEED":
                    return True
                continue

            elif method_name == "vision_click":
                result = await execute_bridge("vision_click", method_info[1])
                if isinstance(result, dict) and result.get("error"):
                    audit("error", message=f"vision_click failed: {result['error']}")
                else:
                    await asyncio.sleep(0.8)
                    esc_decision = await _vision_gate_inside_escalation(
                        f"after_vision_click_{i}",
                        f"vision_click '{description[:40]}'",
                        "Seite hat reagiert",
                    )
                    audit(
                        "vision_check",
                        method="vision_click",
                        verdict=esc_decision.get("verdict"),
                        page_state=esc_decision.get("page_state"),
                    )
                    if esc_decision.get("verdict") == "PROCEED":
                        return True
                continue

            elif method_name == "click_coordinates_js":
                cx, cy = method_info[1]
                js_code = f"""
                (function() {{
                    const el = document.elementFromPoint({cx}, {cy});
                    if (!el) return {{ error: "Kein Element bei ({cx}, {cy})" }};
                    const opts = {{
                        bubbles: true, cancelable: true,
                        clientX: {cx}, clientY: {cy}, screenX: {cx}, screenY: {cy},
                        view: window, detail: 1, button: 0, buttons: 1
                    }};
                    el.dispatchEvent(new PointerEvent('pointerdown', opts));
                    el.dispatchEvent(new MouseEvent('mousedown', opts));
                    el.dispatchEvent(new PointerEvent('pointerup', {{...opts, buttons: 0}}));
                    el.dispatchEvent(new MouseEvent('mouseup', {{...opts, buttons: 0}}));
                    el.dispatchEvent(new MouseEvent('click', {{...opts, buttons: 0}}));
                    if (typeof el.click === 'function') el.click();
                    return {{ success: true, tag: el.tagName, text: (el.textContent || '').substring(0, 60) }};
                }})();
                """
                result = await execute_bridge(
                    "execute_javascript", {"script": js_code, **tab_params}
                )
                if isinstance(result, dict) and result.get("error"):
                    audit("error", message=f"coord_click failed: {result}")
                else:
                    await asyncio.sleep(0.8)
                    esc_decision = await _vision_gate_inside_escalation(
                        f"after_coord_click_{i}",
                        f"coord_click ({cx},{cy})",
                        "Seite hat reagiert",
                    )
                    audit(
                        "vision_check",
                        method="coord_click",
                        verdict=esc_decision.get("verdict"),
                        page_state=esc_decision.get("page_state"),
                    )
                    if esc_decision.get("verdict") == "PROCEED":
                        return True
                continue

        except Exception as e:
            audit("error", message=f"Klick-Methode {method_name} Exception: {e}")
            continue

    audit(
        "error",
        message="ALLE 5 Klick-Methoden fehlgeschlagen!",
        selector=selector[:80] if selector else "",
    )
    return False


# ============================================================================
# SESSION-BACKUP — Cookies sichern bei jedem wichtigen Statuswechsel
# ============================================================================


async def save_session(label: str):
    """
    Sichert die aktuelle Browser-Session (Cookies, LocalStorage).
    WHY: Bei Bridge-Disconnect oder Crash müssen wir die Session wiederherstellen können.
    """
    try:
        params = _tab_params()
        cookies = await execute_bridge("export_all_cookies", params)
        session_file = SESSION_DIR / f"session_{label}_{RUN_ID}.json"
        session_file.write_text(
            json.dumps(cookies, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        audit("session_save", label=label, path=str(session_file))
    except Exception as e:
        audit("error", message=f"Session-Backup fehlgeschlagen: {e}")


# ============================================================================
# HUMAN DELAYS — Zufällige Pausen gegen Bot-Erkennung
# ============================================================================


async def human_delay(min_sec=1.5, max_sec=4.5):
    """
    Wartet eine zufällige Zeitspanne wie ein echter Mensch.
    WHY: Konstante Delays (z.B. immer 3s) sind ein Bot-Signal.
    """
    delay = min_sec + random.random() * (max_sec - min_sec)
    await asyncio.sleep(delay)


# ============================================================================
# VISION GATE CONTROLLER — Herzstück der Sicherheit
# ============================================================================


class VisionGateController:
    """
    Steuert den gesamten Vision-Gate-Loop und verhindert Endlosschleifen.

    WHY: Ohne diesen Controller laufen Agenten in Endlosschleifen.
    CONSEQUENCES: Controller-Verletzung = Sofortiger Abbruch.

    Tracking:
    - total_steps: Gesamtzahl aller Aktionen
    - consecutive_retries: Aufeinanderfolgende RETRY-Verdicts
    - no_progress_count: Aktionen ohne sichtbare Bildschirmveränderung
    - last_screenshot_hash: MD5-Hash des letzten Screenshots für Vergleich
    - failed_selectors: Selektoren die bereits fehlgeschlagen sind (werden nicht nochmal versucht)
    """

    def __init__(self):
        self.total_steps = 0
        self.consecutive_retries = 0
        self.no_progress_count = 0
        self.last_screenshot_hash = None
        self.failed_selectors = set()
        self.last_page_state = None
        self.successful_actions = 0

    def should_continue(self) -> bool:
        """Prüft ob der Worker weitermachen darf."""
        if self.total_steps >= MAX_STEPS:
            audit("stop", reason=f"MAX_STEPS ({MAX_STEPS}) erreicht")
            return False
        if self.consecutive_retries >= MAX_RETRIES:
            audit("stop", reason=f"MAX_RETRIES ({MAX_RETRIES}) erreicht")
            return False
        if self.no_progress_count >= MAX_NO_PROGRESS:
            audit("stop", reason=f"MAX_NO_PROGRESS ({MAX_NO_PROGRESS}) erreicht")
            return False
        return True

    def record_step(
        self,
        verdict: str,
        screenshot_hash: str,
        page_state: str = None,
        dom_changed: bool = False,
    ):
        """Zeichnet einen Schritt auf und aktualisiert alle Zähler."""
        self.total_steps += 1

        # RETRY-Tracking
        if verdict == "RETRY":
            self.consecutive_retries += 1
        else:
            self.consecutive_retries = 0

        # Fortschritts-Erkennung:
        # WHY: Bei survey_active sehen Screenshots Frage-für-Frage fast identisch aus
        # (gleicher Header, gleiche Farben, gleiche Schriftarten). Hash-Vergleich würde
        # das fälschlich als "kein Fortschritt" werten und die Umfrage abbrechen.
        # LÖSUNG: Wenn wir mitten in einer aktiven Umfrage sind (survey_active),
        # gilt der Schritt IMMER als Fortschritt — egal ob Hash gleich ist.
        # Zusätzlich zählt dom_changed=True ebenfalls als Fortschritt.
        currently_in_survey = page_state in ("survey_active", "survey")
        if (
            screenshot_hash
            and screenshot_hash == self.last_screenshot_hash
            and not currently_in_survey
            and not dom_changed
        ):
            self.no_progress_count += 1
        else:
            self.no_progress_count = 0
            self.last_screenshot_hash = screenshot_hash

        # Page-State-Tracking
        if page_state:
            if page_state != self.last_page_state:
                audit("state_change", old=self.last_page_state, new=page_state)
            self.last_page_state = page_state

        # Erfolgs-Tracking
        if verdict == "PROCEED":
            self.successful_actions += 1

    def add_failed_selector(self, selector: str):
        """Merkt sich einen fehlgeschlagenen Selektor um ihn nicht nochmal zu versuchen."""
        if selector:
            self.failed_selectors.add(selector)

    def is_selector_failed(self, selector: str) -> bool:
        """Prüft ob ein Selektor bereits fehlgeschlagen ist."""
        return selector in self.failed_selectors

    def mark_dom_progress(self):
        """
        Setzt no_progress_count zurück wenn DOM-Verifikation echte Änderung bestätigt.
        WHY: record_step() läuft VOR der Aktion und kennt dom_changed noch nicht.
             mark_dom_progress() wird NACH der Aktion aufgerufen um einen fälschlichen
             no_progress-Zähler zu korrigieren — kritisch bei Survey-Fragen deren
             Screenshot fast identisch aussieht aber der DOM sich verändert hat.
        """
        if self.no_progress_count > 0:
            self.no_progress_count = 0
            audit(
                "state_change",
                message="DOM-Fortschritt bestätigt: no_progress_count zurückgesetzt",
            )


# ============================================================================
# CREDENTIAL INJECTION — Sichere Ersetzung von Platzhaltern
# ============================================================================


def inject_credentials(params: dict, email: str, pwd: str) -> dict:
    """
    Ersetzt <EMAIL> und <PASSWORD> Platzhalter mit echten Credentials.
    WHY: Die AI darf NIEMALS echte Passwörter sehen oder ausgeben.
    CONSEQUENCES: Nur Platzhalter werden ersetzt, alles andere bleibt unverändert.
    """
    if "text" not in params:
        return params

    text = params["text"]
    if text == "<EMAIL>" or text.upper() == "EMAIL":
        params["text"] = email or ""
        audit("action", message="Credential injected: EMAIL (redacted)")
    elif text == "<PASSWORD>" or text.upper() == "PASSWORD":
        params["text"] = pwd or ""
        audit("action", message="Credential injected: PASSWORD (redacted)")

    return params


# ============================================================================
# SCROLL-HANDLER
# ============================================================================


async def handle_scroll(direction: str):
    """Scrollt die Seite nach oben oder unten."""
    tab_params = _tab_params()
    pixels = 400 if direction == "scroll_down" else -400
    js_code = f"window.scrollBy(0, {pixels}); ({{ scrolled: true, by: {pixels} }})"
    await execute_bridge("execute_javascript", {"script": js_code, **tab_params})
    audit("action", message=f"Scrolled {direction}", pixels=pixels)


# ============================================================================
# ACTION-DISPATCH — Einheitlicher Pfad für alle Click-Entry-Points
# ============================================================================


async def run_click_action(next_params: dict, gate, img_hash: str, step_num: int) -> bool:
    """
    Leitet alle Click-Aktionen durch genau EINE verifizierte Eskalationspipeline.
    WHY: Issue #86 verlangt, dass `click_ref` keinen direkten Bridge-Bypass mehr hat.
    CONSEQUENCES: Jeder Click-Entry-Point läuft hier zentral durch `escalating_click()`.
    """
    selector = next_params.get("selector", "")
    description = next_params.get("description", "")
    x = next_params.get("x")
    y = next_params.get("y")
    ref = next_params.get("ref", "")

    if selector and gate.is_selector_failed(selector):
        audit(
            "state_change",
            message=f"Selektor '{selector[:50]}' bereits fehlgeschlagen, überspringe",
        )
        gate.record_step("RETRY", img_hash)
        return False

    clicked = await escalating_click(
        selector=selector,
        description=description,
        x=x,
        y=y,
        step_num=step_num,
        ref=ref,
    )

    if not clicked:
        if selector:
            gate.add_failed_selector(selector)
        audit("error", message="Klick-Eskalation komplett fehlgeschlagen")

    return clicked


# ============================================================================
# HAUPTSCHLEIFE — Der komplette Vision Gate Loop
# ============================================================================


async def main():
    audit(
        "start",
        message="A2A-SIN-Worker-HeyPiggy Vision Gate v2.0",
        run_id=RUN_ID,
        artifact_dir=str(ARTIFACT_DIR),
    )

    # 1. BRIDGE-VERBINDUNG PRÜFEN
    try:
        await wait_for_extension(timeout=600)
    except Exception as e:
        audit("stop", reason=f"Bridge-Verbindung fehlgeschlagen: {e}")
        return

    # 2. PRE-FLIGHT — Pflicht-Env + Vision-Auth müssen VOR Browser-Mutation healthy sein
    preflight = await ensure_worker_preflight()
    if not preflight.get("ok"):
        return

    # Credentials erst NACH erfolgreichem fail-closed Preflight auslesen.
    # WHY: Die eigentliche Worker-Logik braucht die Werte für inject_credentials(),
    # aber nur nachdem bewiesen ist, dass Env vollständig und Vision healthy sind.
    email = os.environ.get("HEYPIGGY_EMAIL")
    pwd = os.environ.get("HEYPIGGY_PASSWORD")

    # 3. VISION GATE CONTROLLER INITIALISIEREN
    gate = VisionGateController()

    # 4. INITIALE NAVIGATION
    action_desc = "Navigiere zu HeyPiggy Dashboard"
    expected = "Dashboard mit verfügbaren Umfragen oder Login-Formular"

    global CURRENT_TAB_ID, CURRENT_WINDOW_ID
    try:
        audit("navigate", url="https://www.heypiggy.com/login")
        tab_res = await execute_bridge(
            "tabs_create", {"url": "https://www.heypiggy.com/login", "active": False}
        )
        if isinstance(tab_res, dict) and "tabId" in tab_res:
            CURRENT_TAB_ID = tab_res["tabId"]
            CURRENT_WINDOW_ID = tab_res.get("windowId", CURRENT_WINDOW_ID)
            audit(
                "success",
                message=f"Worker-Tab erstellt und gebunden: tabId={CURRENT_TAB_ID}, windowId={CURRENT_WINDOW_ID}",
            )
        else:
            # tabs_create hat keine tabId zurückgegeben — harter Abbruch.
            # KEIN Fallback auf fremde Tabs, da wir sonst einen User-Tab steuern würden.
            audit(
                "stop",
                reason=f"tabs_create hat keine tabId zurückgegeben: {tab_res}. "
                "Kein Fallback auf aktiven Tab erlaubt.",
            )
            return
    except Exception as e:
        audit("stop", reason=f"Initiale Navigation fehlgeschlagen: {e}")
        return

    # Verifikation: CURRENT_TAB_ID muss jetzt gesetzt sein
    if CURRENT_TAB_ID is None:
        audit("stop", reason="CURRENT_TAB_ID ist nach Init immer noch None — Abbruch")
        return

    # Warten auf Seitenlade
    await human_delay(4.0, 6.0)

    # Session direkt nach Laden sichern
    await save_session("initial_load")

    # 5. VISION GATE LOOP — Das Herzstück
    while gate.should_continue():
        # ---- Bridge-Health-Check vor JEDER Iteration ----
        if not await check_bridge_alive():
            audit("stop", reason="Bridge nicht erreichbar, Abbruch")
            break

        # ---- SCREENSHOT ----
        img_path, img_hash = await take_screenshot(
            gate.total_steps + 1, label=action_desc[:20]
        )
        if not img_path:
            gate.record_step("RETRY", None)
            await human_delay(2.0, 4.0)
            continue

        # ---- VISION CHECK ----
        decision = await ask_vision(
            img_path, action_desc, expected, gate.total_steps + 1
        )

        verdict = decision.get("verdict", "RETRY")
        reason = decision.get("reason", "Kein Grund")
        page_state = decision.get("page_state", "unknown")
        next_action = decision.get("next_action", "none")
        next_params = decision.get("next_params", {})
        progress = decision.get("progress", False)

        # Schritt aufzeichnen
        gate.record_step(verdict, img_hash, page_state)

        print(f"\n{'=' * 60}")
        print(
            f"SCHRITT {gate.total_steps}/{MAX_STEPS} | Verdict: {verdict} | State: {page_state}"
        )
        print(f"Reason: {reason}")
        print(
            f"Next: {next_action} {json.dumps(next_params, ensure_ascii=False)[:120]}"
        )
        print(
            f"Retries: {gate.consecutive_retries}/{MAX_RETRIES} | No-Progress: {gate.no_progress_count}/{MAX_NO_PROGRESS}"
        )
        print(f"{'=' * 60}\n")

        # ---- STOP ----
        if verdict == "STOP":
            audit("stop", reason=reason, page_state=page_state)
            await save_session("stop_state")
            break

        # ---- RETRY ----
        if verdict == "RETRY":
            # Bei RETRY den Selektor als fehlgeschlagen merken
            if next_params.get("selector"):
                gate.add_failed_selector(next_params["selector"])
            await human_delay(2.0, 4.0)
            continue

        # ---- DONE ----
        if next_action == "none":
            audit(
                "success",
                message="Vision meldet: Aufgabe erledigt!",
                total_steps=gate.total_steps,
            )
            await save_session("completed")
            break

        # ---- SURVEY DONE — Bestätigungsseite erkannt ----
        # WHY: Wenn page_state="survey_done" bedeutet das, die aktuelle Umfrage wurde
        # erfolgreich abgeschlossen und eine Bestätigungsseite ist sichtbar.
        # KONSEQUENZ: Wir brechen NICHT ab — wir sichern den Fortschritt und
        # lassen den Hauptloop weiterlaufen, damit die Vision die nächste Umfrage
        # oder die Rückkehr zum Dashboard selbst erkennt und navigiert.
        # WARNUNG: Hier kein "break"! Abbrechen würde weitere ausstehende Surveys verpassen.
        if page_state == "survey_done":
            audit(
                "success",
                message="Umfrage vollständig abgeschlossen — Bestätigungsseite erkannt! Warte auf nächste Umfrage.",
                page_state=page_state,
                total_steps=gate.total_steps,
            )
            await save_session(f"survey_done_{gate.total_steps}")
            # no_progress_count zurücksetzen — Abschluss ist echter Fortschritt
            gate.mark_dom_progress()
            await human_delay(2.0, 4.0)
            continue

        # ---- CREDENTIAL INJECTION ----
        if next_action == "type_text" and next_params:
            next_params = inject_credentials(next_params, email, pwd)

        # ---- AKTION AUSFÜHREN ----
        action_desc = (
            f"{next_action} {json.dumps(next_params, ensure_ascii=False)[:80]}"
        )
        expected = f"UI hat auf {next_action} reagiert und sich verändert"
        audit(
            "action",
            action=next_action,
            params={
                k: v
                for k, v in next_params.items()
                if k != "text" or next_action != "type_text"
            },
        )

        # URL und Title VOR der Aktion für DOM-Verifikation sammeln
        before_url, before_title = "", ""
        try:
            pi_params = _tab_params()
            pi = await execute_bridge("get_page_info", pi_params)
            if isinstance(pi, dict):
                before_url = pi.get("url", "")
                before_title = pi.get("title", "")
        except Exception:
            pass

        try:
            # Scroll-Aktionen
            if next_action in ("scroll_down", "scroll_up"):
                await handle_scroll(next_action)

            # Klick-Aktionen (mit EINER gemeinsamen Eskalationskette)
            elif next_action in CLICK_ACTIONS:
                await run_click_action(next_params, gate, img_hash, gate.total_steps)

            # Explizite Keyboard-Aktion von Vision
            elif next_action == "keyboard":
                keys = next_params.get("keys", ["Enter"])
                if isinstance(keys, str):
                    keys = [keys]
                selector = next_params.get("selector", "")
                await keyboard_action(keys, selector=selector)

            # Text-Eingabe — IMMER mit exaktem tabId
            elif next_action == "type_text":
                params = {**next_params, **_tab_params()}
                await execute_bridge("type_text", params)

            # Navigation — IMMER mit exaktem tabId, KEIN Fallback ohne tabId
            elif next_action == "navigate":
                url = next_params.get("url", "")
                await execute_bridge("navigate", {"url": url, **_tab_params()})
                await save_session(f"nav_{gate.total_steps}")

            # Alle anderen Bridge-Tools — IMMER mit exaktem tabId
            else:
                params = {**next_params, **_tab_params()}
                await execute_bridge(next_action, params)

        except Exception as e:
            audit(
                "error",
                message=f"Aktion {next_action} Exception: {e}",
                traceback=traceback.format_exc()[:500],
            )

        # ---- DOM-VERIFIKATION NACH JEDER AKTION ----
        # WHY: Screenshot-Hash allein kann Survey-Frage-zu-Frage-Übergänge nicht erkennen
        # (gleicher Header, gleiche Farben → gleicher Hash → fälschlicher "kein Fortschritt").
        # DOM-Verifikation prüft URL + Title — ändert sich irgendeins, war es echter Fortschritt.
        # KONSEQUENZ: mark_dom_progress() setzt no_progress_count zurück → kein vorzeitiger Abbruch.
        await asyncio.sleep(1.0)
        dom_check = await dom_verify_change(before_url, before_title)
        if dom_check.get("changed"):
            # DOM hat sich verändert → echter Fortschritt → no_progress_count zurücksetzen
            gate.mark_dom_progress()
            audit(
                "success",
                message="DOM-Verifikation: Seite hat sich nach Aktion erfolgreich verändert!",
            )
        else:
            audit(
                "warning",
                message="DOM-Verifikation: Keine Veränderung nach Aktion erkannt (Vision wird gleich prüfen).",
            )

        # ---- HUMAN DELAY ----
        await human_delay(1.5, 4.5)

    # ============================================================================
    # ABSCHLUSS — Zusammenfassung und Proof-Collection
    # ============================================================================

    # Final Session sichern
    await save_session("final")

    # Zusammenfassung
    summary = {
        "run_id": RUN_ID,
        "total_steps": gate.total_steps,
        "successful_actions": gate.successful_actions,
        "consecutive_retries": gate.consecutive_retries,
        "no_progress_count": gate.no_progress_count,
        "last_page_state": gate.last_page_state,
        "failed_selectors": list(gate.failed_selectors),
        "artifact_dir": str(ARTIFACT_DIR),
        "screenshots": len(list(SCREENSHOT_DIR.glob("*.png"))),
        "audit_entries": sum(1 for _ in open(AUDIT_LOG_PATH)),
    }

    summary_path = ARTIFACT_DIR / "run_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False))

    print(f"\n{'=' * 60}")
    print(f"🏁 LAUF BEENDET — Zusammenfassung:")
    print(f"   Schritte: {gate.total_steps}/{MAX_STEPS}")
    print(f"   Erfolgreich: {gate.successful_actions}")
    print(f"   Screenshots: {summary['screenshots']}")
    print(f"   Artefakte: {ARTIFACT_DIR}")
    print(f"   Audit-Log: {AUDIT_LOG_PATH}")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    asyncio.run(main())
