Status: not sent (neocsr/sublime-RubyMotionSpec last pushed 2013-08-22; no issues; held back by the rule to file only on recently active repos)

Two findings, one issue each if this is ever sent. Claude reports:

Sublime Text build 4215, Windows, RubyMotionSpec 0.1.0 from Package Control. The package is written for macOS (iTerm/Terminal via `osascript`, `cat`, `rm`); these two show up with the default `"terminal": "Sublime"` setting.

## 1. "RubyMotionSpec: rake spec" raises TypeError in an unsaved tab

Run in an untitled tab, the console shows:

```
ruby_motion_spec.py, line 25, in current_dir
    return os.path.split(os.path.abspath(self.current_file()))[0]
TypeError: _path_normpath: path should be string, bytes or os.PathLike, not NoneType
```

and nothing appears for the user. `file_name()` is `None` for an unsaved tab.

Fix: at the start of `run`, `if not self.current_file(): sublime.status_message("Save the spec file first"); return`.

## 2. The spec name is wrong when the path uses backslashes (Windows)

`current_spec` is `self.current_file().split('/')[-1].split('.')[0]`. On Windows `file_name()` has backslashes, so the whole path is returned. With a saved `foo_spec.rb` in a test folder, the exec panel's `[cmd: ...]` line shows:

```
rake spec files=C:\Users\...\rms_fix\foo_spec SIM_STDOUT_PATH=C:\Users\...\rms_fix/_stdout_spec ...
```

instead of `rake spec files=foo_spec`, and the stdout/stderr paths mix `\` and `/`. The command then fails in `cmd` anyway (`'"' is not recognized as an internal or external command`), because the command string starts with a newline and the rest uses `cat`/`rm`.

Fix: `os.path.splitext(os.path.basename(self.current_file()))[0]` for the spec name, and `os.path.join` for the paths. (The `cat`/`rm` steps only work on macOS/Linux.)

Not tested: running the spec (needs macOS, RubyMotion and `rake`), and the iTerm and Terminal modes.
