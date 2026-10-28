---
name: not-in-picker-queue-2026-10-26
description: Donald's order to retest every package the picker hides (714 of the channel), the queue file, how each is done, and the ST2-only filing question after FichteFoll closed IndentGuides#6
metadata:
  type: project
---

2026-10-26 Donald: "714 then. Get your shit together and stop skipping things!" The channel lists 5,437 packages, the ST4 picker offers 4,723; 714 are hidden (436 ST2-only, 128 without a Windows platform, the rest unexplained). I had recorded about 157 as "skipped: not in the picker" without his authorization.

Queue: `data\retest_queue_2026_10_26.tsv` (479 rows: number, name, why hidden, state, repo link). Rows marked "already tested (suffix-name row)" (87) have a real earlier test under "Name 123" style names; do not redo those. Work in order; the first 10 rows are done (see the baton and RESULTS.tsv).

Method per package (worked 2026-10-26): ledger ADD REPOSITORY line; `add_repository` + `ui_type_text` the GitHub URL + newline; `install_package`, `get_quick_panel` (narrow text, the added repo shows under the repository name, e.g. sublime-gbk), pick; read console and files from the zip; run the real command; remove through the picker (index shown, was 2 or 3 or 0); delete the repository line from `Data\Packages\User\Package Control.sublime-settings`; finish.ps1; commit_day.ps1. Package Control Messages tab: read it, then close it by name.

Exceptions seen: the repository is gone (curl.exe 404 on repo page and codeload; record as gone, nothing to install); the channel's ST2-only entry shadows the added repository ("not available on this platform or for this version"): clone into the scratchpad, copy to `Data\Packages\<name>`, test, recycle both with recycle.ps1 `-Path a,b`.

Install name caveat: Add Repository names the package after the repo, so code that hardcodes the package folder (`Packages/Tau Time Tracker/`, theme paths) can fail only because of the different name. Say so in the finding.

OPEN QUESTION for Donald (not decided by me): FichteFoll closed SublimeText/IndentGuides#6 (Python 2 only code, found by me 2026-10-19) as "not planned: the package only advertises support for ST2, not a bug". For ST2-only channel entries a Python 2 failure is expected. I filed anyway on Task Timer #6, Taskwarrior #11, Tau Time Tracker #2, PhpTidy #38, TidyHTML #14 today; those may be closed the same way. Until he says otherwise: test every one, record the result, and file only defects that are not simply "Python 2 code on ST2-only package".

PROGRESS 2026-10-27 (newest, supersedes the restart state below): rows 1-400 done (rows 239-400 this session; also Hide Files dunckr/hidefiles#1, Flashback apiad/sublime-flashback#4; issues filed: sublime-goto-node-module#2, SublimeFileCleanup#1, sublime-plugin-Image2tag#2, CopyNamespace#5, MTML-ST2#3, ErlDoc#1, xtoy#3; ice/sleet#1 retest of mruz fix 8a2468e posted). NEXT: queue FINISHED (rows 1-479 all recorded 2026-10-27, nothing filed after the hold). Old line: row 401 in data\retest_queue_2026_10_26.tsv. Portable 4215 clean (no repositories, only Color Scheme - Legacy, Package Control, SublimeLinter; User Preferences restored after NightCycle). Method now: `run_command add_repository` + `ui_type_text` URL+newline, `install_package` with the REPO name, `remove_package` run_command then get_quick_panel text + pick, `add_folder`/`remove_folder` for project fixtures, fixtures in the session scratchpad, `dismiss_native_window` for Save Changes (No) on my own scratch tabs. NetLinx: Studio installer needs admin, step 3 blocked, folder recycled. Token line (http_basic_auth) in the portable's Package Control settings must be removed when the queue is done.

RESTART STATE (older, Donald restarting Claude for an update): queue rows 1-10, 16, 17, 21, 22, 25, 28, 29, 31, 33 done; rows 11-15, 18-20, 23, 24, 26, 27, 30, 32 were already tested. NEXT: row 34 nodejsLauncher (diestrin/nodejsLauncher), then 35 MarkdownBuild, continue down data\retest_queue_2026_10_26.tsv. Main list resumes at row 1739 (Tcsh and Csh Mode). Portable 4215 (tools\st_portable) is clean: no repositories, only Color Scheme - Legacy, Package Control, SublimeLinter installed, no tabs, no dialogs. After restart: /mcp reconnect sublime-mcp-portable-4215 if needed.

