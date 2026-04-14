#!/usr/bin/env python3
"""
QWEN ACCOUNT QUARANTINE - NON-INTERACTIVE
Automatische Bereinigung ohne Benutzerabfrage
"""

import json
import sys
import os
from datetime import datetime

CONFIG_PATH = "/Users/jeremy/.config/opencode/qwen-auth-accounts.json"
QUARANTINE_PATH = "/Users/jeremy/.config/opencode/qwen-auth-accounts.quarantined.json"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def save_config(data):
    temp_path = CONFIG_PATH + ".tmp"
    with open(temp_path, "w") as f:
        json.dump(data, f, indent=2)
    os.replace(temp_path, CONFIG_PATH)


def main():
    print(f"\n🧹 QWEN ACCOUNT QUARANTINE (AUTO)")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"=" * 60)

    data = load_config()
    accounts = data.get("accounts", [])
    current_active = data.get("activeIndex")

    # 1. Identify quarantine candidates: consecutiveFailures > 20
    to_quarantine = []
    to_keep = []

    for idx, acc in enumerate(accounts):
        health = acc.get("health", {})
        cons = health.get("consecutiveFailures", 0)
        if cons > 20:
            to_quarantine.append(
                {
                    "index": idx,
                    "consecutive": cons,
                    "success": health.get("successCount", 0),
                    "failure": health.get("failureCount", 0),
                }
            )
        else:
            to_keep.append(acc)

    print(f"🔍 Kritische Accounts (>20 cons.fails): {len(to_quarantine)}")
    print(f"✅ Gesunde Accounts: {len(to_keep)}")
    print(f"📊 Aktueller activeIndex: {current_active}")

    if not to_quarantine:
        print("✅ Keine Accounts zu quarantänen.")
        return

    # 2. Bestimme den besten verbleibenden Account für activeIndex
    best_idx_in_kept = None
    best_score = -1

    for idx, acc in enumerate(to_keep):
        health = acc.get("health", {})
        cons = health.get("consecutiveFailures", 0)
        success = health.get("successCount", 0)
        failure = health.get("failureCount", 0)

        if cons == 0 and success > 0:
            # Prefer highest success count
            if success > best_score:
                best_score = success
                best_idx_in_kept = idx

    # 3. If current active is in quarantine, switch to best
    new_active_index = current_active
    if current_active is not None:
        is_active_quarantined = any(q["index"] == current_active for q in to_quarantine)
        if is_active_quarantined:
            if best_idx_in_kept is not None:
                new_active_index = best_idx_in_kept
                print(
                    f"🔁 Aktiver Account (Index {current_active}) ist kritisch → wechsel zu Index {new_active_index}"
                )
            else:
                print(
                    "⚠️  Aktiver Account kritisch, aber kein besserer Ersatz gefunden!"
                )
    else:
        if best_idx_in_kept is not None:
            new_active_index = best_idx_in_kept
            print(
                f"🔁 Kein aktiver Account gesetzt → setze auf Index {new_active_index}"
            )

    # 4. Save new config
    new_data = {
        "version": data.get("version", 1),
        "accounts": to_keep,
        "activeIndex": new_active_index,
    }
    save_config(new_data)
    print(f"✅ Hauptkonfiguration gespeichert: {len(to_keep)} Accounts verbleiben")

    # 5. Save quarantined accounts
    quarantine_data = {
        "version": data.get("version", 1),
        "accounts": [accounts[q["index"]] for q in to_quarantine],
        "quarantinedAt": datetime.now().isoformat(),
        "reason": "consecutiveFailures > 20",
        "count": len(to_quarantine),
    }
    with open(QUARANTINE_PATH, "w") as f:
        json.dump(quarantine_data, f, indent=2)
    print(f"✅ Quarantäne-Datei gespeichert: {QUARANTINE_PATH}")

    # 6. Summary
    print("\n" + "=" * 60)
    print("✅ QUARANTÄNE ABGESCHLOSSEN")
    print(f"🎯 Aktiver Account: Index {new_active_index}")
    print(f"📊 Verbleibende Accounts: {len(to_keep)}")
    print(f"🗑️  In Quarantäne verschoben: {len(to_quarantine)}")
    print(f"\n💾 Quarantäne-Datei: {QUARANTINE_PATH}")
    print(f"   (Kann bei Bedarf wiederhergestellt werden)")

    # 7. List top quarantined
    print(f"\n📋 Top 5 quarantinierte Accounts:")
    for q in sorted(to_quarantine, key=lambda x: x["consecutive"], reverse=True)[:5]:
        print(
            f"   Index {q['index']}: {q['consecutive']} cons.fails, {q['success']}/{q['failure']}"
        )


if __name__ == "__main__":
    main()
