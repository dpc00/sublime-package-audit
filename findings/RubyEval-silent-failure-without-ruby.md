Status: not sent (jugyo/SublimeRubyEval last pushed 2013-11-21; open issues unanswered since 2014; held back by the rule to file only on recently active repos)

Claude reports:

When Ruby is not installed or not on PATH, `ruby_eval` fails silently: no message appears and the buffer is unchanged.

Sublime Text build 4215, Windows, RubyEval 2013.11.21.02.45.39 from Package Control, no `ruby` on PATH. A tab containing `1 + 2` with the cursor on the line, `ruby_eval` run: the text stayed `1 + 2`, no dialog or status message appeared, and the console showed a traceback ending in:

```
RubyEval.py, line 12, in eval_as_ruby
    proc = subprocess.Popen(self.ruby(), ...)
FileNotFoundError: [WinError 2] The system cannot find the file specified
```

Cause: `eval_as_ruby` calls `subprocess.Popen(self.ruby(), ...)` without catching `OSError`.

Fix: wrap the call in `try/except OSError` and show `sublime.error_message("Ruby was not found; set ruby_eval.ruby or put ruby on PATH.")`.

Not run (Ruby is not installed on this machine, so the evaluation itself and the output insertion were not tested).

By reading, not run: `eval_as_ruby` runs Ruby on Sublime's main thread and waits in `proc.communicate()`, so a slow script (`sleep 60`) freezes the editor until it ends.
