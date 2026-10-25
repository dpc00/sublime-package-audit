Status: not sent (zmbacker/RubyFormat last pushed 2012-11-01; one open issue from 2019 unanswered; held back by the rule to file only on recently active repos)

Three findings, one issue each if this is ever sent. Claude reports:

## 1. The package does not load on Sublime Text 4: Python 2 `print` statement

Sublime Text build 4215, Windows. RubyFormat is not in Package Control's Install Package list here, so I copied the repo master into Packages. The console shows:

```
RubyFormat\rubybeautifier.py, line 197
    print "Error: indent/outdent mismatch: %d."%(tab)
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

"Format: Ruby" is still listed in the command palette (from `RubyFormat.sublime-commands`), but `get_commands` shows no class behind `ruby_format`, so choosing it does nothing.

Fix (tested): `print("Error: indent/outdent mismatch: %d." % (tab))`.

## 2. After that, `import rubybeautifier` fails

With the print fixed, `ruby_formatter.py` fails with `ModuleNotFoundError: No module named 'rubybeautifier'` (line 5). The plugin directory is not on `sys.path` on current Sublime Text.

Fix (tested): `from . import rubybeautifier`. With both changes the plugin loads and `ruby_format` is registered.

## 3. The cursor jumps to the end of the file when it starts before the first non-whitespace character

With both fixes applied I put this in a tab, with the cursor at the very start of the file, and ran `ruby_format` with nothing selected:

```
class A
def run(x)
if x > 1
...
```

Indentation was fixed correctly (`class A`, tab-indented `def run(x)`, nested `if`/`else`/`end`, `[1,2].each do |i|`), but the cursor ended at line 13 (the end of the file) instead of staying at the start.

Cause: `get_nws_offset` counts non-whitespace characters before the cursor (0 here) and stops when `nonWsSeen == nonWsChars`, but it increments `nonWsSeen` before the comparison, so with 0 it never matches and the loop runs to the end of the buffer.

Fix: return 0 early when `nonWsChars == 0`, or compare before counting.

Minor: `re.findall('\S', preTxt)` in `ruby_formatter.py` line 57 raises a SyntaxWarning on load on Python 3.14 (`"\S" is an invalid escape sequence`); use a raw string.

Not tested: formatting a selection (`indent_base` path), and formatting files with heredocs, `case/when`, `begin/rescue` or one-line blocks.
