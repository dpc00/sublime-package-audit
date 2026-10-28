---
name: update-audit-repo-at-every-opportunity-2026-10-22
description: HIS ORDER: update (commit and push) the package-audit repo at every opportunity; never leave changes uncommitted
metadata:
  type: feedback
---

2026-10-22, Donald: "just update the package-audit at every opportunity, don't drop the ball like this." I had left the gate erasure uncommitted and waited for his word.

**Why:** he cannot judge when a commit is wanted; unpushed changes in the audit repo are lost work.
**How to apply:** after any change to the audit repo (edits, deletions, new records), run `tools\commit_day.ps1` in the same go (one commit per day, amend plus force-with-lease push, as in [[commit-day-script-one-commit-per-day-2026-10-22]]). Do not ask first. Note: `notes/`, `tools/`, `data/` are in the repo's .gitignore (added in commit d4d6b32 on 2026-10-18 by an earlier session), so they are never in commits.
