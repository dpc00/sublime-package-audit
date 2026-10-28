---
name: stuck-picker-say-what-you-wait-for-2026-10-14
description: 2026-10-14: I left the Install Package picker open and silent for 2 minutes; rule: confirm the list loaded before picking, check any picker after 20 s, and say what I am waiting for
metadata:
  type: feedback
---

On 2026-10-14 I called `pick_quick_panel` for GoImports before the Install Package list had loaded; the call stalled, was moved to the background when he wrote, and I then waited for its notification (about 2 minutes, 300 s timeout) without telling him anything. The panel stayed open and unfiltered in portable 4200; he deliberately did NOT fix it himself (it is my mess to clear; I closed it later with Escape). He said: "you went to install something, then abandoned mini-picker... 2 mins went by with no notice to me of what you were doing."

**Why:** he watches the screen; a stuck panel with no word from me looks like I abandoned it, and he ends up doing my recovery.

**How to apply:** (1) before `pick_quick_panel`, run `get_quick_panel` with limit=1 and wait_ms=15000 to confirm the list loaded; (2) if a pick or any wait is not done in about 20 s, look at the screen, press Escape to close the panel, and say so; (3) never sit waiting for a background notification without one line saying what I am waiting for; (4) a stuck call is my job to clear, not his; he refuses to do my recovery, and he says it is too hard for him to judge what to do, so I decide and say it in one line. Related: [[feedback_confirm_enter_before_typing_name_2026_10_11]], [[feedback_clean_portable_overlays_and_tabs]].
