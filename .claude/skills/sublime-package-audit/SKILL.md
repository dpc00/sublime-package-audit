---
name: sublime-package-audit
description: How to audit Sublime Text packages with an AI agent that drives a real Sublime through sublime-mcp. Use when installing, testing or reporting on Package Control packages in a portable Sublime copy: set-up, the per-package routine, what counts as a finding, how to write the report, and the traps that fooled earlier runs.
---

# Sublime Text package audit

This is the agent version of `PROCEDURE.md` in this repository. `PROCEDURE.md` explains the method; this file says what to do, step by step, with the tools that exist. The audit this came from is described in `README.md`.

## Purpose

Install a package the way a user does, use what it claims to do, and report real defects to its maintainer as short issues. A second purpose is to find gaps in sublime-mcp itself: if a step a user can do cannot be done with sublime-mcp's tools, write that down as a gap instead of working around it.

## Set-up

- Use a **portable copy** of Sublime Text (it has its own `Data` folder). Never test in the everyday install.
- Install [sublime-mcp](https://github.com/dpc00/sublime-mcp) in the portable copy and connect your agent to it. Start with its `get_help` tool.
- Before each package, copy the portable's `Data/Packages/User/Preferences.sublime-settings` and `Package Control.sublime-settings` somewhere outside it. Write one line (package, date) in a "test installs to remove" file **before** installing, so a crash cannot leave unknown leftovers.
- Keep a small tab-separated list of what was tested (name, date, short result). Check it, by name and by repository owner/name, before every package, and again with a plain text search of your log: a package can be done under another name.

## Per-package routine

1. Say which package you are testing.
2. **Install like a user:** open the Command Palette, `Package Control: Install Package`, pick the package. With sublime-mcp: `run_command show_overlay` (`overlay: command_palette`, `text: "Package Control: Install Package"`), press Return, then pick by name with `pick_quick_panel` (`text`, exact name). The `index` it reports is the position in the FULL list, so pick by name. Check the picked item is the one you meant.
3. Wait until Package Control has recorded the package (the console shows "Package Control: Installed package ..."). Then read the console and look for dialogs (`list_native_windows`).
4. **Restart before judging a package that ships settings or a theme.** Sublime reads a package's own `Preferences.sublime-settings` only at start-up (sublimehq/sublime_text#7012); before that its defaults are missing.
5. Inspect the package source (the zip in `Data/Installed Packages`, or its folder) so you know what it promises.
6. Exercise what it promises, one claim at a time: palette commands, menu items (greyed out means the command is missing), key bindings, snippets, completions, settings (does changing one do anything?), syntaxes and color schemes (read the scope under the cursor, apply the scheme and look). Look at the window after each command.
7. If the package needs a real external tool (a language server, a compiler), install the real tool in its own folder and use it. Do not test with a stub.
8. Clean up in this order: close every tab you opened (mark them scratch first so no Save dialog blocks the exit); quit the portable and wait until no process remains; delete the package files and any tool you downloaded (to the Recycle Bin or trash, not permanently); restore the two settings files and compare their hashes with the backups; write the result in the log and the tested list.

## What counts as a finding

- The package does not do what its README or menu says, or fails at load (read the console, and the whole traceback, not only the last lines).
- A name that is not defined or is misspelled, a setting or command that points at nothing, a snippet or key that can never fire, a package listed in Package Control with no releases.
- Typos and invalid or empty values that are plainly wrong are worth a short issue too, if they have a clear effect or a clear fix.

Not findings:

- A package that only fails on the newest Sublime build because it is old, or that only works on the newest build (some packages target scope names of build 4215 and do nothing on 4200). Say so in your log; do not report it as a bug.
- Anything caused by your own test set-up. Rule that out first: a wrong cursor position, a test file in the wrong place, a missing restart, a stray panel that swallowed keystrokes, a missing external tool. Example: the R language server skips diagnostics for files inside the Windows temp folder, so a test file kept there looks like "no diagnostics".

## Proving a finding

- Reproduce it, then find the cause in the source.
- Try the fix on an **unpacked copy** of the package (a folder with the same name in `Data/Packages`, then restart) and see the effect change. Packages that need a patched core package can be tested the same way.
- State plainly what was seen and what was not. If a typo has no visible effect, say so.
- Never file on a guess. Check the repository's existing issues first. One issue per finding.

## Writing the report

- Short and plain. It starts with "Claude reports:" so the maintainer knows an AI wrote it. No greeting, no sign-off.
- Say where (file, line, setting), what happens (with the Sublime build and operating system), and a suggested fix in one line.
- Say what you did **not** try.
- No patches or pull requests unless the maintainer asks for one. If a maintainer asks for no more reports, send none.
- Where issues are disabled or the repository is archived, send the same text by email to the maintainer's commit address, and show the person who owns the audit the exact text first.

## Traps that fooled earlier runs

- **Package Control reinstalls a package you deleted by hand** if its settings file still lists it. Restore `Package Control.sublime-settings` from the backup before you start Sublime again, and then the package stays gone.
- Swapping a package in a running Sublime can fail with "No module named '<Package>.<module>'" when the Python host differs between the release (3.3) and the repository master (3.8). That is an artifact, not a package bug: quit and start again.
- A live install of an LSP helper package may not start its server until Sublime restarts, if the package registers more than one plugin (sublimelsp/LSP#3074). Check that LSP lists the config before you judge "the server never starts".
- Commands run right after an install may silently do nothing until the package is indexed; wait, then run them.
- `eval_python` runs on the editor's main thread: a `time.sleep` in it freezes Sublime. Selection changes made from code do not always fire `on_selection_modified`; a real `move` command does.
- A test that opens a second window or a native modal dialog can freeze the editor. Run one dialog-raising command at a time and look at `list_native_windows` after each.
- A file written through a PowerShell redirect can arrive with a byte-order mark and Windows line endings, and a plugin then does nothing.
- Windows PowerShell: `Expand-Archive` refuses `.sublime-package` (use Python's `zipfile`), and variable names are case-insensitive (`$p` overwrites `$P`).
- GitHub's search API stops at 1000 results and rate-limits quick queries.
- **Real tools, small downloads:** a portable install of the real tool is usually enough (MiKTeX with `miktexsetup --portable`, LDC for a D tool, an unpacked LLVM `bin` folder). Put it in its own folder, add it to `PATH` only for the Sublime process you launch, and delete it afterwards. Verify a download (signature, or the same file from two official sources) before running it. Python 3.14 can open `.tar.zst` files with `compression.zstd` when Windows `tar` cannot.
- A build system with variants opens a picker when you run the plain `build` command; the test then looks stuck. Select the variant, or call the package's own build command directly.
- Edits to an unpacked copy of a package are picked up live only for top-level plugin modules; modules the package imports later (builders, sub-packages) need a Sublime restart.
- Keep scratch files on a SHORT path when testing build tools: TeX wraps log lines at 79 characters, and a long path split an error message and hid the real cause for a while.
- `dismiss_native_window` sometimes needs a second call before a dialog goes away; list the windows again before clicking twice.
