---
name: sublime-package-audit
description: The entire Sublime package audit as steps - queue and precheck, static or live test of a package in a portable Sublime through sublime-mcp, one-line recording, README and ISSUES figures, filing an issue, fronting a window, installing from a zip, toolchain prerequisites, leftovers, commit. Replaces every former tools/*.ps1; nothing here is a script.
---

# The package audit

Why: packages are the vehicle for finding **sublime-mcp** bugs — a call that cannot do what a person
can do, a result that cannot be read back, a step that needs a workaround. A package defect is filed
with its own repository; a sublime-mcp gap is the real product.

Tool usage and tool-design briefings are **not** here: they live in sublime-commander —
`AGENT_GUIDE.md` (served by `get_help`) and `skills/sublime-commander/SKILL.md`. This file is the
testing procedure only.

Files: `RESULTS.tsv` (one row per test record: package, date, result), `ISSUES.tsv`
(every issue filed: repository, number, title, state, dates, link), `data/tested_packages.tsv`
(name, date, issues filed, note — what stops retesting), `data/st_io_packages.tsv` (installability per
channel entry; not a second ledger), `data/do_not_file.tsv`, `data/channel_pc.json` (channel cache),
the channel cache and the do-not-file list.

## The rig — four portables exist, one is the audit's

There are four portable installs under `C:/Users/donal/tools/`: **`st_portable`** and
`ST-portable-4215-omp-1`, `-omp-2`, `-omp-3`. Any of them can in principle be driven — each declares
its own `mcp_port` in `Data/Packages/User/MCP Commander.sublime-settings`.

**The audit uses `st_portable`.** Not because the others cannot run, but because the baselines, the
settings hashes and every recorded result belong to that instance; a result obtained in another
portable is not the same test. Do not switch instances mid-test, and never carry evidence across.

- `st_portable` → MCP server `sublime-mcp-portable`, `http://127.0.0.1:9512/sse`
  (`mcp_port: 9512`, `http_port: 9510`, `require_consent_for_destructive: false`).
- `ST-portable-4215-omp-1|2|3` → `mcp_port` 9542 / 9552 / 9562. Leave them alone.
- **Confirm the target before any test call:** read that instance's `MCP Commander.sublime-settings`
  for the port, then check that `list_native_windows` returns the hwnd of the window you just
  launched — not another install's window. A session that matched on the directory name
  `ST-portable-4215-omp-1` installed a package into a portable nobody was using and cost a full
  restore (2026-11-08).
- **Record the baseline first:** `md5sum` of `Data/Packages/User/Preferences.sublime-settings` and
  `Package Control.sublime-settings`. Restoring after a removal means: delete the package archive
  from `Data/Installed Packages`, delete any `Data/Packages/User/<Package>.sublime-settings` the
  test wrote, drop the name from `installed_packages` in `Package Control.sublime-settings`, and
  both hashes must equal the baseline again — that equality is the proof, not the absence of files.
- **One window at a time.** Close every window the test opened before starting the next step; a
  stack of leftover portable windows is what made an earlier result untrustworthy.

### What "properly set up" means — check all four, not just the one in use

Each portable must satisfy all five, or it will produce a false result:

| check | expected |
|---|---|
| `Data/Packages/MCP Commander` | a junction to `C:/Users/donal/projects/sublime-commander` (the repo is `dpc00/sublime-commander`), reporting version 0.0.0 |
| `Data/Packages/User/MCP Commander.sublime-settings` | its own `mcp_port`/`http_port` pair, plus `"require_consent_for_destructive": false` (otherwise every destructive call asks and stalls an unattended run) and `"install_py33_helper": true` |
| `Data/Packages/MCP Commander Py33` | exists once the instance has started with the helper enabled |
| `Package Control.sublime-settings` | `installed_packages` matches `Data/Installed Packages/*.sublime-package` exactly — an archive missing from the list is an orphan Package Control deletes at the next start, a listed name with no archive is a stale entry |
| ports | distinct per instance and actually bound by its own process |

Ports, as verified 2026-11-08: `st_portable` 9512/9510, `-omp-1` 9542/9540, `-omp-2` 9552/9550,
`-omp-3` 9562/9560. Prove a claim by launching the instance and checking
`Get-NetTCPConnection -State Listen` for its pair — the plugin binding the port is the proof; the
instance needs about 15 s before it binds.

### Dialogs: the `dialog-watch` sidecar answers them

sublime-mcp is a pass-through for ST commands and holds no policy; a command that opens a modal
dialog blocks Sublime's main thread inside the dispatch, so that call cannot return until the dialog
is answered. Answering it through an MCP call costs a round trip (0.6 s), which is why polling from
the agent takes ~3 s per dialog.

Use the sidecar: `C:/Users/donal/tools/dialog-watch/watch.py` (design and all measurements in
`DESIGN.md` next to it). Start it once per rig session, before the first test:

```
python C:/Users/donal/tools/dialog-watch/watch.py \
  --exe "tools/st_portable/sublime_text.exe" --auto \
  --log "C:/Users/donal/tools/dialog-watch/sessions/<date>-<rig>.jsonl"
```

- It resolves the editor's **process tree** (`sublime_text.exe` + `plugin_host-3.x.exe`) and hooks
  `EVENT_OBJECT_SHOW`, answering a top-level visible `#32770` with its Cancel/No button (`BM_CLICK`),
  else `WM_CLOSE`. Measured: **2.6–4.5 ms** from shown to answered; a dispatch that returned
  `main-thread timeout after 5s` in 6.1 s now returns `{"ok": true}` in 0.7–1.6 s.
- It leaves alone any dialog already open when it started (it seeds existing top-level windows). That
  is proved, not assumed: with a dialog up, starting the watcher emitted nothing and the dialog
  stayed.
- A dialog appearing is still **evidence** about the package that raised it: read the log line, and
  the test row says what appeared and that it was cancelled.
- Not covered: elevated dialogs (a non-elevated watcher cannot click them) and custom-button task
  dialogs with no Cancel/No (falls back to `WM_CLOSE`, unobserved so far). A dialog up with the
  watcher not running means the old manual route: `list_native_windows` then `dismiss_native_window`.

Fallback, when the sidecar cannot run (other machine, no `ctypes`): dispatch without awaiting, poll
`list_native_windows` every ~60 ms, `dismiss_native_window` the dialog that appears, and treat the
step as unfinished.

## 0. Step 0 — the repository first, before anything else

Every package, every time, before the queue, before installing, before reading the source:

```
gh issue list -R owner/repo --state all --limit 30
gh pr list    -R owner/repo --state all --limit 30
```

- **Issues *and* pull requests, all states.** A closed, unmerged pull request is still a proposed fix.
- **What is already reported decides the verdict**, not what you find first. A defect that is open is
  "already reported, nothing filed"; a defect fixed upstream is a retest of the fix; a defect with no
  issue is the one to file. Doing this first is what stops a report that duplicates a known one.
- **Read how a closed issue was closed**, never the state alone: `gh issue view <n> -R owner/repo
  --json state,stateReason,closedAt,comments --jq …`. Closed by the maintainer, closed as
  completed, closed by the audit's own 30-day bot ("Reopen it if it is still relevant"), and closed
  because a fix shipped in a release are four different facts. Only the last one means "done".
- **Check whether the fix is in the release Package Control serves.** The channel's `releases[-1]`
  date against `gh api "repos/owner/repo/commits?per_page=1"`. A fix merged after the last release is
  "fixed upstream, unreleased" — the defect is still live for every user, so the issue is not done.
- **Never reopen an issue this audit closed** (Donald, 2026-11-08: "let the maintainer do that"). That
  includes the ones the 30-day bot closed. When the defect is still live on the served release, record
  it in the ledger and leave **one** comment on the closed thread with the reproduction and the fix,
  worded as information for the maintainer, not as a request to act — a closed/reopened/closed
  sequence on our own thread reads as indecision and costs Donald's credibility. Reopening is the
  maintainer's move, or happens because a fix ships.
- Record what step 0 found in the row. It is the difference between "no defect found" and "the
  known defect is unchanged".

## 1. What is next

1. **The queue.** Compare the live channel (`data/channel_pc.json`: `packages_cache` → per-repository
   arrays of `name`, `releases[]` with `version`/`date`/`sublime_text`/`platforms`) against **both
   ledgers at once**: `data/tested_packages.tsv` **and** `RESULTS.tsv`. A name is done if it appears in
   *either*. Reading only the tested list is how Indent XML was retested on 2026-11-08 although
   `RESULTS.tsv` had held its 2026-10-08 row all along — 198 packages were missing from the tested
   list at that moment, so a queue built from it alone offered finished work. Work down by release
   date, newest first.
2. **Is it already tested?** Search `data/tested_packages.tsv` for the name as a word and for the
   repository slug, and search `RESULTS.tsv` for both. Reduce the name first: drop a leading `#<n> `,
   a trailing ` (...)`, a trailing version, a trailing bare row number (`JSON Stringify 515` is
   `JSON Stringify`), and treat `-` and `\u2013` (en dash) as the same character. Any hit means done —
   this is the check that failed once and retested JSON Stringify; do it every time. **2026-11-08: the
   dash was the next trap** — `Okami - Adaptive Color Schemes` was live-tested on 2026-10-25 and was
   retested because the queue held it as `Okami \u2013 Adaptive Color Schemes`; a name can also be
   mojibake (`Ingl\u00e2s`), so search the account/owner as well when the name looks clean.
   **The name is not the identity: the repository is.** Three more packages were wrongly offered as
   untested on 2026-11-08 because the ledger records them under another name entirely —
   `LD library Path` is `LDLibPath`, `Marksy Convert` is `Marksy-Convert`, `Padawan (PHP completion)` is
   `Padawan (padawan-php/padawan.sublime)`. So: search the ledgers for the **owner/repo slug** first
   and treat any hit as done, and never build a to-do list by scripted joins over names — that is how
   each of these was missed. Read the rows.
2b. **Keep the two ledgers in step.** Every finished test writes a row to *both* files. When a name
   is in `RESULTS.tsv` but not in `data/tested_packages.tsv`, that omission is itself a defect: add
   the missing row in the same session (`RECONCILED <date>: already tested; the RESULTS.tsv row of
   <date> is the record…`), because otherwise the next queue schedules it again. 198 such rows were
   added on 2026-11-08; the join between the files must come out empty.
3. **Is anyone there?** `gh repo view owner/repo --json isArchived,hasIssuesEnabled,pushedAt` and
   `gh api "repos/owner/repo/commits?per_page=1" --jq '.[0].commit.author.date'`. Archived, issues
   off, or no commit and no owner activity for three years = record only, do not file. `data/do_not_file.tsv`
   overrides everything.
4. **Pre-check in bulk** (the former `precheck.ps1`): for each candidate, `gh repo view` for archived
   and issue state, `gh issue list -R owner/repo --state open --limit 30` for what is already reported.

## 2. Static check without installing

Worth doing first when a package is syntax-only or its install is heavy: read the release zip
(`gh api repos/owner/repo/contents/...`, or the `releases[].url` codeload zip) and inspect its
`*.sublime-syntax`, `*.tmLanguage`, `*.sublime-settings`, `*.sublime-commands`, `*.sublime-keymap`,
`*.sublime-snippet` for JSON/plist validity, duplicate triggers, missing files and dead settings — then
read one file at a time in the editor. A static-only result is recorded as such and is **not** a live
test: say "static only" in the verdict.

## 3. Install and exercise it

**Step 0 comes first, here too** (section 0): `gh issue list -R owner/repo --state all` and
`gh pr list -R owner/repo --state all`. An open defect decides what the test is — reproduce it and
record whether it still holds, instead of running the README tour and reporting "no defect found"
over a known one.

Portable Sublime only (own `Data`). Copy `Data/Packages/User/Preferences.sublime-settings` and
`Package Control.sublime-settings` outside it first, to compare hashes afterwards.

```
run_command show_overlay {"overlay": "command_palette", "text": "Package Control: Install Package"}
ui_press_key Return
get_quick_panel text="<package>"          # the version the picker offers; note it
pick_quick_panel index=<that index>
get_console mode=visible force_focus=true tail=15
```

When Package Control has no release for it, build the package the way Package Control would: take the
release zip, drop its top folder, and write `Data/Installed Packages/<Name>.sublime-package`, then
restart the portable. An unpacked folder in `Data/Packages/<Name>` is the alternative when the package
ships `.no-sublime-package`.

Then read the package's own README and source (`Data/Installed Packages/<name>.sublime-package` is a
zip; `str_replace_based_edit_tool` with `view` reads a file, and a copy can be unpacked outside the
repo), and exercise each claim, one at a time, looking at the window after every command. One test
window at a time. Restart before judging anything that ships settings, a theme or a syntax, and check
the *resolved* setting (`get_sheets` with `settings: true`) rather than the file you wrote.

**Prerequisites** are installed into their own folder, on `PATH` only for the portable's process, never
machine-wide and never with admin rights: a zip release unpacked under `C:\Users\donal\tools\`, or a
portable toolchain, with the launcher adding it to `PATH`. Say what was installed and how to remove it.

## 4. Record one result

Both ledgers hold **one row per package** — never a second row for a retest. Recording a package that
is already there means replacing its row; the latest result wins.

- `RESULTS.tsv`: `<name>\t<date>\t<result>`. Find the package's existing row (editor search for the
  name as a word) and replace its date and result in place; no new row for a name already present
  under any spelling (strip `#<n> `, ` (…)`, a trailing version, a trailing row number before
  comparing).
- `data/tested_packages.tsv`: `<name>\t<date>\t<issues filed>\t<same result>`, one row per package, same
  replacement rule.

The result is one line: `WORKS: <what proved it>; not filed`, `BROKEN: <symptom> at <file:line>;
filed owner/repo#N`, `SKIPPED: <prerequisite> absent`, `STATIC ONLY: <what the read found>`.

**One file, one editor — the one that has it open.** `RESULTS.tsv`, `ISSUES.tsv`, `data/tested_packages.tsv` and this skill are live buffers in the person's Sublime. Never edit them through a portable's MCP server, through `write`, or through an inline script: a second process editing a file the first one holds is exactly the state nobody can trust, and it looks careless even when the bytes happen to agree (Donald, 2026-11-08: "it just looks stupid when the files are up in main, to see you use the portable. Who can trust editors that are separate processes?"). Open the file in the main editor if it is not already, then edit and save it *there*. The portable is for the package under test, never for the record of the test.

**Edit a ledger in the editor, never through a whole-file tool.** Keep `RESULTS.tsv`, `ISSUES.tsv` and
`README.md` open as tabs in the Sublime that hosts sublime-mcp, and change them with
`str_replace_based_edit_tool` (`command: "str_replace"`, exact old text → new text) followed by
`save_file`. That is a surgical change inside a buffer the person can see, and it cannot truncate the
file. `write` replaces the whole file — a 3,159-line `ISSUES.tsv` becomes one row and git is the only
thing that saves it. Add a row by anchoring on the last line (old = last line, new = last line + the
new row); change a row by anchoring on that row. Read the line count back (`wc -l`) after any ledger
change.

**The ledgers are sorted; an edit that breaks the order is a defect.** `ISSUES.tsv` is sorted by
repository slug: a new issue row goes at its alphabetical position, not at the end. `RESULTS.tsv` is sorted by package name, case-insensitively, with no line-number column: order is not
data, so a query sorts at read time (`sort -t$'\t' -k1,1 RESULTS.tsv`) and the file is never re-sorted.
The three batch notes that carry no result (they begin with `!` or `"`) sit at the end. After any
change,
check both: `awk -F'\t' 'NR>1{k=tolower($1); if(prev!="" && k<prev) print NR": "prev" > "k; prev=k}'
ISSUES.tsv` must print nothing.

**Duplicates are resolved by repository, not by name.** Two rows whose names normalise together are
the same package only when the channel gives them the same `homepage` repository; the merged row keeps
the later date and the dropped rows go to `data/duplicates_merged_<date>.tsv` (168 rows on 2026-11-07).
Similar names on different repositories are different packages — `Pandoc` and `Pandoc (Markdown)`,
`RSpec` and `RSpec (snippets and syntax)` — and both stay. Rows that are notes rather than packages
(`queue status …`, `undefined-name fix PRs batch …`) are never merged.

**Replacing a row is not rewriting it.** A row states only what is verifiable now: the test you ran,
what you saw, the evidence, and the issue numbers with their dates and states. It never reconstructs
what an earlier row used to say. "ISSUES.tsv records #<n> filed <date>, so a live test exists on
record; the row this replaces was a <date> static check" is checkable; "the bulk pass overwrote the
earlier test" is an inference and does not belong in the ledger. Never turn a live test into a static
one or the reverse without the run that proves it, and when the only change is that a known issue was
re-checked, say that instead of writing a fresh "no defect found".

## 5. Keep the README true

The README's figures are computed from the data files, never typed from memory. Every number below is
one pass over a file; do it when a package is recorded, an issue is filed or a state changes.

**Packages (`RESULTS.tsv`)** — rows are `name, date, result`:
- lines = rows in the file.
- distinct packages = the same name spelled in different cases or with a queue prefix counts once; fold
  retests into one entry per package (the latest row wins), and treat a row named `X (correction)` or
  `X (retest …)` as `X`.
- with a conclusion = rows whose `result` field is not empty.
- the bucket table (`not installable`, `repository gone`, `no GitHub link`, `not offered`, `static
  only`, `read-only`) = count the rows whose result begins with that phrase; a row can only sit in one
  bucket.
- tested / not tested = distinct packages minus the buckets above, against the channel names that are
  not in any bucket (`data/channel_pc.json` for the channel; `ALIASES.tsv` so two names for one
  repository count once).

**Issues (`ISSUES.tsv`)** — rows are `repository, number, title, state, filed, link, closed, updated,
kind`:
- rows = lines minus the header; distinct = unique `repository#number`; duplicate log rows = rows minus
  distinct.
- repositories = unique `repository`.
- open / closed / unreadable = count the `state` field (`open`, `closed`, empty = repository no longer
  readable).
- closed within a week = closed rows whose `closed` date is within seven days of `filed`.
- median / mean days to close = the difference between `filed` and `closed` over the closed rows.
- refresh the states before computing: `gh issue view <n> -R owner/repo --json state,closedAt` for rows
  whose state may have changed, and write the new state and closed date back into the row.

**Pull requests** — `gh search prs --author dpc00 --merged --limit 1000 --json number` (length),
the same with `--state open`, and `--state closed` (that count includes merged, so closed-not-merged =
closed − merged).

Write the results into the README's tables, and nowhere else.


## 6. File the finding

`gh issue list -R owner/repo --state all` for a duplicate first. Write the body to a file outside the
repo, then `gh issue create -R owner/repo --title … --body-file …`, and read it back with
`gh issue view -R owner/repo <n>`. The body: what was done, what happened, Sublime build and OS, the
cause with `file:line`, a one-line suggested fix, what was not tried. One issue per finding, never
where `data/do_not_file.tsv` says not to, and never on an archived repo or one with issues disabled.
An author-facing question (not a bug) goes by email when the repo has issues disabled.

## 7. Front the test window when a step needs the screen

Before the first command after a launch, call `list_native_windows`: a registration nag or a
`Save Changes?` dialog left over from the previous session holds the main thread, and every batch
then dies as a 5-second timeout that looks like a broken server. Answer it there and move on.

Most tools post keys and clicks without focus. When a step needs it (native dialog, a picker Sublime
draws itself, a current screenshot), bring the portable to the front once, confirm with
`list_native_windows` that it is the window you think, do the step immediately, then if you raised it
over his window, give the foreground back. A background window repaints late: confirm state with
`get_sheets` / `get_selection` before trusting a picture.

## 8. Read the state, don't infer it

`eval_python` is denied to the MCP client, so a package's internal state (view settings, scope, the
merged defaults) cannot be read directly. Drop a throwaway `TextCommand` into
`Packages/Probe/probe_dump.py` that writes the values you need to a temp JSON file, run it with
`run_command probe_dump`, and read the file. One read answers what a chain of inferences cannot.
Remove `Packages/Probe` afterwards: a loose directory in `Packages` loads as a real package at every
launch, so `ls Packages`, `ls Packages/User` and the `installed_packages` list in
`Packages/User/Package Control.sublime-settings` belong to the teardown check alongside the two
settings MD5s.

**A defect found in a zipped package must be re-checked unpacked.** Sublime Text merges
`Base File.sublime-settings` from an unpacked package directory but not from inside a
`.sublime-package`, and Package Control installs zipped. Extract the archive into `Packages/<Name>/`,
move the zip out of `Installed Packages`, restart, and repeat the test. If the unpacked copy behaves
correctly, the finding is "the shipped defaults never load", not "the feature is broken" — and the
issue has to say which, with the probe output as the evidence.

## 9. Commit

Exactly one commit in this repo; amend, never append. If the log shows more than one — a session that
appended instead of amending — squash them into the single commit before adding anything else
(`git reset --soft <the first commit> && git commit --amend --no-edit`), then push with
`--force-with-lease`:

```
git add -A
git commit --amend --no-edit
git push --force-with-lease origin main
```

**The commit message carries no issue references.** Never put `owner/repo#N` or an issue URL in a
commit message: GitHub turns each mention into a permanent "referenced this issue in ..." event on
the maintainer's issue, and this repo's amend-and-push loop repeats it on every rewrite (24 such
events on 3 issues, 2026-11-09). Refs belong in the ledgers and in the issue body; file contents and
diffs create no events.

## 9. Clean up

**Close the fixture views first.** A view still set to a syntax the package owns pins that file: remove the package first and Sublime raises the native dialog `Error loading syntax file "Packages/<Name>/<Name>.sublime-syntax": Unable to stat …`, which blocks the window until answered (Clafer Tools, 2026-11-09). Close the tab, or switch its syntax to Plain Text, before the removal. The same holds for a package's own settings or theme file held by a view.

Remove the package through the picker (`remove_package` → `get_quick_panel` → `pick_quick_panel`), wait
for `Removed package`; delete what it left in `Data/Packages/User`; compare `Preferences.sublime-settings`
and `Package Control.sublime-settings` with the copies taken before the test (Package Control adds the
package to `ignored_packages` during install/remove, so compare after the removal); check
`Data/Installed Packages` for an archive left behind by a removal followed by a quit; close the portable.
Anything deleted from his machine goes to the Recycle Bin, never permanently, and only what the test
created.

## 10. Bulk static triage over the whole channel (a finished campaign, kept for its method)

The 14 scripts once in `data/campaign_tools/` did one job each; each is a few commands, done by hand:

- **Queue by installs** — order channel entries by install count (from the channel's `install` field or
  the browse pages), then take the top N that are not in `data/tested_packages.tsv`.
- **Served release check** — for each name, read the release the channel serves (`releases[-1]`) and its
  `sublime_text`/`platforms`; a name whose release predates the build or excludes Windows is
  "not installable", recorded as such without installing.
- **Clone all** — `gh repo clone owner/repo` into a scratch folder outside the repo, only when reading
  the source beats installing it.
- **Command scan** — `grep` the clone (or the installed package) for `sublime_plugin.*Command`,
  `sublime_commands` captions and key bindings, to see what the package offers before running it.
- **Defect check** — read for the usual defects: a command id with no class, a caption pointing at a
  missing command, `begin_edit`/`view.word(s)`/`urllib2`-era APIs, a settings key read but never
  shipped, a syntax path that does not exist.
- **Syntax scan** — validate every `*.sublime-syntax`/`*.tmLanguage`/`*.sublime-settings` as JSON/plist
  and look for duplicate snippet triggers.
- **Near-duplicate search** — compare a package name against the tested list after normalising
  (`normalise` in section 1), so a rename is not retested.
- **Session-log and transcript coverage** — before testing, search the old session log and retained
  transcripts for the name: a package already exercised there is a record, not a new test.
- **GitHub record stats** — counts of issues/PRs per repository with `gh api`, for the README figures.
- **File issues** — one `gh issue create` per finding, body written to a file outside the repo first,
  then read back (section 6).
- **Triage** — sort the remaining names into: test live, static only, skip (archived/dead/no release).

