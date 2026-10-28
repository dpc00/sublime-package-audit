---
name: no-premature-issues-2026-10-11
description: 2026-10-11 Donald: do not file an issue until the cause is proven by a retest and he has said so; two NinetyFive issues were filed on guesses
metadata:
  type: feedback
---

On 2026-10-11 I filed numerataz/sublime-plugin #25 (stale reply text, "lass") on a theory; Donald said the stray text came from his auto-approve keystroke landing in the focused window, and had me close it. Then I filed #26 (console window flashes per keystroke, no CREATE_NO_WINDOW) before checking the flashing stopped with my local fix; he said "don't file any more premature issues!".

**Why:** a wrong public issue costs the maintainer's time and his name; a keystroke artifact from his own auto-approve tool looks like a plugin bug.

**How to apply:** reproduce, apply and verify the fix with him watching, rule out artifacts of my own test setup (his auto-approve injects "1"/Enter into the focused window; my typing helper; stray focus), and only then ask him before filing. Issues can only be closed, not deleted, by him or me ([[feedback-check-existing-issues-before-filing]], [[feedback-one-issue-per-finding]] still apply once he agrees).

**CORRECTION (his words, same night): "I just asked that you defer filing until tests were all done on the package and you had confirmed your findings ... Besides that only pertained to one package, an odd one (NinetyFive), not to any others."** The rule is NOT "ask before every issue". Normal rule for every other package: finish the tests, confirm the finding against the tool/source (no test artifacts), then file (after checking for existing issues, one finding per issue, short plain text). When issues are disabled, email the commit address (format: start "Claude reports:", no greeting/thanks/signature) and show him the exact text first ([[limitcode-email-misread-2026-10-07]]). I over-generalised this and held back the GDScriptFormatterLinter finding for no reason.
**Related lesson (flog, same night):** when a test hits a defect, FINISH the proof (read the host's source, run the tool by hand, test the fix) and then file; stopping at "unconfirmed, not filed" made him say "you just run into a bug, and do not do what is correct? Why is my faith sagging?". flog#3 was filed after reading SublimeLinter's normalize_filename.
