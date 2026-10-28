---
name: remove-package-picker-press-down-2026-10-13
description: Palette "Package Control: Remove Package": typing "Remove Package" can put "Remove Channel" first; press Down to move to the right entry and check the highlight before Enter; his fix, not yet tried by me
metadata:
  type: feedback
---

**The detail:** in the command palette, typing "Remove Package" can show "Package Control: Remove Channel" as the first (highlighted) entry. Pressing Enter then opens the wrong picker (remove a channel, not a package). I got around it by calling `run_command remove_package` and then `pick_quick_panel`, which adds steps and still lets me pick under the wrong list.

**His fix (2026-10-13):** a single Down-cursor keystroke moves the highlight from "Remove Channel" to "Remove Package".

**How to apply:** open the palette with the text, read the list (`get_quick_panel`) and look at which entry is highlighted; if it is "Remove Channel", send Down (`ui_press_key Down`), read the highlight again, and only then press Enter. Never press Enter without looking at which entry is highlighted. The same applies to any picker where the first match is a near-name of what is wanted.

**Status:** this is his instruction; I have not yet tried the Down-key sequence myself, so the first use should confirm it with a read of the list before Enter.
