#!/usr/bin/env python3
"""
QWEN AUTH ACCOUNTS HEALTH REPAIR SCRIPT
Autor: OpenCode Agent
Zweck: Automatische Reparatur der Qwen Multi-Account Konfiguration
"""

import json
import sys
import os
from datetime import datetime

CONFIG_PATH = "/Users/jeremy/.config/opencode/qwen-auth-accounts.json"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def save_config(data):
    # Atomic write
    temp_path = CONFIG_PATH + ".tmp"
    with open(temp_path, "w") as f:
        json.dump(data, f, indent=2)
    os.replace(temp_path, CONFIG_PATH)


def select_healthiest_account(accounts):
    """
    Wählt den gesündesten Account basierend auf:
    1. consecutiveFailures == 0 (bevorzugt)
    2. Höchste successCount
    3. Gutes success/failure Verhältnis
    """
    healthy_candidates = []

    for idx, acc in enumerate(accounts):
        health = acc.get("health", {})
        cons = health.get("consecutiveFailures", 0)
        success = health.get("successCount", 0)
        failure = health.get("failureCount", 0)

        # Kriterien für gesunde Accounts
        if cons == 0 and success > 0:
            ratio = success / (success + failure) if (success + failure) > 0 else 0
            healthy_candidates.append(
                {
                    "index": idx,
                    "success": success,
                    "failure": failure,
                    "ratio": ratio,
                    "lastUsed": acc.get("lastUsed", 0),
                }
            )

    if not healthy_candidates:
        print("❌ KEINE GESUNDEN ACCOUNTS GEFUNDEN!")
        return None

    # Sortiere nach successCount (meiste successes zuerst)
    healthy_candidates.sort(key=lambda x: x["success"], reverse=True)

    print(f"✅ {len(healthy_candidates)} gesunde Accounts gefunden:")
    for cand in healthy_candidates[:10]:
        print(
            f"   Index {cand['index']}: {cand['success']} successes, ratio {cand['ratio']:.2%}"
        )

    return healthy_candidates[0]["index"]


def main():
    print(f"\n🔧 QWEN AUTH ACCOUNTS REPAIR TOOL")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"=" * 60)

    # Load config
    try:
        data = load_config()
    except Exception as e:
        print(f"❌ Fehler beim Laden: {e}")
        sys.exit(1)

    accounts = data.get("accounts", [])
    current_active = data.get("activeIndex")
    print(f"Aktueller activeIndex: {current_active}")
    print(f"Total Accounts: {len(accounts)}")

    # Finde Probleme
    problematic = []
    for idx, acc in enumerate(accounts):
        health = acc.get("health", {})
        cons = health.get("consecutiveFailures", 0)
        if cons > 20:
            problematic.append(
                {
                    "index": idx,
                    "consecutive": cons,
                    "success": health.get("successCount", 0),
                    "failure": health.get("failureCount", 0),
                }
            )

    if problematic:
        print(f"\n⚠️  PROBLEMATISCHE ACCOUNTS (consecutiveFailures > 20):")
        for p in sorted(problematic, key=lambda x: x["consecutive"], reverse=True)[:10]:
            print(
                f"   Index {p['index']}: {p['consecutive']} cons.fails, {p['success']}/{p['failure']}"
            )
    else:
        print("\n✅ Keine kritischen Accounts gefunden!")

    # Wähle gesündesten Account
    best_index = select_healthiest_account(accounts)

    if best_index is None:
        print("❌ ABBRUCH: Kein gesunder Account verfügbar!")
        sys.exit(1)

    # Prüfe ob wir wechseln müssen
    if current_active == best_index:
        print(f"\n✅ activeIndex ist bereits optimal: {best_index}")
    else:
        print(f"\n🔄 Wechsle activeIndex von {current_active} → {best_index}")
        data["activeIndex"] = best_index
        try:
            save_config(data)
            print("✅ Konfiguration erfolgreich gespeichert!")
        except Exception as e:
            print(f"❌ Fehler beim Speichern: {e}")
            sys.exit(1)

    print("\n" + "=" * 60)
    print("✅ REPARATURE ABGESCHLOSSEN")
    print(f"🎯 Neuer aktiver Account: Index {best_index}")
    print(
        f"📊 Bitte testen Sie nun einen Qwen API-Call um zu bestätigen, dass der Account funktioniert."
    )


if __name__ == "__main__":
    main()
