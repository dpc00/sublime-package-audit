---
name: exact-quick-find-pr3-retest-2026-10-15
description: 2026-10-15 retest of the Exact Quick Find goto_next leak with real keys on 4215: real repro is Add All then Goto Anything (Ctrl+G :1:17) then Goto Next; the old PR #3 fix cures it; clone ready, no fork, no PR yet
metadata:
  type: project
---

**Why:** aafulei (maintainer of aafulei/sublime-exact-quick-find) could not reproduce my issue #1 part 2 with mouse and keyboard on PR #3 (closed when the forks were deleted 2026-10-14). My original PR body admitted the check ran only on a mock of the sublime API and the repro used `sel.clear()` (an API call, not a user action).

**Finding (real keys, portable 4215, package 1.0.1, keymap ctrl+e = goto_next, ctrl+alt+d = add_all):**
- Shift+arrow or mouse selection after Add All: no leak (on_post_text_command resets the session). Same as the maintainer saw.
- REAL REPRO: buffer `aaa xxx aaa yyy aa`; select first `aaa`, Add All (2 regions); Ctrl+G, type `:1:17`, Enter (caret moves into the trailing `aa` without a text command, status bar still shows the old session "Region 1/2"); Goto Next selects the second `aaa` ("Region 2/2") instead of an `aa` match.
- Old PR #3 commit cherry-picks cleanly onto current main (5b5e146); with it the same steps select only the trailing `aa` ("Region 1/1").

**DONE 2026-10-15 on his word "go ahead, fork it and open the PR": fork dpc00/sublime-exact-quick-find re-created, branch pushed (remote `fork` in the clone), PR https://github.com/aafulei/sublime-exact-quick-find/pull/5 opened with the real-key steps. No comment posted on #3 (closed). Any reply from aafulei: tell Donald, do not answer. The state line below is from before the PR.**

**State:** clone with the fix on branch `fix-stale-session` (commit 5114fde) in `C:\Users\donal\tools\forks\sublime-exact-quick-find` (origin = upstream, NO fork on GitHub). 4215 is clean (junction and test keymap removed; 4215 quit); the 1.0.1 zip was moved to the session scratchpad. Nothing posted, no PR opened: PRs and forks are paused (procedures.md); needs Donald's word, then re-create the fork, push, open a new PR whose body gives the real-key steps (no mock claim) and answers aafulei's two questions (sel.clear() was a script call; the real way is Goto Anything).

**Lessons:** a package installed into a running 4215 did not register commands until 4215 was restarted; the first Add All/Goto command only initialises the session when the state is not BASIC; ui_press_key with modifiers needs method "input"; a posted Return is lost if the overlay is not open yet (it landed in the buffer once); the 4215 "Error loading colour scheme GhostShell/ai_terminal" dialog comes from the old omp-test tab after each restart, dismiss with dismiss_native_window ok.
