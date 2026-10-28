---
name: new-releases-2026-list-2026-10-10
description: 2026-10-10 evening, replacement for the rejected top-1550 list: packages released in 2026, real Python, not archived, nothing needing popups/pointer/native dialogs/paid tools; 5 tested, 2 skipped by Donald
metadata:
  type: project
---

After Donald said he had no interest in the top-1550 list ([[eased-top1500-2026-10-10]]), he asked for a different set. Rule he gave: stay away from packages that exercise things sublime-mcp is not successful at (popups, real-pointer clicks, hidden panels, native dialogs) and anything needing paid or heavy outside software. I built the set from `channel_v3_2026_10_08.json`: any release dated 2026, not in `.tested_packages.tsv`, GitHub repo, at least 4 KB of Python, not archived, not Sainan/alepez/Naereen: 25 packages (script in session scratchpad `new2026.py`).

**Tested (all logged in the tsv and log):** Reform (no defects), Task List (legend inserts with no newline, minor), iRules (no defects), Exact Quick Find (ignored on 4200 because .python-version is 3.14, works on 4215; issue aafulei/sublime-exact-quick-find#4 filed with his OK), LSP-cspell (works after the portable's broken mdpopups library was replaced). CNC Sinumerik and OpenAI completion came earlier from the rejected list (OpenAI: 429 no credits with his key).

**Skipped at his word:** LSP-Deno and sublime-github ("skip both, not interested"). Not offered: Laravel Goto, MayaSublime, BeyondCompare, LSP-lean, Phpcs, themes.

**How to apply:** do not continue this list or loosen a new one unless he asks. Test files `C:\Users\donal\tools\reform_test` are still there (only recycle on his word). Related: [[verify-removal-before-exit-2026-10-10]].
