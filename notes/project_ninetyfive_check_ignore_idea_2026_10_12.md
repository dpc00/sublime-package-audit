---
name: ninetyfive-check-ignore-idea-2026-10-12
description: 2026-10-12 NinetyFive runs git check-ignore on every keystroke on the main thread; tested fix idea (one long-running git check-ignore --stdin); Donald will decide around 9:00 a.m. next day
metadata:
  type: project
---

NinetyFive (numerataz/sublime-plugin) `on_modified` runs `git check-ignore <file>` per keystroke on the main thread (a new process each time; this is the console flash of #26). Its purpose: do not send ignored files to the server. It never runs `git status`, so pybackup's git-status cache (gitclasses.py, keyed on HEAD + index mtime) does not fit; pybackup's `ielist.py` (pathspec, gitwildmatch) could match the root .gitignore only, and Donald rejected mimicking git's file hierarchy ("too hard").

**Chosen direction (tested 2026-10-12, git 2.54 Windows):** keep ONE `git check-ignore --stdin -z -v -n` process running per repo. First answer 36 ms (startup), later 0.1-0.3 ms; nested .gitignore, `build/` and `!` rules are honoured. Gotchas proven: a rule starting with `!` in the -v output means NOT ignored; the process keeps old rules after a .gitignore edit, so restart it when an ignore file changes (or about once a minute). Test script was `scratchpad\ci_test.py` (temp repo, removed itself).

**Status:** nothing changed in NinetyFive. Donald (late night, "too complex for me at this time of the day") will look again about 9:00 a.m. 2026-10-12. Offer then: patch on a copy, test on a portable (flash stops, ignored files still blocked, .gitignore change takes effect). Do not file anything until he says ([[no-premature-issues-2026-10-11]]).

**POSTED 2026-10-12 (his "send it"):** proposal issue https://github.com/numerataz/sublime-plugin/issues/28 (measured 37 ms median / 93 ms max per edit vs 0.07 ms with one long-running process; offers a PR with a test or lets the maintainer implement; fail open/closed left to them). Upstream code checked first: check-ignore call unchanged. No patch written; wait for the maintainer (kevmo314 merges fast). Bench scripts: scratchpad ci_bench.py, ci_test.py.

**Comment posted on #28 (his "send it"):** alternative = plugin-owned rule (.95ignore file + never_send setting with default secrets list), git check optional. Waiting for maintainer.

**PR OPENED 2026-10-12 (his "go ahead"):** https://github.com/numerataz/sublime-plugin/pull/29 from fork dpc00/sublime-plugin branch persistent-check-ignore (dev clone data\dev
inetyfive, commit e63071c). New check_ignore.py (IgnoreChecker), listener change, on_post_save invalidate, 13 new tests (29 pass). MEASURED inside the plugin host (Python 3.8.12, build 4200): old git check-ignore 477 ms per call (and a console window flashes each call: my timing test caused 28 pops, apologised), new 0.2 ms. #26 (console flash) was therefore real. pytest was installed then removed (pip list identical to data\pip_before_pytest.txt). Maintainer kevmo314 must review; watch only when he asks. The .95ignore alternative comment is still on #28.

**MERGED 2026-10-12 21:58 UTC by kevmo314** as merge commit 2517c258: PR numerataz/sublime-plugin#29 (issue #28 closed with it). The clone C:\Users\donal\projects\ninetyfive can be removed when he says (his rule: clones go away after merge; deleting inside projects causes pybackup churn, so ask first). Local fork branch persistent-check-ignore also on dpc00/sublime-plugin.
