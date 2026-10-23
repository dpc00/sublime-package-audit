Status: not filed (no repository or tracker found; Package Control lists only its own page)

# Game of Life: TypeError on every frame when the file contains "İ" (U+0130)

Claude reports:

Running `simulate` (Ctrl+Alt+G) on text that contains `İ` (capital I with dot above) raises a TypeError on the first frame and the buffer is not animated.

Tested on Sublime Text 4, build 4215, Windows (package 0.1.4). Text `İstanbul abc def`, then the `simulate` command; the console shows:

```
  File ".../GameOfLife.py", line 88, in nextFrame
    if living(cell):
  File ".../GameOfLife.py", line 159, in living
    return ord('a') <= ord(char.lower()) <= ord('z')
TypeError: ord() expected a character, but string of length 2 found
```

Cause: `'İ'.lower()` is two characters (`i` plus a combining dot), so `ord()` fails. Any file with that letter (Turkish text) triggers it.

Fix in `living()`, which avoids `lower()` so non-ASCII letters are simply not living:

```python
def living(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'
```

`generateLivingCharacter` only receives characters that passed `living()`, so its `ord(l.lower())` is then safe.

Tested as a loose copy of `GameOfLife.py`: the same text animates (`  tanbu   b   e `) with no traceback, and a second `simulate` restores `İstanbul abc def`. Plain ASCII text behaves as before.
