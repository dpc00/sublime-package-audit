# Sublime Text package audit (2026)

Donald Chitester (dpc00) with Claude (AI agent driving Sublime Text through [sublime-mcp](https://github.com/dpc00/sublime-mcp)). Counts to 2026-11-05.

## Packages (`RESULTS.tsv`)

| measure | count |
|---|---:|
| packages tested (latest row shows a run, install or load; retests not counted) | 5384 |
| packages not tested | 455 |
| — not installable | 102 |
| — repository gone | 136 |
| — no GitHub repository link | 63 |
| — not offered or skipped | 100 |
| — static check only (NOT live-tested yet) | 37 |
| — read-only review, nothing run | 17 |

`data/untested_installable_2026_11_03.tsv` lists the 258 packages that Package Control offered for Windows/ST4 but that the 2026-10-27 bulk pass had not tested. 204 of them have since been dealt with — 185 tested live, and 19 shown to have no release for build 4215 in the ST4 channel, so they never appear in the Install Package picker — leaving 54 that are still offered and still untested.

Eight packages whose tests predate the 2026-10-27 bulk pass are counted as tested after checking their earlier rows and filed issues; that pass's "not tested" placeholder had overwritten them. Package Control alone has 26 issues.

This table reads `RESULTS.tsv` only. Tests recorded in the session log or `ISSUES.tsv` but never written to `RESULTS.tsv` are not in it, so the tested count is a floor and the not-tested count an upper bound.

## Issues (`ISSUES.tsv`)

| measure | count |
|---|---:|
| issues filed | 3137 |
| repositories | 2198 |
| open | 2276 |
| closed | 846 |
| repository no longer readable | 15 |
| closed within a week | 454 |
| days to close, median / mean | 5 / 25.1 |

Open/closed split as of 2026-11-05; closed does not mean fixed. `ISSUES.tsv` has 3139 rows: 2 are duplicate log rows for the same issue (3137 distinct issues).

## Pull requests (GitHub, author dpc00)

| state | count |
|---|---:|
| merged | 53 |
| open | 9 |
| closed, not merged | 81 |
| total | 143 |

## Kinds of defect found

| kind | example |
|---|---|
| name not defined or misspelled | [fight-color-scheme#1](https://github.com/ghyatzo/fight-color-scheme/issues/1), [Theme-AquaSoda#2](https://github.com/Astramata/Theme-AquaSoda/issues/2), [sublime-syntax-edgeos#2](https://github.com/lojoja/sublime-syntax-edgeos/issues/2) |
| setting or command that points at nothing | [NoDialogs#8](https://github.com/maximsmol/NoDialogs/issues/8), [Aethra#1](https://github.com/vlasikhin/Aethra/issues/1) |
| snippet or key that never fires | [StrapdownJS-Boilerplate#1](https://github.com/sonokamome/StrapdownJS-Boilerplate/issues/1) |
| behaviour differs from the README | [sublime-ExpandGroup#5](https://github.com/evanliomain/sublime-ExpandGroup/issues/5), [SublimeTypoScriptr#1](https://github.com/kitzberger/SublimeTypoScriptr/issues/1) |
| output written to the wrong place | [sublime-danmakufu#3](https://github.com/drakeirving/sublime-danmakufu/issues/3), [sublime_dbpedia_lookup#2](https://github.com/rvolz/sublime_dbpedia_lookup/issues/2) |
| command fails on an unsaved tab | [DXL#6](https://github.com/Adarma/DXL/issues/6), [sublime-text-dxr#1](https://github.com/snorp/sublime-text-dxr/issues/1) |
| package cannot be installed (no releases) | two packages |

## Test setup and limits

| item | value |
|---|---|
| machine | one, Windows 11 |
| Sublime Text | portable 4200 (retired 2026-10-20) and 4215, Python 3.14 plugin host |
| Linux / macOS | not tested |
| `requests` / `bs4` packages | not testable (library install lacks `urllib3`, `typing_extensions`); nothing filed |
| test length | brief; "no defects found" means none seen in short real use |
| reports | written by the AI agent, marked "Claude reports:" |
| maintainers who asked not to be written to | respected; email instead where issues are disabled |
| known mistake | [Theme-Treble#1](https://github.com/53v3n3d4/Theme-Treble/issues/1) first report corrected after a retest |
| known mistake | 2026-10-27 static check replaced live testing for 1408 records and the audit was wrongly called complete; corrected 2026-10-29; 37 packages still have only a static check |

## Files

| file | what it is |
|---|---|
| `PROCEDURE.md` | the method |
| `.claude/skills/sublime-package-audit/SKILL.md` | the method as an agent skill (needs [sublime-mcp](https://github.com/dpc00/sublime-mcp)) |
| `RESULTS.tsv` | one row per test record: package, date, result |
| `ISSUES.tsv` | every issue filed: repository, number, title, state, dates, link |
| `lists/` | the package lists worked through |

MIT, see `LICENSE`.
