---
name: no-idle-waits-use-computer-use-2026-10-22
description: Donald's order: never sit in ui_press_key wait_idle_s or short ScheduleWakeup waits for picker keys; use computer-use MCP instead
metadata:
  type: feedback
---

2026-10-22, during Clickability Velocity: Donald asked "why these long waits?" and then said "please don't do this. It is not worth it. If you have to, use computer-use MCP."

**Why:** `ui_press_key` method "input" refuses until he has been idle 8 s; my `wait_idle_s` of 60-120 made each Return/Down in the Install/Remove picker stall whenever he was at the keyboard. ScheduleWakeup also has a 60 s floor, far longer than a picker takes to load.

**How to apply:** tried same day: computer-use `press_key` on the portable returns no_viable_candidate (Sublime is custom drawn). What works with no waiting: `ui_press_key` method "post" for Return/Down in Install/Remove pickers (tested). Never `wait_idle_s`; no wakeup timers for picker loads, just screenshot and go. See [[feedback_always_computer_use_for_dialogs_2026_10_07]].
