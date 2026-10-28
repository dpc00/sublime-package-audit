---
name: redo-list-name-matching-2026-10-16
description: I told him big installs were still open when they were done under renamed tsv rows; a redo or to-do list must be matched by prefix AND checked against GitHub issues before I state what is left; Yollama is skipped by his order
metadata:
  type: feedback
---

2026-10-16: after the redo batches I told Donald that LanguageTool (local server), LSP-Bicep, DFormat, IrView and LSP-bitbake were still open "per the redo list". He said they were done and that I had failed to log properly. He was right: they were done 2026-10-13 under renamed tsv rows ("LSP-Bicep (real .NET 10 test)", "LanguageTool (local server)", "DFormat (real dfmt)", "IrView (real LLVM + Graphviz)", "LSP-bitbake (real server, no Yocto)") and Scheme 2026-10-14. The redo list (built 2026-10-14 from the status of the earlier rows) never matched those names. He also said he had ordered Yollama skipped; that order is not in the tsv or notes, so I recorded it now.

**Why:** he cannot remember what was done and relies on the lists; a wrong "what is left" costs him a day of retests and makes him distrust the records.

**How to apply:** before saying what is left, match each name by PREFIX (rows carry suffixes like "(real ...)", "fix PRs", version numbers), look at ALL rows of that name and their dates, and cross-check `gh search issues --author dpc00 "<package>"` when in doubt. Never copy a category ("deferred", "partly untried") from an old status file as if current. Annotate the redo file when a package is done: `C:\Users\donal\data\st_packages\audit_redo_skipped_2026_10_14.tsv` now has DONE/SKIPPED prefixes. See [[project_session_baton_2026_10_16_redo_batch1]] and [[feedback_procedures_are_skills_2026_10_13]].
