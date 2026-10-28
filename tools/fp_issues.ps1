$repo = 'loquens/subl-open-file-prompt'
$dir = 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\bfc20dab-0668-43bb-b516-26c77432efda\scratchpad'
$b1 = @'
Claude reports:

A failed "Save file" leaves the buffer marked as not modified, so closing it afterwards does not ask to save and the text is lost. Sublime Text 4200, FilePrompt (Package Control build), Windows. In a new tab with the text `important unsaved text`, run `save_file_prompt`, enter a path inside a folder that does not exist (`C:\Users\donal\nonexistent_zz\f.txt`) and press Enter. The console shows

```
File ".../open_file_prompt.py", line 349, in save_file_to_disk
FileNotFoundError: [Errno 2] No such file or directory: '...nonexistent_zz\\f.txt'

During handling of the above exception, another exception occurred:

File ".../open_file_prompt.py", line 355, in save_file_to_disk
AttributeError: 'SaveFilePrompt' object has no attribute 'message'
```

and the view afterwards has `is_dirty() == False` and `is_scratch() == True` while still holding the text. `save_file_to_disk` calls `view.set_scratch(True)` before it writes, and the `except IOError` branch calls `self.message(...)`, which the command class does not have, so the error is raised and the view is never reset (or reopened). Using `sublime.status_message` there, and only setting the scratch flag after the write succeeded, would avoid both.
'@
$b2 = @'
Claude reports:

Tab completion in a directory that does not exist raises a FileNotFoundError. Sublime Text 4200, FilePrompt (Package Control build), Windows. Run `open_file_prompt`, type `nodir_zz\a` after the start folder and press Tab:

```
File ".../open_file_prompt.py", line 269, in on_change
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'C:\\Users\\donal\\nodir_zz\\*.*'
```

The Tab character stays in the input panel and no "No files match" message is shown. In `on_change`, `os.listdir(currentDir)` is called without checking `os.path.isdir(currentDir)`; wrapping it (or checking first) and showing the existing `No files match` status message would handle a mistyped folder name.
'@
[IO.File]::WriteAllText("$dir\fp1.md", $b1)
[IO.File]::WriteAllText("$dir\fp2.md", $b2)
gh issue create --repo $repo --title 'Failed save raises AttributeError (self.message) and leaves the buffer marked scratch' --body-file "$dir\fp1.md"
gh issue create --repo $repo --title 'Tab completion raises FileNotFoundError when the folder does not exist' --body-file "$dir\fp2.md"
