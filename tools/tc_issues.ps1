$repo = 'gkpotter/Sublime-TinyCodeCounter'
$dir = 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\bfc20dab-0668-43bb-b516-26c77432efda\scratchpad'
$b1 = @'
Claude reports:

The `markers` setting is used as a regular expression, so a marker with a regex character (`(`, `+`, `*`, `[`, `.`, `$`) does not work as written. Sublime Text 4200, TinyCodeCounter 1.0.2, Windows. With the user setting `{ "markers": ["#tc("] }` and a Python view containing

```
x = 1
#tc(
```

no counter appears. The setting is a list of plain strings, but `update()` calls `self.view.find(marker, 0)`, which treats the string as a regex unless `sublime.LITERAL` is passed (an invalid pattern like `#tc(` just never matches, there is no error). `self.view.find(marker, 0, sublime.LITERAL)` would match the marker text exactly. A marker like `#p5t.` would also match `#p5tx` today.
'@
$b2 = @'
Claude reports:

No counter is shown when the marker is on the very first line of the file. Sublime Text 4200, TinyCodeCounter 1.0.2, Windows. A Python view with

```
#tinycode
x = 1
```

shows no phantom, while `x = 1` / `print(x)` / `#tinycode` shows `Char count: 20 (-260)`. In `update()` the test is `if found_start > 0:`, but `view.find` returns `-1` when nothing is found and `0` for a match at the start of the buffer, so `>= 0` is the not-found check. With `include_marker_line` on, the marker line itself is counted, so the first-line case should show a count of 9 for `#tinycode`.
'@
[IO.File]::WriteAllText("$dir\tc1.md", $b1)
[IO.File]::WriteAllText("$dir\tc2.md", $b2)
gh issue create --repo $repo --title 'markers are matched as regular expressions, not literal text' --body-file "$dir\tc1.md"
gh issue create --repo $repo --title 'Marker on the first line of the file shows no counter (found_start > 0)' --body-file "$dir\tc2.md"
