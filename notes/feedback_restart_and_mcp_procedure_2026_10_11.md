---
name: restart-and-mcp-procedure-2026-10-11
description: 2026-10-11 Donald: needs a clear procedure when the portable restarts and /mcp is needed; closing the /mcp dialog with Escape stops Computer Use; batch SublimeLinter linters on one install to avoid restarts
metadata:
  type: feedback
---

On 2026-10-11 Donald said: "there has to be a clear/proper procedure here. I can't deal with you quitting because your tools are disconnected."

**Cause seen:** after he ran `/mcp` and closed the dialog with the Escape key, the next Computer Use call returned "stopped by the user with the physical Escape key" and the turn had to end (also seen 2026-10-07, see [[computer-use-false-escape-stop]]). The portable's MCP server only needed the reconnect; the stop came from the Escape.

**Procedure:**
1. After a portable restart, make a test call on the portable's MCP (list_native_windows / get_open_files) BEFORE saying anything. If it answers, do nothing and do NOT mention /mcp (he said: "don't send me down to fix what isn't broken, if it breaks computer-use"). Retry a few times over ~30 s first; it often reconnects itself ([[test-mcp-before-asking-reconnect]]).
2. Only if the calls still fail: tell him in one line what I tried and ask him to type `/mcp reconnect computer-use-mcp` (typed command, no panel, no Escape; see [[computer-use-escape-lock-findings-2026-10-11]]) or `/mcp reconnect sublime-mcp-portable-4200`, and say to close the dialog with Enter or a click, not Escape.
3. If Computer Use reports the Escape stop: one line ("stopped by Escape, say go"), end the turn, and on his "go" resume at the step recorded below. Never treat it as a reason to abandon the test; never leave a half-finished test without saying what is installed.
4. Keep a "where I am" line in the project note while a test spans a restart (what is installed, what is next, what to remove).

**Avoid restarts:** SublimeLinter needs one restart after install (status "SublimeLinter upgrade in progress. Aborting lint."). Test the SublimeLinter-contrib-* / SublimeLinter-addon-* packages in a row on ONE SublimeLinter install; remove SublimeLinter and the external tools only at the end of the batch, and log each.

**Where I am (2026-10-11, todo linter test):** portable 4200 has SublimeLinter + SublimeLinter-contrib-todo installed, restarted and reconnected; User\SublimeLinter.sublime-settings (paths to C:\Users\donal\AppData\Roaming\Python\Python314\Scripts); `todo-linter` 1.0.11 pip-installed into the single Python 3.14 (no deps; remove with `python -m pip uninstall todo-linter` at the end of the linter batch); test file scratchpad todo_test.py open. Next: lint it and read the panel/gutter, then continue the other SublimeLinter packages on this install.

**ROOT CAUSE, his words (2026-10-11 late):** "the problem occurs when you insist that I reconnect a sublime-mcp* that is NOT DISCONNECTED and I see it is not DISCONNECTED and I therefore get pissed off and escape out of the '/mcp'. You fail to check properly if the mcp's are connected." The Escape that stops Computer Use came from him backing out of an unneeded reconnect.
**Rule:** before asking for any reconnect, test EVERY server with a real call (main sublime-mcp, each portable, computer-use). Name only the server whose call failed, with the exact typed command (`/mcp reconnect <name>`). Never ask him to reconnect a server that answered. If only computer-use says "stopped", ask for `/mcp reconnect computer-use-mcp` only.

**STANDING PERMISSION (his words, 2026-10-11 late): "put that on the command line yourself, and in the future you could do that for any mcps you believe are disconnected."** I reconnect myself: `batch` on the main sublime-mcp -> `run_command ai_terminal_send_string` scope view, index 0 (the Claude prompt tab, "Get_console procedure audit changes"), args `{"string": "/mcp reconnect <server-name>\r"}`. Worked first time for computer-use-mcp (it answered right after). Rules: only after a real call to THAT server failed (never for servers that answered), then re-test it; never type it into tab index 1 (his DOS console, "tab 2"). If the main sublime-mcp itself is the one down, I cannot type through it: then ask him once, naming only that server.
**Verified 2026-10-11 late:** after closing and restarting portable 4200, the test call found the tool gone; I checked port 9522 was listening, typed `/mcp reconnect sublime-mcp-portable-4200\r` into the Claude prompt (main sublime-mcp batch, ai_terminal_send_string index 0), and the server was back within seconds (ToolSearch select then loaded the tools again). Works without bothering him.
