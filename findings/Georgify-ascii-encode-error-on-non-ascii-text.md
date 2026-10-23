Status: not filed (no issue tracker: the package page is the UWaterloo SE212 course site)

# Georgify: "Ask George" raises UnicodeEncodeError when the file has a non-ASCII character

Claude reports:

Tested on Sublime Text 4, build 4215, Windows (package 1.0.5, Python 3.14 plugin host). In a tab containing `café = 1`, Georgify: Ask George (`georgify`) fails with this console traceback and shows no message:

```
  File ".../georgify.py", line 11, in run
    screenText = self.view.substr(sublime.Region(0, self.view.size())).encode('ascii')
UnicodeEncodeError: 'ascii' codec can't encode character '\xe9' in position 3: ordinal not in range(128)
```

Any accent, symbol or non-English letter in the buffer (including in a comment or string) triggers it, so the command cannot be used on such a file.

Fix: encode as UTF-8, `.encode('utf-8')`, and send `Content-Type: text/plain; charset=utf-8`, provided the George server accepts UTF-8 (not checked; I did not send test text to the university server).

Also: `urllib.request.urlopen` has no `try`/`except`, so a server that is down or unreachable also only produces a traceback in the console.
