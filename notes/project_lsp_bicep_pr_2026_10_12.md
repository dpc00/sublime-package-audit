---
name: lsp-bicep-pr-2026-10-12
description: 2026-10-12 sublimelsp/LSP-Bicep#17 maintainer (rwols) asked for a PR; Donald said "go ahead with whatever it wants"; PR #18 opened (dotnet check before download + LspPlugin migration), tested for real on 4215
metadata:
  type: project
---

rwols (LSP maintainer) answered my issue sublimelsp/LSP-Bicep#17 ("No dotnet: error is only [WinError 2], server downloaded first") with: make the changes, open a PR, and migrate AbstractPlugin to LspPlugin. Donald (who understands little of it): "you can; go ahead with whatever it wants." So the usual rule (post nothing on a PR request) was overridden by his word.

**Done:** fork dpc00/LSP-Bicep; clone `C:\Users\donal\projects\LSP-Bicep` (origin = fork, upstream = sublimelsp, branch lsp-plugin-and-dotnet-check, commit 4bbdc1b); PR https://github.com/sublimelsp/LSP-Bicep/pull/18. Code: plugin.py now `LspPlugin`, `on_pre_start_async` checks dotnet (`shutil.which` + `dotnet --list-runtimes`, min v10) BEFORE downloading, raises `PluginStartError`; README line. Tested: 8 logic cases with fake dotnet.cmd files; REAL end-to-end on portable 4215 (LSP 2.15.0 + Bicep syntax installed through the picker with my new ui_* tools): status bar "cannot start LSP-Bicep: dotnet not found. Install .NET 10 or set "dotnet_executable" in the LSP-Bicep settings.", Package Storage stayed empty (no download). The 4215 portable was restored: packages removed, folder recycled, settings identical to backups.

**Gotchas learned:** after a failed start LSP disables the config for the window for the session (`_disabled_for_session`), so a second try in the same Sublime does nothing; re-enable with `cm._disabled_for_session.discard(name); cm.update(name)` in eval_python. The picker needs ~1.5 s before Return or the list is empty. Their lint rules: 120-column lines, isort single-line, alphabetical (`sublime` before `subprocess`).

**Waiting for:** rwols's review of PR #18. Watch only when he asks. Keep `projects\LSP-Bicep` while the PR is open; remove when merged/closed.

**REVIEW 2026-10-12 22:03 UTC (rchl):** read dotnet_executable from OnPreStartContext.configuration.root_settings (supports project overrides). Done: commit bb9af88 pushed, import of sublime removed, logic test 8/8 again (not re-run inside Sublime), reply posted on PR #18 (comment 6133892873). Waiting for the next review. Same-day note: Theme-Treble#1 maintainer (53v3n3d4) replied twice, asking me to find why accent blue-vibrant from Mariana does not show on Windows while accent_color blue does; pointed at theme lines 4278-4291 (selected tab 'mi' style), 4419-4432 (accent), 3176-3192 (tabset margins) of Treble Adaptive.sublime-theme at commit 4477f813; not yet investigated.
