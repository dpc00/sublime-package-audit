---
name: ahuff44-blocked-us-2026-10-22
description: ahuff44 (sublime-fish-tank) has blocked dpc00 on GitHub (HTTP 403 Blocked); file nothing in his repos; FishTank fix kept in findings\
metadata:
  type: feedback
---

2026-10-22, row 364 FishTank: `gh issue create` on ahuff44/sublime-fish-tank printed nothing and created nothing (exit 0); `gh api` showed `403 Blocked`. The owner has blocked the account, although he accepted an earlier report (#3, closed).

**Why:** a block is the owner saying no contact; going around it (other account, email, fork PR) is not allowed.
**How to apply:** file nothing in ahuff44's repos; keep the tested finding in `findings\FishTank-empty-tank-st4.md` (Status: NOT POSTED) and say so in the report. Lesson for the rig: `gh issue create` can exit 0 with no output when blocked; check the issue list after every create.
