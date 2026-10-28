---
name: report-oddities-and-typos-2026-10-12
description: 2026-10-12 Donald asked "you don't report oddities or typos?": file them too, as short factual issues, even when there is no visible effect
metadata:
  type: feedback
---

I filed the Hypeon typo (`var(neon_neon_orange)`) but passed over Candy Dark's `black1`-`black3` = "#" and JellyFish's nine empty-string globals as "cosmetic only", without telling the maintainers. Donald: "you don't report oddities or typos?"

**How to apply:** when a test shows a typo, an undefined or invalid value, a comment that contradicts the code, or placeholders left unfilled, file ONE short factual issue per package (list the lines, say plainly whether any visible effect was seen, do not claim one that was not proved, suggest the obvious fix, start "Claude reports:"). Check the repo's existing issues first. Design choices (muted palette, low-contrast comments) are not defects and are not filed. Filed 2026-10-12: rahulsharmagg/Candy-Dark#1, anubhavkrishna1/sublime-jellyfish#1. Related: [[no-premature-issues-2026-10-11]], [[keep-issue-text-short]].
