---
name: protractorninja-account-gone-2026-10-26
description: ProtractorNinja's GitHub account and the SPARC-sublime repo (package SPARC Assembly) returned 404 on 2026-10-26, hours after we filed #4 and commented on #1; cause unknown; nothing more to file
metadata:
  type: project
---

2026-10-26: Donald reported that ProtractorNinja's repo had disappeared. Checked: `gh api users/ProtractorNinja` and `gh repo view ProtractorNinja/SPARC-sublime` both return 404 / "could not resolve"; no redirect (a rename would redirect), so the account was deleted or suspended, by the owner or by GitHub. Cause unknown; do not guess.

What we had there (package SPARC Assembly, tested 2026-10-26): issue #4 (opcode list misses bicc, fbfcc, cbccc, ticc, ta) and a comment with a tested fix on existing issue #1. Both are gone with the repo; the rows in `ISSUES.tsv` (lines 2712-2713) still say open.

Forks still on GitHub: avivkiss/sublime-sparc, jxchrixt/SPARC-sublime (not examined; ours were never forks).

**How to apply:** file nothing about it (the channel entry now points at a dead repo; no reports to package_control, his rule). If it comes up, say plainly that the repo vanished the same day as our report and that the cause is not known. Mark the two ISSUES.tsv rows as "repo gone 2026-10-26" when that file is next edited. Related: [[whitequark-blocked-us-2026-10-25]], [[no-package-control-reports-2026-10-19]].
