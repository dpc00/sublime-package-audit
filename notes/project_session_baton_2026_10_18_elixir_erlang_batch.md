---
name: session-baton-2026-10-18-elixir-erlang-batch
description: START HERE (newest): Elixir/Erlang packages tested in the WSL Sublime, six issues filed, WSL cleaned; what is left; how the WSL launch works now
metadata:
  type: project
---

2026-10-18 (Donald: "I wanted to learn erlang. go with the Elixir ones", then "file the issues, then clean up the WSL").

**Done:** SuperElixir, Erlyman, TestExUnit, ElixirFormatter tested for real in the WSL Sublime 4215 (OTP 27, Elixir 1.18.3 installed in WSL with `wsl -u root apt-get`, no sudo prompt). Rows are in RESULTS.tsv and data/.tested_packages.tsv. Issues filed and logged in ISSUES.tsv: sublimehq/package_control#1805 (root `__init__.py` is never extracted, so SuperElixir installs but does nothing), edelvalle/SuperElixir#16 (erlang.py SMALL_ATOM_UTF8_EXT, one-line fix) and #17 (linter vs SublimeLinter 4), archydragon/sublime-erlyman#11 (module list empty: OTP 27 man archive has only man1), Dania02525/TestExUnit#1 (spec_folder_name) and #2 (panel_settings None crash).

**Cleanup done:** WSL Sublime quit, `wsl --shutdown`, test packages, scratch project `audit_elixir_test` and `~/.mix` moved to `~/removed_packages/elixir-audit-2026-10-18` (WSL has no Recycle Bin), Package Control's installed list back to LSP, Package Control, SublimeLinter. **Then he said "don't keep anything you added for testing": the 129 apt packages my two installs added (Erlang, Elixir, erlang-doc and dependencies, found from /var/log/apt/history.log, dry run showed exactly those) were purged, the OTP 26 man pages, the `/usr/local/lib/erlang` symlink, the MANDATORY_MANPATH line in `/etc/manpath.config` and the moved-aside `~/removed_packages/elixir-audit-2026-10-18` folder were removed. Only the synced MCP Commander copy in the WSL Sublime config stays (it is the rig itself).** To redo Elixir tests, reinstall with `wsl -u root apt-get install erlang elixir`.

**Still open from the deferred list:** Debugger - Maya / 3ds Max, GDL (ARCHICAD), AccuTermClient (paid software, ask him); SublimeSimpleSync SSH rule (needs sshd in WSL); glslc, codeclimate, julialint, SummitLinter rows.

**What I learned (use again):**
- The WSL launch that works and drew the window (no COPY MODE): kill orphan `msrdc`, `wsl --shutdown`, then `Start-Process wsl -ArgumentList '-e','sh','<script>' -WindowStyle Hidden` where the script `exec`s `./sublime_text` in the FOREGROUND with `DISPLAY=:0 WAYLAND_DISPLAY=wayland-0 XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir GDK_BACKEND=x11 LIBGL_ALWAYS_SOFTWARE=1`. A backgrounded `setsid nohup` Sublime died when the wsl session ended. Sync MCP Commander (`sublime_mcp.py`, `AGENT_GUIDE.md`, `.python-version`, `lib/*.py`) from the repo first.
- Reconnect the MCP server myself: `run_command ai_terminal_send_string` with `/mcp reconnect sublime-mcp-wsl-4200\r` into the tab hosting this session; the reconnect happens at once; only its confirmation message waits until my turn ends (Donald's correction 2026-10-19; this line used to say it only runs when the turn ends). He can also type `/mcp`.
- Package Control's Install Package picker is in the other plugin host, so `get_quick_panel` cannot see it; use the `install_package` tool and say so.
- Editing a package file through `\\wsl.localhost` does not trigger a reload; `touch` it from inside WSL. Sublime reloads only the top-level plugin module, so submodules need `importlib.reload` through eval_python.
- Writes to scripts: `wsl -e sh -c '...'` mangles quotes from PowerShell; write a .sh file in the scratchpad and run it with `wsl -e sh /mnt/c/...`.
- No `time.sleep` in eval_python (blocks the main thread, call times out).
