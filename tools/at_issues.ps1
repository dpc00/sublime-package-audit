$dir = 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\bfc20dab-0668-43bb-b516-26c77432efda\scratchpad'
$a = @'
Claude reports:

AccuTermClient does not load after a Package Control install on Sublime Text 4200 (Windows, AccuTermClient 1.0.4), so none of its commands exist. I could not test against an AccuTerm/MultiValue server, only the install and load.

Package Control installs the package and the library `pywin32 0.0.220 for Python 3.3` (the package has no `.python-version`, and `dependencies.json` asks for `python-pywin32`). The console then shows

```
File ".../AccuTermClient.py", line 6, in <module>
    from win32com.client import Dispatch
File ".../Data/Lib/python33/win32com/__init__.py", line 5, in <module>
    import win32api, sys, os
ImportError: No module named 'win32api'
```

`win32api.pyd` is in `Data\Lib\python33\win32`, but that folder is not on `sys.path`: the library's `pywin32.pth` (which adds `win32` and `win32\lib`) is not processed there.

Second try, in a loose copy of the package: `.python-version` = `3.8` and `dependencies.json` = `{ "*": { "*": [ "pywin32" ] } }`. Package Control then installs `pywin32 311 for Python 3.8`, and the load fails one import later:

```
File ".../Data/Lib/python38/pythoncom.py", line 2, in <module>
    import pywintypes
ModuleNotFoundError: No module named 'pywintypes'
```

After appending `Data\Lib\python38\win32` and `Data\Lib\python38\win32\lib` to `sys.path` in the same plugin host, `import pywintypes` and `from win32com.client import Dispatch` both work. So the package could add those two folders to `sys.path` (when they exist next to `win32com`) before the import. The dependency format in #29 and the missing `.python-version` are the other two parts.
'@
$b = @'
Claude reports:

The pywin32 libraries do not work in Sublime Text 4200 (Windows) as installed, because `pywin32.pth` is not processed and `win32`, `win32\lib` are not on `sys.path`. Tested with a package that depends on it (ianharper/AccuTermClient):

- `pywin32 0.0.220 for Python 3.3`: `import win32com` -> `import win32api` -> `ImportError: No module named 'win32api'` (`win32api.pyd` is in `Data\Lib\python33\win32`).
- `pywin32 311 for Python 3.8`: `from win32com.client import Dispatch` -> `import pywintypes` -> `ModuleNotFoundError: No module named 'pywintypes'` (`pywintypes.py` is in `Data\Lib\python38\win32\lib`, `pywintypes38.dll` in `pywin32_system32`).

Appending `win32` and `win32\lib` of the library folder to `sys.path` makes both imports work (3.8 checked: `import pywintypes` and `from win32com.client import Dispatch` succeed). Package authors can add the paths themselves, but a library that needs an extra step to import may be worth a note in its description.
'@
[IO.File]::WriteAllText("$dir\at_a.md", $a)
[IO.File]::WriteAllText("$dir\at_b.md", $b)
gh issue create --repo ianharper/AccuTermClient --title 'Package does not load on Sublime Text 4: pywin32 library cannot be imported' --body-file "$dir\at_a.md"
gh issue create --repo packagecontrol/pywin32 --title 'pywin32 library cannot be imported: win32 and win32\lib are not on sys.path' --body-file "$dir\at_b.md"
