# Sublime Text package audit

Every package in the Package Control channel, installed in Sublime Text on Windows and used the way a
person would use it. What breaks is reported to the maintainer; what holds up is recorded as clean.

[![Donate via PayPal](https://img.shields.io/badge/Donate-PayPal-blue)](https://www.paypal.me/DChitester)

Donate via PayPal: https://www.paypal.me/DChitester
Contact: donaldchitester@gmail.com

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

## What was found

Every report in `ISSUES.tsv` falls into one of the shapes below. The count is how many titles match
that shape — matched on the title alone, and a title can match more than one — so the column is a
measure of how often that failure turns up, not a partition of the total. The link is the clearest
real report of it.

| what goes wrong | reports | an example |
|---|---:|---|
| highlighting or scoping is wrong | 578 | [hyprlang-sublime-syntax#3](https://github.com/0x000C0A71/hyprlang-sublime-syntax/issues/3) — `clear_scopes: true` removes `source.hyprlang`, so `rgba()` and its contents lose every scope |
| it crashes on use | 529 | [ColumnMassage#1](https://github.com/0x7FFFFFFFFFFFFFFF/ColumnMassage/issues/1) — only the first line changes, then `IndexError` when the output length differs |
| a command, setting, snippet or key does nothing | 316 | [niceDarkTheme#1](https://github.com/aaortizb/niceDarkTheme/issues/1) — the Install button in the Terminus dialog does nothing |
| Windows cannot use the file or the name | 274 | [ST-iconFont-snippets#4](https://github.com/badprint/ST-iconFont-snippets/issues/4) — two files differ only by letter case, so Windows keeps one |
| the snippet is wrong, or its trigger is | 209 | [sublime-bemjson-snippets#8](https://github.com/1vank1n/sublime-bemjson-snippets/issues/8) — the `efc` snippet has the trigger `etc` and clashes with it |
| the command gives the wrong output | 197 | [SublimeJSCSFormatter#46](https://github.com/elicwhite/SublimeJSCSFormatter/issues/46) — formatting breaks when Node writes a warning to stderr |
| the package does not load at all | 186 | [sublime-jekyll#100](https://github.com/23maverick23/sublime-jekyll/issues/100) — `ModuleNotFoundError: No module named imghdr`, removed in Python 3.13 |
| it blocks or freezes the UI | 181 | [sublime-0x0#1](https://github.com/axsuul/sublime-0x0/issues/1) — the request runs on the main thread and freezes the whole window |
| a build or run command is broken | 151 | [pyrock#24](https://github.com/abhishek72850/pyrock/issues/24) — `process.terminate()` with `shell=True` leaves the child running after a timeout |
| Python 3 syntax warnings at load | 143 | [go-playground-sublime#3](https://github.com/0x4445565A/go-playground-sublime/issues/3) — `SyntaxWarning: invalid escape sequence` on 3.12+ |
| behaviour differs from the README | 126 | [gotham-theme-sublime#6](https://github.com/0xhjohnson/gotham-theme-sublime/issues/6) — the documented `color_scheme` path fails after a Package Control install |
| package metadata or install is wrong | 119 | [gotham-theme-sublime#6](https://github.com/0xhjohnson/gotham-theme-sublime/issues/6) — the package installs with a name the README does not use |
| a `.sublime-*` file will not parse | 104 | [SublimeAutoItScript#38](https://github.com/AutoIt/SublimeAutoItScript/issues/38) — `CompilerDirectives.sublime-completions` has an invalid control character |
| it fails on an unsaved or untitled tab | 86 | [StataLinux#22](https://github.com/acarril/StataLinux/issues/22) — `TypeError` because `file_name()` is `None` |
| a key binding is wrong or clashes | 61 | [CPrettify-Sublime-text-3#18](https://github.com/aghontpi/CPrettify-Sublime-text-3/issues/18) — the keymap is `{}` instead of an array, so it raises at load |
| a dependency is missing or undeclared | 58 | [syncrow#5](https://github.com/Afzal7/syncrow/issues/5) — imports `yaml` but neither bundles PyYAML nor declares it |
| a menu entry is wrong or missing | 55 | [SublimeReadOnlyBuffer#3](https://github.com/crazybyte/SublimeReadOnlyBuffer/issues/3) — the menu opens a `.sublime-keymap` that was never shipped |
| a theme or asset is missing | 42 | [Theme-Dark-Material#14](https://github.com/artifactdev/Theme-Dark-Material/issues/14) — the theme refers to a texture that is not in the package |
| writes to the wrong place, or the wrong encoding | 42 | [ClearDirtyFlag#2](https://github.com/2shortplanks/ClearDirtyFlag/issues/2) — `open()` without an encoding, so non-ASCII files are never cleared |
| a setting is not applied | 11 | [sublime_ansible_vault#22](https://github.com/adambullmer/sublime_ansible_vault/issues/22) — OS-specific settings are ignored because the getter never reads them |

A further 798 titles are one-off logic bugs that fit no shape — a command that does the wrong thing in
one particular case, and nothing more general to say about it.

Two of the shapes above were also found by reading release archives rather than by using packages:
packages shipping **file names Windows cannot create** (Package Control skips those files without a
word) and packages shipping a **`.sublime-*` file that does not parse** (Sublime ignores the whole
file). Those lists are in `data/`.

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
