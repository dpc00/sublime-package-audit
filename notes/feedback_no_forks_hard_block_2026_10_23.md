---
name: no-forks-hard-block-2026-10-23
description: forks of other people's code on his GitHub are never wanted; six new forks appeared after the 2026-10-14 cleanup; deny rules added to settings.json
metadata:
  type: feedback
---

2026-10-23: Donald found forks on his GitHub again. I had told him "none" without checking; `gh repo list dpc00 --fork` showed 6, all made after the 2026-10-14 cleanup of about 73. His words: "They clog up my github with other people's code. Never desirable, never should have ever come about." Maintainers who ask for a PR (commitment#5, SublimeCloseOldestFile#1) are not a reason to fork.

**Why:** a fork is only made to open a PR; he cannot afford the clutter and has never made a PR.

**How to apply:**
- `C:\Users\donal\.claude\settings.json` now denies `gh repo fork`, `gh pr create` (PowerShell and Bash) and the github MCP `fork_repository` / `create_pull_request`. Do not work around it; he lifts it himself.
- When a maintainer asks for a PR, post a short "Claude reports:" reply saying the tester cannot make PRs and the fix is in the issue text (sent to SublimeCloseOldestFile#1 on his order).
- Before saying what is on his GitHub, run `gh repo list dpc00 --fork`; never answer from notes.
- Deleted 2026-10-23: sublimetext-cakephp, sublime-mit-alloy, sublime-exact-quick-find, json_stringify. Left: ColorHelper (PR #285) and Sublime-Text-Advanced-CSV (PR #59), each with an open PR; deleting a fork closes its PR.
