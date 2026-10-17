# How the audit was done

This is the method as it was used, including the rules that were added after something went wrong.

## 1. Set-up

- Test in **portable copies** of Sublime Text (builds 4200 and 4215), never in the everyday install. A portable copy has its own `Data` folder, so a broken package cannot touch real settings.
- Before each package, **back up** the copy's `Preferences.sublime-settings` and `Package Control.sublime-settings`. After the test, restore them and compare file hashes to prove nothing was left behind.
- The agent drove Sublime through sublime-mcp (an MCP server that runs inside Sublime), reading the editor's own state: tabs, console, scopes, menus, quick panels. A screenshot tool was used to look at the window, and a real pointer click only when the person at the computer had been idle (a rule that was tightened during the audit).

## 2. Choosing packages

Lists were built from the Package Control channel (install rank, date of the last push, amount of Python), then tightened or loosened in steps. `lists/README.md` says what built each list. Archived or long-dead packages were left out: they only cause trouble. Packages that need a paid account or a native dialog that cannot be dismissed were skipped or noted.

## 3. Install like a user

1. Command Palette, `Package Control: Install Package`, pick the package from the list. Do not copy files by hand unless the package cannot be installed from Package Control; say so in the record when that happens.
2. Wait until Package Control has recorded the package in its settings file. If Sublime is restarted too soon, Package Control removes it as an orphan.
3. **Restart the test copy before judging a package that ships settings or a theme.** Sublime reads a package's own `Preferences.sublime-settings` only at start-up; before the restart every default of that package is missing, and anything that depends on them looks broken.

## 4. What is checked

- The console, for errors at load and when the package is used. Note: a captured console only sees the plugin host it was started in; packages in the other host need the other build or a look at the dialogs.
- Everything the README promises, one claim at a time: commands in the palette, menu items (open the real menu and look; greyed out means the command is missing), key bindings, snippets (type the trigger and press Tab in a file of the right type), completions, settings (does changing it do anything?).
- Syntaxes and color schemes: write a small sample, read the scope under the cursor for each token, apply the scheme and look at it.
- Themes: restart, select the theme, open a few tabs, look at it.
- Static checks that find real mistakes cheaply: undefined and unused variables in schemes and syntaxes, JSON and YAML that parse, referenced files that exist, `ruff` with only the rules for undefined names.
- A package's own syntax tests or examples, when it ships them.

## 5. Proving a finding before reporting it

- Finish the proof. If a cause is suspected, test the fix on a **copy** of the file and see the effect change.
- Rule out your own test artifacts first: a wrong cursor position, a file copied with the wrong encoding, a stray panel that swallowed keystrokes, the missing restart above.
- State plainly what was seen and what was not. If a typo has no visible effect, say so.
- Never file on a guess. Check existing issues first, and file one issue per finding.
- No patches or pull requests unless a maintainer asks.

## 6. Writing the report

- Short and plain. It starts with "Claude reports:" so the maintainer knows an AI wrote it. No greeting, no sign-off.
- Say where (file, line, setting), what happens (with the build and operating system), and a suggested fix in one line.
- Where issues are disabled or the repository is archived, send the same text by email to the maintainer's commit address, and show the owner the exact text first.
- If a maintainer asks for no more reports, there are no more reports.

## 7. Clean up

Remove the package, wait for Package Control's "Removed package" line, close every tab and window the test opened, remove any file the test created, restore the two settings files, quit the test copy, and write the result down. Leftovers from earlier packages cause false findings in later ones.

## 8. Things that fooled the audit

- Settings of a just-installed package not being read until a restart (above).
- A file downloaded through a PowerShell redirect arrived with a byte-order mark and Windows line endings and the plugin silently did nothing.
- A test that opens a second window or a modal dialog can freeze the editor; do those from a terminal that is not inside the editor.
- GitHub's search API stops at 1000 results and rate-limits quick queries; list issues in small date windows, slowly.
- A "not installable" package (no releases in the channel) cannot be tested by the normal route; copying its files in by hand is the fallback, and the record says so.
- Added 2026-10-16: wait for the "Removed orphaned library" lines as well as "Removed package" before quitting. Quitting in between left Package Control to reinstall the package at the next start.
- Added 2026-10-16: a package that downloads libraries (ExportHtml) keeps the editor busy for a minute after the "Installed package" line; wait for "Package ... successfully installed" before using it.
- Added 2026-10-16: a file opened right after an install is opened before the package's syntax is indexed (it shows as Plain Text); close and reopen it.
- Added 2026-10-16: a hover popup needs the real mouse pointer over the test window; another window in front blocks it. Making the test window topmost for the one hover (and clearing it after) worked.
- Added 2026-10-16: Sublime's "Syntax Tests" build runs only files named `syntax_test_*` that sit inside the Packages folder; copy a package's test files there (renamed if needed) to run them.
- Added 2026-10-16: when planning which packages are left, match names by prefix against every earlier record ("LSP-Bicep (real .NET 10 test)" is the same package as "LSP-Bicep") and look at all dates, or finished work is planned again.
