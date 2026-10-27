# mdTodo (groenewege/mdTodo), found 2026-10-27, queue row 84

Issues are disabled on the repository. Nothing filed or emailed (small findings; the package works).

Seen on Sublime Text 4 (build 4215), Python 3.14 host, Windows, installed through Package Control (Add Repository).

- `mdTodo.py` lines 40 and 50 print `SyntaxWarning: invalid escape sequence` (`"[-\+]"` and `'(\s)*@done(.)+\)$'`) on every load. Raw strings fix it.
- `MdTodoBase.run` (the file-type guard) is never reached: both subclasses define their own `run`, so the guard does nothing. The guard is also wrong as written: `not (filename or filename.endswith(...))` raises `AttributeError` when `filename` is None.
- `md_todo_new` and `md_todo_done` work: in a scratch buffer, `- buy milk` became `+ buy milk @done (2026-10-27 01:28)` and a new `- ` line was added.
