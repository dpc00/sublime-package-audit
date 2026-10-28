---
name: stop-prs-if-bot-mail-continues-2026-10-14
description: Donald 2026-10-14: PR bot mail (CodeRabbit, Codex, Microsoft CLA) is intimidating junk; if my PRs keep generating it, stop opening PRs; supersedes "fix and PR without asking" until he says go
metadata:
  type: feedback
---

On 2026-10-14 four GitHub notification mails arrived on my PRs (CodeRabbit on sublime-run-command#4, Codex review on DistractionFreeWindow#38 and SublimeText-Nodejs#114, Microsoft CLA bot on OmniSharp/Kulture#41). Donald found them "way intimidating", deleted them and said: "If your PRs continue to generate this crap, then you should stop doing them."

**Why:** the bot comments are inherent to PRs on repos that run review/CLA bots, and they land in his inbox with his name on them. He cannot judge them and they stress him.

**How to apply:** no new PRs from the undefined-name/fix-batch pass until he says go again (the "fix and open the PR without asking" rule in procedures.md is paused). Fixes can still be prepared locally in projects\<repo>. Never reply to bot comments or agree to a CLA for him; tell him in one line which PR needs a CLA. See [[never-reply-to-github-notification-mail]].
