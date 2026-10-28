---
name: track-test-installs-2026-10-10
description: 2026-10-10 Donald was sickened by the pile of untracked test leftovers (Swift 4.9 GB, toolchains, installers, jcode launcher copies); every test install gets logged when made, and test downloads go in one folder
metadata:
  type: feedback
---

2026-10-10, after a disk review (Ollama models 37 GB, ~/.codex 8.7 GB, old installers, Swift, jcode launcher-old copies 4.5 GB): Donald said the amount of questionable items "is literally making me ill" and that if he keeps going this way it becomes a mess too hard to fix.

**Why:** the mess came from test installs and downloads that nothing tracked, so cleanup meant rediscovering them and asking him item by item.

**How to apply:**
- When I install anything for a test (toolchain, app, package, npm global, model), append one line at once to `C:\Users\donal\data\test_installs.md`: date, what, size, why, how to remove.
- Download test installers to `C:\Users\donal\data\test_downloads\`, not `~\Downloads`; remove them when the test ends (Recycle Bin, see [[feedback_recycle_bin_and_keep_big_tools]]).
- At cleanup, work from that list; delete only what he names. A monthly check happens only when he asks (no scheduled polling).
- Keep replies short and ask at most one thing when he is upset ([[feedback_plain_short_answers_no_menus]]).

**2026-10-24 repeat:** he asked what was lying around; Ruby 3.4.11 and its MSYS2 (C:\Ruby34-x64, per-user installs from Sep 26 / Oct 2) were still installed and I could not say who installed them because no log had ever been kept. He said "you didn't take notes", then that a log is pointless now and that he will not allow any more installs outside Package Control. I deleted the log file I had just made. Rule now: install nothing except packages through Package Control; each is removed and verified in the same step. Ruby/MSYS2 still installed, removal awaits his go.

Done 2026-10-10: removed gemini-cli, excel MCP (npm + configs in Claude, Codex, antigravity, jcode, kimi), 4 npm test helpers, Swift, old Temp, kimi updater leftovers; recycled all of Downloads and 37 jcode `.jcode-launcher-old-*.exe`. Later same day he said he is disgusted with Ollama (no local model works here, cloud models cost money): Ollama fully removed (program, ~/.ollama 37 GB, 4 pip packages via UAC, the "vision" MCP entries in Codex/jcode/kimi/Cursor configs); do not reinstall or suggest local models. Also deleted: bun cache, ~/.cache, ~/.codex/.tmp, .rustup, .cargo, .dotnet, .julia (+ PATH entries). C: free went 197.9 to 255.8 GB. Left: ~/.codex packages 6.8 GB, ~/.local\share 4.9 GB, WSL disk 20 GB (own setup). Recycle Bin (about 9.6 GB) kept for a week by his wish. Codex removed on his word ("I'll never use codex"): npm package, ~/.codex, AppData\Local\OpenAI. NEVER remove Junie (~/.local/share/junie, 3 GB): it is part of his IntelliJ setup; do not suggest it again. Later: agent purge on his word ("agents I will never miss"). Removed: Kimi, Kiro (IDE+CLI), mimocode, muse, amp, pi, T3, Cursor, mistral-vibe, ori, qwen data, and npm auggie/continue/dsh/copilot/kilocode/cline/opencode/prime-agent with their data. KEPT by his word: omp, Devin, jcode, Junie, Antigravity, Claude Code (Grok not confirmed, nothing of it touched). C: free ended at 293.4 GB after WSL cleanup: removed agent/Ollama leftovers in ~, apt toolchains (clang, valac, ruby, php-cli, mercurial, meson, ninja, cscope, diction, kcolorchooser, fcitx; autoremove also took zip/unzip), then wsl --shutdown + elevated diskpart compact: ext4.vhdx 19.9 to 9.8 GB. WSL (and the WSL Sublime / tab-2 terminal) was shut down and must be relaunched. llvm-21-dev (368 MB) still needed by something. sudo in WSL was cold: ask him to type the password in the tab, never type it myself.
