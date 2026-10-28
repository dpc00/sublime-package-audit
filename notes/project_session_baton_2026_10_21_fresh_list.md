---
name: session-baton-2026-10-21-fresh-list
description: START HERE (newest, audit): Donald ordered the audit list redone from the full Package Control channel with tested packages removed; fresh list data\audit_list_2026_10_21_fresh.tsv (3154 untested of 5450), nothing tested from it yet; older batons' open/parked lists are NOT the plan
metadata:
  type: project
---

**Date:** 2026-10-21. Donald rejected my status answer (it re-listed old parked items) and ordered: "start over with the package control list, eliminate previously tested packages". See [[dont-relist-old-parked-items-2026-10-21]].

## The plan
- Work down `data\audit_list_2026_10_21_fresh.tsv` in order (columns: order, installs_rank, pkg, repo, installs, last_modified, platforms). It is a copy of `C:\Users\donal\data\st_packages\audit_list_2026_10_21_fresh.tsv`.
- Built from today's channel_v3.json (5450 packages) minus 2296 already tested (matched in `.tested_packages.tsv`, `RESULTS.tsv`, test-log headings, transcript "Installed package" lines, previous names). Number 1 is HTML-CSS-JS Prettify, then Theme - Soda, 3024 Color Scheme, AngularJS.
- Still run the four-point already-tested check by eye before each package (substring hits can be wrong either way). The list of what was excluded and why is in the 2026-10-21 session scratchpad only (`excluded_2026_10_21.tsv`); rebuild with the same logic if needed.
- Testing started 2026-10-21 (see Updates below). Main Sublime only, rules in the sublime-mcp-audit skill ("Main Sublime only" section: post nothing outward, write findings to `findings\`).

## Do not do
- Do not use older batons' "open", "parked", "held" lists as a to-do. Mention an older item only if this or a later baton names it.

## Updates (same day)
- His rule 2026-10-21: SKIP ARCHIVED packages. 268 archived GitHub repos were removed from the list (audit_list_2026_10_21_archived.tsv in data\st_packages lists them, plus 49 whose repo no longer resolves, those stay on the list); list now 2640. Non-GitHub repos (386) were not checked: check archived status before testing one. Also dropped 207 with no Windows release (audit_list_2026_10_21_notinstallable.tsv). If the list is rebuilt with build_list.py (session scratchpad), re-apply the archived filter.
- Tested and logged so far from the fresh list: Seti_UI, Markdown Extended, Theme - Afterglow, Theme - Flatland, JavaScript & NodeJS Snippets, ReactJS, Vuejs Complete Package (its write-up is in findings\, GitHub refused the comment: repo archived), Boxy Theme (not installable). Next: Babel Snippets.


## Portable test Sublime (his order 2026-10-21, "to speed things up")
- Location: `C:\Users\donal\tools\st_portable` (copy of the installed build 4215; `Data` folder makes it portable). Own copy of Package Control and of the repo's MCP Commander (plain folder, not a junction; Package Control must not manage it, `installed_packages` there lists only Package Control; PC's own MCP Commander release is 1.3.2 without AGENT_GUIDE.md and was moved aside).
- Ports 9512 (MCP SSE) and 9510 (HTTP bridge), set in `Data\Packages\User\MCP Commander.sublime-settings`; the existing server entry `sublime-mcp-portable-4215` (~/.claude.json and .mcp.json) points at 9512. Tools: `mcp__sublime-mcp-portable-4215__batch` (ToolSearch select it). Start: `Start-Process C:\Users\donal\tools\st_portable\sublime_text.exe`; reconnect by itself or type `/mcp reconnect sublime-mcp-portable-4215` into the main tab (ui_type_text, then ui_press_key Return as a separate call).
- Use it for package tests instead of his main Sublime: no interruption of his typing, and themes can be applied there. The main Sublime keeps only his own setup. Keep only Package Control and MCP Commander installed in it between tests; remove test packages with the remove picker.
- Setup script and PC release zip are in the 2026-10-21 session scratchpad only.