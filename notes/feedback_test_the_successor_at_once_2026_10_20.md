---
name: test-the-successor-at-once-2026-10-20
description: when a package's README says it was superseded by another package, test that successor in the same go; Donald rebuked me for stopping after List LESS Variables
metadata:
  type: feedback
---

2026-10-20: List LESS Variables (row 870) says "superseded by sublime-list-stylesheet-vars". I logged the package and waited for "go"; Donald: "you do not immediately move to the supercession one? Come on." The successor (installed as "List stylesheet variables") gave three more defects (MaciekBaron/sublime-list-stylesheet-vars #22, #23, #24).

**Why:** the successor is the package users get now; it is part of the same test, not a new batch item.

**How to apply:** when a README, repo description or issue names a successor, fork or replacement, check its tested row, read its issues, and test it right after the original, in the same batch. Log it as its own row.

Same session, other rebukes: after a portable call hangs, retry the reconnect via my own tab before giving up, use computer-use in an emergency, check everything (windows, dialogs, screenshot) before the next step. Confirm an npm publish by reading the cmd tab, not by `npm view`.
