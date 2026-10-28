---
name: refocus-test-window-myself-2026-10-28
description: Donald reads the main Sublime while I test, so focus keeps leaving the test window; I must re-front it myself and retry, never fail a test over it
metadata:
  type: feedback
---

Donald (2026-10-28): "I have to read the main ST to keep up. Thus you have to reset focus where you need it to be. Don't give up and fail a test simply because the annoying user is constantly interfering."

**Why:** during the Remove Package step on portable 4215 posted Return keys went into the editor (stray untitled tab) because the window had lost focus; I switched route instead of fronting and retrying.

**How to apply:** skill sublime-mcp-audit rule 6g: front.ps1 before every step that needs the window, check it printed True, retry the same step 3 times after re-fronting, prefer focus-free routes (run_command install_package/remove_package, get_quick_panel, pick_quick_panel), check get_open_files for stray tabs after posted keys. Related: [[feedback_keyboard_activity_is_permission_prompts]].

**Added same day:** never leave a non-main window always-on-top (obnoxious, thwarts him). tools\front.ps1 now clears the topmost flag on every call and has -Back <main hwnd> to hand the foreground back after a burst (tested: portable and main both topmost=False).
