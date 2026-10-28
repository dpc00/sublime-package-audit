---
name: pr-queue-length-one-2026-10-26
description: HIS DECISION - maintainer PR requests are handled one at a time, in the order received; one fork exists at a time; delete it when merged or after a reasonable wait, then take the next
metadata:
  type: feedback
---

Donald, 2026-10-26, after saying that maintainers asking for PRs was making him ill ("I can't fork all that stuff"): "Handle one PR at a time in order request received; if it gets merged or doesn't merge in a reasonable amount of time, delete the fork and move on to the next one. A queue, length one."

**Rule:** at most ONE fork and ONE open PR at any time. Requests are taken in the order they were received. When the PR is merged, or no merge happens in a reasonable time, delete the fork (this closes the PR) and take the next request. The rest wait; nobody gets a reply that asks him to do anything.

**Why:** the number of PR requests overwhelmed him (heart condition, emergency-room worry). A queue of one bounds the work and the bot mail. This lifts the 2026-10-14 PR pause and the no-forks block only in this form; it does not allow a second fork.

**How to apply:**
- Work from the queue file he has open ("Community PR requests"); keep the order; mark each entry done, merged or timed out.
- Fork into `C:\Users\donal\tools\forks`, never into projects (pybackup runs `git add -A` there).
- "Reasonable time" (his answer, same day): the same length of time the maintainer took to respond to the original issue. Measure it from the issue's creation to the maintainer's comment asking for the PR; the PR gets that long from the day it is opened.
- He has no queue file; I build the queue myself from GitHub (my issues with a maintainer comment asking for a PR), in order of the maintainer's comment date. The "Community PR requests" tab in his IDE was incidental.
- The deny rules for `gh repo fork` and `gh pr create` in `~\.claude\settings.json` are his guardrail; they need his OK to change.
- Do not read or label his email for this; he declined that on 2026-10-26.
- STATUS 2026-10-26: not started. He postponed it ("let's do it later", going out for food) and wants a better queue design first. Draft queue of 15 open requests was built from GitHub (oldest: rawsp33d/sublime-xpath#47, colinta/SublimeSimpleMovements#4, SublimeLinter javac#25, cppcheck#25, tslint#46). Open points: timeout floor (I suggested 7 days), removal of the fork/pr deny rules in settings.json. Do not fork or open a PR until he says go.
- Related: [[stop-prs-if-bot-mail-continues-2026-10-14]], [[no-forks-hard-block-2026-10-23]], [[fix-request-means-pr-2026-10-16]].
