---
name: no-package-control-reports-2026-10-19
description: Donald 2026-10-19: never file issues or comments with Package Control (sublimehq/package_control, packagecontrol.io); #1805 was filed anyway and closed "not planned"
metadata:
  type: feedback
---

On 2026-10-19 Donald said I am never supposed to bother packagecontrol.io / Package Control, and that #1805 (sublimehq/package_control, "Root __init__.py is never extracted", closed "not planned" by deathaxe: "intended behavior") was not the first time. He also pointed at an email from kaste; I could not find a kaste mail in Gmail that day (only the #1805 close notification), so what kaste wrote is unknown.

**Why:** it annoys the maintainers (deathaxe, kaste); the audit has filed some 25 issues there (#1759-#1805). No earlier note in the notes folder stated this rule for the package_control repo itself, only the channel repo PR ban ([[feedback_channel_repo_pr_banned]]), which is why it kept happening.

**How to apply:** file nothing, comment nothing, open no PR in sublimehq/package_control or the channel repo, and do not touch packagecontrol.io. If an audit finding is really about Package Control's behaviour, put it in the audit notes and tell Donald in one line; he decides. Check this note before any `gh issue create`.
