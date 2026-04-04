# Self-Healer Skill

## Beschreibung
Dieser Skill wird automatisch vom macOS Background Watcher ausgelöst, wenn ein SIN-Solver Mikro-Schritt fehlschlägt und eine `healing_request.txt` generiert wurde.

## Instruktionen für die KI (STRICKT BEFOLGEN)
1. **Lesen**: Lese die bereitgestellte Datei `healing_request.processing.txt` im aktuellen Verzeichnis. Sie enthält den fehlgeschlagenen Schritt, den Stacktrace und den PFAD ZUM SCREENSHOT (`SCREENSHOT_PATH`).
2. **Visual Check**: Nutze dein Tool `look_at` um dir den Screenshot unter `SCREENSHOT_PATH` anzusehen! Du MUSST sehen, wie der Browser im Moment des Fehlers aussah.
3. **Web-Suche (Pflicht!)**: Du darfst KEINE Trainingsdaten nutzen. Nutze dein Google/Exa Search Tool, um nach dem genauen Fehler + "nodriver python" zu suchen. Finde mindestens 5-10 aktuelle Quellen.
4. **Reparieren**: Überschreibe die fehlerhafte Mikro-Datei (`step_XX.py`). 
   - Regel 1: Max 30 Zeilen.
   - Regel 2: Keine Kommentare oder Docstrings.
   - Regel 3: `nodriver` auf Port 9222 nutzen.
   - Regel 4: Nach der Aktion Screenshot speichern.
5. **Aufräumen & Cache-Reinigung (PFLICHT)**: Lösche die `healing_request.processing.txt` nach erfolgreichem Fix. 
   - Führe danach einen systematischen Cleanup der Agenten-Umgebung (MacBook oder HF VM) durch, damit der Speicher nicht vollläuft:
     * `rm -rf ~/.local/share/opencode/tool-output/*` (Riesige Log-Buffer)
     * `rm -f /tmp/m*_RESULT.png` (Alte Debug-Screenshots)
     * `rm -rf ~/.npm/_cacache` (Node.js Ballast)
     * `rm -f ~/.local/share/opencode/log/*.log` (Alte Runner-Logs)
     * **ACHTUNG:** Lösche NIEMALS die Agenten-Sessions (`~/.local/share/opencode/sessions`), Kontexte, Memory-Daten oder Auth-Profile!
6. **Dokumentation**: Trage den Bug und den Fix SOFORT in `~/dev/docs/sin-solver/repair-docs.md` ein.
7. **Schließen**: Melde "Reparatur abgeschlossen".