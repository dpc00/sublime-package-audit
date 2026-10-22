Status: NOT POSTED. The owner (ahuff44) has blocked this account: GitHub returns 403 Blocked on issue creation for ahuff44/sublime-fish-tank. Nothing was posted or sent elsewhere.

Title: All Fish Tank commands fail on ST4: tank tab is empty, ValueError in randint(0, -1)

Claude reports:

On Sublime Text 4 (build 4215, Python 3.14 host) every Fish Tank command fails. The "FISH :D" tab opens empty and the console shows:

```
  File ".../fish_tank.py", line 177, in run
    random.randint(0, TANK_WIDTH-1),
ValueError: empty range in randint(0, -1)
```

Cause: `DuplicateViewToBufferCommand.run` (a TextCommand on the original view) inserts into the new view with `tank_view.insert(edit, ...)`. That `edit` belongs to the original view, so the insert into `tank_view` does nothing, the tank stays empty, `TANK_WIDTH` is 0, and `FishTankCommand` then calls `random.randint(0, -1)`.

Fix: build the tank text in Python (wrapping and padding the lines) and put it in the new view with its own command, `tank_view.run_command("append", {"characters": text})`. In `DuplicateViewToBufferCommand.run`, replace everything from `tank_view.insert(edit, 0, file_text.replace(...))` to the end with:

```python
        text = file_text.replace("\t", " "*tab_size)
        tank_view.set_syntax_file(syntax)

        # set word wrap to maximum line length, otherwise pain
        tank_view.settings().set("wrap_width", 0)
        tank_view.settings().set("word_wrap", False)

        lines = text.split("\n")

        # replace word wrap with newlines
        if force_line_wrap or word_wrap == True or word_wrap == "auto":
            if wrap_width == 0:
                line_length = tank_view.viewport_extent()[0]
                wrap_width = int(line_length / tank_view.em_width())
            if wrap_width > 0:
                wrapped = []
                for line in lines:
                    wrapped.extend([line[i:i + wrap_width] for i in range(0, len(line), wrap_width)] or [""])
                lines = wrapped

        # Determine tank dimensions
        TANK_WIDTH = max(map(len, lines))
        TANK_HEIGHT = len(lines)

        # pad lines with spaces, then put the text in the tank view with its own command
        tank_view.run_command("append", {"characters": "\n".join(line.ljust(TANK_WIDTH) for line in lines)})
```

Tested: with this change in a copy of the package, `fish_tank` with `count: 6` on a four-line file opens the tank with the file's text, the fish are drawn and move, and the console shows "Fish Tank created with 6 fish." and no error. Closing the tank tab afterwards leaves no errors in the console.

Not tried: the `fish_tank_custom` input prompt, the `count_multiplier` commands, and a file long enough to need word-wrap splitting (the tested file had no wrapped lines).
