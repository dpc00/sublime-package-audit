Status: not sent (GitHub issues are disabled on paza/RemotePHPUnit-for-Sublime-Text, last push 2013-10-08; held for Donald's word on emailing the maintainer)

Claude reports:

Two defects in RemotePHPUnit 1.0.0 found on Sublime Text build 4215, Windows (Package Control install, project folder with `app/phpunit.xml.dist` and `tests/FooTest.php`).

1. Default `server_address` is empty. The command only shows a status-bar message ("You have to set the server_address ...") from `__init__` and then runs anyway. Console after "Remote PHPUnit: Run unit tests" on the default settings:

```
Running ssh vagrant@ 'cd //vagrant; /usr/bin/phpunit --exclude-group functional_test -c app/'
```

A standalone run of that line took 14.5 s and ended with `ssh: connect to host  port 22: Connection refused`. Fix: return from `run` when `server_address` is empty. (`cd /` + `root_folder` also gives `cd //vagrant` with the default `/vagrant`.)

2. On Windows "Run tests in current file" sends the local path with backslashes to the remote shell. With `tests\FooTest.php` open:

```
Running ssh vagrant@ 'cd //vagrant; /usr/bin/phpunit -c app/ tests\FooTest.php'
```

Cause: `self.filename[len(self.PROJECT_PATH):]` keeps the local separators. Fix: replace `\` with `/` before building the command.

3. The plugin sets the colour scheme and syntax of the shared `exec` output panel to its own theme and never resets them. After "Run unit tests", a plain `exec` build (`echo control`) in the same window showed the plugin's dark teal Solarized panel. After the package was removed, eight "Error loading colour scheme Packages/RemotePHPUnit/RemotePHPUnit.hidden-tmTheme: Unable to open ..." dialogs appeared (they kept coming back after OK, one per redraw) and blocked the window, which also stopped the next package from loading until all were dismissed. Fix: use the plugin's own panel name, or restore the panel settings after the build.

Not established: the exec output panel stayed empty in my runs (the ssh line also stayed empty under a plain `exec`, so I cannot blame the plugin); no ssh server was available, so a real PHPUnit run was not tested.
