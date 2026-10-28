---
name: verify-removal-before-exit-2026-10-10
description: 2026-10-10: I quit a portable right after picking remove in the picker; Package Control had not finished, and on the next start it reinstalled OpenAI completion and Exact Quick Find; wait for the console line 'Removed package' before exit
metadata:
  type: feedback
---

On 2026-10-10 I removed OpenAI completion and Exact Quick Find on portable 4200 by picking them in the remove_package picker and then ran `exit` within seconds, without reading the "Package Control: Removed package" line. On the next start both `.sublime-package` files were back in `Installed Packages` (the installed list had not been updated yet, so Package Control reinstalled them), and OpenAI completion even raised its "Folder ... does not exist. Create it?" dialog. My logs had said "removed" for both: that was not verified.

**Why:** the picker only starts the removal; the file and the settings list are updated a moment later, and quitting in between leaves them half-removed.

**How to apply:** after picking a package in the remove picker, read the console for `Removed package "<name>"` (get_console captured, tail 3) and check `Installed Packages` before quitting or logging "removed". Related: [[feedback_diagnose_dont_retry_install_2026_10_07]], [[feedback_track_test_installs_2026_10_10]].
