---
name: audit-tool-findings-2026-10-19
description: Things learned driving the portable 4200 audit on 2026-10-19 (Ctrl+C via ui_press_key mods + method input, exact picker index, plugin load wait, async open_file, Save Changes dialog, recycle.ps1 args, npm package.json first, ST2-only packages, scratch-profile Chrome); plus Donald's rule to keep going and stop only for alarming errors or report overload
metadata:
  type: reference
---

**Donald's rule (2026-10-19): do not stop between packages.** Stop only if I am overrunning him with reports, or an error is alarming (data touched outside the test copy, a package that could damage the machine). Keep logging with rec.ps1 and keep the baton current. He also said: save findings like the Ctrl+C one (this note and the skill).

**Keys and clicks**
- A chord goes through `ui_press_key` with `key: "c"`, `mods: ["ctrl"]`, `method: "input"` (real keys; the window comes to the front; waits for him to be idle, use `wait_idle_s: 30`). `"ctrl+c"` as the key string fails ("unknown key"); method `post` carries no modifiers. Proof: Clipboard History recorded the copy only after this (status bar "Copied N characters").
- `click_menu_item` takes `View > toggle_tabs` (command name) when the menu entry has no caption.

**Pickers**
- `pick_quick_panel text=` picks the FIRST item whose first line contains the text: "Clipboard History" installed "Jimbly's Clipboard History" by mistake. Safe way: `get_quick_panel text=<name> limit=5` (small reply, gives `indexes`), then `pick_quick_panel index=<n>`. Arguments are flat (`text`, `index`, `wait_ms`), not nested under `args`.
- A package's own picker (3.3 host) is invisible to get_quick_panel: use `ui_screenshot` and `ui_press_key` (Down, Return).
- An ST2-only package (README says Sublime Text 2) is missing from the Install Package list: download the repo with `Invoke-WebRequest https://api.github.com/repos/<owner>/<repo>/zipball -OutFile x.zip` (NOT `gh api ... > file`, PowerShell redirect corrupts binary), extract with Python into Data\Packages\<Name>, test, recycle.

**Timing**
- A new package's plugin takes about 20-60 s to load; commands run before "reloading python 3.3 plugin <name>" appears in the console do nothing and give no error. Wait, then judge by a visible effect.
- `open_file` returns before the view is ready: check `get_active_file` path before inserting or saving, or the edit goes to the previous tab.
- Settings files written from outside Sublime (a package's user settings) can be picked up one command late.

**Dialogs and cleanup**
- `close_file` / `close_all` on a modified pathless tab raises "Save Changes?": `dismiss_native_window` with `button: "No"` (one per tab). Package tests that insert text leave these.
- `get_output_panel name=exec` reads build output (Start Chrome error text).
- `recycle.ps1`: pass each path as its own argument; an array is joined into one string and reported "not found".
- `Start-Sleep` of 25 s is blocked by the harness; use 20 s or less.
- A modal dialog (error_message) shown by a plugin appears in the `dialogs` field of the `run_command` result when `settle_ms` is set.

**Added later 2026-10-19**
- In `batch`, `get_quick_panel` / `pick_quick_panel` took their arguments nested under `args` that evening (flat form: "give index or text", or the filter was ignored and 100 items came back). `get_command_palette` filters by `package`, `caption` or `command`, never `text`; unfiltered it returns every entry (200+). `drive_input_panel` takes `text` only and submits. `ui_press_key` has no `period` and `up` did not move a quick panel; `down`, `return`, `tab`, `escape` and single letters (method post) work.
- A picker that Sublime itself opens (UI: Select Theme, Select Color Scheme, file navigator panels) is invisible to get_quick_panel: screenshot it, type the filter with single-letter post keys, Return.
- Hand copies of packages that are not in the channel (unmanaged folders) are removed with the normal remove picker ("remove unknown version"); this avoids recycling a folder the portable still watches (recycle.ps1 then raises a UAC prompt for nothing; seen twice on an empty folder).
- A command can sit in the palette and `run_command` return ok while nothing runs because the command class never loaded (ES6-Toolkit, module shadowed by a folder of the same name): check the console after "reloading python 3.3 plugin" and the palette entry.
- Swapping a package folder in while Sublime runs under a name it already had fails ("No module named"): use a fresh folder name.
- PowerShell 5.1 `Set-Content -Encoding utf8` writes a BOM; write settings with `[IO.File]::WriteAllText(path, text, (New-Object Text.UTF8Encoding($false)))`.
- Package Control can leave a removed folder package's name in `installed_packages` (Markdown Slideshow): compare the PC settings hash after every removal and restore from the backup.
- `open_file` is still async: with a command that reads the buffer (Markdown Slideshow) the first run saw an empty buffer. Call get_active_file and check the content before the command.

**Safety**
- Packages that run npm, pip or git on save/open: put a package.json (or run inside a git repo made for the test) first. npm-install climbed to `C:\Users\donal` and emptied its `node_modules` ([[feedback_npm_install_needs_own_package_json]]).
- Browser packages: use a scratch `--user-data-dir` Chrome and stop only processes whose command line contains it. Chrome 111+ needs `--remote-allow-origins=*` for old DevTools clients (Web Inspector #126).
- Text piped to node from PowerShell carries a hidden BOM and gives misleading output; test inside Sublime instead.
- The MCP reconnect (`/mcp reconnect <server>` typed into the main tab) happens at once; only its message waits for the turn end ([[session-baton-2026-10-19-jquerydocs-syncedsidebarbg-localhistory]]).
