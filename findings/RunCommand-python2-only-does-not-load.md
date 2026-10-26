Status: not sent (qfel/RunCommand last pushed 2012-12-08; two open issues unanswered since 2013; held with the other 2012-2013 repos until Donald says)

Claude reports:

The plugin does not load on current Sublime Text: it is Python 2 code, and the three palette commands ("Run Text Command", "Run Window Command", "Run Application Command") do nothing.

Sublime Text build 4215 (Python 3.14 plugin host), Windows. RunCommand is not in Package Control's Install Package list here, so I copied the repo master into Packages. The console shows:

```
RunCommand\RunCommand.py, line 10, in <module>
    from inspect import getargspec
ImportError: cannot import name 'getargspec' from 'inspect'
```

`get_commands` lists `run_text_command`, `run_window_command` and `run_application_command` from the package's `Default.sublime-commands`, but with no class behind them, so choosing one in the palette does nothing and shows no message.

By reading (the import stops first, so these were not reached): the file also needs `izip` (Python 2 only; use `zip`), `unicode()` (use `str`), `commands = map(...)` followed by `commands.extend(...)` (a `map` object has no `extend` on Python 3; use a list), and `spec.keywords` (use `spec.varkw` with `inspect.getfullargspec`, which replaces `getargspec` removed in Python 3.11).

Not tested: the plugin itself, because it does not load.
