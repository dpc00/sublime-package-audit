---
name: session-baton-2026-10-10-evening
description: 2026-10-10 evening handoff before Donald restarts Claude: what was finished (Python 3.14 only, ~/tools cleaned, OSC 7501 probe answered), what is open, machine state, rules he restated
metadata:
  type: project
---

Supersedes [[session-baton-2026-10-10]] (its Python-cleanup item is done).

**Done today:**
- Python: only 3.14.7 all users (`C:\Program Files\Python314`, `py` launcher in `C:\Windows`). 3.12, uv, venvs removed. pip pruned 225 to 163 packages (top level: ccstatusline-editor, claude-agent-sdk, digital-mcp-server, flake8, git-filter-repo, git_int, mistral-vibe, numpy, ollama, ollama-vision-mcp, ollmcp, parsy, pillow, pyahocorasick, pyap, pylint, ruff, sqids, strsimpy, sublime-mcp, tarjan, textual-dev, xxhash). `digital-mcp-server` had been installed without its module; reinstalled from a patched copy; project `.mcp.json` (git-ignored) repointed to Python314; Digital MCP connects. Details: [[one-python-314-no-uv-no-venv-2026-10-10]].
- `~/tools` now holds only ColorHelper (PR #284 portable junction), Digital (his circuit MCP needs it), list-coding-agents (re-cloned from ThatOneCheat; his own edits are lost), screenshot-mcp-fix (the screenshot MCP runs from it). Mistakes and rules: [[tools-cleanup-mistakes-2026-10-10]]. cmux and ghostty were deleted permanently (GhostShell reference); he said he does not need them now; re-clone only if he asks (about 1.9 GB, public).
- Console readers: all seven tested once with a watcher; none selected anything in the Claude tab. The freeze has not recurred today. AgentIDE debug log is still ON in `User\AgentIDE.sublime-settings` to catch it (turn off after catching); note is in the AgentIDE repo (agentide-debug-trap-2026-10-10).
- GhostShell answers Claude Code's OSC 7501 probe in the right order (commit c74757d, pushed; note in the GhostShell repo). Claude 2.1.296 still sends no status reports; issue anthropics/claude-code#101114 filed (open, no replies as of 15:00); check it only when he asks.
- Broker test: Windows ConPTY answers DA1 and cursor-position queries with no client attached; the OSC 11 background-colour query gets no answer. Decision: leave the broker alone.

**Open / next:**
- Check issue #101114 only if he asks. If Claude Code starts sending OSC 7501, `term.program_status` and `term.program_status_seen` on `sys._stext_ai_terminals[view_id]` hold what arrived (in memory only).
- Not made, by his word: the one-line AgentIDE change (skip `is_widget` views in `_send_view_state`) to stop "[Now in untitled]" on console reads.
- pybackup GUI not run on 3.14 (imports resolve only).
- Laptop cleanup list `C:\Users\donal\data\cleanup_list_2026_10_10.md`: caches, npm global assistants, WSL packages still untouched (WSL: he said remove unused packages and caches, not the install). Ask before each; never delete what he did not name.
- Recycle Bin holds `_downloads`, `st4215_linux`, `sublime_mcp_snapshots`, pkl, vale, sema, xmake, plantuml, pluto, qljs, php-tools, gh_status, deleted by him in Explorer.

**Rules he restated today:** plain short answers; keep tool output small (he scrolls); never use the Bash tool (I made one pointless call); GhostShell and AgentIDE notes go in their own repos, not sublime-mcp; do not delete anything he did not name, check configs first, say so before any permanent delete; no scheduled polling; answers to his typos about frustration: ask the one thing that is wrong. A real soda spill happened near the USB port; he cleaned it, the laptop is fine.
