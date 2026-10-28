$repo = 'AlexLamson/DataWrangler'
$dir = 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\bfc20dab-0668-43bb-b516-26c77432efda\scratchpad'
$b1 = @'
Claude reports:

All four commands that write to a new tab (`line_freq`, `flatten_list_of_lists`, `align_columns`, `delete_columns`) open an empty tab on Sublime Text 4200 (Data Wrangler 1.1.0, Windows). Example: a view with the lines `b`, `a`, `b`, `B`, `c`, then "Data Wrangler: Write word/line frequencies to a new tab" gives a new untitled tab with 0 characters, and no error in the console.

The code does `new_view = sublime.active_window().new_file()` and then `new_view.insert(edit, 0, output_string)`, using the `edit` of the original view. A minimal TextCommand that does the same (`nv.insert(edit, 0, 'hello')`) returns 0 and leaves `nv.size()` at 0 on this build, while `self.view.insert(edit, 0, 'X')` works. Inserting with `new_view.run_command('append', {'characters': output_string})` avoids the edit token.
'@
$b2 = @'
Claude reports:

`delete_columns` raises an AttributeError on space-separated data. Sublime Text 4200, Data Wrangler 1.1.0, Windows. A view with

```
aa bb cc
dd ee ff
```

and the cursor on the first line, "Data Wrangler: Delete all columns that contain cursor":

```
File ".../DataWrangler.py", line 255, in run
AttributeError: 'NoneType' object has no attribute 'join'
```

In `detect_separations` the last branch is `else:` followed by a bare `' '` with no `return`, so the function returns `None` when the first line has neither a tab nor a comma. `align_columns` survives that because `line.split(None)` splits on whitespace, but `sep.join(filtered_columns)` in `delete_columns` does not. `return ' '` would fix it.
'@
$b3 = @'
Claude reports:

"Data Wrangler: Write word/line frequencies to a new tab" raises a ValueError on an empty view. Sublime Text 4200, Data Wrangler 1.1.0, Windows:

```
File ".../DataWrangler.py", line 93, in run
ValueError: max() arg is an empty sequence
```

The same happens for a view that has only blank lines, since blank lines are dropped before counting. A check for an empty `lines` list before `max(counts[x] for x in counts)` would avoid it.
'@
[IO.File]::WriteAllText("$dir\dw1.md", $b1)
[IO.File]::WriteAllText("$dir\dw2.md", $b2)
[IO.File]::WriteAllText("$dir\dw3.md", $b3)
gh issue create --repo $repo --title 'New-tab commands open an empty tab: insert(edit) used on another view (ST 4200)' --body-file "$dir\dw1.md"
gh issue create --repo $repo --title 'delete_columns: AttributeError on space-separated data (detect_separations has no return)' --body-file "$dir\dw2.md"
gh issue create --repo $repo --title 'line_freq: ValueError on an empty view' --body-file "$dir\dw3.md"
