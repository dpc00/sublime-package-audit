# Sublime package audit — agent entry point

This file is the pointer so every harness loads the operating rules (harnesses that read
`AGENTS.md` first would otherwise skip the Claude-local files).

Read, in this order, before any package test, issue or PR:

1. `CLAUDE.local.md` — operating rules: the rig (use `st_portable`, 9512 only), settings hashes,
   no scripts in this repository, ever, and the git discipline (one amended commit).
2. `.claude/skills/sublime-package-audit/SKILL.md` — the whole procedure; read it before a batch.
3. `PROCEDURE.md` — the public description and method.
4. `data/do_not_file.tsv` — repositories that must not receive reports.
