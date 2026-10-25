Status: not filed (GitHub issues disabled, repo untouched since 2014-05, and the break is on the newest build; no email sent, his rule on abandoned repos and newest-build lag)

OrigamiEmacs 2014.05.13: sbp.py does not load on Sublime Text build 4215

Console: AttributeError: module 'Default.paragraph' has no attribute 'WrapLinesCommand'. Did you mean: 'OldWrapLinesCommand'? (sbp.py line 105, class SbpWrapParagraphCommand(paragraph.WrapLinesCommand)).
Result: no command from sbp.py is registered. The Windows keymap binds ctrl+x o to sbp_cycle_focus_group; running it via run_command returned ok and the active group did not change (2 stayed 2).
Works: origami.py (create_pane, create_pane_with_file, travel_to_pane, set_layout) on 4215.
README oddities: C-x down/left/right all say 'Move Cursor to pane above'; Move File lists C-x-up etc. but the keymap uses ctrl+k shift+arrow; Zoom lists CMD+] and CMD+[ but the keymap uses ctrl+k ctrl+z / ctrl+k ctrl+shift+z.
Fix (not run): guard the class, for example getattr(paragraph, 'WrapLinesCommand', None) or paragraph.OldWrapLinesCommand.
