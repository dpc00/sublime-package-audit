"""Watch the rig's own windows with Win32 calls only, so a startup dialog is recorded too.

A dialog that appears before sublime-commander's servers bind cannot be seen through the bridge, and
a rig killed with a dialog up takes the text with it — both happened on 2026-11-11. This uses
EnumWindows on the st_portable process tree, needs nothing inside the editor, and logs every dialog
and menu it sees (title, buttons, message text) to data/dialogs_seen.tsv. It never clicks.

    python watch_rig.py 30          # watch for 30 s
    python watch_rig.py 0           # until Ctrl+C
"""

from __future__ import annotations

import ctypes
import json
import os
import sys
import time
from ctypes import wintypes
from pathlib import Path

PORTABLE = r"c:\users\donal\tools\st_portable"
LOG = Path(__file__).resolve().parent / "data" / "dialogs_seen.tsv"

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
user32.GetWindowTextLengthW.argtypes = [wintypes.HWND]
user32.GetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
user32.GetClassNameW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
user32.GetWindowThreadProcessId.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
user32.IsWindowVisible.argtypes = [wintypes.HWND]
user32.EnumChildWindows.argtypes = [wintypes.HWND, ctypes.c_void_p, wintypes.LPARAM]
kernel32.OpenProcess.restype = wintypes.HANDLE
kernel32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
kernel32.QueryFullProcessImageNameW.argtypes = [
    wintypes.HANDLE, wintypes.DWORD, wintypes.LPWSTR, ctypes.POINTER(wintypes.DWORD)]
kernel32.CloseHandle.argtypes = [wintypes.HANDLE]

ENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)


def rig_pids() -> set[int]:
    """Process ids whose executable lives under the portable folder."""
    pids = set()
    for entry in os.listdir("/proc") if os.path.isdir("/proc") else []:
        pass
    # Windows: enumerate via a toolhelp-free route — check every sublime/plugin host by name.
    import subprocess

    try:
        out = subprocess.run(
            ["powershell", "-NoProfile", "-Command",
             "Get-CimInstance Win32_Process | Where-Object { $_.ExecutablePath -like '*st_portable*' } "
             "| ForEach-Object { $_.ProcessId }"],
            capture_output=True, text=True, timeout=20).stdout
        for line in out.split():
            if line.strip().isdigit():
                pids.add(int(line))
    except Exception:
        pass
    return pids


def window_pid(hwnd: int) -> int:
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    return pid.value


def text_of(hwnd: int) -> str:
    length = user32.GetWindowTextLengthW(hwnd)
    buffer = ctypes.create_unicode_buffer(length + 2)
    user32.GetWindowTextW(hwnd, buffer, length + 2)
    return buffer.value


def class_of(hwnd: int) -> str:
    buffer = ctypes.create_unicode_buffer(256)
    user32.GetClassNameW(hwnd, buffer, 256)
    return buffer.value


def child_texts(hwnd: int) -> list[str]:
    found: list[str] = []

    def collect(child, _):
        try:
            if class_of(child) in ("Static", "Edit"):
                value = text_of(child).strip()
                if value:
                    found.append(value)
        except Exception:
            pass
        return True

    callback = ENUMPROC(collect)
    user32.EnumChildWindows(hwnd, callback, 0)
    return found


def buttons(hwnd: int) -> list[str]:
    found: list[str] = []

    def collect(child, _):
        try:
            if class_of(child) == "Button":
                value = text_of(child).strip().replace("&", "")
                if value:
                    found.append(value)
        except Exception:
            pass
        return True

    callback = ENUMPROC(collect)
    user32.EnumChildWindows(hwnd, callback, 0)
    return found


def snapshot(pids: set[int]) -> list[dict]:
    rows: list[dict] = []

    def collect(hwnd, _):
        try:
            if not user32.IsWindowVisible(hwnd):
                return True
            if window_pid(hwnd) not in pids:
                return True
            cls = class_of(hwnd)
            kind = {"#32770": "dialog", "#32768": "menu"}.get(cls)
            if kind is None:
                return True
            rows.append({
                "hwnd": int(hwnd) if hwnd else hwnd,
                "kind": kind,
                "class": cls,
                "title": text_of(hwnd),
                "buttons": buttons(hwnd) if kind == "dialog" else [],
                "messages": child_texts(hwnd) if kind == "dialog" else [],
            })
        except Exception:
            pass
        return True

    callback = ENUMPROC(collect)
    user32.EnumWindows(callback, 0)
    return rows


def main() -> None:
    seconds = float(sys.argv[1]) if len(sys.argv) > 1 else 20
    LOG.parent.mkdir(parents=True, exist_ok=True)
    deadline = time.time() + seconds if seconds > 0 else None
    seen: dict[int, dict] = {}
    while deadline is None or time.time() < deadline:
        pids = rig_pids()
        if pids:
            for row in snapshot(pids):
                key = row["hwnd"]
                if key in seen:
                    continue
                seen[key] = row
                line = json.dumps(row, ensure_ascii=False)
                print(line, flush=True)
                with LOG.open("a", encoding="utf-8") as handle:
                    handle.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(
                        time.strftime("%Y-%m-%dT%H:%M:%S"), row["kind"], row["hwnd"], row["title"],
                        "|".join(row["buttons"]),
                        " / ".join(row["messages"]).replace("\t", " ").replace("\n", " / ")))
        time.sleep(0.15)


if __name__ == "__main__":
    main()
