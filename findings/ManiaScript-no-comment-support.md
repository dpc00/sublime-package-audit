Status: not filed (issues are disabled on Anthodev/Sublime-ManiaScript, last push 2013-08-16; no email sent, see notes digitrev-asked-why-issues-2026-10-24)

Claude reports:

Toggle Comment does nothing in a ManiaScript file: the package has no comment settings.

Steps: Sublime Text build 4215, ManiaScript (2013.08.16 release) from Package Control, a file `t.Script.txt` (opens as ManiaScript, scope `source.ms`). Put the cursor on the line `declare Integer X = 1; // comment` and run Toggle Comment (Ctrl+/). Nothing is inserted and the buffer stays unmodified.

Cause: the package contains only `ManiaScript.tmLanguage` and `ManiaScript.sublime-completions`. There is no `.tmPreferences` file that sets `TM_COMMENT_START` / `TM_COMMENT_START_2` / `TM_COMMENT_END_2` for `source.ms`.

Related oddity: the text after `//` has the scope `comment.block.ms`, not a line-comment scope.
