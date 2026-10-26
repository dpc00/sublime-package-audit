Status: not sent. shagabutdinov/sublime-run-macro-file-with-context was last pushed 2015-03-30 (the author is active elsewhere); no open issues. The README does name the dependency (Context) and says the package belongs to sublime-enhanced, so this is a documentation/packaging gap rather than a defect; kept as a finding.

Sublime Text build 4215, Windows. RunMacroFileWithContext 1.0.0 installed from Package Control's Install Package list.

Observed:

1. Right after the install, the plugin fails to import and its command `run_macro_file_with_context` is not registered (`get_commands` shows nothing for the package; the picker gave no message):

```
RunMacroFileWithContext\commands.py, line 3, in <module>
    from Context import context
ModuleNotFoundError: No module named 'Context'
```

2. After installing `Context` (also from the picker, v2016.10.25), `Context` itself fails the same way, two hops down the chain:

```
Context\base.py, line 4, in <module>
    from Expression import expression
ModuleNotFoundError: No module named 'Expression'
```

3. From reading `Context`'s own source (not run): it imports `Expression`, `Statement` and `IndentationNavigation`, all packages by the same author. None of the packages declares its dependencies for Package Control (no `dependencies.json`), so a user who installs only RunMacroFileWithContext, as the picker invites, gets a package that silently does nothing. After installing `Expression` the console showed it loading cleanly; I did not install `Statement` or `IndentationNavigation`.

Not tested: the macro itself (`run_macro_file_with_context` with `context` entries), which needs the whole chain installed plus a restart of the plugin host, since a module that failed to import is not retried when a dependency is installed later.

Possible fix for the maintainer: a `dependencies.json` in each package (for example `{"*": {">=3000": ["..."]}}` with libraries, or documenting the install order in the package's Package Control description, which currently reads "No description provided").
