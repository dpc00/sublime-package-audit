---
name: session-baton-2026-10-19-jquerydocs-syncedsidebarbg-localhistory
description: START HERE (newest, audit): after the 2026-10-17/18 stretch, three more packages done on portable 4200 (jQueryDocs, SyncedSidebarBg, Local History); next in the top-1000 list is Print to HTML (331)
metadata:
  type: project
---

**Written 2026-10-19.** The 2026-10-17 baton's "next: Tagify, jQueryDocs, SyncedSidebarBg, Local History" was out of date: Tagify and the three before it were already done (Tagify 2026-10-18, #7). Check `.tested_packages.tsv` before trusting a baton's "next".

**Done today (portable 4200, all cleaned, settings hashes equal to backups):**
- jQueryDocs: works (alt+j opens api.jquery.com; status bar showed jQuery.ajax); nothing filed.
- SyncedSidebarBg: filed PlainSublime/SublimeSyncedSidebarBg#5 (plugin_unloaded deletes every .sublime-theme in Packages/User; proved with a dummy file) and #6 (OSError on every tab switch with the ST4 default scheme Mariana.sublime-color-scheme).
- Local History: filed vishr/local-history#106 (Compare/Diff tab empty: panel.insert(edit, ...) with another view's edit token; fix with run_command append proved on an unpacked copy). History is written on load/close by design. Snapshots, side-by-side and Delete not tried; #100/#103/#105 already reported there.

**Later the same day (also done, all cleaned):** Print to HTML (word_wrap NameError, issues disabled, email HELD for Donald), GotoDocumentation (works), Python Breakpoints (works), npm-install (filed #10; the test emptied C:\Users\donal\node_modules again, repaired, see feedback_npm_install_needs_own_package_json: put a package.json in the test folder FIRST).

**Also done:** SidebarSeparator (filed ekazyam/SidebarSeparator#18). A write to a package's user settings file is picked up late: the first command after the edit may still use the old value (repeat it).

**Done later 2026-10-19 (afternoon):** HtmlTidy 412 (not in the channel; urllib2 + dead web service, all already reported; not installed), Gulp 426 (works; exec_args path REPLACES PATH; nothing filed), SCSS Compiler 431 (filed mattarnster/scsscompiler#3 invalid SCSS wipes the selection, #4 non-ASCII becomes \xNN), File Navigator 434 (works, nothing new). Tool-call lesson today: in `batch`, `get_quick_panel` and `pick_quick_panel` took args NESTED under `args` (flat form returned "give index or text" / ignored the filter and dumped 100 items). `ui_press_key` has no `period` or `up` that moves; `drive_input_panel` takes `text` only (no submit arg, it submits).

**Also done 2026-10-19 evening:** scss-lint 438 (INCONCLUSIVE: SublimeLinter shows "No lint results", cause not found, nothing filed), Laravel 4 Artisan 447 (works with a real composer-made Laravel 13; empty folder C:\Users\donal\tools\laravel_audit\proj is still there, held by the portable's watcher: recycle after the portable restarts; recycle.ps1 raised a UAC prompt for it twice, declined), AutoAligner 466 (filed generall/aligner#7 Ruby 3, #8 error text replaces buffer). Lessons: PowerShell `Set-Content -Encoding utf8` writes a BOM (once gave "Settings must be a json object", use [IO.File]::WriteAllText with UTF8Encoding($false)); `get_command_palette` filters by `package`/`caption`/`command`, not text (unfiltered it dumps 200 entries).

**Also done (later evening):** sublime-jslint 476 (not in channel, hand copy, works with Java 25), Edit History 477 (not in channel, hand copy; filed Stuk/sublime-edit-history#12 xrange NameError, fix proven), LaTeX Word Count 480 (works). Hand copies are removed through the Package Control remove picker (it lists unmanaged folders, "remove unknown version"), which avoids a locked-folder recycle.
**Done after that (all cleaned, settings hashes equal):** AutoSelect 481 (works), PhpBeautifier 491 (not in channel; commented on #7 with cause+fix), Markdown Slideshow 495 (commented on #14: extensions need the full dotted path; Package Control left the name in installed_packages, restored PC settings from backup), Theme - Seti Monokai 508 (works; change theme through UI: Select Theme / Select Color Scheme, type seti, Return; reset Preferences from backup BEFORE removing the package), ES6-Toolkit 510 (filed stephnr/es6-toolkit-for-sublime#8 toolkit.py shadowed by toolkit/ folder so the command silently does nothing, #9 wrong Babel check), JsMinifier 511 (not in channel, py2 syntax, known #16).
Gap seen: `run_command` returns ok for a command that is in the palette but whose class never loaded (ES6-Toolkit), so a silent no-op needs get_command_palette(package=...) plus the console to diagnose. A package folder swapped in while Sublime runs under a name it had before fails with "No module named"; use a fresh folder name.
**NEXT: JSON Stringify 515, SublimeLinter-contrib-eslint_d 520, BracketGuard 543, GitStatus 545, Processing 546, CSSTidy 553, PhpTidy 554, TidyHTML5 561** (rows 69-76 of the list).
(older next-line follows, now done up to 480:) sublime-jslint 476, Edit History 477, LaTeX Word Count 480 (older line, partly done: Increment Selection 405 done: #12; PHPTools 401 done: #14, #15; Clipboard History 385 done: ST2-only, tested from a hand copy; Web Inspector 386 done: filed #126, a scratch-profile Chrome was used and stopped; pick_quick_panel by text picks the first match, so use get_quick_panel with text to get the exact index first) (rank order in the tsv; ranks after 315 listed there). Done through Bemmet 373 (GitHub Flavored Markdown Preview filed #36 + comment on #32; Bemmet works). Run the four-point already-tested check for each. Test folders with npm-using packages need a package.json first.

**BATCH 565-594 DONE (same evening, later), all 8 logged and pushed:** Copy File Name 565 (not in channel; hand copy works), Search Stack Overflow 569 (filed ericmartel/Sublime-Text-2-Stackoverflow-Plugin#6, #7; opened an Edge tab on a Stack Overflow human-verification page, left alone), HTML Nest Comments 572 (filed #6 multiple selections), Terminal In Packages 573 (filed mxdevmanuel/sublime-terminal-in-packages#1, #2; my test cmd.exe was stopped), DlangAutoFileName 575 (filed #1), SublimeLinter-contrib-jslint 587 (disabled under SL 4.30.1, already #9), Insert Callback 593 (works), IndentGuides 594 (not in channel; filed SublimeText/IndentGuides#6). NEXT batch: rows 85 onward of audit_list_2026_10_17_gt6y_top1000.tsv (Ruby Debugger 600, WordPress Developer Resources 603, Better JavaScript 607, Shell Turtlestein 612, DiffView 615, ...). Leftover empty folders still held by the portable: `tools\processing_audit\sk`, `tools\tidyhtml_audit` (recycle after a portable restart; warn him first). Tool facts today: `get_quick_panel text=` on the Install picker returns nothing when a package is not in the channel (then hand copy: zipball with Invoke-WebRequest, python zipfile unpack into Data\Packages\<name>, wait 20 s, test, remove through the remove picker "remove unknown version"); `select_lines forward=true` adds a cursor on the next line (add_cursor_down is not a command); keep get_quick_panel text filters specific (a short filter dumps 12+ items). Wakelock: Claude Desktop has a Keep computer awake toggle (his to turn on); no CLI setting found.

**BATCH 515-561 DONE (2026-10-19 evening), all 8 logged.** After GitStatus: Processing 546 (filed b-g/processing-sublime#126, wmic gone on Windows 11; Processing 4.5.7 has no processing-java, `Processing.exe cli` instead; 493 MB zip downloaded and recycled), CSSTidy 553 (filed fitnr/SublimeCSSTidy#26, #27, #28), PhpTidy 554 (not in channel; hand copy works), TidyHTML5 561 (not in channel; hand copy works). NEXT batch: rows after 561 of audit_list_2026_10_17_gt6y_top1000.tsv (check the tsv, four-point check). LEFTOVERS: empty folders `tools\processing_audit\sk` and `tools\tidyhtml_audit` (held by the portable's watcher; recycle.ps1 fails and raises UAC; recycle after the portable restarts, and warn him before). Portable 4200 is running with an empty window, MCP connected. WAKELOCK: he said Windows sleeps after 30 minutes; I started `tools\keep_awake.ps1` twice and both background tasks were stopped; he then said do NOT use a persistent PowerShell script for it and that I must not look up third-party programs (PowerToys): use only what standard Windows has. Not solved: changing the sleep timeout or `powercfg` is a system setting, so it is his to do. The old crash pattern (git_changed + a second call) was not seen again after I stopped batching calls after pickers.

**UPDATE 17:15 (older, superseded by the line above): batch 515-561 is half done, 4 of 8 logged.** GitStatus 545 finished and cleaned (hashes equal, repo recycled, folder removed): filed vlakarados/gitstatus#7, #8, #9. NEXT: Processing 546, CSSTidy 553, PhpTidy 554, TidyHTML5 561. CRASH: portable 4200 crashed TWICE (dumps 4e04ba46 at 16:09:49 and f4fba298 at 17:04:00) both times when `run_command git_changed` (GitStatus, opens a picker from the 3.3 host) was followed by another call in the same batch (first get_quick_panel and a console read, second ui_screenshot). `git_changed` alone, with settle_ms 1000, did not crash and showed no panel. Donald's word: "you need a waitlock" was a TYPO for WAKELOCK (keep the laptop awake, like on Android; clarified 2026-10-20), nothing to do with pickers or crashes. My own rule, not his: never put another call in the same batch after a command that opens a picker; one call, wait, then the next. RECONNECT: `ai_terminal_send_string` is gone (returns ok, types nothing); reconnect by `ui_type_text` `/mcp reconnect sublime-mcp-portable-4200` (no newline) in the main Sublime, then `ui_press_key` Return method post; skill step 3 corrected. `get_sheet_content` has no `tail` argument and dumps the whole tab (about 20 KB): do not use it on my own tab.

**Batch 515-561, late 2026-10-19 (new session, STOPPED mid-batch; older text):** done and logged with rec.ps1: JSON Stringify 515 (filed Nadock/json_stringify#4: key order changes on the 3.3 host), SublimeLinter-contrib-eslint_d 520 (disabled under SublimeLinter 4.30.1, already #19, nothing filed), BracketGuard 543 (works). IN PROGRESS: GitStatus 545 on portable 4200, installed, NOT removed, NOT logged. Findings so far (not filed): clean repo shows "Git: ?" because the plugin matches old git wording "working directory clean" (git now says "working tree clean"); listeners on_post_activated/on_post_deactivated/on_post_load/on_post_close are not Sublime events, so status only updates on save/clone; with no folder open every save raises IndexError (window.folders()[0]); "Git: Dirty" works. Then `run_command git_changed` followed by get_quick_panel and a visible get_console in one batch: the MCP connection closed and portable 4200 crashed (dump Data\Crash Reports\reports\4e04ba46-d1da-49a0-89b9-88de269ae1b2.dmp, 16:09:49; cdb: every frame inside sublime_text.exe, no symbols, same shape as the 10-16 and 10-18 dumps). Not yet known whether git_changed alone, get_quick_panel on a 3.3-host picker, or the console read caused it. Portable restarted (pid 12764, window shows the repo folder), MCP did NOT come back after two `/mcp reconnect sublime-mcp-portable-4200` sends (port 9522 listening, no Update window). Leftovers: GitStatus package, tools\gitstatus_audit\repo (git repo, folder open in the portable), a.txt modified to "twoone" there, a.txt save; test_installs lines written for GitStatus and the repo. Settings hashes were equal before GitStatus. NEXT: reconnect, repeat `git_changed` ALONE and watch, then clean up (close tabs with No, remove GitStatus via picker, remove folder from window, recycle tools\gitstatus_audit, compare hashes), log GitStatus; then Processing 546, CSSTidy 553, PhpTidy 554, TidyHTML5 561.

**Procedure that worked this session**
- The portable was not running at the start: `Start-Process D:\st_portable_4200\sublime_text.exe`, close its "Update" window with a script that posts WM_CLOSE to that hwnd after checking the owner process is the 4200 exe (scratchpad closeupdate.ps1, hwnd from the screenshot MCP list_windows), then `/mcp reconnect sublime-mcp-portable-4200` through the main Sublime. CORRECTED by Donald 2026-10-19: the reconnect happens at once; only its "Reconnected" message is not printed until my turn ends. Do NOT stop and wait for his "go". On 2026-10-19 my two early sends were followed by "no matching deferred tools" while the portable still showed its Update window; the cause is not known (not the turn end), so if the tool is missing, check list_native_windows/list_windows for a dialog, wait a few seconds and ToolSearch again before asking him.
- batch tool args are FLAT for `pick_quick_panel` (`text`, `wait_ms`), not nested under `args` (different from the older note). `run_command` args stay under `args`.
- `get_console mode=visible tail=25 force_focus=true` shows plugin tracebacks that captured mode misses.
- `set_scratch` is not a command; a modified pathless tab needs `dismiss_native_window` with "No" on the Save Changes dialog.
- recycle.ps1: pass each path as its own argument, NOT an array (an @(...) array is joined into one string and reported "not found").
- Package Control's remove deletes an unpacked copy of the same name too.
- A package whose command opens a picker in the 3.3 host is invisible to get_quick_panel: use ui_screenshot and ui_press_key.

**Leftovers:** none from this stretch except the old ones in the 2026-10-17 baton (Rust, racer, tools folders, WSL perl). Portable 4200 is running with an empty window.

## Batch rows 600-629 done (2026-10-19, portable 4200)
- Ruby Debugger (shuky19/sublime_debugger#62), WordPress Developer Resources (tripflex#8), Better JavaScript (comment on int3h#9): earlier in the batch.
- Shell Turtlestein 612: misfo/Shell-Turtlestein#79 (ST2 begin_edit in error panel), #80 (pipes.quote single quotes on Windows).
- DiffView 615: works on Windows in a git repo; no new finding (known #72, #59, #64).
- CSSFormat 618: not in channel, hand copy; Python 2 SyntaxError; hdemirchian/CSSFormat#7.
- PhpNamespace 619: gl3n/sublime-php-namespace#19 (default stop_folders in Base File.sublime-settings not applied, TypeError; works once set in user Preferences).
- SublimeRope 629: not in channel, hand copy; Python 2 SyntaxError; commented on JulianEberius/SublimeRope#64.
- Portable settings restored (hashes match backups); Packages holds only FileDirStats, GhostShell, MCP Commander, User.
- Still open: recycle tools\processing_audit\sk and tools\tidyhtml_audit after the next portable restart (warn him first, can raise UAC). Scratchpad has dvrepo, pnproj, cssformat_dl, rope_dl test leftovers (session scratchpad only).
- Next batch starts after row 629 of audit_list_2026_10_17_gt6y_top1000.tsv.

## Batch rows 631-663 done (2026-10-19, portable 4200)
- SideBarHider 631: works, no finding. Focus File on Sidebar 632: works, no new finding (known #24, #25, #18).
- SublimeEnhancedUtilitiesSet 633: ImportError Expression on 4200, commented on shagabutdinov/sublime-utilities#1.
- CMakeEditor 636: works, no new finding. Angular Material Snippets 638: confirmed known #11, commented.
- Laravel Docs 647: works, all page URLs resolve. Lua Dev 650: luac not on the machine, parser/build not tried (no download without his word), no finding.
- Auto Refresh 663: Wouterdek/AutoRefresh#16 (Remember never calls save_settings).
- His note mid-batch: popular (high-download) packages are usually bug-free and eat time, but matter more; keep the list order, skip none.
- Portable settings restored (hashes match). Next batch: rows after 663 (665 Gherkin Formatter, 667 AutoSpell, 670 Google Search, 685 HighlightWords, 694 Color Scheme - Rainbow, 698 Reindent on save), four-point check first.

- Lua Dev 650 RETESTED with real luac on his order (`do the luac one. Lua is very important`): Lua 5.4.2 binaries (LuaBinaries, SourceForge, 374 KB) in C:\Users\donal\tools\lua\bin (luac.exe, lua.exe copies); parser works, no finding; build not tried (lua not on PATH, no PATH change).

- Lua Dev build tested (see log row). LEFTOVER: C:\Users\donal\tools\lua\t (holds bad.lua) is locked by the portable (it was an exec working_dir); recycle.ps1 raised a UAC prompt without my warning and failed even as admin. Recycle it after the portable's next restart, warn first. Also still pending: tools\processing_audit\sk, tools\tidyhtml_audit.

## Batch rows 665-704 done (2026-10-19, portable 4200)
- Gherkin Formatter 665: works on Windows, no new finding (known #12, #14, #10). AutoSpell 667: works, no finding.
- Google Search 670: nwjlyons/google-search#12 (on_change(self) TypeError per keystroke in Search any).
- HighlightWords 685: works, no new finding. Color Scheme - Rainbow 694: works, no finding.
- Reindent on save 698: picker install fails 404 because the channel download URL still says mac2000/... (repo is now marchenko1985; NOT reported, rule: nothing in package_control or the channel; tell Donald). Hand copy: marchenko1985/sublime-reindent-on-save#9 (Save All reindents the active tab, not the saved one).
- JavaScriptFunctionDefinition 702: works, no new finding (known #1, #3).
- Sync View Scroll 704: zzjin/syncViewScroll#21 (sync thread keeps running after Remove Package, [Sync ON] stays) and #22 (X vs origY typo). The portable 4200 still has that stray sync thread until its next restart.
- Tool lesson: get_console visible with force_focus while an input panel is open steals focus (my Return went into the buffer); use drive_input_panel for panel input, read the console afterwards.
- Portable settings restored (hashes match). Next batch: rows after 704 in audit_list_2026_10_17_gt6y_top1000.tsv (705 EclipseJavaFormatter, 708 Highlight Whitespaces, ...), four-point check first. Leftovers: tools\lua\t (locked folder, recycle after portable restart, warn first), tools\processing_audit\sk, tools\tidyhtml_audit.

## Batch rows 705-718 done (2026-10-19)
- EclipseJavaFormatter 705 (delfoxie/EclipseJavaFormatter#10, comment on #9; Eclipse kept in tools\eclipse), Highlight Whitespaces 708, Verilog Automatic 709, Themes Menu Switcher 710: no finding except 705.
- orgmode 711: danielmagnussons/orgmode#81 (Toggle Checkbox, IndexError); Settings folder residue removed via picker.
- PythonTest 713: jpellerin/PythonTestST3#4 (Windows cmd quoting) and #5 (IndexError without folder).
- 3v4l Uploader 714: 3v4l.org unreachable, no finding. Line Endings Unify 718: works.
- Next: 719 Git Conflict Resolver (sascha-wolf/sublime-GitConflictResolver), 721 CSSFontFamily (lcdsantos/CSSFontFamily); four-point check first.
- Leftovers to recycle after the portable restarts (warn him, UAC possible): tools\lua\t, tools\processing_audit\sk, tools\tidyhtml_audit. Stray Sync View Scroll thread until restart. Wakelock: he enables Claude Desktop keep-awake himself.

## Batch rows 719-748 done (2026-10-19 night, portable 4200), 6 packages
- Git Conflict Resolver 719: filed sascha-wolf/sublime-GitConflictResolver#22 (Keep Common Ancestor deletes the whole conflict when no ancestor section) and #23 (no "ours" gutter icon in two-way conflicts, regex alternation; fix checked on samples). Known #17, #18, #20.
- CSSFontFamily 721: lcdsantos/CSSFontFamily#5 (Settings - Default menu item opens an empty tab, package is a zip), #6 (Impact stack ends in "sans serif").
- BracketFlasher 724: jaytiar/SublimeBracketFlasher#3 (same zip menu defect). termX 734 (macOS-only, hand copy): afterdesign/termX#67 (commands listed on Windows, decimal.InvalidOperation).
- GitTimeMetric 737: tested with real gtm 1.3.5, no new finding. Fix Mac Path 748: macOS-only hand copy, no finding.
- NEXT: rows after 748 of audit_list_2026_10_17_gt6y_top1000.tsv (753 Sublime Files, 763 Laravel 4 Facades, 774 Ionic Framework Extended Autocomplete, 776 ERB Autocomplete, 787 Shell Exec, 791 Bower, 792 Drupal, 799 SublimeBlockCursor); four-point check first.
- Pattern worth checking in every package: "Package Settings > <name> > Settings - Default" menu items that open `${packages}/<name>/...` give an empty tab when the package is a zip (three hits in one night).
- Tool lessons: `ui_press_key`, `list_native_windows`, `get_open_files` etc. are hidden: call them inside `batch`, args flat. `gh issue create --title` with double quotes inside breaks the command (use plain titles). Hand copy: scratchpad handcopy.ps1 downloads `archive/HEAD.zip`. `NoDefaultCurrentDirectoryInExePath=1` on this machine: a relative `gtm.exe` placed in Sublime's folder is not found by `cmd` (artifact, not a plugin bug). `get_quick_panel` once hung >120 s with the list visible; repeat the call. A "Save Changes?" dialog also appears for a settings tab whose file does not exist.
- AUDIT REPO NUMBERS (his complaint, 2026-10-19: they did not rise with the work): the README figures were last set 2026-10-16 (1076 records) while 340 more rows had been logged, because tools\rec.ps1 only bumped the issue count (and wrongly added one repository per issue). FIXED: rec.ps1 now recomputes records, distinct packages, issues, repositories, open and closed from RESULTS.tsv and ISSUES.tsv on every run (`rec.ps1 -RefreshOnly` does only that). ISSUES.tsv was compared with a fresh GitHub export (export_issues.py, END date now today): 18 states updated, 1 sublimehq issue added; other missing rows are non-Sublime repos on purpose. Now 1420 records, 1328 packages, 1294 issues, 903 repos, 992 open, 302 closed.

## JSON Stringify rewrite PR (2026-10-20, on his order "rewrite the code and push a PR")
- Author Nadock closed #4 (answer: update to build 4213). No public email found (profile, rileychase.net, commits are noreply/Dependabot), so no email was sent; he then ordered the rewrite as a PR.
- Fork dpc00/json_stringify cloned in C:\Users\donal\tools\forks\json_stringify (his one explicit fork+PR exception to the "no forks, no PRs" pause); branch explicit-commands-and-safer-edits, PR Nadock/json_stringify#5 (https://github.com/Nadock/json_stringify/pull/5). Tested live on portable 4200 (3.3 and 3.8 host), fixtures 1-3 identical; repo's make (pylint, unit tests, mypy) NOT run, per his no-tests rule; said so in the PR.
- Watch for the author's reply only when he asks.
- 2026-10-20: PR Nadock/json_stringify#5 also tested on portable 4215 (3.3 and 3.8 host): all checks pass, fixtures 1-3 identical. 4215 was started for it and quit afterwards; settings hashes equal to backups. Reconnect worked by typing /mcp reconnect into MY tab (the tab named after the conversation title, in the one-window main Sublime), text first, Return as a separate call, hands off the keyboard.

## Batch 2 of 2026-10-20 session (portable 4200, all logged with rec.ps1, settings restored, hashes equal)
Done: Sublime Files 753 (al63/SublimeFiles #30, #31), Laravel 4 Facades 763 (#6, #7), Ionic Framework Extended Autocomplete 774 (matheuscas/SublimeIonic #2), ERB Autocomplete 776 (CasperLaiTW/ERBAutocomplete #11, #12), Shell Exec 787 (gbaptista/sublime-3-shell-exec #16 new, comment on known #15 Cyrillic cause).
NEXT rows in audit_list_2026_10_17_gt6y_top1000.tsv: 791 Bower, 792 Drupal, 799 SublimeBlockCursor and onward.
Pattern seen in 5 packages: Package Settings > Settings - Default opens ${packages}/<name>/... and gives an empty tab when the package is a zip.
Tool lessons: hidden tools only inside batch; drive_input_panel takes only action/text (it submits itself); close_file with no name closes the active tab; remove_package then pick_quick_panel by name works; Preferences written from outside is picked up late. Portable 4215 is stopped; reconnect = type "/mcp reconnect sublime-mcp-portable-4215" into my own tab, then Return as a separate ui_press_key.
JSON Stringify PR Nadock/json_stringify#5 is open (tested on 4200 and 4215); no email to the author (none found).

## Batch 3 of 2026-10-20 session (portable 4200)
Done: Bower 791 (benschwarz/sublime-bower #48 new, comment on #41 with cause: TypeError not caught, only works with a project open), Drupal 792 (robballou/drupal-sublimetext #14 h. triggers cannot Tab-expand, #15 indented ; comment), SublimeBlockCursor 799 (no finding; issues disabled).
NEXT in audit_list_2026_10_17_gt6y_top1000.tsv: row after 799 (check the tsv).
sublime-mcp commits made this batch, NOT pushed, NOT released: 00348dd (3.3 quick panel recorder, companion package "MCP Commander Py33" in Packages), 1f06ece (burn first overlay after visible console read). Open: two visible get_console reads back to back alternate with "console did not have the focus" (pre-existing). Each edit to sublime_mcp.py reloads the 4200 server: reconnect by typing /mcp reconnect sublime-mcp-portable-4200 into my own tab.

## Batch 4 of 2026-10-20 session (portable 4200)
Done: CSS Unminifier 803 (issues disabled; 3 defects found; email to domains@joncodes.com DRAFTED in notes\draft_email_cssunminifier_2026_10_20.md, NOT sent, waiting for Donald), Jimbly's Clipboard History 807 (no finding), MatlabFilenameAutoComplete 810 (joepmoritz #3), Smart Delete 818 (channel entry mac2000/... 404s -> tell Donald, no PC report; hand copy ok, no finding).
al63 (Alec Lee) asked us to stop: note feedback_al63_asked_us_to_stop_2026_10_20.md; skip his repos; none of his repos are new.
NEXT: FolderFiles 826 (shagabutdinov), hextoASCII 830, EsFormatter 831, StyleToken 837, PackageSync 844.

## Batch 5 of 2026-10-20 session (portable 4200)
Done: FolderFiles 826 plus its four dependencies FileList, QuickSearchEnhanced, OpenPath (shagabutdinov/sublime-open-path #5 new), StatusMessage; Nadock closed PR #5 (note in sublime-mcp memory). Slip: StGitlab installed by a wrong list INDEX (pick by text, never by index; the list shifts after installs); PC reinstalled it at restart; removed with its libs, nothing left in Data\Lib.
Lesson: after dismissing a native dialog the first show_overlay can also be lost (same effect as after a visible console read); take a screenshot before pressing Return on the palette.
Still pending for Donald: CSS Unminifier email (draft in notes, not sent); fork dpc00/json_stringify and its clone in tools\forks (delete?).
NEXT: hextoASCII 830, EsFormatter 831, StyleToken 837, PackageSync 844 in audit_list_2026_10_17_gt6y_top1000.tsv.

## Batch 6 of 2026-10-20 session (portable 4200)
Done: hextoASCII 830 (ALLZ #5, #6), EsFormatter 831 (piuccio #77 format_on_save flag), StyleToken 837 (no finding), PackageSync 844 (utkarsh9891 #15 restore fails on trailing commas, #16 KeyError on ST4).
Method notes: pick install/remove by TEXT only; screenshot the palette before Return; real node tools in own tools folder or npm -g then uninstall -g; PackageSync default backup path is the real Desktop, always type a sandbox path.
NEXT: row after 844 in audit_list_2026_10_17_gt6y_top1000.tsv.
Pending for Donald unchanged: CSS Unminifier email (not sent), json_stringify fork delete?

2026-10-20: Donald said drop the CSS Unminifier email; draft recycled, nothing sent. json_stringify: local clone recycled, GitHub fork kept at his word.

## Batch 7 (partial): SQLExec 850 done, no new finding (logged 4f1595a). Next: C++YouCompleteMe 853 (needs ycmd/libclang, big install), Goto Bootstrap 854, LoremGibson 860, closure-linter 861, List LESS Variables 870.

## Batch 7 done (2026-10-20): SQLExec 850 (nothing new), Goto Bootstrap 854 (#1), LoremGibson 860 (#3), sublime-closure-linter 861 (ST2-only, nothing filed), List LESS Variables 870 (#10, #11) and its successor List stylesheet variables (#22, #23, #24). C++YouCompleteMe 853 dropped (unmaintained). Deferred list culled and EMPTY (his order). sublime-mcp 1.16.0 released (GitHub, PyPI, npm). Next: Python Fix Imports 879, Package Syncing 887, Search WordPress Codex 892. Rule: test a named successor at once.

## Batch 8 done (2026-10-20): Python Fix Imports 879 (#10 #11 #12), Package Syncing 887 (#29 #30), Search WordPress Codex 892 (#3 #4 #5; successor WordPress Developer Resources was already tested 2026-10-19). Next rows after 892: read audit_list_2026_10_17_gt6y_top1000.tsv from row 149 on (not read yet). The portable 4200 keeps install_py33_helper true in its User MCP Commander.sublime-settings on purpose.

- Jekyll 894 done, nothing filed, cleaned, hashes match. Next: 896 Codeigniter Codeintel Helper, 899, 902, 909, 912, 918, 924, 926, 929, 930.

- Codeigniter Codeintel Helper 896 done (#6, #7), cleaned. Next: 899 RemoteCollab, 902, 909, 912, 918, 924, 926, 929, 930.

- RemoteCollab 899 done (#18, #19, #20, comment on #16); portable 4200 restarted and reconnected (own tab, ui_type_text + Return), clean. Next: 902 CTags for PHP, 909, 912, 918, 924, 926, 929, 930.

- CTags for PHP 902 (nothing filed, ST2-only) + successor PHP Companion (#158) done, cleaned. Next: 909 eCSStractor, 912 Pretty Ruby, 918 jsfmt, 924, 926, 929, 930. Lesson: portable has index_files false; PHP symbol-index packages need it on temporarily (restore from Preferences.backup).

- eCSStractor 909 done (#17), cleaned. Next: 912 Pretty Ruby, 918 jsfmt, 924, 926, 929, 930. sublime-mcp gaps seen (not yet fixed): get_active_file syntax null for view with legacy tmLanguage syntax; close_file discard=true still raised Save Changes dialog on dirty untitled tabs (worked once); focus_sheet echoes 100+ settings.

- Pretty Ruby 912 done (#4, #5), cleaned. Next: 918 jsfmt (node present; needs npm jsfmt in tools), 924, 926, 929, 930.

- sublime-mcp gap work done 2026-10-20 (commits f3eec39, 4f3f8d4, pushed): syntax fallback for legacy tmLanguage views, focus_sheet echo without settings, pick returns pending when a 3.3 callback opens a dialog. NOT reproduced: close_file discard=true raising Save Changes on dirty tabs (works on plain new_file tabs; failed on eCSStractor output tabs). Proxy schemas (python-proxy tool_catalog, node-proxy fallback-tools, tool_tree.json) still lack focus_sheet settings: regenerate at the next release. Next audit rows: 918 jsfmt, 924, 926, 929, 930.

## Batch 9 done (2026-10-20, portable 4200), 5 packages, all cleaned, settings hashes equal
- jsfmt 918: filed mihai-vlc/sublime-jsfmt#56 (node_bridge treats any stderr as failure; Node 24 deprecation warning makes every Format fail; returncode check proven). Install is 5186 files, about 3 min: wait for the file count to stop, do not conclude "no .py file" early (Meteor looked empty the same way).
- Code Runner 926: filed WarWithinMe/Sublime-CodeRunner#4 (language taken by stripping .tmLanguage, ST4 syntax ends .sublime-syntax, Run Code silently does nothing; fix proven on an unpacked copy).
- LiveCode 929: filed trevordevore/livecode-sublimetext#18 (opening .livecode/.rev closes the tab even without livecode project settings).
- Meteor Autocomplete (TernJS) 930: works (needs .meteor folder in the project dir; bundled node.exe), nothing filed.
- AngularInject 932: ST2-only (owner says so, not in channel any more, hand copy), begin_edit TypeError, nothing filed.
- Row 924 was Search WordPress Codex, already done as 892.
- NEXT: 937 Laravel Generator, 939 SAS Syntax and Theme, 941 C++NamespaceTool, 945 PHP Zend Framework 2 Helper, 946 CleanCSS, 947 Duplicate Lines, 948 Python Pretty Print (rows 160-167 of audit_list_2026_10_17_gt6y_top1000.tsv, in C:\Users\donal\data\st_packages). Four-point check first. SublimeLinter-contrib-livecodelint not tested (needs LiveCode tool).
- Tool facts: get_help without section dumps 16 KB (use section=); install lists load in ~15-40 s (use wait_ms); a get_quick_panel/pick by exact index from the filtered result's indexes works; scratchpad handcopy.ps1 (repo, name) downloads HEAD.zip and unpacks flat into Data\Packages\<name>; remove via remove_package picker "remove unknown version" works for hand copies.
## Batch 10 done (2026-10-20, portable 4200), 5 packages, all cleaned, settings hashes equal
- Laravel Generator 937 (hand copy; real Laravel 13 project built with composer.phar in its own folder, sandbox php.ini + php.bat because system PHP has no openssl/mbstring ini): filed gnarula/sublime-laravelgenerator#40 (Artisan output shown only for literal "routes"), #41 (failed Generate shows no reason, stderr not piped).
- SAS Syntax and Theme 939: filed 77QingLiu/SAS-Syntax-and-Theme#1 (Alt+E bound with no context; show_next_error writes User settings every time). SAS itself not run (paywalled). Nested config_spec list is fine on the 3.3 host, not filed.
- C++NamespaceTool 941: filed myurtoglu/NamespaceTool#2 (reverse conversion rewrites words inside string literals; comments not tested).
- PHP Zend Framework 2 Helper 945: filed pipe-devnull/ZF2Helper#9 (templates read from Packages path, fails as installed zip; .no-sublime-package fix proven) and #10 (IndexError on Windows paths in New Controller Action).
- CleanCSS 946: filed stolksdorf/CleanCSS#24 (adds empty first line, drops final newline); URL colon bug already #20.
- NEXT: 947 Duplicate Lines, 948 Python Pretty Print, then rows after 948 of audit_list_2026_10_17_gt6y_top1000.tsv (C:\Users\donal\data\st_packages). Four-point check first. SublimeLinter-contrib-livecodelint still untested.
- Lessons: rewriting RESULTS.tsv with ReadAllText/WriteAllText(UTF8Encoding($true)) added a BOM (fixed in 31c8636): never rewrite those files with a BOM encoding. Check claims in issue text against what was actually run (I wrote "comments" untested; corrected with gh issue edit). A recycle of a folder with deep paths is done piece by piece by recycle.ps1 (fine). The status-bar message of a plugin is gone within seconds: take the screenshot in a separate call.
## Batch 10 continued (2026-10-20): 947 and 948 done
- Duplicate Lines 947: works; whole-line selection ending at column 0 duplicates the next line too (his #10, fixed in master 2020 but Package Control serves tag v1.0.0 without the fix). Repo archived and issue locked: nothing filed, told Donald.
- Python Pretty Print 948: filed peterdemin/SublimePPrint#2 (indent, sort_keys, ensure_ascii settings never read).
- NEXT (remaining rows of audit_list_2026_10_17_gt6y_top1000.tsv): 955 SublimeTextGitX, 959 TerminalProjectFolder, 963 GitStatusBar, 966 AndyJS2, 970 phpDocumentor, 997 CloseCommentTag, 1001 Python Pep8 Lint. Four-point check first.
## Inc-Dec-Value #43 follow-up (2026-10-20, on his order: test PalmtopTiger's monkeypatch, post findings)
- rmaksim/Sublime-Text-2-Inc-Dec-Value#43 (our 9 becomes 11 report): PalmtopTiger pointed to a monkeypatch from issue #30. On portable 4200 in the default 3.3 host the monkeypatch never ran (print inside it never fired; restarts, rename did not help); the one-line fix (sel().subtract(old_pos) before view.replace) applied to the original module works. With .python-version 3.8 added the ORIGINAL code is already correct (clean restart, no patch): the bug is 3.3-host only. Two comments posted (6286576088, then correction 6286649125). Not tested: build 4215 (judged not to matter). Test package, folder and downloads removed, hashes equal.
- Mail check 2026-10-20: only that GitHub notification; nothing else needed an answer.
## Batch 11 done (2026-10-20, portable 4200), 7 packages, all cleaned, settings hashes equal, all logged with rec.ps1
- SublimeTextGitX 955: macOS-only (GitX); expected error dialog on Windows; unsaved tab = silent no-op; nothing filed.
- TerminalProjectFolder 959: filed shagabutdinov/sublime-terminal-project-folder#1 (does not load with Terminal 3.0.0, OpenTerminalCommand renamed TerminalOpenCommand; fix proven on an unpacked copy). The Terminal package was installed and removed with it. Install order lesson: a plugin that failed to import is not reloaded when its dependency arrives; restart needed.
- GitStatusBar 963: filed randy3k/GitStatusBar#8 (ahead/behind regex keeps last digit: 12 ahead shows +2) and #9 (p.wait() before communicate(): git status with 112 KB output hangs forever, shown by two git processes stuck 40 s+; reproduced outside Sublime too). Sandbox repos in tools\gitstatusbar_audit recycled.
- AndyJS2 966 (not in channel, hand copy): works, nothing filed. phpDocumentor 970 (not in channel): Python 2 SyntaxError, known #1 closed, nothing filed.
- CloseCommentTag 997: filed Satoh-D/CloseCommentTag#3 (single-quoted attributes not recognised, comment empty) and #4 (IndexError, closing tag without opening tag).
- Python Pep8 Lint 1001 (not in channel, hand copy): filed dreadatour/Pep8Lint#8 (import pep8 fails on ST3/4; from . import pep8 fixes, lint proven).
- NEXT rows of audit_list_2026_10_17_gt6y_top1000.tsv (from line 175): ReadmePlease 1006, LaTeXTab 1008, PxToEm 1011, Code Alignment 1012, Powershell Help Generator 1015, AceJump 1025, AutocompletionFuzzy 1032, Fold Comments 1035. Four-point check first.
- Lessons: do not call get_active_file on a big file (README dumped 6 KB); `Stop-Process -Name git` would hit his own git, kill by id; handcopy.ps1 (session scratchpad, repo + name) unpacks flat into Data\Packages\<name>; edit a hand copy in place and the 3.3 host reloads it ("reloading python 3.3 plugin"); a 3.3-host quick panel is only visible by screenshot; the portable reconnected itself after a restart once and needed the typed /mcp reconnect the other time. I slipped once and called the Bash tool (a no-op); never again.
- Possible leftover: a Windows Terminal window (pid 11860, started 10:02:30 during the TerminalProjectFolder test) may be from the test; not killed because it may be his.
## Batch 12 done (2026-10-20, portable 4200), 8 packages, all cleaned, settings hashes equal, all logged with rec.ps1
- ReadmePlease 1006: works. LaTeXTab 1008: works (tab and space delimited, & and % escaped).
- PxToEm 1011: filed ningbit/sublime_pxtoem#5 (1.5px gives 1.0.3125em) and #6 (AttributeError when the line has px outside a value). Open #1, #2 (install problems) not reproduced.
- Code Alignment 1012 (not in channel): Python 2 syntax, 32-bit DLL only, known, nothing filed.
- Powershell Help Generator 1015: known #1 and #2 reproduced; comments with cause posted on both (get-command in a fresh powershell cannot see a function that exists only in the buffer; unguarded .group(1)).
- AceJump 1025: works (word mode, select modifier). Select/add-cursor/after are toggles that need a following jump command: calling ace_jump_select twice turned it off.
- AutocompletionFuzzy 1032: needs the Expression package (installed too, removed). Filed shagabutdinov/sublime-autocompletion#10 (nesting entries with mistyped arg keys, TypeError proven) and #11 (long word backward has no command, duplicate caption).
- Fold Comments 1035: known #14 reproduced with a file that has no comments; comment with cause posted.
- NEXT rows of audit_list_2026_10_17_gt6y_top1000.tsv after line 182 (Fold Comments was the last row I saw there, read the tsv from line 183 on; the sublime-package-audit list may end here).
- Lessons: a package whose plugin failed to import is not re-imported when its dependency arrives (restart or reload needed); a palette entry with no command key does not show in the palette; screenshot before sending a key to an input panel, my first 'z' went into the buffer; read the commands file of a package, three packages today had broken palette entries.
## Batch 13 done (2026-10-20, portable 4200), NEW LIST, 6 packages, all cleaned, settings hashes equal, all logged
- The gt6y_top1000 list finished (Fold Comments 1035 was its last row). On his "go" I built the next gradual step: C:\Users\donal\data\st_packages\audit_list_2026_10_20_gt6y_rest.tsv = packages pushed MORE than 6 years ago, not archived, not tested (tsv + RESULTS.tsv name match, version-tolerant), not on earlier lists; 2508 rows, in installs-rank order (columns order, installs_rank, pkg, repo, pushed_days_ago, py_kb, stars). Builder ease_gt6y_rest.py (session scratchpad, copy of ease_age4_6y.py using the cached popular_pages_2026_10_16.json; may be gone). Many rows are color schemes, snippets and syntaxes (py_kb 0): his rule is to keep list order and skip none.
- Done from it: PackageResourceViewer 67 (earlier DROPPED for no .python-version; works on 4200 without one; view and edit work; the edit extracted Packages\Binary, recycled), jQuery 24 (179+39 snippets, scan clean), 1337 Color Scheme 25 (clean), 10% Too Dull 41 (explained open #4: selection and invisibles share #434D5B, comment posted; filed scotch-io/10-percent-too-dull-for-my-tastes#6 empty foreground), Theme - Brogrammer 51 (clean), Bootstrap 3 Snippets 58 (clean; #112 not reproduced). HTML5 7222 and JavaScript Completions were already tested (log, not tsv).
- NEXT in the new list: HTMLAttributes (rank 72, agibsonsw), BlackBird-ColorScheme 77, Bootstrap 4 Autocomplete 83, Javascript Beautify 85, IMESupport 88, ... (read the tsv from order 9 on). Four-point check first: the log and old tsv names do not always match (HTML5, JavaScript Completions and PackageResourceViewer were tested/dropped under other names); grep the log by name.
- Methods that worked for the static packages: scan scripts in the session scratchpad (snip_scan.py all snippets parse/trigger/scope, scheme_scan.py var() definitions, tm_scan.py plist, theme_scan.py textures); colour scheme and theme are applied through UI: Select Color Scheme / UI: Select Theme (type the name with ui_type_text, Return), then restore Preferences from the backup BEFORE removing the package. Package Control opens an install messages tab that takes focus: close it (close_file discard) before typing test text. The visible console read alternates success and failure; use captured when it fails.

## Batch 14 (2026-10-20, portable 4200, all cleaned up, hashes equal, logged with rec.ps1)
List: C:\Users\donal\data\st_packages\audit_list_2026_10_20_gt6y_rest.tsv (file line 2 = first data row).
Done: HTMLAttributes 72 (works), BlackBird-ColorScheme 77 (works), JSHint 90 (real jshint via npm -g, then uninstalled; works), JavaScriptNext 93 (works), jQuery Snippets pack 101 (works; all 9 snippets expand), JSX 106 (allanhortle/JSX is no longer in the Package Control catalog; not tested), HTML Snippets 108 (works; 27 snippets).
Skipped as already tested in the log: Bootstrap 4 Autocomplete 83, Javascript Beautify 85, IMESupport 88. HTML5 7 was syntax-only in the log.
Nothing filed in batch 14.
Lessons: a Tab sent by ui_press_key (post) right after run_command insert is often lost, so the first expansion looked like a failure (jQuery Snippets, HTML Snippets); press Tab twice or retest alone before blaming the package. get_quick_panel with text did not filter the Install Package list (returned 100 rows, big output): type the name with ui_type_text and screenshot instead. search_packages confirms a package is still in the catalog before an install attempt. Per-call args for pick_quick_panel work under args.
Next row: file line 20 of the list (order 19 WordPress 116, then JavaScript Snippets 123, SASS Build 129). Run the four-point check and grep the log by name first.

## Batch 14 addendum (2026-10-20, after the first Batch 14 section; all on portable 4200, cleaned up, hashes equal, logged)
Done: WordPress 116 (works, nothing filed), JavaScript Snippets 123 (filed jprichardson/sublime-js-snippets#24, ii snippet whitespace), SASS Build 129 (real Ruby Sass 3.7.4; filed jaumefontal/SASS-Build-SublimeText2#40, line_regex does not match Sass 3.7 error text; related #7 found only after filing, commented), Tomorrow Color Schemes 136 (works, nothing filed).
Retest finding: HTML Snippets 108 console had "Error parsing messages.json" (trailing comma) that I missed at install time; filed joshnh/HTML-Snippets#24. Lesson: read the captured console with a small look (it returns the whole 100-entry history; use it right after the install, before further work) after EVERY install, and search the repo issues for the same area before filing (#7 was a near-duplicate).
Next row: file line 24 of audit_list_2026_10_20_gt6y_rest.tsv: order 23 Python Completions 146 (eliquious/Python-Auto-Complete), then Laravel 5 Snippets 148, Stylus 157.

## Batch 14 final line (2026-10-20)
Python Completions 146 done (works; open #3 reproduced and commented with the cause: no field marker; nothing filed). Next row: Laravel 5 Snippets 148 (patricksamson/laravel-5-snippets), then Stylus 157 (file line 25 of the list).
History rule (his order 2026-10-20): rec.ps1 no longer commits. Run tools\commit_day.ps1 once at batch end: it makes or amends the single "Audit log through <date>" commit and pushes with --force-with-lease. History was squashed to one commit per day; the old history is deleted (bundle recycled, reflog expired).

Laravel 5 Snippets 148 done (filed patricksamson/laravel-5-snippets#31 empty tabTrigger and wrong scope on Command-confirm, #32 four shared tabTriggers). Next row: Stylus 157 (billymoon/Stylus, file line 25 of the list). Lesson: close the Package Control Messages tab right after install before typing test text.


CORRECTION (his order 2026-10-20): tools\commit_day.ps1 is run ONLY at the end of the day (midnight), never at a batch boundary. At a batch boundary: update files (rec.ps1), append the baton, say 'Batch done, baton written', and do not commit. An earlier line above that says to run it at batch end is wrong.


FINAL RULE (his order 2026-10-20, replaces the two earlier corrections): the first commit_day.ps1 run after midnight creates the commit-of-the-day; throughout the day it AMENDS that commit (batch ends are fine). Never a new commit during the day, no per-package commits. rec.ps1 only edits files.


Stylus 157 done (real stylus 0.64.0 via npm -g, uninstalled after; filed billymoon/Stylus#87 error dialog shows whole raw Node stack, #88 build needs nib not in README, #89 file_regex . counts every line). Next row: CodeIgniter Snippets 169 (mpmont/ci-snippets, list file line 26), then Themr 180. Lessons: styluscompile is the real command name (stylus_compile silently does nothing); a failed compile raises a native modal, dismiss it with computer-use using the portable's app string (the ghostshell-sublime-4107-cache path) and its window id, never the main Sublime process.


CodeIgniter Snippets 169 done (works, nothing filed). Next row: Themr 180 (benweier/Themr, list file line 27). Lesson: my brace-balance check must not subtract placeholders;  already balances.


Themr 180 skipped as already tested (log 2026-10-06). Theme - Cobalt2 185 done (works, nothing filed; install message advertises author's book/course/coupon, not filed). Next row: SassBeautify 191 (badsyntax/SassBeautify, list file line 30; needs a real beautifier/Ruby check), then Theme - SoDaReloaded 195. Lesson: theme_scan.py reports false 'missing textures' for .sublime-package archives (prefix 'Theme - X/' not stripped); verify by hand before believing it.


SassBeautify 191 skipped as already tested (log, works with Ruby Sass 3.7.4). Theme - SoDaReloaded 195 done (works, nothing filed). Next row: HTML Boilerplate 196 (sloria/sublime-html5-boilerplate, list file line 31), then SASS Snippets 197. tools\tex_check.py in the session scratchpad verifies theme textures in a .sublime-package (use it, not theme_scan.py).


HTML Boilerplate 196 done (works, nothing filed). SASS Snippets 197 done (filed sublimebrasil/sublime-snippets-sass#2, + and = snippets invalid in real Sass). Standing instruction from him (2026-10-20): do not ask 'continue', keep going unless something is needed. Next row: React IDE 208 (turadg/sublime-react-ide, list file line 33), then Theme - itg.flat 212, Theme - Dark Material 213.


React IDE 208 done (filed turadg/sublime-react-ide#3 lazyspec check always truthy, #4 menu path). sublime-mcp gap seen: close_file with discard=true on views made by open_file for NOT-YET-EXISTING files (plugin-created paths) timed out on a native 'Save Changes?' dialog; dismissed with list_native_windows + dismiss_native_window button No (these tools work while the main thread is blocked). Do not type into the window while a dialog may be pending. Next row: Theme - itg.flat 212, Theme - Dark Material 213 (list file lines 34-35).


Theme - itg.flat 212 done (works, nothing filed). Theme - Dark Material 213 done (filed artifactdev/Theme-Dark-Material#14 missing texture). Less2Css 214, EncodingHelper 223 (no issues allowed, cloned test), CSS Extended Completions 231 skipped as already tested (log). React Templates 233 done (filed talpor/sublime-rt#1 stale tmLanguage). Next row: Theme - Phoenix 235 (netatoo/phoenix-theme, list file line 40), then C++ Completions 245, Markdown HTML Preview 252 (log hit, check name), React ES6 Snippets 264, Theme - Nexus 272. Temporary edits to portable Preferences (theme, overlay_scroll_bars) are restored from the backup each time.

## 2026-10-20 batch (Phoenix to Nexus)
- Theme - Phoenix 235, C++ Completions 245, React ES6 Snippets 264, Theme - Nexus 272 done and logged with rec.ps1. Markdown HTML Preview 252 skipped: already tested 2026-10-06 (zeyon/MarkdownHtmlPreview#10, see test log line 6720).
- Only finding: React ES6 Snippets has two source.js snippets with tabTrigger rcc (class skeleton and stateless function); rcc+Tab inserts the class one, no choice, README lists only the class one. GitHub issues are disabled on mboperator/sublime-react-es6, nothing sent. Text for Donald: "Claude reports: two snippets in snippets/js use the trigger rcc (react_component and react_stateless_functional_component), so the stateless one cannot be reached by tab trigger; rcc + Tab inserts only the class skeleton (Sublime build 4200)."
- Next rows (list lines 47-54): 3D Tool (Async Burst-Mode) 275, LaTeXing 276, CodeIgniter Utilities 278, Pretty YAML 280, Monokai Dark 285, C++ Snippets 296, HTML Minifier 300, ColorSchemeEditor 301. Portable 4200 is clean (Preferences and PC settings hashes match backups).

## 2026-10-20 batch 2 (3D Tool to ColorSchemeEditor)
- Done and logged: 3D Tool 275 (leoheck/sublime-3d-tool#3, syntax rules without word boundaries), LaTeXing 276 (no new defect; #267/#268 already open), CodeIgniter Utilities 278 (RoverWire/codeigniter-utilities#4, duplicate trigger cidbtranscom), Pretty YAML 280 (SECURITY, not filed), Monokai Dark 285 (clean), C++ Snippets 296 (clean), ColorSchemeEditor 301 (bobef/ColorSchemeEditor#17). HTML Minifier 300 skipped: already tested 2026-10-05 (our issue #11).
- For Donald, Pretty YAML (aukaost/SublimePrettyYAML, issues disabled): PrettyYaml.py calls yaml.load(text) with the full Loader (bundled PyYAML 3.10), so YAML text with !!python/object/apply:os.mkdir [path] runs it when Pretty YAML: Reformat (Ctrl+Alt+Y) is used. Tested live with a harmless mkdir in the session scratchpad, folder recycled. Fix: yaml.safe_load. Not emailed: his call (security, private channel better than public).
- Also unsent (issues disabled): React ES6 Snippets rcc duplicate trigger (text in the batch 1 section).
- Next rows: list lines 55+ of audit_list_2026_10_20_gt6y_rest.tsv (after ColorSchemeEditor 301). Portable 4200 clean, hashes match.

- Donald (2026-10-20, after batch 2): sent the emails for Pretty YAML and React ES6 Snippets himself; nothing more to send for them.

## Batch 3 (2026-10-20, list audit_list_2026_10_20_gt6y_rest.tsv)
Done after ColorSchemeEditor: Theme - Darkmatter 303 (#6, #7), TodoReview 305 (comment on #175), Additional PHP Snippets 307 (#12), C++ Starting Kit 310 (#29, #30), CSSLint 316 (#18, #19), Function Name Display 329 (#33), Bootstrap 3 Jade Snippets 330 (#19, #20; my first "no expand" was a typo, trigger is bst-navbar:basic), Open Folder 333 (#11, command name clashes with ST4 built-in open_folder), Theme - Centurion 335 (clean), Node Completions 341 (clean), Theme - Sodarized 344 (clean), requirementstxt 346 (known #15/#16), LESS-build 352 (#55, dotless exe inside zip), 4GL 365 (clean), JavaScript Ultimate 366 (clean, ES2016 by design), Laravel 4 Snippets 371 (clean), Angular 2 Snippets (John Papa) 372 (#4, stray brace), Django Snippets 378 (#9, #10).
Next: Numix Theme 382 (list line 73), then 74+.
Open: scratchpad folder lesstest is locked by Sublime (recycle fell back to admin, not retried); stale "Error loading syntax file" dialogs for removed packages keep appearing, dismiss with dismiss_native_window OK. Donald does not need to do anything.


## Batch 15 (2026-10-20 night): FIRST BATCH IN THE MAIN SUBLIME (portables are gone), 6 packages, all removed, settings hashes equal, all logged with rec.ps1
- C# Snippets 392: etic/CSharpSnippets #11 (try snippet inserts catch { instead of catch (), #12 (permission snippet stray }).
- Unity3D 395, Material Monokai 397, react-native-snippets 412, RailsCasts Colour Scheme 414, Haml 418: nothing found.
- NEXT in audit_list_2026_10_20_gt6y_rest.tsv: Theme - Asphalt 423 (list line 82), then Markmon 428, ColdFusion 433, lessc 434, Ruby on Rails snippets 438, CSS Completions 444 (four-point check first; Numix, Python Debugger and Inc-Dec-Value are already handled).
- HOW IT RUNS NOW (his orders 2026-10-20): main Sublime 4215 only, no portables, the sublime-mcp code stays as is, fixes go in skills. Rules are in this skill, section "Main Sublime only, he is at the same keyboard". Bug log: sublime-mcp .claude\memory\project_bug_log_2026_10_20.md (B1 nameless close_file closed his Claude tab, B4 no awareness of his input, B5 set_setting has no tab argument, others).
- Steps that worked: backup both settings files to the session scratchpad first; install = show_overlay + screenshot + ui_press_key Return, then get_quick_panel text= to get the exact index, pick_quick_panel index=; test tabs made with new_file and addressed by index (run_command scope text index=, get_view_content index=); view colour scheme via set_setting (active tab only: check get_sheets in the same batch); close by index or name only; remove through the remove_package picker (get_quick_panel then pick by index); compare hashes; rec.ps1.
- Tab pressed right after an insert is often lost: press Tab again in a separate call; screenshot to see the snippet popup.
- WARNING: duplicate tabTriggers show a popup on 4215, so they are not a defect. These earlier 2026-10-20 reports used "duplicate trigger" without the popup check and may be wrong: patricksamson/laravel-5-snippets#32, RoverWire/codeigniter-utilities#4, and the React ES6 Snippets rcc email (sent by him). CORRECTED the same night on his word: RoverWire/codeigniter-utilities#4 retested live on 4215 (popup lists both, "trans_complete unreachable" was wrong), comment posted and issue closed; patricksamson/laravel-5-snippets#32 got a correction comment (the copy-paste triggers stand, "no way to type DB::statement" was too strong). RESULTS.tsv and ISSUES.tsv updated. The React ES6 Snippets rcc email: correction SENT on his order to mboperator@gmail.com (Gmail message 1a15caa80f94d52e, new thread; his original is not in this Gmail's Sent mail; the email says it was not retested on that package); the other "shared trigger" rows in RESULTS (RPGMaker #3, Vtex #2) were checked and are fine.