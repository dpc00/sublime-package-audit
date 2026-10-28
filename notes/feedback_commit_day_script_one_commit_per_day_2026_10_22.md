---
name: commit-day-script-one-commit-per-day-2026-10-22
description: audit repo history is one commit per day; at batch ends and when stopping run tools\commit_day.ps1 (amends the day's commit and force-with-lease pushes); never commit by hand there
metadata:
  type: feedback
---

On 2026-10-22 I committed the audit results by hand ("Audit results and filed issues for rows 337-358") and asked whether to push, then claimed there was no one-commit-per-day rule. Donald: "It is not my fault that you have forgotten that. It is in session transcripts from days ago."

**Why:** Donald's order of 2026-10-20: the repo keeps one commit per day, "Audit log through <date>". The first run after midnight creates it, every other run that day amends it. It is written in the sublime-mcp-audit skill ("Where things are") and in the header of `tools\commit_day.ps1`.

**How to apply:** in `C:\Users\donal\projects\sublime-package-audit`, at every batch end and when he says wrap or stop, run `tools\commit_day.ps1` (it does `git add -A`, amends, and pushes with `--force-with-lease`; this is his standing routine, so no second permission for the push). Never `git commit` there by hand. `rec.ps1` and `finish.ps1` only change files. Search the skill and `tools\` before saying a rule does not exist. See [[session-baton-2026-10-21-fresh-list-batch4]].
