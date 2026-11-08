# Sublime Text package audit (2026)

Donald Chitester (dpc00) with Claude (AI agent driving Sublime Text through [sublime-mcp](https://github.com/dpc00/sublime-mcp)). Counts to 2026-11-09.

## Packages (`RESULTS.tsv`)

These are the ledger figures. `RESULTS.tsv` holds one row per package — 5,693 of them, of which 5,185 carry a conclusion. A retest or a correction replaces that package's row; it never adds a second one. Rows merged on 2026-11-07 are in `data/duplicates_merged_2026-11-07.tsv`.

`data/st_io_packages.tsv` is **not** a second ledger. It is a shopping list built for a different purpose (installability per channel entry), it covers 4,843 channel entries — 4,612 marked tested, 231 pending — and an audited package may be absent from it entirely. Do not reconcile the two: when the question is "how much of the audit is done", the answer is the table above.

| measure | count |
|---|---:|
| packages tested (latest row shows a run, install or load; retests not counted) | 5453 |
| packages not tested | 439 |
| — not installable | 102 |
| — repository gone | 136 |
| — no GitHub repository link | 56 |
| — not offered or skipped | 97 |
| — static check only (NOT live-tested yet) | 31 |
| — read-only review, nothing run | 17 |

This split is the 2026-11-07 figure and is unchanged: every row added since is a retest of a package already counted, so no package moved between the two lines. Only the row and conclusion counts above moved.

`data/untested_installable_2026_11_03.tsv` lists the 258 packages that Package Control offered for Windows/ST4 but that the 2026-10-27 bulk pass had not tested. 212 of them have since been dealt with — 194 tested live, and 18 shown to have no release for build 4215 in the ST4 channel, so they never appear in the Install Package picker — leaving 46 that are still offered and still untested.

Eight packages whose tests predate the 2026-10-27 bulk pass are counted as tested after checking their earlier rows and filed issues; that pass's "not tested" placeholder had overwritten them. Package Control alone has 26 issues.

This table reads `RESULTS.tsv` only. Tests recorded in the session log or `ISSUES.tsv` but never written to `RESULTS.tsv` are not in it, so the tested count is a floor and the not-tested count an upper bound.

## Provenance (`ALIASES.tsv`, `data/unresolved_resolution.tsv`)

Package names are not identities; repositories are. `ALIASES.tsv` lists the package names that the live channel (`packagecontrol.io/channel_v3.json`) proves share one repository, so they are counted once. `data/unresolved_resolution.tsv` records what happened to names that no longer appear in the channel: matched after normalisation, matched by GitHub repository search, ambiguous, or no match at all. A name in the record that resolves nowhere is still an entry — it just is not evidence of a package that exists today.
What the 792 names that left the channel turned out to be: 8 matched after normalisation, 107 matched a GitHub repository of the same name, 68 share their name with several repositories and stay unresolved, and 609 match no repository at all. Full detail in `data/unresolved_resolution.tsv`. Fifteen duplicate names are listed in `ALIASES.tsv`, eight of them cases where the same package was recorded twice because one copy had UTF-8 mojibake (`Inglês` and `InglÃªs`).


## Issues (`ISSUES.tsv`)

| measure | count |
|---|---:|
| issues filed | 3202 |
| repositories | 2231 |
| open | 2299 |
| closed | 888 |
| repository no longer readable | 15 |
| closed within a week | 475 |
| days to close, median / mean | 5 / 24.4 |

Counts to 2026-11-10, each recomputed from the file by one rule. Open/closed split after the 2026-11-08 sweep of all 2,301 rows that were open; closed does not mean fixed. `ISSUES.tsv` holds 3,208 rows — 3,202 with a link, the rest recorded as unfiled because the repository has issues disabled or is archived.

That sweep found 36 newly closed, 33 as completed and 3 as not planned (Ennosuke/PHP-Codebeautifier#7, NotSqrt/SublimeLinter-contrib-dennis#2, SublimeText/Pywin32#12), and 0 unreadable repositories. Two more came from mail: 23maverick23/sublime-jekyll#100 closed as completed on 2026-11-08 (fixed in 6216c14), and allejo/sublime-language-bzw#2 was already recorded closed without a date, now 2026-11-09 (0d3b018; its sibling #1 the same day in 622e893). TheClams/PasteAsColumn#2 was closed as completed on 2026-11-09 (fixed in 1.0.1).

Two rows were corrected on 2026-11-10 and pushed with the record: lindskogen/RandomHEXColor#1 is closed, withdrawn by the reporter — the package is correct (`Region.begin()` is `min(a, b)`, so both selection directions take the replace branch) and the original observation was a harness artifact — and orgmir/mint-sublime-text#2 was filed and withdrawn the same night: its premise, that TextMate XML under a `.sublime-snippet` name never loads, was falsified by test (an unscoped one expanded; a `source.python` scoped one expanded only in a `.py` buffer), so the 18 snippets are fine and #1's syntax failure is the whole defect.

Also on 2026-11-10, from mail: b3ni/Sublime-Fabric#14 closed as completed by the maintainer's own PR #15 (`2850ede`, three files +17/−14), which fixed the Unix `find` search with `os.walk` and, in the same code, reversed task output (`_output_end` never advanced), tasks silently dropped (`zip` over `len(f)`, the path, instead of `len(ft)`), and the missing comma in `messages.json`. Re-checked from master on 4215 / Windows: a nested `fabfile.py` is now returned where the old code found none. The channel entry serves `zip/master`, so the fix reaches users without a release. Nine minutes later he merged a second PR, #16 (`de5f356`) — the root cause #15 had listed as out of scope: a `fab_path` setting plus virtualenv detection, closing #3 and #12 and leaving #11 open. That PR replaced `set_folders` with `configure(folders, fab_path, search_virtualenv)`, so the check was re-run against the new API (in plain Python — the wrapper imports only `os` and `subprocess`) and the nested fabfile is still found.

`ISSUES.tsv` records issues **filed**, not comments. 788 issues carry a dpc00 comment (111 of them in the 2026-10-25..30 window) and only their outcomes are tracked. One comment's outcome is worth a line because nothing else records it: [matthew-dumas/syntax_definition_helper#2](https://github.com/matthew-dumas/syntax_definition_helper/issues/2), a 2015 report about ST2 keymaps, was commented on 2026-10-27 and closed as completed by the maintainer on 2026-11-10 with no comment and no commit — the repository's last push is still 2014-01-09, so "completed" there is housekeeping, not a fix.

## Pull requests (GitHub, author dpc00)

| state | count |
|---|---:|
| merged | 56 |
| open | 16 |
| closed, not merged | 82 |
| total | 154 |

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
| file name Windows cannot create, so Package Control skips it (28 packages, 507 files, found by listing every release archive) | [Stylus-Snippets#3](https://github.com/billymoon/Stylus-Snippets/issues/3) — 310 of 495 files; [Linguist Syntax#1](https://github.com/hronro/sublime-linguist-syntax/issues/1) — `F*.tmLanguage` |
| `.sublime-*` file that is not valid JSON (32 packages, found by parsing every release archive) | [AGC Assembly#1](https://github.com/jimlawton/AGC-Assembly/issues/1), [On Save#6](https://github.com/wl879/SublimeOnSave/issues/6), [microbit Build System#1](https://github.com/stefanbates/sublime-micro-bit/issues/1) |

## Test setup and limits

| item | value |
|---|---|
| machine | one, Windows 11 |
| Sublime Text | portable 4200 (retired 2026-10-20) and 4215, Python 3.14 plugin host |
| Linux / macOS | not tested |
| `requests` / `bs4` packages | not testable (library install lacks `urllib3`, `typing_extensions`); nothing filed |
| test length | brief; "no defects found" means none seen in short real use |
| reports | written by the AI agent, marked "omp - deepseek v4 flash reports:" |
| maintainers who asked not to be written to | respected; email instead where issues are disabled |
| known mistake | [Theme-Treble#1](https://github.com/53v3n3d4/Theme-Treble/issues/1) first report corrected after a retest |
| known mistake | 2026-10-27 static check replaced live testing for 1408 records and the audit was wrongly called complete; corrected 2026-10-29; 35 packages still have only a static check |
| open question (2026-11-07) | the "static check only" figure above (31) does not match `RESULTS.tsv`: 180 rows carry the phrase, and 79 of them belong to repositories that already have a row in `ISSUES.tsv`, so a live test exists for them. Needs a per-row review against the issue, not a bulk rewrite |

## Files

| file | what it is |
|---|---|
| `PROCEDURE.md` | the method |
| `.claude/skills/sublime-package-audit/SKILL.md` | the method as an agent skill (needs [sublime-mcp](https://github.com/dpc00/sublime-mcp)) |
| `RESULTS.tsv` | one row per test record: package, date, result |
| `ISSUES.tsv` | every issue filed: repository, number, title, state, dates, link |
| `data/windows_invalid_paths_2026_11_09.tsv` | the 28 packages whose release archives ship file names Windows cannot create, with offender counts and what was filed |
| `data/json_parse_failures_2026_11_09.tsv` | the 32 packages whose `.sublime-*` files do not parse, with the error and what was filed |

MIT, see `LICENSE`.
