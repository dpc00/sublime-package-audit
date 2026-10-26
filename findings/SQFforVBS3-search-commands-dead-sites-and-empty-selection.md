Status: not sent. zahngol/SQF-VBS3 was last pushed 2016-11-23, and the product it serves (VBS3, BISim) has moved on: the search commands open sites that no longer answer. Held as a finding; nothing posted.

Sublime Text build 4215, Windows. SQF for VBS3 1.0.1 installed from Package Control's Install Package list. Syntax ("SQF - VBS3" is picked automatically for `.sqf`), completions (`hintS` offers `hintSilent`) and snippets (`while`, `includeDIK`, `includeFunctions`, backslashes kept) all worked live.

## 1. By reading (not run): "Search Selection" with nothing selected searches for empty text

`VBS3_Resource_Search.py`, all three `*SearchSelectionCommand` classes:

```python
if selection.empty():
    text = self.view.word(selection)

text = self.view.substr(selection)
```

`text` is overwritten on the next line, so for an empty selection the search is for an empty string, although the README promises the highlighted word. Fix: `text = self.view.substr(self.view.word(selection))` in the `if`, and `else` for the second assignment. Not run, because the commands open the default browser.

## 2. By reading: VBS Forums search URL has `q=test` hard-coded, and its input prompt says "Dev Ref"

`SearchForumsFor` builds `https://forums.bisimulations.com/search?q=test&searchJSON=...`, and `VbsforumsSearchFromInputCommand` asks "Search VBS3 Dev Ref for" (copied from the Dev Ref command).

## 3. By reading: color picker validity check does nothing

`VBS3_Color_Picker.py`, `__is_valid_vbsrgb_color`: the line `0 < float(x) < 1` is an expression whose result is discarded, so any three comma-separated numbers count as a valid colour. Not run: `color_pick` opens the native Windows colour dialog, which can freeze Sublime.

## Why nothing was filed

Checked 2026-10-26 with curl: `resources.bisimulations.com` gives no answer, and `manuals.bisimulations.com` and `forums.bisimulations.com` both redirect to https://onearc.com/. The three search shortcuts therefore lead nowhere, and the maintainer has not touched the repo in ten years.
