---
name: session-baton-2026-10-28-flags-done
description: START HERE (newest, audit): all 8 static flags live-checked on portable 4215 (Piranha/PLI10 real, 6 false positives), 2 emails to Kostasn2, prerequisite revisit mostly done, nothing queued
metadata:
  type: project
---

**Done 2026-10-28**
- Revisited prerequisite-skipped packages after Donald's "installs OK if undoable, no account/ban risk" (see [[feedback_installs_ok_if_reversible_2026_10_28]]): Ruby Markers, Rubyfmt, PerlTidy, perldoc, Pmccabe, PyCover, PyRefactor, Python Unittest Helper, PipenvPath tested in the WSL Sublime (rows in RESULTS.tsv, all removed and verified).
- Live check of the 8 flags in data\auto_static_flags.txt on the portable 4215: Piranha and PLI10 (Kostasn2) are REAL: three `#` lines before `%YAML 1.2` make Sublime refuse the syntax ("%YAML indicator is required in"). Focus, Enhanced HTML and CFML, Squirrel, MayaSublime, Jester, Mediawiker (ex.py never imported; plugin needs .python-version, oauthlib missing for 3.14) are false positives or age. Rows are in RESULTS.tsv; ledger lines for every add and removal; portable back to baseline (Color Scheme - Legacy, Package Control, SublimeLinter).
- Emails sent to gentouros@gmail.com (Kostasn2): first one named the WRONG cause (undefined contexts strings/comments, which exist but are not why it fails), then a correction (ids 1a1817ff7874951b, 1a18184a70d45ff1). Lesson: wait for Sublime's own error text before emailing; the RESULTS row 6146 was corrected in place.
- Released sublime-mcp 1.17.1 and 1.17.2 earlier the same day (close_file, save_file, disk_differs, off-Windows dialog help).

**Later the same day (supersedes "Nothing queued" below)**
- Donald: "you give up too easily and skip things"; WSL is disposable. I redid ~10 WSL-dependent rows and the Perforce family (Perforce, P4Gutter, Waza, P4Explorer, DiffP4Merge with real p4d/P4Merge), Nim, MiniZinc, rtags, pgcli, arduino, notmuch, thunar/nautilus rows; apt tools stay installed in WSL (he said no cleanup), everything else removed and verified; ledger complete. ScalafmtEnhanced recorded as not fully tested (needs coursier-built scalafmt_ng plus a nailgun client; obsolete, RECORD-ONLY).
- CORRECTION (2026-10-28, Donald): the list "RSL, C++YouCompleteMe, LSP-tagml, DreamMaker Language Client, NestingSnippet" is DONE: retry rows dated 2026-10-28 in .tested_packages.tsv (lines ~5872-5876). I listed them from this stale baton at the start of the next session; check the tested list before naming what is left. Phabricator, PlasticSCM, NetSuite SDF were tested 2026-10-25 (prerequisite not installed) and have no retry; low priority, need accounts/servers.
- sublime-mcp: 1.17.3 released (eval_python consent prompt shows all the code); portable st_portable now runs the 1.17.3-era plugin with consent ON (old copy in the session scratchpad). Package Control: MCP Commander is withdrawn from the channel (his decision, "premature, not safe"); he is not resubmitting; npm/PyPI only hand out the proxy.
- Rule of this audit stays: WSL Sublime server `sublime-mcp-wsl-4200` (reconnect by typing `/mcp reconnect sublime-mcp-wsl-4200` into my own tab and Return).

**Left**
- Remaining prerequisite rows (see the list above) need accounts/servers/tools; PhpSimpleRefactor is already reported by others.
- Hold on GitHub action stays; email only per the 10-27 redesign.
- Tool traps seen: `get_syntaxes` ignores its query and dumps ~200 entries; `close_file` takes `index`/`name`/`discard` at top level in the portable batch (an `args` wrapper is dropped with a warning); `dismiss_native_window` on stacked dialogs needs repeating (first click only enables the one behind).


## Update, later 2026-10-28 (last untested channel packages)
- Done and removed on portable 4215: ReadableResume Snippets, BlackboardForever Color Scheme, Icons - FileIcons (inert alone), Deep JSON Color Schemes, AMX Mod X Pawn, 3D Tool, Meteor Autocomplete (SyntaxWarning only, record-only). Rows in RESULTS.tsv, ledger lines written and verified. Portable is back at baseline (Color Scheme - Legacy, Package Control, SublimeLinter).
- Lesson: for Remove Package and Install Package pickers use run_command remove_package / install_package, then get_quick_panel (text, wait_ms) and pick_quick_panel (index or text). Posted Return keys and computer-use Return went into the editor buffer (stray untitled tab); advanced_install_package is a text input, not the picker.
- No retry yet: Phabricator (arc and server), PlasticSCM, NetSuite SDF, macOS-only or paid rows. Next main audit row 1739 (per the 10-27 baton). Nothing queued for GitHub; hold stays.
