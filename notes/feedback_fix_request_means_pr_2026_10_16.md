---
name: fix-request-means-pr-2026-10-16
description: When he says a maintainer wants a fix and tells me to do it, that already means fork, test and open the PR; keeping the patch local is useless to him
metadata:
  type: feedback
---

2026-10-16: wadetb asked on Sublime-Text-Advanced-CSV#58 whether Donald wanted the fix. Donald: "1 wants a fix. Try to do it." I fixed and tested it but held the PR back because of the PR pause. He answered "i just said make a pr, didn't I?" and then "what else would I mean? I don't use that myself." PR opened: wadetb/Sublime-Text-Advanced-CSV#59.

**Why:** he does not use these packages; a patch left in a clone helps nobody. A request to fix something a maintainer asked about is a request for the PR.

**How to apply:** on "fix it" for someone else's package: clone into tools\forks, fix, test for real on the portable, fork, push a branch, open the PR in the same go (short "Claude reports:" body, test evidence, "Fixes #N"). The general PR pause ([[feedback_stop_prs_if_bot_mail_continues_2026_10_14]]) still covers PRs nobody asked for; a maintainer's request plus his "fix it" is the exception. No comma-only messages.json PRs. See also [[project_session_baton_2026_10_16_redo_batch1]].
