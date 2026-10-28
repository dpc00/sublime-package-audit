---
name: session-baton-2026-10-27-queue-done-hold
description: START HERE (newest, audit): retest queue finished (479 rows), HOLD on all public GitHub action, emails-only redesign, mass closures, next = main audit row 1739
metadata:
  type: project
---

**State at the end of 2026-10-27**
- Retest queue (`data\retest_queue_2026_10_26.tsv`) is FINISHED: rows 1-479 recorded in RESULTS.tsv (now 4211 rows, last column `line` = its own line number). Rows after 392 were read-only records, nothing filed.
- HOLD (Donald: "too dangerous, sensitive toes"): no issues, comments, closes, reopens, PRs or forks on anyone's repo. Only exception granted: the fix comment on sublimelsp/LSP-copilot#322 (rchl asked for a fix after my automated close comment).
- Redesign (his): findings go to `findings\` and RESULTS.tsv only; at most ONE short email to a maintainer with a link to RESULTS.tsv#L<line>; never email an owner we already filed an issue on or exchanged mail with (so none of the existing 3010 issues). No email text approval needed. `tools\maintainer_mail_list.ps1` builds recipients for future findings. No email was sent.
- Same day: ~450 of our issues closed by us (99 on archived/old repos, 350 with no reply in 30 days). 3 were reopened by maintainers (RemoveDuplicateLines#32, Modelines#20, pretty-edn#8). Four maintainers said they no longer maintain the package (StatusBarWeather#4, StatusBarTime#6, git-co-author#1, glualint#9). Nothing posted back.
- README numbers refreshed (3950 packages, 3010 issues, 2167 open, 828 closed, 15 gone).
- Portable's `http_basic_auth` token line removed (ledger line added); repositories empty.
- Filing gate `tools\file_gate.ps1` is in HOLD mode (returns RECORD-ONLY for all).

**Next**
- Main audit resumes at row 1739 "Tcsh and Csh Mode", record-only (local testing and RESULTS.tsv; no GitHub action) unless he lifts the hold.
- Unanswered for Donald: the amclain note, SimpleCov transfer offer, what "binary logic at 9GHz" meant, whether to push the sublime-mcp Lean proof commit 366c135.

**Update, later 2026-10-27:** the main list (rows 1739 to the end) is finished by a static pass only (tools\auto_static.ps1, nothing installed or run, nothing filed): 322 rows recorded, 15 flagged in data\auto_static_flags.txt (Python 2 code, bad XML or JSON; not verified live). Row 1739 Tcsh and Csh Mode was a real install test. Hold on GitHub and email still in force. Repaired a RESULTS.tsv damage from multi-line checker output (backups in the session scratchpad). Next: nothing queued; wait for his word.

**Decision 2026-10-27 (Donald):** SimpleCov transfer offer (Kevin Yank): not taking it, Ruby is outside his repertoire. No action, no reply unless he asks me to draft a one-line decline. NetLinx also dropped (see feedback_amclain_file_nothing_2026_10_27).

**Correction (2026-10-27, Donald):** the hold covers GitHub only (no issues, comments, closes, PRs, forks). EMAIL IS ALLOWED under his redesign: one short email per maintainer, link to RESULTS.tsv#L<line> in the audit repo, no text approval needed, never to an owner we already filed on or exchanged mail with. Send only for a defect CONFIRMED in a real test on a live repo (pushed within 3 years, not archived); parse-only flags are not enough. Earlier lines saying email was on hold were wrong.
