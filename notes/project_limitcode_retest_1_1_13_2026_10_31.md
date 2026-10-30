---
name: limitcode-retest-1-1-13-2026-10-31
description: 2026-10-31 Donald asked "retest limitcode (may be updated, at least in repo)": 1.1.13 tested on portable 4215; #11 #13 #14 #15 #17 fixed, #12 still by design; nothing filed
metadata:
  type: project
---

**Ask (2026-10-31):** "retest limitcode (may be updated, at least in repo)". Package Control and the repo both serve 1.1.13 (repo HEAD 90347e6, 2026-10-26). Installed through the Install Package picker on portable 4215, removed through the Remove Package picker, baseline verified, Packages\User\Limitcode (debug log folder) recycled. No keys, offline tool tests only (ToolManager run in a worker thread, see [[project_limitcode_full_test_2026_10_06]]).

**Where it stands:** PR #22 (mine) was closed not merged on 2026-10-07; the author took #11, #13, #14, #16, #17, #18 with co-author credit (1.1.9), did #19-#21 on his own, deferred #15 (done in 1.1.10, commit 693f1b0: edits go to the buffer, not saved) and closed #12 as by design.

**Live results on 1.1.13:**
- #11 fixed: wrong-indent fuzzy edit keeps `    if y:` / `        return 2`.
- #13 fixed: CRLF write gives `a\r\nb\r\n` on disk (no `\r\r\n`).
- #14 fixed: read past the end gives "Invalid range: start_line 99 is after the last line to read (1); the file has 1 lines."
- #15 fixed: edit with unsaved typing leaves the file on disk untouched (buffer only; new open issue #23 asks the same from the user side).
- #17 fixed: relative `d.py` read works.
- #12 unchanged by the author's decision (first of three identical matches replaced, success reported). Empty `old_str` still succeeds (agent argument check blocks it, not user-reachable).
- Not re-run: #16 text, #18-#21 chat/mock paths, new Llamafile provider (1.1.12), sticky scroll (1.1.13).

**Filed:** nothing (#12 is closed with a stated reason; no new defect found). Open issues #23 and #24 are the author's to answer.
