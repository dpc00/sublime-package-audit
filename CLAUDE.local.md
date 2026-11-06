# Sublime package audit: notes for Claude

The audit procedure is the skill `sublime-mcp-audit` (`.claude/skills/sublime-mcp-audit/SKILL.md`).
Working notes, one file each with a date, are in `notes/`; the tested list and the test log are in `data/`;
scripts (`rec.ps1` logs one package) are in `tools/`. Check a note's date before relying on it.

First action of a session: read the newest baton note in `notes/` (file name contains "baton"), then say the plan in two lines.

@notes/MEMORY.md

## Git

This repo carries exactly one commit. Amend it for every change and push it
straight away (`git commit --amend --no-edit && git push --force origin main`);
never add a second commit, a backup ref, a tag or a stash. Working material
(`RESULTS.tsv`, `ISSUES.tsv`, `notes/`, `findings/`, `data/`, `lists/`, `scripts/`,
`.claude/`, `.scratch/`) stays on disk and is gitignored, never deleted.
