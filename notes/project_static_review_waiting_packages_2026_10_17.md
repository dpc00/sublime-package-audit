---
name: static-review-waiting-packages-2026-10-17
description: 2026-10-17 read-only source review (no installs) of the toolchain-waiting audit packages; findings by reading only, nothing filed or logged
metadata:
  type: project
---

Donald (feeling unwell, 2026-10-17): "just review/inspect the code for errors, don't download any tools", then "use your own judgement". I read the sources through `gh api` only. Decision: file nothing (all by reading, several unproven; filed reports have not been well received), log nothing in RESULTS.

**Findings by reading (unproven):**
- ElixirFormatter (myskoach/sublime-elixir-formatter): `find_project` stops at `os.path.realpath('/')`, which on Windows is only the current drive's root, so a .ex file on another drive with no mix.exs above it recurses until RecursionError; `file_name.replace(project_root + "/", "")` does nothing with backslashes, so the `.formatter.exs` :inputs check never matches on Windows; formatting runs in a thread on on_pre_save (save race). Issue #11 (test file import) already open.
- SublimeLinter-contrib-codeclimate: `get_working_dir()` is `Optional[str]` in SublimeLinter but is passed straight to `os.path.abspath`; None would raise TypeError instead of the intended PermanentError. `${xoo}` at the end of cmd is undocumented (README only has `args`).
- SublimeLinter-contrib-julialint: SL3-era (`syntax = 'julia'`, no `selector` in defaults); current SublimeLinter sets `cls.disabled = True` and logs an error when `selector` is missing, so it never runs. Lint.jl is dead.
- LSP-tagml: imports `LanguageHandler` from `LSP.plugin`, which current LSP no longer has; also `set(value) + set(new_value)` in merge_configs is a TypeError (latent).
- SublimeLinter-contrib-glslc: nothing certain (`glslc -c` may drop a .spv next to the shader; unverified).
- Not read: OpenDSS and Reach IDE (no Python), AccuTermClient server part, Debugger Maya/3ds Max, GDL (paid), Erlyman/SuperElixir/TestExUnit (WSL).

**Why:** he cannot judge whether to file; I decide, and unproven findings stay as notes.
**How to apply:** if he later says file, test the two provable ones first (codeclimate None, julialint disabled) on the portable.
