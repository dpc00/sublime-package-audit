"""Stop the rig the way it must always be stopped: read the dialogs first, then kill.

A rig killed with a dialog up takes the dialog's text with it — that is how the
"Error loading syntax file Packages/C Improved/C Improved.tmLanguage" message was lost on
2026-11-11, and why a dialog sat unread for 50 s before that. Every modal in the rig's process tree
is on screen for a reason, so this snapshots them with Win32 calls (no bridge, so it works while the
main thread is blocked), appends them to data/dialogs_seen.tsv, and only then ends the processes.

    python rig_stop.py            # record dialogs, then stop the rig
    python rig_stop.py --keep     # record dialogs and leave the rig running
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import watch_rig  # noqa: E402  (shares the Win32 window reader)

LOG = Path(__file__).resolve().parent / "data" / "dialogs_seen.tsv"


def snapshot_rig() -> list[dict]:
    pids = watch_rig.rig_pids()
    return watch_rig.snapshot(pids) if pids else []


def record(rows: list[dict]) -> None:
    if not rows:
        return
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(
                time.strftime("%Y-%m-%dT%H:%M:%S"), row["kind"], row["hwnd"], row["title"],
                "|".join(row["buttons"]),
                " / ".join(row["messages"]).replace("\t", " ").replace("\n", " / ")))


def answer(rows: list[dict]) -> None:
    """Answer each dialog through the bridge when it is up (Cancel, else OK), else leave it logged.

    Answering is deliberately second: the text is already on disk before any click, so a dialog that
    cannot be answered still leaves evidence.
    """
    import urllib.error
    import urllib.request

    for row in rows:
        if row["kind"] != "dialog":
            continue
        cancel = any(b.lower() == "cancel" for b in row["buttons"])
        body = json.dumps({"hwnd": row["hwnd"], "action": "cancel" if cancel else "ok"}).encode()
        request = urllib.request.Request("http://127.0.0.1:9510/dismiss_native_window", data=body,
                                         headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=8) as response:
                print("answered:", row["title"], "->", response.read().decode()[:90])
        except Exception:
            print("could not answer (bridge down), logged only:", row["title"])


def stop_rig() -> None:
    script = (
        "Get-Process | Where-Object { $_.Path -like '*st_portable*' } "
        "| ForEach-Object { taskkill /PID $_.Id /F 2>&1 | Out-Null }; Start-Sleep -Seconds 2; "
        "'rig procs: ' + ((Get-Process | Where-Object { $_.Path -like '*st_portable*' } "
        "| Measure-Object).Count)"
    )
    print(subprocess.run(["powershell", "-NoProfile", "-Command", script],
                         capture_output=True, text=True, timeout=60).stdout.strip())


def main() -> None:
    rows = snapshot_rig()
    print(f"{len(rows)} dialog/menu window(s) in the rig")
    record(rows)
    answer(rows)
    time.sleep(0.5)
    remaining = snapshot_rig()
    if remaining:
        record(remaining)
        print(f"still up after answering: {[r['title'] for r in remaining]}")
    if "--keep" in sys.argv:
        print("left running (--keep)")
        return
    stop_rig()


if __name__ == "__main__":
    main()
