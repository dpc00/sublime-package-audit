# Sublime package audit: notes for Claude

What this is: a way to find bugs in **sublime-mcp** by driving real Sublime Text through it while
exercising packages. When something is broken, file the issue with the package's repository — that issue
is the record.

The whole procedure is `.claude/skills/sublime-package-audit/SKILL.md`. Read it before a batch.

## The rig (read this before touching an editor)

- Four portables exist under `C:/Users/donal/tools/`: `st_portable` and `ST-portable-4215-omp-1`,
  `-omp-2`, `-omp-3`. Any could be driven; **the audit uses `st_portable`**, because the baselines,
  hashes and every recorded result belong to that instance.
- `st_portable` = MCP server `sublime-mcp-portable`, `http://127.0.0.1:9512/sse` (`mcp_port: 9512`,
  `http_port: 9510`). The `-omp-*` instances declare 9542 / 9552 / 9562 — leave them alone.
- Before a test call: confirm the port in `Data/Packages/User/MCP Commander.sublime-settings`, then
  confirm `list_native_windows` reports the hwnd you just launched.
- Record both `Data/Packages/User` settings hashes before installing; after removing, the same two
  hashes must match again. One window at a time.
- Verified 2026-11-08: all four bind their own ports (9512/9542/9552/9562), `MCP Commander` 1.18.4
  junction to this repo, `require_consent_for_destructive: false`, `install_py33_helper: true` with
  `MCP Commander Py33` present, and `installed_packages` matching `Installed Packages` exactly. A
  new instance needs the same five checks before it may be used.

**No scripts in this repository, ever.** Any job that would have been a script is a step in that skill.

The files, all of them:

| file | what it is |
|---|---|
| `RESULTS.tsv` | one row per package: name, date, one-line result |
| `ISSUES.tsv` | one row per issue filed: repository, number, title, state, dates, link |
| `data/tested_packages.tsv` | one row per package: what stops a package being tested twice |
| `data/do_not_file.tsv` | repositories that must not receive reports |
| `data/open_asks.tsv` | follow-ups waiting on a maintainer |
| `data/st_io_packages.tsv` | installability per Sublime HQ channel entry (a shopping list, not a ledger) |
| `data/untested_installable_2026_11_03.tsv` | the 258 offered-for-Windows/ST4 packages the bulk pass had not tested |
| `data/channel_pc.json` | cache of the Package Control channel, so the queue can be read offline |
| `ALIASES.tsv` | package names the live channel proves share one repository |
| `README.md`, `PROCEDURE.md`, `LICENSE` | the public description and method |
| `.claude/skills/` | the procedure and the traps, as skills |

## Git

Exactly one commit; amend it, never append: `git add -A`, `git commit --amend --no-edit`,
`git push --force-with-lease origin main`.
