# Sublime Text package audit

Every package in the Package Control channel, installed in Sublime Text on Windows and used the way a
person would use it. What breaks is reported to the maintainer; what holds up is recorded as clean.

Donald Chitester ([dpc00](https://github.com/dpc00)), with an AI agent driving Sublime Text through
[sublime-mcp](https://github.com/dpc00/sublime-mcp).

## How it works

1. **Install** the package from Package Control, in a portable Sublime Text that is thrown away after
   the test.
2. **Use it.** Open a file it is meant for, run its commands from the palette, press its keys, read
   the console. Check what it wrote, not just that it said ok.
3. **Record** one row in `RESULTS.tsv`. If something is broken and the project is maintained, file an
   issue and record it in `ISSUES.tsv`.

A test is a short session, not a suite. "Clean" means no defect was seen in real use — it is not a
proof of correctness.

## Reading the ledger

`RESULTS.tsv` — one row per test record: `package`, `date`, `verdict`, `detail`.

| verdict | meaning |
|---|---|
| `CLEAN` | exercised, nothing wrong found |
| `FILED` | defect found and reported; the issue number is in the detail |
| `FINDING-LEDGER` | defect found, nothing filed — usually the project is abandoned or has no issue tracker; the reason is in the detail |
| `FINDING-COMMENTED` | defect reported as a comment on an existing thread rather than a new issue |
| `KNOWN-FIXED` | defect confirmed fixed upstream (or in a release we can see) |
| `STALE-ROW` | an older record that no longer reproduces against the current release |
| `FIX-PUSHED` | we wrote the fix; a pull request or commit is named |

Rows written before 2026-11-11 predate the verdict column and still carry prose in the third field.

`ISSUES.tsv` — one row per issue filed: repository, number, title, state, dates, link.

## Scale

| | |
|---|---:|
| test records in `RESULTS.tsv` | 5.7k |
| packages tested live | 5.4k |
| packages not testable (gone, no release, no repository) | 439 |
| issues filed across 2.2k repositories | 3.2k |
| pull requests written and sent | 154 (56 merged) |

Counts are a floor, not a ceiling: they only count what reached the files.

## The kinds of defect that keep turning up

- a command, setting or snippet that names something that does not exist, so it silently does nothing
- a palette entry whose command was renamed in the code but not in the command file
- output written to the wrong place, or a command that fails on an unsaved tab
- `.sublime-*` files that are not valid JSON, so the whole file is ignored
- release archives containing file names Windows cannot create, so Package Control skips them
- packages that cannot load at all on a current Sublime Text (Python 2 leftovers)

## Limits

- One machine, Windows 11, Sublime Text 4215. Linux and macOS are untested.
- Each test is brief. A clean row means "nothing seen here", not "nothing exists".
- Counts describe the files, not the ecosystem; the channel changes weekly.

## Files

| file | what it is |
|---|---|
| `PROCEDURE.md` | the method, the traps, and the dated corrections |
| `RESULTS.tsv` | every test record, one row each |
| `ISSUES.tsv` | every issue filed |
| `ALIASES.tsv` | package names that resolve to the same repository, counted once |
| `data/` | the sweeps behind the figures (channel archives, path and JSON checks) and their findings |
| `.claude/skills/sublime-package-audit/` | the method as an agent skill |

MIT, see `LICENSE`.
