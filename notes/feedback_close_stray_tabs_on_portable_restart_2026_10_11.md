---
name: close-stray-tabs-on-portable-restart-2026-10-11
description: 2026-10-11 Donald: when a portable restarts and tabs remain that are not part of the current test, close them; also write a fix plan for every sublime-mcp gap the testing reveals
metadata:
  type: feedback
---

Donald (2026-10-11 late): "if you restart a portable and there are any tabs remaining that are not pertinent to the current test, you should get rid of them." The 4215 portable came back with t.css (dirty, from an old session's scratchpad), "Ai (SDK)" and "other"; I worked around them instead of closing them.

**How to apply:** right after a portable restart and the connection test, `get_open_files`; close everything that is not part of this test (revert a dirty file first with `revert_file` so no save prompt opens, or use the documented scratch-and-close snippet; `close_file` by name or index). Do not close tabs on his MAIN Sublime. Also: findings about sublime-mcp itself must get a written fix plan the same night, see [[sublime-mcp-fix-plan-from-audit-2026-10-11]].
