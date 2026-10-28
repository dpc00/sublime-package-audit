---
name: no-messages-json-comma-prs-2026-10-14
description: Donald 2026-10-14: do not open PRs that only remove a trailing comma in messages.json; other fix PRs may be fine once the PR pause ends; plain issues are still fine
metadata:
  type: feedback
---

On 2026-10-14 a maintainer (spthiel, KeeMeng/MKB-Syntax-Highlighting#2) answered my one-line messages.json trailing-comma PR with "The audacity to generate this minuscule fix with Claude". Donald replied himself and concluded: "should not do PRs for ',' removal in messages.json. The rest might be fine."

**Why:** a one-character PR on an inactive repo reads as noise and clogs his account (1000+ issues already); it draws hostile replies with his name on them. The 10 messages.json PRs from the 2026-10-13 fix pass are already open; leave them, do not chase them.

**How to apply:** never open a PR whose whole change is a trailing comma (or similar one-character JSON tidy) in messages.json; report it as a short issue instead, as before. The general PR pause ([[stop-prs-if-bot-mail-continues-2026-10-14]]) still stands until he says go. Real code fixes with a test on the portable (for example FileTabRename#3, merged 2026-10-14) are the kind that may resume then.
