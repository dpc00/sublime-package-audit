---
name: close-pcm-and-test-tabs-properly-2026-10-26
description: Donald's orders on tabs in the portable: always close Package Control Messages (PCM) tabs, leave none of my test tabs open, close only with close_file by index or name, closing a tab must never kill Sublime
metadata:
  type: feedback
---

Donald, 2026-10-26, said these details are "very important" (multe importante):

- "Always get rid of pcm tabs!" and later "Always read it. But dont leave it": a Package Control Messages tab can open after an install (it held the README text of many linter packages). READ it first (`get_open_files` shows it by name; then `get_sheet_content(index=N)`), say in the finding what it asks of the user, THEN close it with `close_file(name="Package Control Messages")`. On 2026-10-26 I closed TamarinProver's without reading it (it was only release notes).
- "Dont keep one open!" Leave none of my own test tabs open in the portable after a test. Sublime puts its own empty untitled tab back when the last one closes; that one cannot be removed and `get_sheets(settings=false)` then reports an empty list.
- "Closing a tab doesnt kill st unless you did it wrong." Close with `close_file(index=N)` or `close_file(name=...)` (the documented way), never `run_command close`. I used `run_command close` on 2026-10-26 and the portable exited after the last tab (no crash event, not reproduced afterwards; logged in the sublime-mcp bug log).
- Before answering Save Changes with No, look at the tab: only my own test text. "alpha beta" and "x" were closed unchecked; they turned out to be leftovers.
- Do not read a PCM tab with `get_active_file` (it returned about 1000 lines). Use `get_sheets(settings=false)` for names and `get_sheet_content` only when needed.

**Why:** leftover tabs and PCM tabs pile up and cover the work; a wrong close exits the test Sublime and costs a relaunch and a reconnect.
**How to apply:** after every package test: `get_sheets(settings=false)`, close PCM and my own tabs by index or name, then `list_native_windows` to confirm no dialog and no exit.

Related: [[feedback-end-test-agent-tabs]], [[feedback-clean-up-after-each-test-2026-10-11]].
