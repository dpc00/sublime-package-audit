---
name: test-trouble-is-focus-or-his-hands-2026-10-29
description: When a portable test misbehaves it is probably window focus or Donald's own input; test from clean state, prefer file-based runners, leave nothing behind
metadata:
  type: feedback
---

Donald, 2026-10-29, after the EasyFileHider#3 test went wrong several times: "If something goes wrong, it is probably 1) window focus 2) user jerking things around, trying to keep up." Also "dialog, and you typed into the buffer", "It is complex, user is interfering. Retest", and "Please clean up your testing."

**Why:** computer-use type_text returned no_viable_candidate or interrupted whenever the portable lost the foreground or he touched the keyboard; a Save Changes dialog left by my runner took my typing into the buffer; the first panel run started from settings an earlier run had written.

**How to apply:**
- Prefer a file-based runner that needs no typing (set views scratch so closing never raises Save Changes). Only use the GUI for what has to be real (an input panel): front.ps1, then `post_keys.ps1`-style PostMessage (WM_CHAR then Return) worked when computer-use refused; scratchpad copy only, not in a repo.
- Before each run restore Preferences from the backup and recycle any User\<package>.sublime-settings the command wrote; read the result from the saved file.
- When a dialog may be up, look first (screenshot_window), dismiss it, then continue; never type blind.
- After the last test check the portable's User folder too, not only Packages: 10-27 residue (ANSIescape, HighlightToken, Log Highlight, MySFTP) was still there and was recycled today.

Related: [[feedback_refocus_test_window_myself_2026_10_28]], [[feedback_clean_up_after_each_test_2026_10_11]].
