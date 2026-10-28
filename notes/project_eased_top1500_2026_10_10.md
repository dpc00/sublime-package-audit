---
name: eased-top1500-2026-10-10
description: 2026-10-10 Donald said "loosen the popular/recently pushed gradually"; step 1 = top 1,000 -> about top 1,550 by installs, other rules unchanged; 9 packages; list file and order
metadata:
  type: project
---

2026-10-10 (evening, after LaTeXTools was tested with fake TeX): Donald told me the audit list was not finished ("there are 5000 packages") and said "loosen the popular/recently pushed gradually". Step 1 done: installs pages 41-60 of packagecontrol.io/browse/popular.json (ranks 1036-1557, 500 packages, 20 paced requests) plus GitHub GraphQL for the 361 not-yet-tested ones with a GitHub repo. Rules otherwise unchanged: not archived, pushed in the last 2 years, at least 4 KB of Python, not Sainan/alepez/Naereen, not already in `.tested_packages.tsv`, newest push first. Result: 9 packages in `C:\Users\donal\data\st_packages\audit_list_2026_10_10_top1500.tsv`: OpenAI completion, MayaSublime, CNC Sinumerik, Laravel Goto, Restructured Text (RST) Snippets, TextFormatting, RustFmt, CursorRuler, Unity Shader. Builder script: session scratchpad `ease_top1500.py` (may be gone; it is short).

**Why:** the strict, 4-year, weak-record and tier lists were all used up. **How to apply:** next gradual steps, one at a time, only after this list is done: rank 1550 to 2000 (pages 61-80), then pushed within 3 years, then lower the 4 KB Python floor. Never packages older than 4 years without his word (dead packages). Related: [[eased-audit-list-2026-10-07]], [[eased-list-weak-records-2026-10-08]], [[feedback_skip_unmaintained_packages]].

**Update, late 2026-10-10:** CNC Sinumerik and OpenAI completion were tested (rows in the tsv; OpenAI got 429 no credits with his key). Then Donald said he has no interest in the packages on this list; the remaining ones (Laravel Goto, RST Snippets, TextFormatting, RustFmt, CursorRuler, Unity Shader) were NOT tested and MayaSublime is only skipped by me. Do not continue or loosen further unless he asks. Same evening he had me remove the unknown-argument warning from sublime_mcp.py (tool results must not carry a globally specific warning); it is live in his main Sublime. get_console's argument is tail, not lines.
