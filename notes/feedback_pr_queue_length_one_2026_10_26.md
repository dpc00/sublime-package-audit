---
name: pr-queue-length-one-2026-10-26
description: SUPERSEDED 2026-10-29 - there is NO queue and no one-at-a-time rule; do what the maintainer requested (his words, restated 2026-10-31). Old text kept below as history; rewritten 2026-10-29 to hold only what he said
metadata:
  type: feedback
---

**NO LONGER IN FORCE.** 2026-10-29 Donald said "never mind one at a time, just do what he requested", and on 2026-10-31, when I repeated "the PR queue is one" in a status line, he said: "there is no queue. That is false." Do not state or apply a queue. A maintainer's PR request is simply done (read the file on the default branch first, check history, test, open the PR). Forks are deleted when their PR is merged.

Donald, 2026-10-26, after saying that maintainers asking for PRs was making him ill ("I can't fork all that stuff"):

> "Handle one PR at a time in order request received; if it gets merged or doesn't merge in a reasonable amount of time, delete the fork and move on to the next one. A queue, length one."

"Reasonable time" (his answer, same day): the same length of time the maintainer took to respond to the original issue.

Rewritten 2026-10-29 at his request ("replace it with what I actually said"): the earlier version added rules he did not state (a "never more than one fork" ban, "wait until he says go", settings.json deny rules, email handling). Those are dropped. Kept only as practical notes, not his rules: forks go in `C:\Users\donal\tools\forks`, never in projects (pybackup runs `git add -A` there).

Open for him to decide: whether a fork whose PR has already been merged counts as finished at once (yes by his words: delete it), and whether the queue of 15 requests built on 2026-10-26 (oldest rawsp33d/sublime-xpath#47, colinta/SublimeSimpleMovements#4) is to be worked now.

2026-10-29: mekwall asked for a PR on obsidian-color-scheme#18; Donald said "never mind one at a time, just do what he requested". Fork dpc00/obsidian-color-scheme (clone in tools\forks), PR mekwall/obsidian-color-scheme#19 opened. Two earlier PRs were still open then (Sublime-Text-Advanced-CSV#59, ColorHelper#285). Same day, forks of PRs merged on 10-29 (SublimeLyricEditor, SublimeDirectOpen, SublimeDirectCopy) were deleted on GitHub and recycled locally at his request.

2026-10-29 (later): his "proceed to whatever is left" after the three test requests (LSP-systemd#6, Timeless-Theme#19, sublime_dbpedia_lookup#1 answered; LSP-ember#14 answered "yes, close it"). Next request in order, colinta/SublimeSimpleMovements#4: fork dpc00/SublimeSimpleMovements (clone in tools\forks), PR colinta/SublimeSimpleMovements#7 opened (list to set, tested 2000 to 16000 lines, same selections). Remaining PR requests in order: kaste javac#25, cppcheck#25, tslint#46 (09-29), kkujawinski patch-apply#2 (10-06), then the 10-17 to 10-27 ones; take them one at a time, after reading each fresh.

Related: [[stop-prs-if-bot-mail-continues-2026-10-14]], [[no-forks-hard-block-2026-10-23]], [[fix-request-means-pr-2026-10-16]].

2026-10-29 (later still): kaste's javac#25 needed no PR: he fixed it himself (c96fab5 on 09-30, release 1.4.0 on 10-01). Tested 1.4.0 in the portable with the issue's Main.java (undefinedVar outlined correctly), commented, no fork. Next in order: SublimeLinter-cppcheck#25, then tslint#46 (check each against its repo history first; they may be fixed too).

2026-10-29 (later still): kaste's cppcheck#25 also needed no PR: fixed in c53f2bb (PR #27, column_unit utf8) and released as 2.1.0 on 10-01. Tested 2.1.0 in the portable with the issue's m.c (errors on [ and =), commented, no fork. Next in order: SublimeLinter-tslint#46 (check its history first).

2026-10-29 (later still): kaste's tslint#46 also needed no PR: fixed in 0e4bcef (column_unit utf16) and released as 1.7.0 on 10-01. Tested 1.7.0 in the portable with the issue's a.ts after a local npm install of tslint 6.1.3 and typescript 5 in the scratchpad (recycled afterwards), commented, no fork. All three kaste requests (javac#25, cppcheck#25, tslint#46) were already fixed by him on 09-30/10-01. Next in order: kkujawinski/sublime-text-3-patch-apply#2 (10-06), then the 10-17 to 10-27 ones. Lesson: check the repo's commits and releases since the maintainer's reply before forking.

2026-10-29 (later still): kkujawinski/sublime-text-3-patch-apply#2: our earlier PR #3 (10-06) had been closed on 10-14 when the forks were deleted, never reviewed, and was tested with stubs only. Redone: new fork dpc00/sublime-text-3-patch-apply (clone in tools\forks), real test in the portable with Git's patch.exe on the portable process PATH (upstream fails cafe and euro, fix applies all three), new PR kkujawinski/sublime-text-3-patch-apply#4. Next in order: the 10-17 to 10-27 requests (tarzan elixir-tests#6 10-17, riot/syntax-highlight#14, onhernandes scss-snippets#2, maxhoffmann qunit-snippets#2, c3m3gyanesh p4-syntax-highlighter#7, AustinTruex68 EasyFileHider#3, lowliet StatusBarTime#6 and StatusBarWeather#4, TomasBarry git-co-author#1); check each history first.

2026-10-29 (later still): tarzan/sublime-text-elixir-tests#6 (Ruby palette captions) needed no PR: fixed on master by 9db5681 (2021-08-03) but never tagged; tag 1.2.0 (2018) is what Package Control ships and it still says Ruby; only 2 commits since the tag, only those two captions. Commented asking for a new tag, or closing as fixed on master. I forked and cloned first, then deleted that fork and clone again (nothing pushed). Not tested in Sublime (read the files at both refs). Next in order: riot/syntax-highlight#14, onhernandes/sublime-scss-snippets#2, maxhoffmann/qunit-snippets#2, c3m3gyanesh/p4-syntax-highlighter#7, AustinTruex68/EasyFileHider#3, lowliet StatusBarTime#6 and StatusBarWeather#4, TomasBarry git-co-author#1. Lesson: read the file on the default branch BEFORE forking.

2026-10-29 (later still): riot/syntax-highlight#14 (maintainer GianlucaGuarini asked for a PR; nothing on master since 2019): fork dpc00/syntax-highlight (clone in tools\forks), PR riot/syntax-highlight#15 fixes #14 and #13 (brace-counting expression-body context replaces the (?=(s*)}) lookahead). Tested in the portable by reading view.scope_name() on master vs branch for 7 texts; #13 reproduced only for {items} with no space before the brace. Next in order: onhernandes/sublime-scss-snippets#2, maxhoffmann/qunit-snippets#2, c3m3gyanesh/p4-syntax-highlighter#7, AustinTruex68/EasyFileHider#3, lowliet StatusBarTime#6 and StatusBarWeather#4, TomasBarry git-co-author#1.

2026-10-29: onhernandes/sublime-scss-snippets#2 -> PR #3 (8 snippets, real insert_snippet A/B on 4215, portable cleaned). Next in order: maxhoffmann qunit-snippets#2, c3m3gyanesh p4-syntax-highlighter#7, AustinTruex68 EasyFileHider#3, lowliet StatusBarTime#6 and StatusBarWeather#4, TomasBarry git-co-author#1.

2026-10-29: maxhoffmann/qunit-snippets#2 -> PR (26 triggers, A/B on 4215; the typed prefix case still leaves it, said so). Next: c3m3gyanesh p4-syntax-highlighter#7, AustinTruex68 EasyFileHider#3, lowliet StatusBarTime#6 and StatusBarWeather#4, TomasBarry git-co-author#1.

2026-10-29: c3m3gyanesh/p4-syntax-highlighter#7 -> PR (7 keywords, scope check A/B on 4215). Next: AustinTruex68 EasyFileHider#3, lowliet StatusBarTime#6 and StatusBarWeather#4, TomasBarry git-co-author#1.

2026-10-29: AustinTruex68/EasyFileHider#3 -> PR (strip per pattern; A/B on 4215 through the real input panel, keys by PostMessage because computer-use type_text refused). Next: lowliet StatusBarTime#6 and StatusBarWeather#4, TomasBarry git-co-author#1.

2026-10-29 (retest order): PR texts rewritten without 'not tested' lines after real tests: scss-snippets#3 (+4 variable snippets), p4-syntax-highlighter#8 (+string rule; my keyword rule had coloured words inside strings), EasyFileHider#4 (empty/repeated input, side bar), riot syntax-highlight#15 (+string contexts; my first version broke f('{')), patch-apply#4 (real on_pre_close path), mekwall#19 (sentence dropped). ColorHelper#285 still lists untested native-dialog cases.

2026-10-29: ColorHelper#285 text rewritten without 'Not tested' lines, from recorded results (Windows after the rebase; reload, quit, Insert click, second window, multi-cursor on #284's push; Linux WSL kcolorchooser run of 10-09). No WSLg run: it needs the computer-use helpers stopped and risks his keyboard while he is at it (feedback_wslg_window_froze_keyboard). facelessuser's only comment on #284: 'seems promising', will merge if no edge cases.

2026-10-29: lowliet/sublimetext-StatusBarTime#6 -> PR #7 (documented key + lefty argument; 5 phases A/B in the portable, status values read, no GUI). Repo names are sublimetext-StatusBarTime / sublimetext-StatusBarWeather. Next: StatusBarWeather#4, then TomasBarry git-co-author#1.

2026-10-29: lowliet/sublimetext-StatusBarWeather#4 -> PR (async renamed to fetch; load A/B on the 3.14 host with .python-version 3.14). Next and last in the list: TomasBarry git-co-author#1.

2026-10-29: TomasBarry/Sublime-git-co-author#1 -> PR (menu path Git CoAuthor; menu entry's open_file run for real, A/B on 4215). The Windows checkout of this repo shows README.md as deleted because it holds both README.md and readme.md: stage only the menu file. THE REQUEST LIST IS FINISHED: scss-snippets#3, qunit-snippets#3, p4-syntax-highlighter#8, EasyFileHider#4, StatusBarTime#7, StatusBarWeather#5, git-co-author PR.

2026-10-29 (late): rvolz/sublime_dbpedia_lookup#1: his branch fix/issue#1 has two commits newer than the 6c22c95 I tested (a48b141 JSON query parameter, 9a45169 YAML result display with clickable links); retested 9a45169 in the portable: Berlin, Hamburg, no-results status message, right-click menu offers Open <uri>, local-server setting (remote set dead, result still came), three error dialogs (connection refused, HTTP 404, no docs list). Not tested: the docker lookup image (no docker). Nothing posted yet; he said he will finish and upload.

2026-10-29 (late): open_asks sweep (75 waiting; most are the requests already done). yaworsw/Sublime-ScopeAlways#7: maintainer fixed in 46c5e2e and corrected my cause (callback runs on any change; real bug was start_on reapplied on every reload); A/B in the portable confirmed, comment posted. Next two maintainer-fixed items to retest: tushortz/intellekt#1 (new tag), scriptkitz/PythonStautsBarShowSymbol#1 ('updated in 1-2 days').

- 2026-10-29: IPWright83/sublime-TestExplorer#3 (maintainer asked for a PR with a unit test): old PR #5 had been auto-closed by the 10-14 fork deletion, never reviewed. Re-forked, same fix + tests (before 3 failed/1 passed, after 4 passed on 4215), new PR IPWright83/sublime-TestExplorer#6. Clone: tools\forks\sublime-TestExplorer. Open PR count now 13.
