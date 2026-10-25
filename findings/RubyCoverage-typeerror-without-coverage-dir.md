Status: not sent (GitHub issues are disabled on integrum/SublimeRubyCoverage, last push 2015-06-15; not in Package Control's list for ST3/ST4; held for Donald's word)

Claude reports:

Opening any Ruby file that is not inside a project with a `coverage` directory raises a TypeError in the console, and the "Could not find coverage directory" check is never reached.

Sublime Text build 4215, Windows. I downloaded `SublimeRubyCoverage.py` and `Default.sublime-keymap` from this repository into a folder in `Packages` (the package is not in the Install Package list) and opened a three-line `a.rb` in a folder without a `coverage` directory. The `on_load` listener runs `show_ruby_coverage`; the console showed:

```
File ".../SublimeRubyCoverage.py", line 86, in file_exempt
    ignore = os.path.join(root, '.covignore')
TypeError: expected str, bytes or os.PathLike object, not NoneType
```

Cause: `run` calls `self.file_exempt(filename)` before it checks `find_project_root`, and `file_exempt` calls `find_project_root(self.view.file_name())` again and passes the result, `None` when no `coverage` directory exists, to `os.path.join`.

Fix, tested: `ignore = os.path.join(root, '.covignore') if root else None` and `if ignore and os.path.isfile(ignore):`. With that change `show_ruby_coverage` on the same file printed `Could not find coverage directory.` and no traceback.

Also seen by reading: `file_exempt` and `run` print to the console on every Ruby file load, and `Default.sublime-keymap` binds `super+shift+c` on every platform (on Windows `super` is the Windows key).
