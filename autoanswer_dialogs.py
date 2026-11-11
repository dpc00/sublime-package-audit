"""Answer native dialogs as they appear, while a package test runs, and record what they said.

Why this exists
---------------
A modal dialog freezes Sublime's main thread, so a test step that raised one hung until a person
noticed. Detection alone did not help: the dialog was seen at 0.15 s and still sat there for 50 s
while the step waited for something that was never going to happen (2026-11-11). This is the missing
half: a thread that polls the process's own windows and answers the dialog immediately.

Policy
------
Cancel when the dialog offers one (it keeps the state the test can still inspect), otherwise OK.
Everything it answers is appended to data/dialogs_autoanswered.tsv, so the dialog is not silently
swallowed: its title, every message line, its buttons and which button was pressed become evidence.
That is how a package's own complaint reaches the ledger.

Donald, 2026-11-11, after the 50 s stall: a dialog must not stall testing. Clicking one is the test
harness's job, never sublime-commander's.

Usage
-----
    from autoanswer_dialogs import AutoAnswer
    with AutoAnswer() as answers:          # starts the thread, stops it at the end
        ...step that may raise a dialog...
    print(answers.answered)                # [{at, title, messages, buttons, chosen}, ...]
"""

from __future__ import annotations

import json
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

PORT = 9510
LOG = Path(__file__).resolve().parent / "data" / "dialogs_autoanswered.tsv"
LOG_HEADER = "when\ttitle\tbuttons\tchosen\tmessages\n"


def _post(tool: str, payload: dict | None = None, timeout: float = 10.0) -> dict:
    request = urllib.request.Request(
        f"http://127.0.0.1:{PORT}/{tool}",
        data=json.dumps(payload or {}).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as error:
        try:
            return json.loads(error.read().decode())
        except Exception:
            return {"error": f"HTTP {error.code}"}
    except Exception as error:  # noqa: BLE001 - a monitor thread must never raise
        return {"error": repr(error)[:160]}


class AutoAnswer:
    """Answer dialogs of the rig on `port` until the context manager exits."""

    def __init__(self, port: int = PORT, interval: float = 0.1):
        global PORT
        PORT = port
        self.interval = interval
        self.answered: list[dict] = []
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self._seen: set[int] = set()

    # -- thread -----------------------------------------------------------------
    def _run(self) -> None:
        while not self._stop.is_set():
            windows = _post("/list_native_windows").get("windows", [])
            for window in windows:
                if window.get("kind") != "dialog":
                    continue
                hwnd = window.get("hwnd")
                if hwnd in self._seen:
                    continue
                buttons = [b.get("text", "") for b in window.get("buttons", [])]
                chosen = "Cancel" if any(b.lower() == "cancel" for b in buttons) else "OK"
                action = {"action": "cancel"} if chosen == "Cancel" else {"action": "ok"}
                result = _post("/dismiss_native_window", dict(hwnd=hwnd, **action))
                if result.get("ok"):
                    self._seen.add(hwnd)
                    record = {
                        "at": round(time.time(), 3),
                        "title": window.get("title"),
                        "messages": window.get("messages") or [],
                        "buttons": buttons,
                        "chosen": chosen,
                    }
                    self.answered.append(record)
                    self._log(record)
            self._stop.wait(self.interval)

    def _log(self, record: dict) -> None:
        try:
            LOG.parent.mkdir(parents=True, exist_ok=True)
            new = not LOG.exists()
            with LOG.open("a", encoding="utf-8") as handle:
                if new:
                    handle.write(LOG_HEADER)
                handle.write("{}\t{}\t{}\t{}\t{}\n".format(
                    time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(record["at"])),
                    record["title"], "|".join(record["buttons"]), record["chosen"],
                    " / ".join(record["messages"]).replace("\t", " ").replace("\n", " / ")))
        except Exception:  # noqa: BLE001
            pass

    # -- lifecycle --------------------------------------------------------------
    def __enter__(self) -> "AutoAnswer":
        self._thread = threading.Thread(target=self._run, daemon=True, name="autoanswer-dialogs")
        self._thread.start()
        return self

    def __exit__(self, *_exc) -> None:
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=2)


if __name__ == "__main__":
    import sys

    seconds = float(sys.argv[1]) if len(sys.argv) > 1 else 10
    with AutoAnswer() as monitor:
        deadline = time.time() + seconds
        while time.time() < deadline:
            time.sleep(0.2)
    for item in monitor.answered:
        print(json.dumps(item, ensure_ascii=False))
    print(f"{len(monitor.answered)} dialog(s) answered; recorded in {LOG}")
