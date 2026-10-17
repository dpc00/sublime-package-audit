# Sublime Text package audit (2026)

An audit of Sublime Text packages from [Package Control](https://packagecontrol.io), done between August and October 2026 by Donald Chitester (GitHub: dpc00) together with Claude, an AI agent that drove a real Sublime Text through [sublime-mcp](https://github.com/dpc00/sublime-mcp). Each package was installed the way a user installs it, used, and checked against what it claims to do. Problems were reported to the maintainers as short issues.

This repository holds the data and the method. It is a draft: the numbers will be updated.

## In numbers (to 2026-10-16)

- **1076 test records** for **987 different packages** (`RESULTS.tsv`). Most records are a live test in a real Sublime; a few are shorter (the package was loaded, or only its source was read), and the note in each row says which.
- **1144 issues** filed on **804 repositories** (ISSUES.tsv): 862 still open, 282 closed. Closed does not mean fixed; the list does not say why an issue was closed.
- The package lists used from 2026-10-07 on, and what built each one: `lists/`. The earlier September queue, by install count, is not published; its results are in `RESULTS.tsv`.

## What was found

Mostly small, concrete defects that a maintainer can fix in a few minutes and that nobody had reported. Typical kinds, each with a real example:

- **A name that is not defined or not spelled right.** A color scheme used a variable it never defines, so a function name in Python code was invisible ([fight-color-scheme#1](https://github.com/ghyatzo/fight-color-scheme/issues/1)); a theme property had a stray space in its name ([Theme-AquaSoda#2](https://github.com/Astramata/Theme-AquaSoda/issues/2)); a regular expression had `d` where `\d` was meant, so an IPv6 address with an embedded IPv4 part was not recognised ([sublime-syntax-edgeos#2](https://github.com/lojoja/sublime-syntax-edgeos/issues/2)).
- **A setting or command that points at nothing.** A menu item ran a command the package does not define and showed greyed out; a package read a setting under a different name than the one it documents ([NoDialogs#8](https://github.com/maximsmol/NoDialogs/issues/8)); a menu file pointed at color scheme files that do not exist ([Aethra#1](https://github.com/vlasikhin/Aethra/issues/1)).
- **A snippet or key that never fires.** A snippet scoped `source.Markdown` never matches, because Sublime's scope is `text.html.markdown` ([StrapdownJS-Boilerplate#1](https://github.com/sonokamome/StrapdownJS-Boilerplate/issues/1)).
- **Behaviour that differs from the README.** In the 2x2 layout, Alt+left and Alt+right jump to the other row ([sublime-ExpandGroup#5](https://github.com/evanliomain/sublime-ExpandGroup/issues/5)); an example in a README does not match what the plugin does ([SublimeTypoScriptr#1](https://github.com/kitzberger/SublimeTypoScriptr/issues/1)).
- **A package that cannot be installed.** Two packages are listed in Package Control with no releases (no git tags), so nobody can install them.

Many packages had nothing to report; those rows say so (for example the ISF syntax, Comments-only color scheme and npc_sheets, which behaved as described).

## Limits

- One machine: Windows 11, portable copies of Sublime Text builds 4200 and 4215. Linux and macOS behaviour was not tested.
- Brief tests. "No defects found" means none found in a short, real use of the package, not that there are none.
- The reports were written by an AI agent and are marked as such ("Claude reports:"). Every report states what was observed and what was not.
- The audit made mistakes, and said so when it found them. Example: a report on the Theme - Treble issue first blamed missing default settings on Sublime ignoring a package's own `Preferences.sublime-settings`; a retest showed that Sublime reads those only at start-up, and the report was corrected in the thread the same day ([Theme-Treble#1](https://github.com/53v3n3d4/Theme-Treble/issues/1)).
- Some maintainers asked not to be written to, or have issues disabled. Those requests were respected; where issues are disabled, an email was sent instead.

## Files

| file | what it is |
|---|---|
| `PROCEDURE.md` | the method: setup, what is checked, how a report is written, what went wrong |
| `.claude/skills/sublime-package-audit/SKILL.md` | the same method as a step-by-step skill for an AI agent (Claude Code loads it when you open this repository); needs [sublime-mcp](https://github.com/dpc00/sublime-mcp) |
| `RESULTS.tsv` | one row per test record: package, date, short result |
| `ISSUES.tsv` | every issue filed on a Sublime Text package or tool: repository, number, title, state, dates, link (from GitHub) |
| `lists/` | the package lists the audit worked through, as tab-separated files |

The data comes from the audit's own notes and from GitHub's public records of the issues; package metadata comes from the Package Control channel. Notes in `RESULTS.tsv` have had local file paths and personal names removed. The raw working log is not published.

## License

MIT, see `LICENSE`.
