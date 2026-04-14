#!/usr/bin/env python3
"""
QWEN ACCOUNT QUARANTINE SCRIPT
Verschiebt/kennzeichnet Accounts mit hohen consecutiveFailures in Quarantäne
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
    print(f"\n🧹 QWEN ACCOUNT QUARANTINE TOOL")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"=" * 60)

    data = load_config()
    accounts = data.get("accounts", [])
    current_active = data.get("activeIndex")

    # Identify quarantine candidates: consecutiveFailures > 20
    to_quarantine = []
    to_keep = []

    for idx, acc in enumerate(accounts):
        health = acc.get("health", {})
        cons = health.get("consecutiveFailures", 0)
        success = health.get("successCount", 0)
        failure = health.get("failureCount", 0)

        if cons > 20:
            to_quarantine.append(
                {
                    "index": idx,
                    "consecutive": cons,
                    "success": success,
                    "failure": failure,
                    "refreshToken": acc.get("refreshToken", "")[:20] + "...",
                }
            )
        else:
            to_keep.append(acc)

    print(f"🔍 Gefundene kritische Accounts: {len(to_quarantine)}")
    print(f"✅ Verbleibende gesunde Accounts: {len(to_keep)}")
    print(f"📊 Aktueller activeIndex: {current_active}")

    if to_quarantine:
        print(
            f"\n⚠️  KONTROLLE: Werden diese Accounts wirklich in Quarantäne verschoben?"
        )
        print(f"   (Sie werden aus der Hauptkonfiguration entfernt)")
        for q in sorted(to_quarantine, key=lambda x: x["consecutive"], reverse=True)[
            :10
        ]:
            print(
                f"   Index {q['index']}: {q['consecutive']} cons.fails, {q['success']}/{q['failure']}"
            )

        # Check if active account is among them
        if current_active is not None and any(
            q["index"] == current_active for q in to_quarantine
        ):
            print(
                f"\n❌ KRITISCH: Der aktive Account (Index {current_active}) ist in Quarantäne!"
            )
            print(
                f"   Bitte vor dem Verschieben einen neuen aktiven Account auswählen."
            )

        confirm = input(
            f"\n?? Drücke ENTER um diese {len(to_quarantine)} Accounts zu quarantänen, oder 'n' um abzubrechen: "
        )
        if confirm.lower() == "n":
            print("❌ Abgebrochen.")
            sys.exit(0)

    # Build new accounts list (only healthy)
    new_data = {
        "version": data.get("version", 1),
        "accounts": to_keep,
        "activeIndex": data.get("activeIndex"),
    }

    # Save new config
    save_config(new_data)
    print(f"\n✅ Hauptkonfiguration gespeichert: {len(to_keep)} Accounts verbleiben.")

    # Save quarantined accounts separately (for recovery)
    if to_quarantine:
        quarantine_data = {
            "version": data.get("version", 1),
            "accounts": [accounts[q["index"]] for q in to_quarantine],
            "quarantinedAt": datetime.now().isoformat(),
            "reason": "consecutiveFailures > 20",
        }
        with open(QUARANTINE_PATH, "w") as f:
            json.dump(quarantine_data, f, indent=2)
        print(
            f"✅ Quarantäne-Datei gespeichert: {QUARANTINE_PATH} ({len(to_quarantine)} Accounts)"
        )

    # Recompute best active index if needed
    if current_active is None or any(
        q["index"] == current_active for q in to_quarantine
    ):
        # Pick healthiest remaining account
        best_idx = None
        best_score = -1
        for idx, acc in enumerate(to_keep):
            health = acc.get("health", {})
            cons = health.get("consecutiveFailures", 0)
            success = health.get("successCount", 0)
            if cons == 0 and success > 0:
                score = success
                if score > best_score:
                    best_score = score
                    best_idx = idx

        if best_idx is not None:
            new_data["activeIndex"] = best_idx
            save_config(new_data)
            print(f"✅ Neuer aktiver Index gesetzt: {best_idx} (gesündester Account)")
        else:
            print("⚠️  Kein optimaler aktiver Account gefunden – bitte manuell prüfen.")

    print("\n" + "=" * 60)
    print("✅ QUARANTÄNE ABGESCHLOSSEN")
    print(f"🎯 Aktive Accounts: {len(to_keep)}")
    print(f"🗑️  In Quarantäne: {len(to_quarantine)}")
    print(f"📍 Quarantäne-Datei: {QUARANTINE_PATH}")


if __name__ == "__main__":
    main()
