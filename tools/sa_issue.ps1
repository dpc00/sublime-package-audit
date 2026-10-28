$repo = 'yaworsw/Sublime-ScopeAlways'
$dir = 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\bfc20dab-0668-43bb-b516-26c77432efda\scratchpad'
gh issue list --repo $repo --state all --limit 10 --json number,title,state
$b1 = @'
Claude reports:

"ScopeAlways: Settings" in the command palette cannot open the settings file. Sublime Text 4200, ScopeAlways 0.3.0, Windows. A dialog appears:

```
The settings file "res://Packages/Sublime-ScopeAlways/ScopeAlways.sublime-settings" could not be opened
```

`ScopeAlways.sublime-commands` uses `${packages}/Sublime-ScopeAlways/ScopeAlways.sublime-settings` as `base_file`, but Package Control installs the package as `ScopeAlways`, so the folder `Sublime-ScopeAlways` does not exist. `${packages}/ScopeAlways/ScopeAlways.sublime-settings` would be the right path.
'@
$b2 = @'
Claude reports:

Editing `status_format` in `User/ScopeAlways.sublime-settings` while Sublime Text is running does not change the status bar. Sublime Text 4200, ScopeAlways 0.3.0, Windows. With `{ "status_format": "SCOPE=%s" }` saved, `sublime.load_settings('ScopeAlways.sublime-settings').get('status_format')` returns `SCOPE=%s`, but after moving the cursor the status still shows `source.python ` (the default format). In `plugin_loaded` the callback is registered with `settings.add_on_change('extensions_path', update_settings)`, so it only fires when a setting named `extensions_path` changes, not `status_format` or `status_key`. Registering it on the settings keys the package uses (or `settings.add_on_change('ScopeAlways', ...)` with any key) would apply edits without a restart.
'@
[IO.File]::WriteAllText("$dir\sa1.md", $b1)
[IO.File]::WriteAllText("$dir\sa2.md", $b2)
gh issue create --repo $repo --title 'ScopeAlways: Settings opens Sublime-ScopeAlways, a folder that does not exist' --body-file "$dir\sa1.md"
gh issue create --repo $repo --title 'status_format changes are not applied while running (callback listens to extensions_path)' --body-file "$dir\sa2.md"
