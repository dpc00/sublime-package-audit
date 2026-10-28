---
name: issue-body-file-race-2026-10-24
description: Ledger issue #3 went out with the LangDocs body because Write failed and gh ran in the same message on a stale file
metadata:
  type: feedback
---

2026-10-24: I sent `Write` (issue body to `ld1.md`) and `gh issue create --body-file ld1.md` in one message. `Write` failed ("file has not been read yet", the name existed from an earlier session), `gh` ran anyway and posted the old LangDocs text as the body of moeffju/sublime-ledger-syntax#3. I replaced it with `gh issue edit 3 --body-file` within a minute and read it back.

**Why:** a failed Write does not stop a parallel PowerShell call; the stale file is posted publicly.

**How to apply:** one call at a time for issue filing: Write the body to a NEW unique file name (package + date), wait for success, then run `gh issue create`, then read the issue back with `gh issue view --json body`. Never batch the Write and the `gh` call.
