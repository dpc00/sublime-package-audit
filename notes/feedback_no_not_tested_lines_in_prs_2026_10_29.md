---
name: no-not-tested-lines-in-prs-2026-10-29
description: Donald does not want "not tested" / "did not test" lines in PR texts; test the case and put the result in the table, or leave out what is not part of the change
metadata:
  type: feedback
---

Donald, 2026-10-29, after the EasyFileHider#3 PR: "clean up your testing, so that I don't see any 'didn't test' output. retest!"

**Why:** a "Not tested: ..." line is an open question handed to the maintainer. Retesting those cases found real defects in my own PRs: the new keyword rule in the P4 grammar coloured words inside strings, and the riot brace-counting change broke `f('{')`, which `master` handled. Both fixed and pushed.

**How to apply:**
- Before opening a PR, list every case you would otherwise write as "not tested" (empty input, repeated input, strings and comments, the real UI path such as the input panel, side bar, close handler) and run them in the portable, original against fixed. Put the results in the table.
- Do not write sentences about files or platforms that the change does not touch ("I did not test the iTerm2 files"); say which file is changed instead. Say where it was tested ("Windows, build 4215") rather than listing what was not.
- If a case cannot be run at all (macOS), say where it was tested, in one positive sentence.
- Keys into an input panel: computer-use type_text refused when the window lost focus or he was typing; PostMessage WM_CHAR plus Return to the portable's window handle worked without touching his focus (`post_keys.ps1` pattern in the scratchpad). Put `C:\Program Files\Git\usr\bin` on PATH for the test process when a plugin shells out to `patch`.

ColorHelper#285 had such lines too; rewritten the same day from recorded results of the earlier tests (Windows, and the WSL Linux run of 10-09), labelled with the push they were run on. No new WSLg run: it needs the computer-use helpers stopped and once froze his keyboard.

Related: [[feedback_test_trouble_is_focus_or_his_hands_2026_10_29]], [[feedback_pr_queue_length_one_2026_10_26]].
