Status: POSTED 2026-10-25 as diemer/RubyMotionSublimeCompletions#8 (Donald: "2015 is not that long ago, to me")

Claude reports:

The package gives no completions in a Ruby file on current Sublime Text, because its completions file is scoped to `source.rubymotion`, which no syntax in a stock build produces.

Sublime Text build 4215, Windows, RubyMotion Autocomplete 2014.05.05.17.54.29 from Package Control. In a tab set to Ruby I typed `CFURLCopyNe` and opened completions: the status bar said "No available completions". The scope at the cursor was `source.ruby support.class.ruby`.

`RubyMotion.sublime-completions` starts with `"scope": "source.rubymotion"` and holds 18,130 entries (14,869 with a trigger and contents, 3,261 bare strings). The README says to just start typing inside a RubyMotion project, but the bundled Ruby syntax names its scope `source.ruby`; `source.rubymotion` only exists if a separate RubyMotion syntax is installed.

Fix, tested: I copied the completions file into a second package with the scope changed to `"scope": "source.ruby"`. The same input then opened the popup with `CFURLCopyNetLocation`, `CFURLCopyHostName`, `CFURLCopyUserName`, `CFURLCopyLastPathComponent` and the `CFURLCreateCopy...` entries.

Alternative if RubyMotion-only completion is intended: say in the README which syntax package provides `source.rubymotion`, or use a selector such as `source.ruby, source.rubymotion`.

Not tested: the completions inside a RubyMotion project, the insertion of the `${1:...}` placeholders, and `Support/compile_completions.rb` (needs Ruby, not installed).
