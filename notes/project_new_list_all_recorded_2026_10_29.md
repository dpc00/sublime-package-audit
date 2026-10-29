---
name: new-list-all-recorded-2026-10-29
description: packagecontrol.io/browse/new has 219 pages (5452 packages); every one is already in our records; the filter must strip version suffixes; LSP helper install order
metadata:
  type: project
---

Donald (2026-10-29) asked to audit the packagecontrol.io "new" list ("over 220 items"). `https://packagecontrol.io/browse/new?page=N` runs to page 219 (25 per page, 5452 packages, newest first). Page 1 alone is the 25 newest.

**Result:** after normalising names, 0 of the 5452 are untested. Only Cremisi Color Scheme (first seen 2026-10-28) was new: installed, both schemes applied, removed (RESULTS row). The first filter said "196 untested" because RESULTS and `.tested_packages.tsv` record many names with a version suffix ("LSP-lean 1.2.5", "Typst 0.2.23", dated 2026-10-01 to 10-03); match names with the suffix stripped, case-insensitive, never by exact name. The 196 were all tested 2026-10-01..03. If Donald still sees about 220 new items, ask which page or filter he means (the page count is 219).

**Second look (same day, Donald: "over 220", page=10):** 140 of the 250 newest (pages 1-10) and 480 of all 5452 have NO result text in RESULTS.tsv or `.tested_packages.tsv`. Cross-checked the 140: 130 are covered by a section in `data\.package_skill_test_log.md` (heading "## Name (date)") or an issue we filed; 10 had no evidence anywhere and were tested 2026-10-29: Copy Python Import, Theme - Timeless, LSP-oxlint, LSP-oxfmt, LSP-zuban (needs uv; none here, server not started), SublimeLinter-contrib-oxlint, LSP-wren-lsp, LSP-pawnforge, LSP-nsis, LSP-gh-actions (the last four only work with Wren, AMX Mod X Pawn, NSIS and YamlPipelines installed; all four then passed). Nothing filed (hold). The other 340 of the 480 (pages 11-219) were not cross-checked against the log yet.

**LSP helper packages:** install `LSP` first, then the helper, then restart the portable once (the helper fails to import with `No module named 'LSP'` otherwise and is not reloaded). LSP-ltex-ls-plus 1.1.1 then starts (259 MB server in Data\Package Storage, 180 files) and underlines misspellings. Stop the server (java under Package Storage) before recycling its folder.

**Session facts:** my Claude session runs in the main Sublime tab named after the conversation ("Email responses, merged issues stats"); `/mcp reconnect sublime-mcp-portable-4215` is typed there with ui_type_text then ui_press_key Return (post). sublime-mcp's consent prompt refused `close_file discard` and `run_command exit` with "no elicitation support" although the client declares elicitation (bug log B11). Close the portable with CloseMainWindow instead.
