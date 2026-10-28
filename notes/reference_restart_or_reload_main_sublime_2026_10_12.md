---
name: restart-or-reload-main-sublime-2026-10-12
description: THE procedure for reloading or restarting his main Sublime without losing the Claude session: detach all sessions to Windows Terminal (I can run it), do the thing, reattach; supersedes older notes that said only he can move the session
metadata:
  type: reference
---

**Verified 2026-10-12** (renaming a folder that his main Sublime had open; and he says a plugin reload does not drop the session connection anyway):
1. `run_command` `ai_terminal_detach_all_to_windows_terminal` with `scope: "app"` (an ApplicationCommand; I CAN run it) moves every GhostShell session to Windows Terminal.
2. Do the thing: `exit` tool on the main Sublime and relaunch, or reload the plugin.
3. Run `ai_terminal_reattach_all_from_windows_terminal` (scope app) to bring the sessions back.
4. The sublime-mcp tools of the main Sublime usually reconnect by themselves (they did on the 2026-10-12 restart, no `/mcp reconnect` needed); if a call fails, he types `/mcp reconnect sublime-mcp`. Order that worked: detach_all, `exit` tool, Start-Process `C:\Program Files\Sublime Text\sublime_text.exe`, wait for port 9502, reattach_all, then a test call; both tabs (cmd.exe and Claude) came back and the session survived.

**Superseded:** [[native-dialog-tests-from-windows-terminal-2026-10-09]] said I cannot and must not move the session (only he, via the GhostShell toolbar); that was about the toolbar button, the command above exists and works. [[feedback_st_restart_vs_tab_close_risk]]'s 2026-09-15 doubt (Claude CLI exits when its tab is detached) did not show up here.

**Why:** he asked "where is that in your notes? You keep forgetting what the truth is." The facts were in three notes that disagreed. **How to apply:** read this note before any restart or reload of the main Sublime; do not ask him to click the toolbar.
