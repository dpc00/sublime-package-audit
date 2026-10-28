$repo = 'monsieurluge/ruler_proximity_indicator'
$dir = 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\bfc20dab-0668-43bb-b516-26c77432efda\scratchpad'
$b1 = @'
Claude reports:

`rulers` set per syntax, per project or per view are ignored. Only `Preferences.sublime-settings` is read. Sublime Text 4200, RulerProximityIndicator 1.0.1, Windows. With `"rulers": [40]` in the user Preferences and a view with a 38 character line, the indicator is `─═─┼───` (two columns before the ruler). After `view.settings().set('rulers', [100])` on that view the indicator stays `─═─┼───`, it should move to the far left (62 columns before the ruler). The same code path means syntax-specific and project `rulers` are not used either.

`on_activated` does `sublime.load_settings('Preferences.sublime-settings').get('rulers')`. `view.settings().get('rulers')` returns the value that is in effect for that view (it also includes the Preferences value when nothing overrides it).
'@
$b2 = @'
Claude reports:

With no rulers configured the indicator is stuck at the right end. Sublime Text 4200, RulerProximityIndicator 1.0.1, Windows, default Preferences (`"rulers": []`): every line, short or long, shows `───┼──═`. The class has `rulers = [80]` as its default, but `on_activated` replaces it whenever `settings.get('rulers') is not None`, and Sublime Text's own default for `rulers` is `[]`, not unset, so the `[80]` is never used once a view is activated. Treating an empty list like "not set" (`if settings.get('rulers'):`) would keep the 80 default, or the README could say that a ruler must be configured.
'@
$b3 = @'
Claude reports:

A tab counts as one column, so lines indented with tabs show the wrong distance to the ruler. Sublime Text 4200, RulerProximityIndicator 1.0.1, Windows, `"rulers": [40]`, `"tab_size": 4`. A line made of 10 tabs ends at column 40, exactly on the ruler, but the indicator is `═──┼───` (far left, 30 columns away), because `line_length = view.line(point).size()` is a character count (10). Rulers are drawn at visual columns, so the line length needs tabs expanded to `tab_size` before comparing.
'@
[IO.File]::WriteAllText("$dir\rp1.md", $b1)
[IO.File]::WriteAllText("$dir\rp2.md", $b2)
[IO.File]::WriteAllText("$dir\rp3.md", $b3)
gh issue create --repo $repo --title 'rulers from syntax, project or view settings are ignored (only Preferences is read)' --body-file "$dir\rp1.md"
gh issue create --repo $repo --title 'Default [80] is never used: an empty rulers list overrides it' --body-file "$dir\rp2.md"
gh issue create --repo $repo --title 'Tabs count as one column in the distance to the ruler' --body-file "$dir\rp3.md"
