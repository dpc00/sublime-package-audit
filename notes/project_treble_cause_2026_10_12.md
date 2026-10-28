---
name: treble-white-tab-cause-2026-10-12
description: Theme - Treble issue #1 (white selected tab) traced on 4200; package defaults not applied, comment posted
metadata:
  type: project
---

2026-10-12: Theme-Treble#1 (white selected tab, Treble Dark + Mariana, Windows 11, build 4200). Maintainer 53v3n3d4 asked why Mariana's accent doesn't show.

Cause found: Sublime here returns nothing for `tab_style`, `accent_color`, `dark_theme_style` (get_setting), although the package's own Preferences.sublime-settings defines them. All tab rules need those settings, so only the base `tab_control` rule (layer1.opacity 1, no tint) applies = opaque white block. Deleting that rule removes the white; deleting mi rules, textures or tabset margins did not. Setting `"tab_style": "mi"` in User prefs fixes it; adding `"accent_color": "color-scheme"` shows Mariana's blue accent.

Posted on Donald's "go for it": https://github.com/53v3n3d4/Theme-Treble/issues/1#issuecomment-6134280238 (suggested fix: base rule layer1.opacity 0). Not known why defaults apply on macOS.

Test copy removed (portable 4200 package, unpacked folder, ZMar scheme recycled; settings restored from backups). Gotcha: the theme only reloads when Preferences change (toggle tab_style to force); removing a color scheme file while it is selected makes a dialog on every palette open.

**Why:** Donald asked for the investigation. **How to apply:** wait for maintainer reply; don't file more.

**CORRECTION (2026-10-12 late):** the first comment's cause was incomplete. Sublime reads a package's own Preferences.sublime-settings only at startup; right after installing in a running session all its defaults (tab_style, dark_theme_style, adaptive_theme_style, folder_icon_color) are missing, and after a restart they are present and Treble Dark + Mariana looks right (no white block). Tested with a throwaway package too: same, so it is general Sublime behaviour. Correction posted on Donald's "post it": https://github.com/53v3n3d4/Theme-Treble/issues/1#issuecomment-6135042240 (answers Seven Eda's two questions, suggests base rule not draw white without tab_style, or a restart note).

**Lesson for the audit:** for any package that ships Preferences.sublime-settings (themes especially), restart the test Sublime after installing before judging missing defaults; a finding made before a restart can be wrong. Check "ST restart" before blaming the package.

