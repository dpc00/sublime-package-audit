---
name: confirm-enter-before-typing-name-2026-10-11
description: 2026-10-11 Donald: after pressing Enter on Package Control: Install Package, confirm by screenshot that the package list is showing before typing the name key by key; detect failed key presses
metadata:
  type: feedback
---

When I drove the Install Package picker on a freshly started portable (Theme - Sone, 2026-10-11), the first Return and every letter returned `no_viable_candidate`: the palette stayed on the typed text "Package Control: Install Package" while I sent the name. Donald watched it and said: you have to detect that; do not enter the name key by key until you have established that Enter took effect.

**Why:** key presses to a just-started or unfocused window silently fail (`no_viable_candidate`, `interrupted`), so typing the name does nothing and looks like a forgotten Enter.

**How to apply:** after `Return`, wait for the list, take a `get_window_state` image and check the package list is showing; only then type the name. If the tool says `no_viable_candidate`/`interrupted`, click the AXTitleBar, `get_window_state`, and retry. Same check for the Remove picker. Written into `.claude/skills/sublime-mcp-audit/SKILL.md`. See [[feedback_popup_clicks_need_real_pointer_and_front_2026_10_10]] for other focus traps.
