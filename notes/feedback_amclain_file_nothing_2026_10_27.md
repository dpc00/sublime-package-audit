---
name: amclain-file-nothing-2026-10-27
description: amclain (sublime-netlinx #10) told us not to open issues unless we are users who actually ran the tool; file nothing more in his repos
metadata:
  type: feedback
---

2026-10-27: amclain closed sublime-netlinx#10 (NetLinx: Fix Indentation) as correct behavior. His words: run NetLinx Studio and the library before submitting; reports from source reading alone, by someone who is not an A/V professional using the tooling, are unacceptable; do not open issues on his repositories without being a user of them.

**Why:** the issue was a "Fix (not run)" from reading only, for software we cannot run.

**How to apply:** file nothing more in amclain's repositories. In general, do not file read-only findings for packages whose tooling we cannot run. Also: Donald answering a maintainer does not close a thread; read the thread before calling it handled (SimpleCov: Kevin Yank offered to transfer the repo to Donald, still unanswered 2026-10-27).

**Decision 2026-10-27 (Donald):** NetLinx Studio is not to be installed or tested. He finds the installer suspicious (could be malware; it also needs admin and the hardware to be useful), and the risk is not worth it. No note to amclain either. Findings file stays local.
