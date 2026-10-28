---
name: audit-rows-383-400-lessons-2026-10-23
description: rows 383-400 of the fresh list done; issues filed, one findings file, and three rig lessons (stale Flowstate listener erases saved test files, close_file args, picker hides ST2-only packages)
metadata:
  type: project
---

2026-10-23, rows 383 to 400 of `data\audit_list_2026_10_21_fresh.tsv`, run on the portable 4215 in the original procedure (install via the palette picker, loose-copy test of each fix, issue, remove, finish.ps1, commit_day.ps1).

Filed: Foundation 6 Autocomplete (webchun#3), Foundation Snippets (Zurb-Foundation-Snippets#1), FramerCompletion (SublimeCompletionFramerjs#1), Front End Snippets (sublime-text-2-front-end#2), Front-end Project Snippets (sublime-front-end-snippets#13), FuzzyImports (fuzzy-imports#3), GAMS language (sublime-gams#16). Fuzzy Clock has no repo or tracker: written up in the audit repo `findings\FuzzyClock-wrong-hour-at-minute-33-and-hour-13.md` (Status: not filed). No finding: Fountainhead, FreeMarker, Freya, Frontend Light, FullScreenStatus, FullUndo, Future Funk Codeception, GAS-x86, GCC Assembly Listing. FoxCode skipped: not in the Install picker on 4215.

Lessons:
- The Flowstate package (tested earlier) stays loaded after removal. Its listener erases the text of any SAVED file after 5 s idle ("Your work will be erased!"). A file-based test (open a file from disk, edit, read back) loses its content: it looked like a FuzzyImports bug until the console line was read. Restart the portable before tests that open saved files, or test with unsaved tabs.
- `close_file` through `batch`: `name` belongs inside `args`. `{"tool":"close_file","name":"x"}` is a nameless call and closes the ACTIVE tab (it happened once, harmless because only that tab was open).
- A package missing from the picker is hidden by Package Control for build 4215 (ST2-only, FoxCode): log as skipped, do not search for another way.
- The first Tab after typing a snippet trigger often does nothing; a second Tab expands. Press Tab, read, press again before calling a snippet broken.
- Auto-indent staircases multi-line `insert` text in the test tab; not a package defect. It nearly produced a false report on GCC MAP File (row 401): `^`-anchored rules stopped matching on the indented lines, and my "fix" changed nothing when I re-ran the baseline with unindented text. Before filing a syntax finding, rerun the ORIGINAL with unindented text (set `auto_indent` false on the test view first).
- `set_file_type` with `Packages/MATLAB/Matlab.sublime-syntax` raised "Unable to stat" dialogs and left the scope `text.plain` while the status bar showed the syntax name. `syntax: "scope:source.matlab"` worked. Check `get_scope_at_cursor` before testing completions.
- When he says "Emails" or "another email": read each maintainer reply for what it asks (retest, question) and act on it, do not just summarise. 2026-10-23: commitment v1.0.9 retested (comment on #5), HeaderDoc#2 (Package Control serves the 0.1.0 tag, master has the fix), dbpedia#1; SublimeCloseOldestFile#1 asks for a PR, so nothing posted.
- Removing a syntax package while a tab still uses its syntax (even after closing the tab: the dotted empty tab) gives "Error loading syntax file ... Unable to stat" dialogs at the next palette use or syntax change, and the install palette ignores Return until the dialog is dismissed. Set the test tab to `scope:text.plain` before closing and removing. Not a package defect.
- GearboxSencha (row 418), left UNVERIFIED on purpose, not filed: its Windows keymap binds F5 to `restart_sublime`, which on win32 runs `os.execl(sys.executable, '')` (probably the plugin host, not sublime_text.exe), and `ctrl+shift+p` to `related_files` (Sublime's palette key; closed issue #1 was about ctrl+alt+p). Running F5 on the portable could kill the plugin host that carries the MCP link; posted chords (`ui_press_key` mods, method post) only type the letter, and `method input` is refused while he types. Needs a real-key test on his word.
- Loose copy of a package in `Data\Packages\<name>` is removed by Package Control's remove_package together with the zip; the recycle step is only needed when it still exists.
