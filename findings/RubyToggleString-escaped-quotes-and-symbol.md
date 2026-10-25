Status: POSTED 2026-10-25 as jugyo/SublimeRubyToggleString#4, #5 (Donald: "2015 is not that long ago, to me")

Two findings, one issue each if this is ever sent. Claude reports:

Sublime Text build 4215, Windows, RubyToggleString 2013.10.22.15.10.38 from Package Control. Simple cases work: `"foo"` becomes `'foo'`, `"it's"` becomes `'it\'s'`, `'x'` becomes `%Q{x}`, `"a'b'"` becomes `'a\'b\''`.

## 1. A string with escaped quotes is cut at the first `\"` and the line is corrupted

In a tab I typed `c2 = "say \"hi\""`, put the cursor inside `say` and ran `ruby_toggle_string`. Result:

```
c2 = 'say \'hi\""
```

The string was converted as `"say \"` (the match stops at the first escaped quote), the replacement `'say \'` now ends with an escaped quote, and the rest `hi\""` is left over. The line no longer parses. With the cursor at the end of the line the plugin matched the last two quotes `""` and produced `c = "say \"hi\''`.

Cause: the pattern `(".*?"|\'.*?\'|%Q{.*?})` in `RubyToggleString.py` does not treat a backslash-escaped quote as part of the string.

Fix: match strings with escapes, for example `"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|%Q\{[^}]*\}`.

## 2. "Toggle string and symbol" turns `"hello world"` into the invalid `:hello world`

Cursor inside `e = "hello world"`, `ruby_toggle_string_and_symbol`. Result: `e = :hello world`. A symbol containing a space (or any non-word character) needs quotes: `:"hello world"`.

Fix: only drop the quotes when the inner text matches `\A\w+\z`; otherwise produce `:"` + inner + `"`.

Not tested: `RubyToggleHashSymbol`, multi-line strings (documented as unsupported), and `%Q{}` strings with braces inside.
