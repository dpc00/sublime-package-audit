Status: not filed (SublimeText/GotoTab has issues disabled)

Claude reports:

`goto_tab` with `"tab": "last"` (the default `ctrl+9`) raises an uncaught IndexError when the window has no open tabs.

Installed v2016.09.27 from Package Control, Sublime Text build 4215. With every tab closed, run `goto_tab` with `{"tab": "last"}`:

```
  File ".../GotoTab.py", line 8, in run
    self.window.focus_view(self.window.views()[len(self.window.views()) - 1])
IndexError: list index out of range
```

Fix I tested (loose copy in Packages): at the start of `run`, `views = self.window.views()` and `if not views: return`. After that the command does nothing and the console stays clean.

Also seen: `"tab": "0"` (only reachable through a custom keymap) focuses the last tab, because `views()[-1]` is valid in Python.