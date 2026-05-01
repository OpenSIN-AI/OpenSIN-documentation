import importlib.util
import os
import pathlib
import unittest
from unittest.mock import AsyncMock, patch


MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / "heypiggy_vision_worker.py"
SPEC = importlib.util.spec_from_file_location("heypiggy_vision_worker", MODULE_PATH)
worker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(worker)


class DummyGate:
    def __init__(self):
        self.failed_selectors = []
        self.recorded = []

    def is_selector_failed(self, selector: str) -> bool:
        return False

    def add_failed_selector(self, selector: str):
        self.failed_selectors.append(selector)

    def record_step(self, verdict: str, img_hash: str):
        self.recorded.append((verdict, img_hash))


class HeyPiggyWorkerPreflightTests(unittest.IsolatedAsyncioTestCase):
    async def test_main_stops_before_browser_mutation_when_credentials_missing(self):
        execute_bridge = AsyncMock()
        check_bridge_alive = AsyncMock(return_value=True)
        run_vision_model = AsyncMock(
            side_effect=AssertionError("vision probe must not run when credentials are missing")
        )

        with patch.dict(
            os.environ,
            {"HEYPIGGY_EMAIL": "", "HEYPIGGY_PASSWORD": ""},
            clear=False,
        ), patch.object(worker, "wait_for_extension", AsyncMock(return_value=True)), patch.object(
            worker, "check_bridge_alive", check_bridge_alive
        ), patch.object(worker, "run_vision_model", run_vision_model), patch.object(
            worker, "execute_bridge", execute_bridge
        ):
            await worker.main()

        execute_bridge.assert_not_awaited()
        check_bridge_alive.assert_not_awaited()

    async def test_main_stops_before_browser_mutation_when_vision_auth_fails(self):
        execute_bridge = AsyncMock()

        with patch.dict(
            os.environ,
            {
                "HEYPIGGY_EMAIL": "ops@example.com",
                "HEYPIGGY_PASSWORD": "secret",
            },
            clear=False,
        ), patch.object(worker, "wait_for_extension", AsyncMock(return_value=True)), patch.object(
            worker, "check_bridge_alive", AsyncMock(return_value=True)
        ), patch.object(
            worker,
            "run_vision_model",
            AsyncMock(
                return_value={
                    "ok": False,
                    "auth_failure": True,
                    "error": "401 invalid authentication credentials",
                }
            ),
        ), patch.object(worker, "execute_bridge", execute_bridge):
            await worker.main()

        execute_bridge.assert_not_awaited()

    async def test_ask_vision_turns_auth_failure_into_stop(self):
        with patch.object(worker, "dom_prescan", AsyncMock(return_value="DOM")), patch.object(
            worker,
            "run_vision_model",
            AsyncMock(
                return_value={
                    "ok": False,
                    "auth_failure": True,
                    "error": "401 invalid authentication credentials",
                }
            ),
        ):
            decision = await worker.ask_vision("/tmp/probe.png", "action", "expected", 1)

        self.assertEqual(decision["verdict"], "STOP")
        self.assertEqual(decision["page_state"], "error")
        self.assertEqual(decision["next_action"], "none")


class HeyPiggyWorkerClickPipelineTests(unittest.IsolatedAsyncioTestCase):
    async def test_run_click_action_routes_click_ref_through_escalation_pipeline(self):
        gate = DummyGate()
        escalating_click = AsyncMock(return_value=True)

        with patch.object(worker, "escalating_click", escalating_click):
            clicked = await worker.run_click_action({"ref": "@e9"}, gate, "hash123", 7)

        self.assertTrue(clicked)
        escalating_click.assert_awaited_once_with(
            selector="",
            description="",
            x=None,
            y=None,
            step_num=7,
            ref="@e9",
        )
        self.assertEqual(gate.failed_selectors, [])
        self.assertEqual(gate.recorded, [])


if __name__ == "__main__":
    unittest.main()
