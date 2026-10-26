# Package Control: a package that depends on `requests` gets a `requests` that cannot be imported (found 2026-10-26, row 1419 Share File)

ALREADY REPORTED: sublimehq/package_control#1804 (opened by dpc00 on 2026-10-17, open, label "enhancement"). deathaxe answered the same day: PC was never designed to resolve dependencies recursively, package authors are expected to list all sub-dependencies themselves, and resolving them needs dropping Python 3.3, which will not happen before a next major release. So nothing new was filed for this on 2026-10-26 (Donald asked to check it, then "do file it"; the issue already exists).

What this note adds to #1804: the same failure on the 3.14 host (Share File, `requests` 2.34.2 without `urllib3`), `satisfy_libraries` answering "All libraries have been satisfied!", and `certifi` not being a channel library at all, so an author following deathaxe's advice cannot list it. Not posted anywhere.

## What happens
Portable Sublime 4215 (Python 3.14 host), Package Control 4.2.8, default channel `https://packages.sublimetext.io/channel.json`.

1. Install "Share File" from the picker. Its `dependencies.json` asks for `requests`.
2. Console: `Package Control: Installed library "requests" 2.34.2 for Python 3.14`. Nothing else is installed (`Data\Lib\python314` holds only `requests`).
3. The plugin fails to load: `import requests` -> `requests\__init__.py line 45: import urllib3` -> `ModuleNotFoundError: No module named 'urllib3'`.
4. Command `satisfy_libraries` answers `Package Control: All libraries have been satisfied!` and installs nothing more.

## Why (checked)
- The channel's `requests` library records (py 3.8: 2.32.4, py 3.13/3.14: 2.34.2) are plain PyPI wheels (`files.pythonhosted.org/...py3-none-any.whl`). A library record has only `sublime_text, platforms, python_versions, version, url, date, sha256`; there is no dependency field in any of the 576 release records.
- The wheel itself says `Requires-Dist: charset_normalizer<4,>=2; idna<4,>=2.5; urllib3<3,>=1.26; certifi>=2023.5.7`.
- The channel does have libraries `urllib3` (2.2.3 / 2.8.0), `idna` (3.15 / 3.20) and `charset-normalizer`, but no `certifi` at all.
- Package Control's own source (`package_control/package_manager.py`) takes library names only from the package's `dependencies.json` (`libraries`, or legacy `dependencies`). `distinfo.py` reads only `requires-python` from wheel metadata; nothing reads `Requires-Dist`.

So a package that lists just `requests` works only if it also lists `urllib3`, `idna`, `charset-normalizer` and `certifi` itself, and `certifi` cannot be installed as a library today. The old 3.3 `requests` (2.15.1) was a re-packed copy with its dependencies inside, which is why old packages were written this way.

## Effect
Every package that depends on `requests` and runs on the 3.8, 3.13 or 3.14 host is likely broken on a fresh install (I saw it for Share File; Share File's own backend is dead too, so it is not a good example of a working package). Not tested: a package on the 3.8 host.

## Where it would be reported (his decision)
Either `packagecontrol/channel` (library records for requests) or `wbond/package_control` (resolve wheel `Requires-Dist`). Not done.
