# Sublime Text package audit (2026)

Donald Chitester (dpc00) with Claude (AI agent driving Sublime Text through [sublime-mcp](https://github.com/dpc00/sublime-mcp)). Counts to 2026-10-30.

## Records (`RESULTS.tsv`)

| measure | count |
|---|---:|
| rows (test records, retests included) | 7246 |
| distinct package names | 5748 |
| packages with more than one row | 1447 |
| rows that are a static file check only (2026-10-27, nothing installed or run) | 1408 |
| packages whose latest row is a static check only (NOT live-tested yet) | 248 |
| packages whose latest row is "not installable" (repository gone, download 404) | 86 |
| packages whose latest row is "not tested" (not offered in the picker) | 9 |

## Issues (`ISSUES.tsv`)

| measure | count |
|---|---:|
| issues filed | 3096 |
| repositories | 2177 |
| open | 2235 |
| closed | 846 |
| repository no longer readable | 15 |
| closed within a week | 453 |
| days to close, median / mean | 5 / 25.2 |

Open/closed split as of 2026-10-30; closed does not mean fixed.

## Pull requests (GitHub, author dpc00)

| state | count |
|---|---:|
| merged | 50 |
| open | 11 |
| closed, not merged | 78 |
| total | 139 |

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
| known mistake | 2026-10-27 static check replaced live testing for 1408 records and the audit was wrongly called complete; corrected 2026-10-29, live retest of the 248 in progress |

## Files

| file | what it is |
|---|---|
| `PROCEDURE.md` | the method |
| `.claude/skills/sublime-package-audit/SKILL.md` | the method as an agent skill (needs [sublime-mcp](https://github.com/dpc00/sublime-mcp)) |
| `RESULTS.tsv` | one row per test record: package, date, result |
| `ISSUES.tsv` | every issue filed: repository, number, title, state, dates, link |
| `lists/` | the package lists worked through |

MIT, see `LICENSE`.
