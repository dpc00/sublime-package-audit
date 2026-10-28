---
name: session-baton-2026-10-21-fresh-list-batch2
description: START HERE (newest, audit): fresh list worked from Nord through Language - Spanish on portable 4215; 8 issues filed, rules 6c-6e added, Unity Completions and sass-lint deferred
metadata:
  type: project
---

Baton written 2026-10-21 evening, batch boundary. Supersedes `project_session_baton_2026_10_21_fresh_list.md` (same list, state moved on).

**Where the audit is.** List `C:\Users\donal\data\st_packages\audit_list_2026_10_21_fresh.tsv` (copy in repo `data\`), 2,447 rows left. Next by order: Gradle_Language, MasmAssembly. Skip by name: Deviot (Arduino IDE, deferred), SublimeLinter-contrib-sass-lint (npm install stalled, deferred, test folder `tools\sasslint_test` has only package.json). Unity Completions was skipped (209,208 snippet files, install did not finish after 8+ minutes; logged in RESULTS).

**Per package (unchanged):** install through the palette picker on portable 4215 (server `mcp__sublime-mcp-portable-4215__*`), inspect the zip, test, `remove_package`, `tools\rec.ps1`, `refilter.py` (scratchpad) + copy list into repo `data\`, `tools\commit_day.ps1` (amends the day commit, force-with-lease). Restore the portable's `Preferences.sublime-settings` to 168 bytes after theme tests. A stuck `Installing package Unity Completions` text stays in the portable's status bar; it is harmless, the other installs work.

**Filed this stretch (all "Claude reports:", fix tested, repo not archived):** onhernandes/sublime-scss-snippets#2 (unescaped `$` in for/each/while/adjust-color), stormwarning/jsont-tmbundle#5 (injections not applied), kliu/sublime-theme-lanzhou#2 (messages.json trailing comma + wrong file), UnicornForest/Unity3DSnippets#3 (unclosed `${3:`), jampow/velocity-sublime#7 (`$_reader` unescaped), petereichinger/Unity3D-Shader#10 (scope source.shader vs source.unity_shader); comment on mattbanks/dotfiles-syntax-highlighting-st2#42 (settings file named for a syntax that no longer exists). Earlier in the day: Bootstrapper, Media Query, Simple JSX, CUDA, Hero Light, Vim Blackboard, HTML Mustache.

**Skill:** `sublime-mcp-audit` rules 6c (spaced tabTriggers), 6d (`$` in snippets, install Sass package for scss scope), 6e (never wait silently; defer stalled npm/downloads).

**Rules he restated today:** keep going without stopping; he saw a blank screen for 7 minutes while I waited on npm, so say a line before any wait over a minute. His internet is 93 Mb/s (curl measured 9 MB/s); a slow Package Control or npm run is not the line, check the package size (`gh api repos/OWNER/REPO --jq .size`) first.

**Open/parked (not the plan):** bug log entry B6 in sublime-mcp `.claude\memory\project_bug_log_2026_10_20.md` (large package install never finishes, no progress tool and no cancel).
