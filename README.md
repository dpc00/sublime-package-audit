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

## What was found

The defects cluster into a few shapes. Each line is a real report from `ISSUES.tsv`, and the links are
the clearest example of that shape.

- **A crash in the console.** The command half-works, then raises: `ColumnMassage#1` changes the first
  line and then throws `IndexError`; `sublime-language-1c-bsl#11` raises when SublimeLinter is not
  installed.
- **Windows cannot use the file, or the name.** `Craft-Twig.tmbundle#33` ships 43 files with characters
  Windows forbids, so Package Control silently skips them; `ST-iconFont-snippets#4` ships two files
  that differ only by letter case, so only one survives.
- **Python 2 code on a Python 3 host.** `go-playground-sublime#3` emits `SyntaxWarning: invalid escape
  sequence`; elsewhere an implicit relative import, or a call to `inspect.getargspec`, kills the plugin
  at load.
- **A command or setting that silently does nothing.** `niceDarkTheme#1`: the Install button in the
  dialog is inert. `sublime-exact-quick-find#4`: a `.python-version` pins 3.14, so on build 4200 the
  plugin is ignored entirely. This is the largest family, and the hardest to notice from the outside.
- **A `.sublime-*` file that is not valid JSON,** so Sublime throws the whole file away:
  `ChoiceScript.sublime-completions` has an invalid control character, `Dart - Pubspec.sublime-build`
  a missing comma.
- **A command that assumes a saved file.** `StataLinux#22` raises `TypeError` when `file_name()` is
  `None`; `DXL#6` raises `AttributeError` on an untitled tab.

Two of these were found by reading the release archives rather than by using the packages, and the
lists are in `data/`: packages shipping file names Windows cannot create (Package Control skips those
files without a word), and packages shipping a `.sublime-*` file that does not parse.

The pattern behind most of the silent ones is a name that changed on one side only: a command renamed
in the code but not in the palette file, a setting key spelled differently where it is read, a keymap
binding to a command nobody registered.

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
