---
name: limitcode-retest-1-1-13-2026-10-31
description: 2026-10-31 Donald asked "retest limitcode (may be updated, at least in repo)": 1.1.13 tested on portable 4215; #11 #13 #14 #15 #17 fixed, #12 still by design; nothing filed
metadata:
  type: project
---

**Ask (2026-10-31):** "retest limitcode (may be updated, at least in repo)". Package Control and the repo both serve 1.1.13 (repo HEAD 90347e6, 2026-10-26). Installed through the Install Package picker on portable 4215, removed through the Remove Package picker, baseline verified, Packages\User\Limitcode (debug log folder) recycled. No keys, offline tool tests only (ToolManager run in a worker thread, see [[project_limitcode_full_test_2026_10_06]]).

**Where it stands:** PR #22 (mine) was closed not merged on 2026-10-07; the author took #11, #13, #14, #16, #17, #18 with co-author credit (1.1.9), did #19-#21 on his own, deferred #15 (done in 1.1.10, commit 693f1b0: edits go to the buffer, not saved) and closed #12 as by design.

**Live results on 1.1.13:**
- #11 fixed: wrong-indent fuzzy edit keeps `    if y:` / `        return 2`.
- #13 fixed: CRLF write gives `a\r\nb\r\n` on disk (no `\r\r\n`).
- #14 fixed: read past the end gives "Invalid range: start_line 99 is after the last line to read (1); the file has 1 lines."
- #15 fixed: edit with unsaved typing leaves the file on disk untouched (buffer only; new open issue #23 asks the same from the user side).
- #17 fixed: relative `d.py` read works.
- #12 unchanged by the author's decision (first of three identical matches replaced, success reported). Empty `old_str` still succeeds (agent argument check blocks it, not user-reachable).
- Not re-run: #16 text, #18-#21 chat/mock paths, new Llamafile provider (1.1.12), sticky scroll (1.1.13).

**Filed:** nothing (#12 is closed with a stated reason; no new defect found). Open issues #23 and #24 are the author's to answer.

**Anthropic key test (same day, he put a key on the clipboard; first clipboard value was 69 chars, not sk-ant, rejected by the API: invalid x-api-key; second was 108 chars sk-ant and worked):** with provider anthropic, model claude-haiku-5-5, the chat sent NO tools: tool_schemas.get_tools_for_provider('anthropic') returns flat ANTHROPIC_TOOLS (3, none with type function) and providers/anthropic.py create_message_with_tools line 185 keeps only type == function, so tools is []. Proven by replaying the request to the API (3 tools: tool_use; tools []: end_turn, no file tool). Filed Jawuilp/Limitcode#26. Key lived only in the portable Limitcode.sublime-settings, recycled; History/logs folder recycled; package removed, baseline verified.

**Provider tests with his keys (api_keys.txt, he asked; labels and lengths only were read, values never printed):** probes: ANTHROPIC works; OPENAI no credits (429 insufficient); GEMINI key 0 works on gemini-flash-lite-latest (2.5-flash no longer available to new users, other models 503/timeout), key 1 list ok; OPENROUTER both keys ok (key 0 about 5.45 of 20 dollars left); OLLAMA cloud ok (not tested in Limitcode). Live in Limitcode 1.1.13 on the portable: GEMINI read_file then edit_file succeeded with dict args, so the #10 EscapeGate fix is confirmed live; OPENROUTER openai/gpt-4.1-mini called edit_file ok; ANTHROPIC fails (no tools sent, issue #26) and with the converter input patched in memory (get_tools_for_provider wrapped) it called read_file and edit_file ok, posted as a comment on #26. Keys lived only in the portable Limitcode.sublime-settings (recycled); package removed, User\Limitcode recycled, baseline verified. Not tested: Moonshot, DeepSeek, Ollama, LM Studio, Llamafile, OpenAI (no credits).
