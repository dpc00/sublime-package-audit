Status: emailed 2026-10-27 (Gmail id 1a17c0f28f357eb9), then a short 'please ignore' follow-up the same day (1a17c17b2074319f) at Donald's word, because ST2 packages get no emails; no more emails will be sent about ST2-only packages.

Package: CompleteSharp (quarnster/CompleteSharp), installed through Package Control with Add Repository, Sublime Text 4 build 4215, Python 3.14 host, Windows.

1. `completesharp.py` line 31 calls `imp.load_source`. The `imp` module was removed in Python 3.12, so the plugin fails on import with `AttributeError: module 'imp' has no attribute 'load_source'`.
2. The installed package contains no `sublimecompletioncommon` folder. It is a git submodule (`.gitmodules`: `git://github.com/quarnster/SublimeCompletionCommon.git`) and the archive Package Control downloads has no submodule files. Line 31 loads `sublimecompletioncommon/completioncommon.py` from that folder.

Nothing else was tested, because the plugin does not get past loading.
