---
name: mcp-reconnect-full-slash-command-2026-10-24
description: reconnect an MCP server by typing the full slash command `/mcp reconnect <server>` into my own tab, never a bare `/mcp`
metadata:
  type: feedback
---

2026-10-24: computer-use-mcp was stopped by his Escape. He told me to run the reconnect myself. I typed a bare `/mcp`, which opens the interactive menu and interrupted my turn; he had to handle it. He pointed out the slash command I have used hundreds of times is `/mcp reconnect <server>`.

**Why:** a bare `/mcp` raises a menu only he can answer and cuts my turn off.

**How to apply:** when he says to reconnect a server, check that only my own tab is open in the main Sublime (get_sheets settings=false), then `ui_type_text` the full line `/mcp reconnect computer-use-mcp` plus newline, and read the result back. Say one line first that the turn may be interrupted. Related: [[no-admin-installs-2026-10-24]].

**2026-10-31 addendum:** the 1.18.0 server has no ai_terminal_send_string. My own tab can show up as the only sheet in the main Sublime with an unrelated name (it was called 'Previous session transcript tail'); I wrongly decided it was not my tab and asked Donald to run /mcp. Rule: if get_sheets shows exactly one sheet, that is my tab; ui_type_text the full '/mcp reconnect <server>' + newline (worked, reconnected at once). Do not ask him.
