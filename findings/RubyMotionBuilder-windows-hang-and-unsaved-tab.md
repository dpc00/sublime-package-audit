Status: POSTED 2026-10-25 as RubyMotionJP/SublimeRubyMotionBuilder#45, #46, #47 (Donald: "2015 is not that long ago, to me")

Three findings, one issue each if this is ever sent. Claude reports:

Sublime Text build 4215, Windows, RubyMotionBuilder 2016.10.24.12.45.43 from Package Control. The package is written for macOS (`sh`, `open dash://`, `/Library/RubyMotion`); these are the problems that show up on any platform with an unsaved tab or on Windows.

## 1. "RubyMotionBuilder: Build" (and Clean, Run, Run Spec, Deploy, Rake list) raises TypeError when the active tab has no file

In an untitled tab I ran `ruby_motion_build`. The console showed:

```
RubyMotionBuilder.py, line 31, in GetProjectRootDirectory
    dir_name = FindRubyMotionRakefile(os.path.split(sublime.active_window().active_view().file_name())[0])
TypeError: expected str, bytes or os.PathLike object, not NoneType
```

No message is shown to the user. `file_name()` is `None` for an unsaved tab.

Fix: return `None` from `GetProjectRootDirectory()` (or show a status message "Save the file first") when `file_name()` is `None`, before calling `os.path.split`.

## 2. By reading (loop checked outside Sublime, not run in it): opening any `.rb` file or `Rakefile` outside a RubyMotion project can hang Sublime on Windows

`FindRubyMotionRakefile` walks up with `while dir_name != "/":` and `dir_name = os.path.dirname(dir_name)`. On Windows `ntpath.dirname("C:\\")` returns `"C:\\"`, never `"/"`, so when no `Rakefile` is found on the way up the loop never ends. I ran the walk in Python on `C:\Users\donal\scratchpad\proj`: it goes `...\scratchpad`, `C:\Users\donal`, `C:\Users`, `C:\`, `C:\`, `C:\`, ... and never reaches `/`. `SetRubyMotionSyntax.on_load` and `on_pre_save` call this for every `.rb` file and `Rakefile`, on the main thread, so the editor would freeze on opening such a file. I did not run it in Sublime, because it would wedge the instance.

Fix: stop when the parent equals the current directory:

```python
parent = os.path.dirname(dir_name)
if parent == dir_name:
    return None
dir_name = parent
```

## 3. SyntaxWarning on load (Python 3.14)

Console at plugin load: `RubyMotionBuilder.py:166: SyntaxWarning: "\w" is an invalid escape sequence` for `re.compile('rake ([\w:]+)')`. Fix: `re.compile(r'rake ([\w:]+)')`.

Not tested: build/run (needs macOS, `rake`, the simulator), the RubyMotion syntax, and the completions generator.
