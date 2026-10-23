Status: not filed (HapoItak is distributed from https://tolemy.sakura.ne.jp/ and has no issue tracker)

Claude reports, two findings (v1.2.9 from Package Control, Sublime Text build 4215):

1. `HapoItak: Replace Html Special Character Set` raises an uncaught `AttributeError` when the current tab has no file name (a new untitled tab):

```
  File ".../HapoItakReplaceHtmlSpecialCharacter.py", line 17, in run
    extension = sublime_view_util.get_extension_from_view(self.view)
  File ".../util/sublime_view_util.py", line 9, in get_extension_from_view
    return get_extension(file_name)
  File ".../util/sublime_view_util.py", line 16, in get_extension
    word_array = text.split(".")
AttributeError: 'NoneType' object has no attribute 'split'
```

`view.file_name()` is `None` for an unsaved tab. Suggested guard: return an empty extension when the file name is `None`. The command also does nothing, without a message, for a saved file whose extension is not html, htm or jsp (not a bug if that is intended).

2. Two invalid escape sequences print a warning in the console every time the plugin loads:

```
.../jsf/autocomp_jsf_if.py:12: SyntaxWarning: "\$" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\$"? A raw string is also an option.
.../jsf/autocomp_jsf_if.py:16: (same)
```

Use raw strings or `"\\$"` on those two lines.

Neither fix was run here.