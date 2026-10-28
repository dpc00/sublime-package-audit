---
name: clean-up-after-each-test-2026-10-11
description: 2026-10-11 Donald: stop leaving test mess; remove my own test leftovers at the end of each package; admin deletes go through his tab 2 (admin cmd)
metadata:
  type: feedback
---

On 2026-10-11 (late) Donald said I was "leaving a mess, like in prior days"; clearing ~/tools by hand in Explorer was a struggle (admin granted, still refused).

**Why:** untracked leftovers cost him pain and time ([[track-test-installs-2026-10-10]], [[tools-cleanup-mistakes-2026-10-10]]).

**How to apply:**
- After each audited package, before reporting: remove what that test created (Package Storage folder, User settings I wrote, downloaded tools, clones) and say what went. Recycle Bin first (`Microsoft.VisualBasic.FileIO.FileSystem`); it can refuse ("not supported") on some folders, then `Remove-Item` is fine for a clean public clone with no edits of mine.
- Anything he did not make or I did not make this session: ask first. Never delete by exclusion.
- Admin deletes: WRONG method (corrected 2026-10-13, see end of file). Only for folders he names.
- Cleaned 2026-10-11: ~/tools now only ColorHelper, Digital, list-coding-agents, screenshot-mcp-fix, submarine (his keep list). Portable 4200 Package Storage still holds older test leftovers (Debugger, LSP-cspell, LSP-gh-actions, LSP-nsis, LSP-oxfmt, LSP-oxlint, LSP-pawnforge, LSP-tombi, LSP-yaml, LSP-zuban) and Installed Packages has LSP; 4215 has ColorHelper (his PR work). Not deleted: he has not named them.

**2026-10-13, HOW TO RUN ANYTHING AS ADMIN (Donald: I have done this over 10 times and keep forgetting; no console in a Sublime tab is ever elevated):** write the commands to a .ps1 file in the scratchpad, then run Start-Process powershell -Verb RunAs -ArgumentList '-NoProfile','-ExecutionPolicy','Bypass','-File','<that .ps1>'. Windows shows the UAC prompt; he clicks Yes; the script runs elevated and I read its result from a log file the script writes. Do this myself without asking for another method. Only for what he named. Never click 'Continue with automatic administrator rights' in an Explorer prompt, and first try to avoid admin (cmd rmdir /s /q worked for my own git clone). Earlier transcripts with examples: session 58e5f82e-cce8-4a1f-b955-0078a4100a57.

