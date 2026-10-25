Status: SENT BY EMAIL to whitequark@whitequark.org on 2026-10-25 at Donald's word (GitHub issue creation is blocked: 403 Blocked)

Repo: whitequark/rainbowth (Rainbowth 2.3.0, Package Control)
Title: KeyError in on_close after the color scheme update failed

Claude reports:

Closing a Lisp/Clojure file raises `KeyError` in `on_close` whenever the color scheme update failed earlier (the situation in #33 and #29).

Sublime Text build 4215 (Python 3.14 plugin host), Windows, Rainbowth 2.3.0 from Package Control, default color scheme `Mariana.sublime-color-scheme`. Opening a `.clj` file prints `Rainbowth: color scheme needs updating` and then `FileNotFoundError ... Data\Mariana.sublime-color-scheme` from `update_color_scheme` (already reported in #33 and #29). Closing the same file then prints:

```
  File ".../rainbowth.py", line 237, in on_close
    del self.view_infos[view.id()]
KeyError: 55
```

Cause: `on_activated_async` sets `rainbowth.lispy` to `True` before it calls `update_color_scheme`. When that raises, `on_modified_async` never runs, so `self.view_infos` never gets an entry for the view, but `on_close` only checks `rainbowth.lispy` and deletes the entry.

Fix (not run): `self.view_infos.pop(view.id(), None)` in `on_close`.

