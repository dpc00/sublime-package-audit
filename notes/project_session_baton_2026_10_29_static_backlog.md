---
name: session-baton-2026-10-29-static-backlog
description: START HERE (newest, audit): 1,240 packages whose latest result is a static check only; live testing resumes in main-list row order, DrSync (row 1) done; hold is lifted; how the list was built
metadata:
  type: project
---

**State 2026-10-29 (evening)**
- Hold on GitHub is LIFTED (Donald: "We did PRs today, so of course it is lifted"); `tools\file_gate.ps1` works again (FILE or RECORD-ONLY by age, installs, archived). Filed today: szensk/subllualove#17 and #18 (Lua Love), eddorre/SublimeERB#39.
- The new-list work (packagecontrol.io/browse/new, 219 pages) is finished and recorded; see [[project_new_list_all_recorded_2026_10_29]].
- BACKLOG found by reading RESULTS.tsv, not by a list: 1,240 packages whose LAST row is "static check only" (parse of repo files, not installed or run; the 2026-10-27 pass under the hold). They carry "Main list row N" in the note. Live testing goes in row order, starting at row 1. Done: row 1 DrSync (not in the picker, installed through Add Repository; bundled urllib3 breaks on Python 3.14, record-only by the gate).
- How to list what is left: take the last row per name (strip a trailing version suffix, lower case) and keep those whose note contains "static check only"; sort by the row number in "Main list row N". Skip names that already have a later live row. Install counts are not in the audit lists for most of these, so row order is the order.
- Method for a package missing from the picker: ledger ADD REPOSITORY line, `add_repository` plus URL and newline, `install_package` and narrow with `get_quick_panel` text, pick; at the end restore `Package Control.sublime-settings` from the baseline copy (hash FBBFAC8A) after closing the portable.
- Tool trap: `get_quick_panel` with a short `text` such as "Dr" dumps 40 items; use the full package name.

**Next:** row 4 "0x0", then 5 "42 Function Count Lines", "ABC Notation", ...
