# Static-triage tooling for the Package Control bug hunt (2026-09-25)

Scripts (all expect a scratch dir with `repos/`, `served_idx.json`, `served_info.json`, `available.json`; edit BASE paths at the top):
- `clone_all.py A B N` -- shallow-clone queue entries A..B (GitHub only) into `repos/NNNN_Name`.
- `triage.py A B` -- ruff bug-class rules (F5/F6/F7/F82/B015/B018/PLE/S...) + py3.3-host detector; writes `report_A_B.json`.
- `show_hits.py report.json F821,F823 2 2 [idx,idx]` (env SERVED=1 to restrict to packages Package Control serves on ST 4200) -- prints hits with context.
- `defcheck.py IDX:name,name` -- confirms an undefined name has no definition anywhere in the repo (also check for `globals()[...] =` and `try/except NameError` idioms by hand!).
- `greps.py KIND A B` -- security/pattern scans (unverified TLS, tar extractall, http downloads, yaml/pickle, os.system, callbacks called instead of passed).
- `cmd_scan.py`, `near.py` -- commands referenced in palette/menu/keymap that no class defines (needs `st_known_commands.json` from the ST host); near-miss typo finder.
- `check_served.py` -- downloads the served release archive of each candidate and re-checks root-level .py syntax (needs `served_info.json` from `PackageManager().list_available_packages()`).
- `file_issues.py batch.py` -- files a batch of (repo, title, body) tuples with `gh issue create` (prints only the URL).
- `syntax_scan.py` -- PyYAML check of .sublime-syntax files (noisy: PyYAML != Sublime's parser; kept for reference).
Rules learned: verify every claim (captions, versions, interpreters) BEFORE filing; skip archived repos; one finding per issue; check `git show <served tag>:file` when the served release differs from HEAD.
