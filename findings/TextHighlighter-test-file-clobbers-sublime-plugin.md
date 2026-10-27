# Text Highlighter (kdnk/sublime_text_highlighter): test_highlighter.py breaks the plugin host

Found 2026-10-27 in a live install-and-load test on portable 4215 (Package Control 0.0.11).

The package root contains test_highlighter.py. Sublime loads every .py file in the package root as a plugin, so on load the file runs
`sys.modules["sublime"] = <stub>` and `sys.modules["sublime_plugin"] = <stub>` (lines 6-12). After that every package in the same plugin host
fails: console fills with `module 'sublime_plugin' has no attribute 'reload_plugin' / 'notify_application_commands' / 'on_modified_async' ...`,
Package Control can no longer open its remove-package panel, and only a restart of Sublime recovers (and the file loads again on the next start).
Also `import highlighter` in that file fails (ModuleNotFoundError) since the package root is not on the path.

Fix: move the tests out of the package root (e.g. tests/ with a .no-sublime-package or exclude via .gitattributes export-ignore so they are not shipped), or do not stub sys.modules at import time.

Not reported: kdnk already has our issue #7 (closed 2026-09-26), so by Donald's rule no email or GitHub action.
