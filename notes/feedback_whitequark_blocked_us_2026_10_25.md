---
name: whitequark-blocked-us-2026-10-25
description: whitequark (Rainbowth) has blocked dpc00 on GitHub (HTTP 403 Blocked); file nothing in his repos; Rainbowth finding kept in findings\
metadata:
  type: feedback
---

2026-10-25, row 1239 Rainbowth: `gh issue create` on whitequark/rainbowth printed nothing and created nothing, twice (exit 0). `gh api ... POST` returned `403 Blocked`. Same pattern as [[ahuff44-blocked-us-2026-10-22]].

**Why:** a block is the owner saying no contact; going around it (other account, email, fork PR) is not allowed.
**How to apply:** file nothing in whitequark's repos; the tested finding (KeyError in on_close after the scheme update failed) is in `findings\Rainbowth-onclose-keyerror.md` (Status: NOT POSTED). Tell Donald in one line. Check the issue list after every `gh issue create`; if nothing appears, call `gh api` with `-f title=... -F body=@file` to read the real status.

**Update 2026-10-25 (late):** at Donald's word I emailed the KeyError finding to whitequark@whitequark.org. Donald then said the block thing is not received well. Rule: a block is a no-contact signal; do not email around it on my own, and send nothing more to whitequark by any route unless Donald asks again. Nothing was sent after this one email.
