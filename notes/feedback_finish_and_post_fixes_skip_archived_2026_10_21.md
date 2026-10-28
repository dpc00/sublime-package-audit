---
name: finish-and-post-fixes-skip-archived-2026-10-21
description: His standing order 2026-10-21: for a real defect write the fix, test it, post it as a comment on the issue, no second permission; skip archived packages; no forks/PRs without asking once
metadata:
  type: feedback
---

**Date:** 2026-10-21. I found the Vue grammar bug (Vuejs Complete Package, open issue #3 for 9 years) and Babel Snippets' dead class-body selectors, wrote the fix down and did not publish. He: "I do not understand why you do something then do not follow through with a fix that you publish... You are sickening. On again off again. Waste no more time and effort. If you think it will help someone, go through with it." Also: "Skip archived ones."

**Why:** the older rules (post nothing outward 2026-10-20, no forks/PRs 2026-10-14) made me stop halfway; he reads that as pointless work.

**How to apply:**
- Real, reproduced defect: write the fix, test it live, then post evidence + tested fix as a comment on the existing issue (or a short new issue), "Claude reports:", update the `findings\` file Status to POSTED with the link, log in RESULTS.
- Do not ask again per finding. Do not flip back to "write it down and stop".
- Skip archived repos (GitHub rejects comments there). The list already excludes 303 of them (`audit_list_2026_10_21_archived*.tsv` in data\st_packages).
- Forks and PRs: still ask once before the first one (bot mail upset him 2026-10-14); a comment with the exact change is the default.
- First case: babel/babel-sublime-snippets#10 comment 6327510586 (selector `source.js meta.class.js meta.block.js - meta.function`, tested). Vue (#3) could not be posted: archived.
