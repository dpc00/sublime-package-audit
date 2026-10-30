---
name: session-baton-2026-10-29-static-backlog
description: START HERE (newest, audit): 1,240 packages whose latest result is a static check only; live testing resumes in main-list row order, DrSync (row 1) done; hold is lifted; how the list was built
metadata:
  type: project
---

**State 2026-10-29 (evening)**
- Hold on GitHub is LIFTED (Donald: "We did PRs today, so of course it is lifted"); the file gate is RETIRED and deleted (SKILL rule 6f, 2026-10-30; the earlier "works again" was wrong). Filed today: szensk/subllualove#17 and #18 (Lua Love), eddorre/SublimeERB#39.
- The new-list work (packagecontrol.io/browse/new, 219 pages) is finished and recorded; see [[project_new_list_all_recorded_2026_10_29]].
- BACKLOG found by reading RESULTS.tsv, not by a list: 1,240 packages whose LAST row is "static check only" (parse of repo files, not installed or run; the 2026-10-27 pass under the hold). They carry "Main list row N" in the note. Live testing goes in row order, starting at row 1. Done: row 1 DrSync (not in the picker, installed through Add Repository; bundled urllib3 breaks on Python 3.14, record-only by the gate).
- How to list what is left: take the last row per name (strip a trailing version suffix, lower case) and keep those whose note contains "static check only"; sort by the row number in "Main list row N". Skip names that already have a later live row. Install counts are not in the audit lists for most of these, so row order is the order.
- Method for a package missing from the picker: ledger ADD REPOSITORY line, `add_repository` plus URL and newline, `install_package` and narrow with `get_quick_panel` text, pick; at the end restore `Package Control.sublime-settings` from the baseline copy (hash FBBFAC8A) after closing the portable.
- Tool trap: `get_quick_panel` with a short `text` such as "Dr" dumps 40 items; use the full package name.

**Next:** row 4 "0x0", then 5 "42 Function Count Lines", "ABC Notation", ...

**Update 2026-10-30 (batch 23 done):** live testing continues in main-list row order from data\untested_static_only_2026_10_29.tsv (regenerate with scratchpad make_list.ps1 + picker_split.ps1; skip names not in the picker: Edge Theme Addon, AMPscript, CBP Syntax Highlighter, Boron, BetaCode, Camaleon, Alan, Artisan, AVR-ASM, BazelSyntax, Behat, Better TypeScript, Biml, CodeIgniter 3 Snippets). About 1,123 left; next row 100 CMakeFormat. Portable 4215 stays open between batches. Always run list_native_windows before concluding a package breaks commands (skill rule 6h). Issues filed 10-30: AutoBackups#42, BrowserBookmarks#5, sublime-butane#2, caniuse_local#12, code-test-switcher#3, ChineseLocalization#60, Sublime_Chromeless#1. Package Control side (one line for him): requests installs without urllib3 (ChromeREPL) and cson without speg (CSON Converter) on Python 3.14.

Update 2026-10-30 (batches 30-35 done, audit repo 931667b): Composer, Enhanced Clojure, Console Wrap (issue consolewrap#36), Entypo Completions, Context (missing Expression package, already sublime-context#1); Epitech Coding Style, Continuous Merge, ConvertFullHalfWidth, Express Completion, Cool; Extract Lines, Copy as HTML (CopyAsHtml#9), Extract Text to Laravel Blade View, Copy Relative Path, Coreboot syntax; Cottle, FakeImg.pl, CP Parser, Crypto, fasd; Crystal, Fat-Free Framework Snippets, CSharpier, FEI, CSS Extended Completions (CSS-Extended#61); Fex, Csslisible, FileSync, CSSOrder (cssorder#8), FilterPipes. Package Control side for Donald in one line: requests installed without urllib3, cson without speg, beautifulsoup4 without soupsieve (all on Python 3.14). Next: rebuild the list with make_list.ps1 then picker_split.ps1, take the first five picker rows not in the skip list.

Update 2026-10-30 (batches 36-40 done, audit repo b04e55f): FindSelected, Cucumber (drewda/cucumber-sublime-bundle#47), Flight JS Snippets, DailyOrganizer, Focus Last Tab; DaisyUI Autocomplete, Fold Python, Dart (guillermooo/dart-sublime-bundle#592), Foundation 5 Snippets, DataConverter (fitnr/SublimeDataConverter#31, cause proven: CRLF buffer and selection.find(newline)); FSharp, Default File Type, Definition Preview, Deselect, GameMaker Language (GML) Bundle; Devastate, Gemma (parachute-io/gemma#1), Devastate Mode-Z, GLSL Compiler, GoDebug; Diffable, Golite, Google Closure Template snippets, Django Manage Commands (vladimirnani/DjangoCommands#46), DocPHPManualer (garveen/docphp#16). OPEN CLEANUP: Data\Packages\.logs\Dart.log (0 bytes) on the portable is held open by the plugin host; recycle the .logs folder the next time the portable is quit. Package Control side for Donald, one line: shellenv library 'not available for Python 3.14' (Golite, Django Manage Commands, DocPHPManualer, Closure snippets installs). Rule learned: a wrong guessed syntax path in set_file_type raises an Error loading syntax file dialog that disables the window; list_native_windows and dismiss it.

Update 2026-10-30 (batches 41-44 done, audit repo 57d2a8b): Grepmark, Done, DoxyDoc, Groupie, Grunt (row corrected in batch 42: its 'Gruntfile not found' dialog surfaced late, skill rule 6i added); Grunt Snippets, EasyMotion, HackerTyper, Hammer for Mac Snippets, Edit Preferences (sublimator/EditPreferences#13); EDN, EJS, ElasticsearchClient (KunihikoKido/sublime-elasticsearch-client#9, bundled requests imports cgi), ElixirDocs, Homebrew Build System; ElixirSublime (vishnevskiy/ElixirSublime#46), Eloquence, HTML5 Doctor CSS Reset snippet, HTML Email Snippets, Emoji Code. Package Control side for Donald, one line: libraries not available for Python 3.14: shellenv (Golite, Django Manage Commands, DocPHPManualer, Closure snippets) and emojitations (Emoji Code); earlier: requests without urllib3, cson without speg, beautifulsoup4 without soupsieve. Still open: recycle Data\Packages\.logs when the portable is next quit.

## Update 2026-10-30, after batches 45-48

- Batches 45-48 done, recorded, pushed (latest sha 1957e7d). List was 1,004 rows before batch 49.
- Filed: aronwoost/sublime-expand-region#87 (messages.json trailing comma) and #88 (invalid escapes); anly2/sublime-extend-selection#3 (messages.json missing comma).
- ExpandSelectionToComments: no load line (.python-version 3.3), command did nothing, cause not established, not filed.
- Open: Data\Packages\.logs (Dart.log held by the plugin host) to recycle when the portable is next quit; reconcile_issues.ps1 at a quiet point; Package Control one-liner for Donald (libraries not available for Python 3.14: shellenv, emojitations; libraries installed without dependencies: urllib3, speg, soupsieve).
- Routine unchanged: make_list.ps1, picker_split.ps1, first 5 picker rows minus the skip regex, ADD ledger line, install/exercise/remove, baseline hashes 78CEFE76 / FBBFAC8A, rec_bNN.ps1.

## Update 2026-10-30, after batches 49-54

- Batches 49-54 done, recorded, pushed (latest sha 7ac7712). List was 974 rows before batch 55.
- Filed: anly2/sublime-extend-selection#4 (IndexError at line 195, which also corrects the batch 48 row), papaDoc/FastSwitch#9, yann-shi/FileHeader#120, skuroda/FindKeyConflicts#12, ment4list/SublimeZilla#28.
- Record-only (archived repos): Kirby2 CMS Snippets ("::" file name), Kivy Language (messages.json commas), FileZilla (dirConfig.py:83), Kodery (Python 2 except syntax), LightningComponentsCompletions (aura_completions.py:103).
- Lesson: a package command can open an input panel (FileHeader: Add Header) that then swallows select_all/insert; look at the screen when a command seems to do nothing. A package's syntax settings can name a colour scheme: set the test buffer back to Plain Text before removing it (knockdown dialog, rule 6i).
- Open: Data\Packages\.logs (Dart.log) to recycle when the portable is next quit; reconcile_issues.ps1 at a quiet point; Package Control one-liner for Donald (libraries not available for Python 3.14: shellenv, emojitations; libraries installed without dependencies: urllib3, speg, soupsieve).

## Update 2026-10-30, after batches 55-61

- Batches 55-61 done, recorded, pushed (latest sha fbe9400). List was 939 rows before batch 62.
- Filed: math2001/FoldFunctions#3 (selectors no longer exist in ST4 syntaxes), sagold/FuzzyFilePath#62 (21 escapes), fuse-open/sublime-plugin#40 (plugin_loaded overwrites the global open_files_in_new_window), kemayo/sublime-text-git#587, SnoringFrog/GitlabIntegrate#13 and #14 (ST4 import check).
- Record-only: archived MakeTargets, MapTool Syntax, LightningComponentsCompletions, Kodery; Gitignorer's Preferences rewrite is the closed #27.
- OPEN, needs Donald: the portable still runs Gitignored File Excluder's 5-second timer (known #27) and its Preferences.sublime-settings is not baseline (hash 11653DBC instead of 78CEFE76: file_exclude_patterns emptied, folder_exclude_patterns added). Fix: run_command exit on the portable (it asks Donald to Accept a consent prompt; it was not answered and not retried), answer the Save Changes dialogs with Don't Save after reading them, restore Preferences (remove folder_exclude_patterns, put the 21-entry file_exclude_patterns list back; check hash 78CEFE76), recycle Data\Packages\.logs, start the portable again with computer-use start_app.
- Lessons: read the console BEFORE other tools after an install (a long package's output pushes the others out of the tail); packages can write to User and to Preferences on load or on timers (Fuse, Gitignorer, MakeTargets): compare Preferences hash and the User folder after every batch and restore; get_quick_panel takes limit, so use text plus limit for short names (Git).
- Package Control notes for Donald (still unsent as one line): libraries not available for Python 3.14 (shellenv, emojitations); libraries installed without dependencies (urllib3 for requests, speg for cson, soupsieve for beautifulsoup4); the GitHubIssue zip lacks the root __init__.py that the repo has.

## Update 2026-10-30, after batches 62-70 (supersedes the OPEN item above)

- Done and pushed through batch 70 (3efb141); list about 888 rows. Next: rebuild with make_list.ps1 and picker_split.ps1 (scratchpad), take the next 5 picker rows.
- The portable was restarted 2026-10-30: Preferences restored to baseline (SHA-256 prefix 78CEFE76), .logs recycled, and Data\Packages\MCP Commander is now a JUNCTION to projects\sublime-mcp (Donald: portable was not linked; the plugin now follows the repo, including omp's commits). Reconnect after a restart: type `/mcp reconnect sublime-mcp-portable-4215` into my own tab with the main sublime-mcp (`ui_type_text` without newline, then `ui_press_key` Return); it sometimes reconnects by itself.
- omp (Tab 2 in the main Sublime) also commits to sublime-mcp: dialog text, no more main-thread hangs, close_file refuses with no name, install_package/search_packages tools removed (Package Control's own install_package command still works from run_command). Read its summary with get_view_phantoms on the omp tab (html false).
- Filed: ggordan/GutterColor#128, xjsender/haoide#222 (import cgi), hayaku/hayaku#315, larlequin/PandocAcademic#32. Record-only: Haskell HSX syntax recursion error, My Snippets zombie thread, Goto Related no-project crash, GoGdb, Gourmet, GoTools, Gofmt/Golang Tools Integration (Package Control libraries missing for 3.14).
- Lessons: a bad-arg shape (name inside args) ran a nameless close, now refused by the tool; leftover leftovers after removal: My Snippets thread, Gitignorer timer, GPG settings, Gutter Color cache folder; late dialogs show syntax errors (read them with list_native_windows).

## Update 2026-10-30, after batch 75
- Batches 72-75 done and pushed (latest 91c84b1). One issue filed: Hog-CERN/HogSublime#2 (served tag v0.0.1 has the nested file_extensions list; master has the fix). Everything else was withheld by the stale gate; WRONG, see the 2026-10-30 filing policy (rule 6f) and the withheld list.
- Next: rebuild the list (scratchpad make_list.ps1, then picker_split.ps1; both read data\untested_static_only_2026_10_29.tsv), take the next five rows with picker = picker in main-list row order; next is Prismic.io snippets (row 307) onward.
- New rule 6i in the audit skill (by omp): before filing, record "repo: last commit YYYY-MM, N open, last human reply YYYY" in the RESULTS note and say which version was checked (release tag or master).
- Tool notes: `move` ignores `amount` (one step per call); get_scope_at_cursor and get_selection are cursor-based (line/col args ignored); `ui_hover` works after `front.ps1 -Hwnd` brings the portable forward; keep get_console tail small (Prettify prints about 5 KB per run); polyfill's sort_user_settings rewrites Preferences (copy it first and restore).
- Picker gaps: CBP Syntax Highlighter is not in the Install picker (recorded as such); a large repo-folder package (HTML-CSS-JS Prettify, about 3,100 files) takes minutes to install.

Update 2026-10-30, after batch 80:
- Batches 76-80 done, recorded, pushed (latest audit commit 17bbe95). Next list rows start after Incrementor (main_list_row 324); about 837 left. Routine unchanged (make_list.ps1, picker_split.ps1 in the session scratchpad rebuild the list; five picker rows in row order).
- Not packages: his email request 2026-10-30 was taw/sublime-paradox#1 "check PR #3"; tested on 4215 (stray } and # comment scopes fixed with the PR), result posted as a comment on #1 (no PR or fork by us).
- Tool notes: show_overlay needs settle_ms 1500-2000 or the palette opens but Return is ignored (then a Return lands in the untitled buffer); front.ps1 -Hwnd 852668 helps; ui_hover takes x,y pixels (not line/col); close_file with no name/path/index refuses (by design, B1 fix); open_file of a .docx with Incomprehensible Ex writes a .inex file beside it.
- Python 3.14 patterns seen again: shlex.split(None) (PyYapf), invalid escape SyntaxWarnings, collections.Iterable, cgi, binary PIL.

Update 2026-10-30 (late): FILING POLICY is SKILL rule 6f. No age/installs gate. Before any issue run tools\is_alive.ps1 <owner/repo>: DEAD (archived, issues off, or last commit > 3 years with no owner comment or issue in 3 years) = record in RESULTS only, never file; ALIVE = short factual issue (also data\do_not_file.tsv, no duplicate, one per finding). Lesson: 17 issues filed today (the gate backtrack) were all on DEAD repos by this test; left open, not touched again. Alive repos seen: taw/sublime-paradox, Hog-CERN/HogSublime.

Update 2026-10-30 (after batch 93): batches 81-93 done, recorded, pushed (latest audit commit a901779 at the time); about 772 static-only packages left. Routine unchanged (make_list.ps1 then picker_split.ps1 in the session scratchpad, five picker rows in main_list_row order, ADD ledger line, install/exercise/remove, baseline hashes 78CEFE76 / FBBFAC8A, rec_bNN.ps1, commit_day.ps1). Next: row 370 onward after Kick Assembler (C64).
- README figures are now recomputed by tools\rec.ps1 (-RefreshOnly recomputes without logging): never hand-type them (Donald, 2026-10-30: "those numbers are crap and misleading"). ISSUES.tsv was reconciled from GitHub (3096 rows).
- Merged-PR forks and clones deleted 2026-10-30 (sublimetext-StatusBarWeather, sublimetext-StatusBarTime, EasyFileHider); 11 forks with open PRs remain.
- Traps: after a package that ships its own libs is removed the 3.14 host keeps a stale sys.path entry (a later import error names the removed .sublime-package): restart the portable and retest before recording a load error. Install picker index is the GLOBAL index from get_quick_panel "indexes", not the filtered position. A Package Control Messages tab can take focus after an install and swallow insert/set_file_type: check get_sheets before typing. insert auto-indents my test text: set_setting auto_indent false first. A native Save Changes dialog on closing a dirty untitled tab: dismiss_native_window button No.
- Package Control installs some libraries without their dependencies (requests without urllib3 for JSONComma); not ours to file.

Update 2026-10-30 (after batch 97): batches 94-97 done and pushed; about 752 static-only left. OPEN: C:\Users\donal\.subl.log (SublimeLog leftover, locked by the plugin host) to recycle after the portable is next quit; first check the lock with a plain file open, never run recycle.ps1 on a locked file (it asks for UAC). The portable window project data is {"folders": []} after add_folder/remove_folder (clears on restart). Packages that need a project folder (Laravel Blade AutoComplete, Launch) can be tested with add_folder and remove_folder.

Update 2026-10-30 (after batch 105): batches 98-105 done and pushed (4882b27); about 712 static-only left; next from the rebuilt list (make_list.ps1, picker_split.ps1) is main_list_row 424 onward. Traps seen: plugin-created files in Packages\User (LikeGit, sublime-llm, Localpod, LSL) and %TEMP% (preview html) get recycled after a lock check; theme-only packages (Pigment, Spacefunk) cannot be activated without changing global Preferences, so they are recorded as install-only; never rewrite installs_ledger.md with Set-Content (it changed every line ending); set_setting color_scheme goes to the ACTIVE view, close any Messages tab first. The leftover C:\Users\donal\.subl.log is still to recycle after the portable's next quit.


## After batch 115 (2026-10-30)
Batches 106 to 115 done and pushed (last audit commit 5068b90). 560 rows still untested in the picker-list; next is Notepad++ Color Scheme (main row 462). Open: the Match output panel from batch 106 keeps raising a stale 'Error loading syntax file match_syntaxes' dialog after every removal or syntax change until the portable restarts; dismiss it with dismiss_native_window before pressing Return in a picker. C:\Users\donal\.subl.log (SublimeLog leftover) still to recycle after the portable's next quit (lock check first).


## After batch 121 (2026-10-30)
Batches 116 to 121 done and pushed (last audit commit 692dc98). 535 rows left in the picker-list after the rebuild; next is SublimeLinter-contrib-elixirc's successors in main-row order (rebuild with make_list.ps1 then picker_split.ps1 in the scratchpad). New lessons: set_file_type right after an install can give one 'Unable to stat' dialog (index lag, retry after a few seconds, OpenWrt); open_default_for_current_view launches the Windows OpenWith chooser when no default app is set (close OpenWith.exe afterwards); Solarized Toggle rewrites the portable Preferences (back up first, restore, recycle its User settings file). Open items unchanged: stale Match dialog until the portable restarts; .subl.log to recycle after the next quit.

## After batch 130 (2026-10-30)
- Batches 126-130 done and pushed (last a0d8b3b); 490 rows left in the picker list after the batch-130 rebuild; next main-list row 541 onward (rebuild with make_list.ps1 then picker_split.ps1 in the session scratchpad, take the next five rows where picker -like 'picker*' by main_list_row).
- Nothing filed in 126-130: every defect was on a DEAD repo. Live repos checked: PHP CS Fixer (IndexError when the window has no folders; cause is project_data[folders][0] at fixer_possible_paths line 56; user path to that state not shown, so not filed), Projectionist (same IndexError kind, cause not traced).
- Lessons: a literal backslash-u escape in a single-quoted PowerShell note is not converted (batch 129 note fixed in RESULTS.tsv and .tested_packages.tsv); do not run New Project style commands of project packages (default path /projects/<name> writes outside the portable); the stale Match dialog still appears after nearly every install and blocks the pickers until dismissed (dismiss_native_window, then hide_overlay and retry).

## After batch 138 (2026-10-30)

Batches 131-138 done, each baseline-verified (Preferences 78CEFE76, Package Control settings FBBFAC8A) and pushed; last commit afb01f5. 449 picker rows were left when batch 138 started; next rows after main-list row 596. Per batch: rebuild list (scratchpad make_list.ps1, picker_split.ps1), ADD ledger line, five packages, REMOVED ledger line, rec_bNNN.ps1 (also commits and pushes).

Lessons since batch 130:
- A package marked picker in the list may no longer be offered (RemoteTree, batch 135): search for the neighbours, record it as not installable, take the next row as the fifth.
- auto_indent doubles typed indents in multi-line insert; set auto_indent false on the view before testing indent tools.
- Dangerous commands are read, not run: Restart (taskkill all sublime_text.exe), RSync (deletes), RemoteDiff/ RemoteEdit need remote hosts.
- rsub: the listener on 127.0.0.1:52698 stays open in the portable plugin_host after Remove Package (ends when the portable quits); recorded in RESULTS.
- RESTer HTTP Client (3.3 host): its command and palette entry did nothing, cause not found; recorded only.
- Recurring: stale Match dialog (dismiss, hide_overlay, retry), Messages tab (close_file by name), bare get_quick_panel cannot see Python 3.3 host panels or the command palette (use ui_screenshot).
- Open: .subl.log to recycle after the portable quits; portable restart also clears the Match dialog and the rsub listener.

## After batch 149 (2026-10-30)

Batches 139-149 done, each baseline-verified and pushed; last commit e83c8f7. Next rows after main-list row 682 (Syncrow). Same per-batch routine as above; nothing was filed in 139-149 (every defect was in a DEAD repo; the ALIVE ones, Smarty, SmPL, Starlark, StGitlab, Structurizr DSL, Swift, Swift Next, had no defect).

Lessons since batch 138:
- A command can open a SECOND Sublime window a few seconds later (SublimeGDB gdb_launch, batch 147); my picker keys then went to that window. After any command that may raise a "configure the plugin" dialog, run list_native_windows before the next picker; close the extra window with dismiss_native_window action close and answer No to the save questions.
- Packages can leave folders behind that Package Control lists as a package with "unknown version" (Syncrow Snippets, batch 149): remove them through the Remove Package picker, not by hand.
- Packages that pull libraries (SmojSubmit, StGitlab) clean them from Data\Lib on removal; still check Lib after each batch.
- Plugins that write outside the package folder (Sublime Bookmarks pickle in Data, SortTabs User settings): recycle with recycle.ps1 after removal.
- Common load failures on the 3.14 host: collections.MutableSet/Iterable aliases, cgi module (3.13), inspect.getargspec (3.11), def async (3.7), unresolved bundled six.moves.

## After batch 156 (2026-10-30)
- Batches 150 to 156 done and pushed (rows 683 to 741); the list had 358 picker rows left after 156, next row 742.
- TOML ships with Sublime (Packages\TOML.sublime-package) so the picker hides it: record as not installable, take one more row to keep five live.
- HTML-embedding syntaxes (push scope:text.html.basic with with_prototype) fail on build 4215 with Apparent recursion 25000 sanity limit; confirmed with my own control syntax (UL4, Super Templates); sublimehq/sublime_text#6555 is open. Do not file it against the packages.
- Plugins leave files behind: Text Marker makes Data\Packages\Color Scheme - Default (recycled), Test Runner makes Data\Installed Packages\Test Runner.log (locked by Sublime, recycle after the portable quits, along with C:\Users\donal\.subl.log).
- Theme and scheme packages: set the scheme on the view with set_setting color_scheme; for a theme edit Preferences and restore from scratchpad\Preferences.baseline.sublime-settings (hash 78CEFE76).


## After batch 199 (2026-10-31, new session after the portable restart)

- PACKAGE CONTROL PICKER EMPTY: the public https://packagecontrol.github.io/channel/channel_v4.json has `"packages_cache": {"...repository.json": []}` (272 KB, libraries only) since about 2026-10-30 night; Install Package says "There are no packages available". Not our rig (curl and PC's own ChannelProvider agree). Donald's order (2026-10-31): carry on with release-zip installs, batch 199 and the rest. Nothing filed in package_control/packagecontrol.io (standing rule).
- METHOD while the picker is empty: release URL from scratchpad channel_v3.json (packagecontrol.io/channel_v3.json still has packages; picker_split.ps1 downloads it), `tools\install_zip.ps1 -Name <pkg> -Url <zip>` repacks the zip without its top folder into Data\Installed Packages\<Name>.sublime-package (edit its $sp path first), test with eval_python, remove with run_command remove_package then get_quick_panel text <full name> and pick_quick_panel index, never recycle.ps1 on a loaded package (locked). ADD ledger line says release zip. Rows say "picker unavailable".
- LESSONS: get_console takes `tail`, not `lines` (a wrong arg dumped 18 KB); never open a zip in eval_python without `with` (an open handle blocked the removal: PC scheduled a clean up on restart, Preferences got ignored_packages, PC settings got in_process_packages; fixed by gc.collect, recycle, restoring Preferences.baseline (78CEFE76) and emptying in_process_packages); Package Control settings hash is now A153962D (PC rewrote it; content = the three baseline packages plus the channels entry), not FBBFAC8A; wait ~6 s after the pick before checking files.
- Batch 199 done and pushed (ac4e8bc): WDL Syntax, WLST, WP Keygen, WRAMPAssemblyLanguage, Web Audio API Autocomplete; all DEAD repos, nothing filed. 245 static-only rows were left before it (143 picker rows); next from the rebuilt list (scratchpad make_list.ps1 + picker_split.ps1 from session 95abb597): main row 1923 WebDavSync, 1925 WebExPert - ColorScheme, 1926 WebFocus, then onward.

- After batch 200 (2026-10-31, pushed f8d2522): WebDavSync (Python 2 code, SyntaxError), WebExPert - ColorScheme, WebFocus, WebGLCompletions, WeexTemplate (debug print of settings.__dict__ raises AttributeError, create-file commands do nothing; plugin_loaded makes Packages\User\WeexTemplate, recycled). All DEAD repos, nothing filed. 240 static-only rows before it, 138 picker rows; next main-list rows after 1930 (rebuild with make_list.ps1 and picker_split.ps1 from session 95abb597's scratchpad). Removal of a package that created files: check Data\Packages and Data\Packages\User after the pick.

- After batch 201 (2026-10-31, pushed 84e7fe3): Wget, White Night Color Scheme, Whitespace Removal, WhizzML, WhooshSearch; all DEAD, nothing filed; 235 static-only rows before it, 133 picker rows; next main-list rows after 1937. Release-zip lessons: a zip that contains .no-sublime-package must be installed as a FOLDER in Data\Packages (Expand-Archive, copy the top folder), not repacked; switching a package from zip form to folder form leaves a stale zipimport entry (clear sys.path_importer_cache and sys.path entries for the old .sublime-package, pop the modules, then sublime_plugin.reload_plugin); remove_package takes no package argument (picker only: run_command remove_package, get_quick_panel text <name>, pick_quick_panel index, wait 7 s, verify); installing all five at once is fine (ledger says so); never list zip contents of big packages (whoosh) in the output; call the plugin's own panel through ui_type_text when the check needs the panel (I used the module function for Wget: say so in the row).

- After batch 202 (2026-10-31, pushed with the batch commit): Wildlife gutter theme, WinMerge (unguarded winreg.QueryValue at import: does not load without WinMerge), Wisedu TrunPage Snippets, Witch Hazel, Witcher Script Syntax; all DEAD, nothing filed; 230 static-only rows before it, 128 picker rows; next main-list rows after 1944. tools\install_zip.ps1 now copies a .no-sublime-package archive as a folder. NEVER name a PowerShell helper rd (alias of Remove-Item); use Show-PkgFile.

- After batch 203 (2026-10-31, pushed): Wolf Theme, WolframAlpha Lookup (needs requests; not installable while the channel is empty), Wollok, Wombat Theme (UI theme tested by setting theme in Preferences and restoring baseline 78CEFE76), Wombatish; all DEAD, nothing filed; 225 static-only rows before it, 123 picker rows; next main-list rows after 1950. Packages that need a library (dependencies.json) cannot be tested while the picker channel is empty: record as not testable.

- After batch 204 (2026-10-31, pushed): WooCommerce Autocomplete, WordCompletion, WordPress Code Reference, WordPress Generate Salts, WordPress Gutenburg Blocks Autocompletions; all DEAD, nothing filed; 220 static-only rows before it, 118 picker rows; next main-list rows after 1956. Five batches of the day (199-204 = 30 packages) done on release zips; the public channel_v4.json was still empty at the start of batch 204.

- After batch 205 (2026-10-31, pushed): WordPress i18n, WordPress Readme to Markdown (silently does nothing on Windows: regex needs a forward slash), WoW Macro Syntax, WoW XML Syntax (Lua scope never ends), Wrap U; all DEAD, nothing filed; 215 static-only rows before it, 113 picker rows; next main-list rows after 1961. NOTE: this session started 2026-10-30 21:34 local (03:34 UTC 10-31); it is not old. Eval with time.sleep runs on the main thread: keep sleeps under 3 s in total per call (a 5 s main-thread timeout hit once). get_sheets dumps all settings: use get_open_files instead.

- After batch 206 (2026-10-31, pushed): WrapStatement (dialog: dependency packages Statement/Expression missing), WriteGooder (needs npm write-gooder), Writing Color Scheme, Writing Style (breaks on the 3.14 host: sublime.Settings has __slots__ ['settings_id'], so setattr on the loaded settings raises; same cause as WeexTemplate in batch 200), Wux Weapp Snippets; all DEAD, nothing filed; 210 static-only rows before it, 108 picker rows; next main-list rows after 1969. Python 3.14 pattern to add to the list: setattr on sublime.Settings.

- After batch 207 (2026-10-31, pushed): X10Language, X3-Alpha Color Scheme, XMPFilter (does not work on Windows: /usr/bin/env, plus a NameError on shell), XQuery (snippet comment has stray backslashes), XUL and XBL (build 4215 with_prototype recursion dialog, known #6555); all DEAD, nothing filed; 205 static-only rows before it, 103 picker rows; next main-list rows after 1977.

After batch 208 (2026-10-31, pushed 3c3c968): XmlDocs (macro path xmldoc wrong), XssEncode (3 SyntaxWarnings), Xtend, Yaf Completions, YandexTranslate (needs API key). Next: rebuild list with make_list.ps1 + picker_split.ps1, take the next five picker rows after YandexTranslate.

After batch 209 (2026-10-31): YandexWiki, Yang Syntax Highlighting, Yate, YetAnotherCodeSearch (two TypeErrors without a project, record only), Yii2 Snippets. 88 picker rows left. Next: rebuild list (make_list.ps1 + picker_split.ps1 in scratchpad 95abb597), next five picker rows after Yii2 Snippets (Yosys is next).

After batch 210 (2026-10-31): Yosys (Script syntax newline bug), ZPL Syntax, Zen Language (loads Zig settings), Zen2Han, ZenScript; all DEAD, record only. Picker rows may be nearly exhausted (the list after ZenScript, main row 1996, was not checked); rebuild with make_list.ps1 + picker_split.ps1 and take the next picker rows, else move to the non-picker rows.

After batch 211 (2026-10-31): Zenoss, Zeus, Zimpl (top-level # comment not scoped), Zurb Foundation (default zip_url 404), Zurb Foundation 4 Snippets; all DEAD, record only. Next: rebuild list (make_list.ps1 + picker_split.ps1 in scratchpad 95abb597), next five picker rows after main row 2006.

CORRECTION 2026-10-31: the empty picker was the portable's own channels override (v4 only); removed, picker works (4728). From batch 213 install through the picker again; batch 212 was installed from zips before the fix. See feedback_portable_channels_override_2026_10_31.md.

After batch 212 (2026-10-31): Zurb Ink Snippets, apiDoc Autocompletion, cFos ml syntax, cexio-ticker (API now 301, traceback on every load), cfengine_beautifier (parsetab.pickle write inside zip). All DEAD, record only. Picker works again: batch 213 onward install through Install Package. Next: rebuild list (make_list.ps1 + picker_split.ps1 in scratchpad 95abb597), five picker rows after main row 2014.

After batch 213 (2026-10-31, picker installs): cheat_sh (requests lib installed without urllib3, plugin cannot load; Package Control side, tell Donald in one line), chester-atom, choo snippets, coala (prereq, thread traceback), cocos2dx js api. All DEAD. Next: rebuild list (make_list.ps1 + picker_split.ps1 in scratchpad 95abb597), five picker rows after main row 2020.

After batch 214 (2026-10-31, picker): codic (requests without urllib3 again), colorToVal (unsaved-view TypeError), cp2k-syntax (linter disabled by SublimeLinter), devebkit (list_of_attributes AttributeError), doTjs (embedding does not close). All DEAD. Tip: get_console mode=captured with tail 5 only; a pattern argument is not supported and the console is large. Next: rebuild list, five picker rows after main row 2027.

After batch 215 (2026-10-31, picker): dotsyntax (Windows directory walk never ends), eScript Syntax, eZ Publish Syntax, eco, esoftplay. All DEAD. Faster method: one batch call = pick, three eval time.sleep(2.5), run_command install_package, get_quick_panel with wait_ms 20000 and limit 3; fuzzy matches return several rows, pick the exact trigger index. After the last removal wait, then check installed_packages in the User Package Control settings for a stale name. Next: rebuild list, five picker rows after main row 2032.

After batch 216 (2026-10-31, picker): ferm Syntax, fibjs Completions, fido (per-folder fido never fires), file-downloader, fundamentals Snippets. All DEAD. Next: rebuild list, five picker rows after main row 2037.

After batch 217 (2026-10-31, picker): gamY (unsaved-view TypeError in both switch commands), gislacks (two modal dialogs without the Go tool), gmESSI-Tools, greybeard theme, i3 wm. All DEAD. Next: rebuild list, five picker rows after main row 2045.

After batch 218 (2026-10-31, picker): iA Writer (mac only, bytes env TypeError), iCalendar, iconfont snippets, img-placeholder (find() logic bug), industrial-coding-theme. All DEAD. Next: rebuild list, five picker rows after main row 2052.

After batch 219 (2026-10-31, picker): jEdit Color Theme, jolie (folder install), jrnl (3.3 host, I/O dialog), jsimports (unsaved-view TypeError), knitr (folder install). All DEAD. About 39 picker rows left. Next: rebuild list, five picker rows after main row 2060.

After batch 220 (2026-10-31, picker): lay-out Syntax, lebab, lessy (TabError, cannot load), lioshiTheme (folder install), multiAlign. All DEAD. Stale installed_packages lines again after the chained removals (fixed by hand): after the last removal ALWAYS read the Package Control settings and the Packages folder before recording. About 34 picker rows left. Next: rebuild list, five picker rows after main row 2070.

After batch 221 (2026-10-31, picker): myPDDL (folder), nRepeat, naomi-syntax, neko nml syntax, ng-snippets. All DEAD, nothing filed. About 29 picker rows left. Donald interrupted with: retest Limitcode (may be updated, at least in repo); do that, then resume: rebuild list, five picker rows after the last done row.

Limitcode retest done 2026-10-31 (note project_limitcode_retest_1_1_13_2026_10_31). Resume: rebuild list (make_list.ps1 + picker_split.ps1), five picker rows after batch 221's last row; about 29 picker rows left.
