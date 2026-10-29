---
name: open-asks-tool-2026-10-29
description: tools\open_asks.ps1 lists open issues of ours whose last comment is not ours (who is waiting on us); run on demand, read-only; first run 82 of 2166
metadata:
  type: reference
---

Donald, 2026-10-29: "I am not keeping good enough notes. I have to rely on you and your 'gh' skills." So the answer to "who wrote back?" is a tool, not memory.

`tools\open_asks.ps1` reads ISSUES.tsv (refresh it first with `tools\reconcile_issues.ps1`), fetches the last comment of every open issue (GraphQL, 25 per query, about 90 calls) and writes `data\open_asks.tsv` (date, author, repository, number, title, first line, url), newest first. Last comment by someone other than dpc00 = they are waiting on us or have had the last word. An issue where we wrote last is not listed (for example ice/sleet#1 after our 10-27 test comment).

First run 2026-10-29: 82 of 2166 open issues. Top authors: Jah-yee 20 (not looked at), deathaxe 4, kaste 4, oleg-shilo 4. Several are maintainers saying "send a PR" (mekwall#18 was then done as PR #19, InsertNums#35 got a fix comment).

Read-only against GitHub, on demand only (no scheduled polling, see his 2026-10-07 rule). Does not cover PRs or email; pull requests: `gh search prs --author dpc00 --state open`.
