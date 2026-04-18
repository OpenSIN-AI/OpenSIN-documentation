#!/usr/bin/env python3
"""
QWEN ACCOUNT MONITORING & AUTO-ROTATION
Überwacht Account-Health und rotiert automatisch bei Problemen
"""

import json
import sys
import os
import time
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# Configuration
CONFIG_PATH = "/Users/jeremy/.config/opencode/qwen-auth-accounts.json"
STATE_PATH = "/Users/jeremy/.config/opencode/qwen-monitor-state.json"
LOG_PATH = "/Users/jeremy/.config/opencode/qwen-monitor.log"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_PATH), logging.StreamHandler()],
)


class QwenMonitor:
    def __init__(self):
        self.config = None
        self.state = self.load_state()

    def load_state(self) -> Dict:
        if os.path.exists(STATE_PATH):
            with open(STATE_PATH) as f:
                return json.load(f)
        return {"lastCheck": None, "rotations": [], "alerts": []}

    def save_state(self):
        with open(STATE_PATH, "w") as f:
            json.dump(self.state, f, indent=2)

    def load_config(self):
        with open(CONFIG_PATH) as f:
            self.config = json.load(f)

    def analyze_health(self) -> Dict:
        """Analysiert den Health-Status aller Accounts"""
        accounts = self.config.get("accounts", [])
        health_summary = {
            "total": len(accounts),
            "activeIndex": self.config.get("activeIndex"),
            "healthy": 0,
            "warning": 0,
            "critical": 0,
            "dead": 0,
            "by_cons": {},
        }

        for idx, acc in enumerate(accounts):
            health = acc.get("health", {})
            cons = health.get("consecutiveFailures", 0)
            success = health.get("successCount", 0)
            failure = health.get("failureCount", 0)

            # Kategorisierung
            if cons == 0 and success > 0:
                health_summary["healthy"] += 1
            elif cons > 20:
                health_summary["critical"] += 1
            elif cons > 0:
                health_summary["warning"] += 1
            elif success == 0 and failure > 0:
                health_summary["dead"] += 1
            else:
                health_summary["healthy"] += 1  # neutral

            health_summary["by_cons"][str(idx)] = cons

        return health_summary

    def find_best_healthy_account(self) -> Optional[int]:
        """Findet den gesündesten Account (consecutiveFailures == 0, max successes)"""
        accounts = self.config.get("accounts", [])
        candidates = []

        for idx, acc in enumerate(accounts):
            health = acc.get("health", {})
            cons = health.get("consecutiveFailures", 999)
            success = health.get("successCount", 0)

            if cons == 0 and success > 0:
                candidates.append(
                    {
                        "index": idx,
                        "success": success,
                        "failure": health.get("failureCount", 0),
                    }
                )

        if not candidates:
            return None

        # Sortiere nach successCount (descending)
        candidates.sort(key=lambda x: x["success"], reverse=True)
        return candidates[0]["index"]

    def should_rotate(self, health_summary: Dict) -> bool:
        """Entscheidet ob Rotation nötig ist"""
        active_idx = health_summary["activeIndex"]
        if active_idx is None:
            return True

        accounts = self.config.get("accounts", [])
        if active_idx >= len(accounts):
            return True

        active_health = accounts[active_idx].get("health", {})
        cons = active_health.get("consecutiveFailures", 0)

        # Rotiere wenn:
        # - active account hat > 10 consecutive failures
        # - oder active account ist in quarantine (wurde entfernt)
        if cons > 10:
            return True

        return False

    def rotate_account(self) -> bool:
        """Führt Account-Rotation durch"""
        old_active = self.config.get("activeIndex")
        new_active = self.find_best_healthy_account()

        if new_active is None:
            logging.error("❌ KEIN GESUNDER ACCOUNT VERFÜGBAR!")
            return False

        if old_active == new_active:
            logging.info(f"✅ Aktiver Account (Index {old_active}) ist bereits optimal")
            return False  # Keine Rotation nötig

        logging.warning(f"🔄 ROTATION: Index {old_active} → {new_active}")

        # Atomic update
        self.config["activeIndex"] = new_active
        with open(CONFIG_PATH + ".tmp", "w") as f:
            json.dump(self.config, f, indent=2)
        os.replace(CONFIG_PATH + ".tmp", CONFIG_PATH)

        # Record rotation
        self.state["rotations"].append(
            {
                "timestamp": datetime.now().isoformat(),
                "oldIndex": old_active,
                "newIndex": new_active,
            }
        )
        self.save_state()

        logging.info(f"✅ Rotation abgeschlossen")
        return True

    def run_check(self):
        """Führt einen Monitor-Check durch"""
        logging.info("=" * 60)
        logging.info("🔍 QWEN ACCOUNT MONITOR CHECK")
        logging.info("=" * 60)

        self.load_config()
        health = self.analyze_health()

        logging.info(f"📊 GesamtAccounts: {health['total']}")
        logging.info(f"✅ Healthy: {health['healthy']}")
        logging.info(f"⚠️  Warning: {health['warning']}")
        logging.info(f"❌ Critical: {health['critical']}")
        logging.info(f"💀 Dead: {health['dead']}")
        logging.info(f"🎯 Aktiver Account: Index {health['activeIndex']}")

        # Prüfe Rotationsbedarf
        if self.should_rotate(health):
            logging.warning("⚠️  ROTATION ERFORDERLICH")
            rotated = self.rotate_account()
            if rotated:
                logging.info("🔄 Account erfolgreich rotiert")
            else:
                logging.error("❌ Rotation fehlgeschlagen")
        else:
            logging.info("✅ Keine Rotation nötig – aktiver Account ist gesund")

        self.state["lastCheck"] = datetime.now().isoformat()
        self.save_state()
        logging.info("✅ Check abgeschlossen\n")


def main():
    monitor = QwenMonitor()
    try:
        monitor.run_check()
    except Exception as e:
        logging.error(f"❌ Monitor fehlgeschlagen: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
