---
name: session-baton-2026-10-20-csl-linter-test
description: START HERE (newest, audit): Marcool04's untested SublimeLinter-contrib-csl fix tested for real, it WORKS on master but v3.0.1 (what Package Control installs) still has the old dependencies.json; result posted on issue #1 on his word; why four of my tests failed; rig gaps seen; nothing left installed
metadata:
  type: project
---

**Date:** 2026-10-20 (evening). Session opened with a question about the Claude Code 2.1.306 release notes (two bug fixes: `claude -p` "Not logged in" in cloud sessions; API error replaced by "prompt is too long" plus a needless compaction in sessions with many MCP tools). I did not read the newest baton first that time; Donald did not object, but the rule stands.

## What happened
- Marcool04 (Mark Collins) owns `Marcool04/SublimeLinter-contrib-csl`. Donald's issue #1 ("Does not load after install: requests is installed without urllib3, idna, certifi, charset_normalizer") is closed. Mark said he no longer uses Sublime, then pushed a `dependencies.json` listing the five libraries and set the README to "untested". Donald read that as a request to test and report back.
- Package Control installs the **v3.0.1 tag** (picker says "install v3.0.1"). That tag's `dependencies.json` lists only `requests`. Mark's fix is on `master`, four commits past the tag (commit `247609c`). So users get no fix until he pushes a new tag.
- Master commit `247609c` **works**: after a restart of the main Sublime, an invalid CSL file gets W3C validator errors (2:78 unknown element, 2:94 missing `info`), red gutter mark, status bar `sublimelintercontribcsl (e:2)`. Same result with and without a `.python-version` of 3.8, so that file is not needed.
- Package Control says `The library "certifi" is not available for Python 3.14` and shows "One or more libraries could not be installed or updated" (dismiss with OK; it hid my tab). The linter worked anyway.
- Posted on his word ("Send") as a comment on issue #1: https://github.com/Marcool04/SublimeLinter-contrib-csl/issues/1#issuecomment-6308947520 (issue is closed, Mark may not be notified). Nothing else was posted, no fork, no PR.

## Why four tests failed (all my setup, not his code)
1. First test installed the v3.0.1 tag from Package Control: not the fix, and SublimeLinter was not installed.
2. SublimeLinter installed **fresh into a running Sublime** sets `persist.kill_switch = True` and clears its registry (its `plugin_loaded` install branch); disable/enable of SublimeLinter did not clear it. Only a restart did. A linter installed in that session never lints, with no message.
3. `eval_python` runs in the **Python 3.14.6 host**, same as SublimeLinter and the csl module. After reloads there are TWO copies of SublimeLinter's registry: `from SublimeLinter.lint import persist` was stale (empty); `linter.persist.linter_classes` is the live one (`persist.linter_classes is linter.persist.linter_classes` was False). I wrongly reported "no registered linters" and a `.python-version` theory from that. Read `linter.persist`, not `persist`.
4. A loose clone in `Packages` never loaded (`No module named 'SublimeLinter-contrib-csl.linter'`, also after disable/enable); a `.sublime-package` zip (what Package Control installs, built with `git archive`) loaded at once.

## Rules Donald restated today (hold to them)
- Verdict first and plain: working or not working. "Loads without a traceback" is not a pass; test what the package is for (here: lint a broken file and see marks).
- Do not ask him technical decisions ("what kind of a question is that?"): decide, and use his own procedure notes. I asked whether to restart; the answer was to follow `reference_restart_or_reload_main_sublime_2026_10_12.md` (detach_all, `exit`, Start-Process sublime_text.exe, port 9502, reattach_all). It worked: session came back as the same tab (view id 20 to 12).
- Say what I am doing when he has heard nothing for a while; he sat for minutes with my tab hidden.
- Report what I will do on pass and fail before testing (he asked; I said: report in one line, post nothing unless he says, remove what I installed).

## Rig gaps seen (candidates for sublime-mcp / skill notes, none filed)
- After a Package Control install the "Package Control Messages" tab opens in FRONT of the Claude tab; I closed it by name every time (`close_file name=...`). Check `get_sheets` right after any install.
- `satisfy_libraries` failure shows a native dialog that blocks the view of the session tab; `run_command settle_ms` returned it as `dialogs`, `dismiss_native_window action=ok` cleared it.
- `run_command sublime_linter_lint` and `sublime_linter_toggle_debug` returned ok and did nothing (silent no-op, as the guide warns); `sublime_linter_panel_toggle` with no args works, `get_output_panel name=SublimeLinter` reads it.
- `ui_type_text` right after `open_file` can land before the new tab is active (my space did not reach bad.csl, may have gone to my own tab). Confirm the active tab with `get_active_file` before typing.
- `revert_file` acts on the ACTIVE view only; `focus_sheet` first, check, then revert.

## State left
- Nothing installed: package, SublimeLinter and library `charset-normalizer` removed through the Remove Package list (console shows each "Removed"); one tab open (the Claude tab), no dialogs.
- My loose test folder went to the Recycle Bin (recycle.ps1, piece by piece). Scratch files (zips, `csl-clone`, `bad.csl`) are in the session scratchpad only.
- Main Sublime was restarted once; sublime-mcp reconnected by itself.

## Open
- Nothing owed to Mark. If he tags a new release, re-test the Package Control install (picker should say the new version) before telling anyone it is fixed.
- The audit baton named in `~/.claude/rules/procedures.md` is stale (it still points at the 2026-10-17 note); this note is newer for the audit repo. Not edited without his word.
