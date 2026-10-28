$repo = 'k-meissonnier/LaravelDumpMan'
$dir = 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\bfc20dab-0668-43bb-b516-26c77432efda\scratchpad'
$b1 = @'
Claude reports:

`dumpman` (F1) inserts nothing, with no message, when the cursor or selection is on the last line of a file that has no trailing newline. Sublime Text 4200, LaravelDumpMan 2.0.0, Windows. Buffer `<?php\n    $foo = 1;` (no final newline), `foo` selected, F1: the buffer is unchanged. The same with a plain cursor on that line. With a trailing newline, or on any other line, the `dd($foo);` line appears below.

The insert is `self.view.insert(edit, line.end() + 1, indentation + content)`. On the last line `line.end() + 1` is one past the end of the buffer, and Sublime Text ignores the insert. Inserting at `line.end()` with a leading `"\n"` when `line.end() == self.view.size()` would cover that case.
'@
$b2 = @'
Claude reports:

`dumpman` can loop forever and freeze Sublime Text when the selected word is followed by `(` that has no `)` and no newline after it until the end of the file. Sublime Text 4200, LaravelDumpMan 2.0.0, Windows. Example: the buffer `<?php\nfoo(` (no final newline, the user is still typing), `foo` selected, F1.

In the `elif self.view.substr(region.end()) == '('` branch the loop

```python
while (self.view.substr(i) != ')'):
    if self.view.substr(i) == "\n":
        errorFunction = 1
        break
    i = i + 1
```

has no end-of-buffer check. Past the end `view.substr(i)` returns `'\x00'`, which is neither `)` nor `"\n"`. Running a copy of the loop on that buffer I stopped it at 100000 iterations (`i` was 100010, buffer size 10), so in the real command the main thread never returns. Stopping when `i >= self.view.size()` and treating it like the newline case would fix it.
'@
[IO.File]::WriteAllText("$dir\ld1.md", $b1)
[IO.File]::WriteAllText("$dir\ld2.md", $b2)
gh issue create --repo $repo --title 'dumpman inserts nothing on the last line of a file without a trailing newline' --body-file "$dir\ld1.md"
gh issue create --repo $repo --title 'dumpman loops forever on an unclosed "(" at the end of the file' --body-file "$dir\ld2.md"
