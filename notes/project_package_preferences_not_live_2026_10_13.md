---
name: package-preferences-not-live-2026-10-13
description: 2026-10-13 controlled test on portable 4200: a Preferences.sublime-settings in a package added while Sublime runs is never merged until restart (cause of Theme-Treble#1 white tab, MarkdownEditing#827); not yet filed in sublimehq
metadata:
  type: project
---

Donald (2026-10-13) told me to treat the Treble white tab as a real Sublime bug and investigate rigorously, with research. Result on portable 4200 (build 4200, Windows 11), test package files ZZTest1 (folder) and ZZTest2 (.sublime-package), both removed afterwards:

- `find_resources` lists the new package's `Preferences.sublime-settings` at once, but `load_settings('Preferences.sublime-settings')` and `view.settings()` return None for its keys.
- Still None after: waiting 20 s, rewriting the file, saving User Preferences, adding/removing the package in `ignored_packages`.
- After a restart both packages' values appear (also the rewritten value).
- After that restart, rewriting the same file at runtime IS picked up live (a2 to a3). So the failing case is only a package Preferences file that did not exist at startup.
- Control: a new package's own `Foo.sublime-settings` loads on demand at once; a new `Preferences (Windows).sublime-settings` is not merged either.
- Same symptom already reported: MarkdownEditing#827 (deathaxe called it an ST core bug, fix is restart); my 2026-10-09 comment on sublimehq/sublime_text#2099 (a related but different report) was answered by deathaxe with "Claude just copied my report and violated copyright" even though I credited him. No reply from me; do not argue.
- Not filed as a clean sublimehq issue yet; needs Donald's yes. Theme-Treble#1 maintainer asked "Windows inside a VM?"; answer is no (physical HP laptop), and it is not Windows-specific as far as tested here (not tried on macOS/Linux).

**Why:** this is the root cause behind the Treble report; the theme is only the visible victim.
**How to apply:** when a theme/package seems to ignore its own default settings right after install, restart before judging; for a report, cite this test, not deathaxe's wording.

**Update 2026-10-13, his yes:** filed sublimehq/sublime_text#7012 (my own test, credits MarkdownEditing#827) and answered the Treble maintainer on Theme-Treble#1 (not a VM, cause is the Sublime bug, optional base-rule change).
