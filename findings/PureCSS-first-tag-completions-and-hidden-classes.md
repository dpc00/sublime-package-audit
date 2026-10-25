Status: NOT SENDABLE. Issues #3 and #4 were filed 2026-10-25 on EstebanForge/PureCSS-sublime; at 21:49:52-59 UTC the owner commented "Ty?" on each, closed both "as completed" and disabled the repository's issues, all within seven seconds and with no commit (last push 2017-02-07). Reinvestigated 2026-10-26. Treat the disabled issues as a no-contact signal: no email, no fork, no PR.

Retest on Sublime Text build 4215, Windows, PureCSS 1.0.1 from Package Control (the same version as when the issues were filed).

## 1. Class completions do not appear when `class` is the first `=` before the cursor (issue #3): confirmed, fix tested

In an HTML tab, `<div class="pure-bu` with `auto_complete`: status bar "No available completions" (scope at the cursor was the class string, so the scope is right). `<div id="a" class="pure-hid` offers the list.

Cause: `PureCSS-completions.py` line 130, `if len(parts) > 2 and parts[-2].strip().endswith("class")`. For `<div class=` the split on `=` gives two parts.

Fix, tested: `if len(parts) >= 2 and ...`. In a copy of the package with only that change, `<div class="pure-bu` lists `pure-button`, `pure-button-disabled`, `pure-button-active`, `pure-button-primary`, `pure-button-group`.

The owner closed #3 as completed, but the code on master still has `> 2`; nothing was changed.

## 2. `pure-hidden-*` (issue #4): my report was incomplete

I said `pure-hidden-sd` looked like a typo for `sm` and that `xs`/`sm` were missing, and I wrote "I did not check the Pure project itself". Checking now: the official Pure builds (purecss 1.0.1 and 0.6.2, `pure-min.css` and `grids-responsive-min.css` from unpkg) define no `pure-hidden-*` or `pure-visible-*` class at all, and the plugin's own comment points to yui/pure#326 ("pure-hidden-* removed but not documented"), where the maintainers say the helpers were removed in favour of the HTML `hidden` attribute and responsive CSS. So the plugin offers helper classes (`pure-hidden-sd/md/lg/xl`) that Pure no longer ships; the typo is secondary. `pure-paginator` is not in the 1.0.1 build either. Not checked: whether older Pure versions (before 0.6) had them.

## Reading the owner's reply

"Ty?" most likely means "Thank you?" with doubt, from an owner who did not expect or want a report on a package untouched since 2017. Combined with disabling issues in the same second it reads as "stop". I cannot tell more. Do not contact the owner again.
