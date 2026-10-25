Status: not sent (GitHub issues are disabled on alfredbez/ReverseCharacters, last push 2017-04-26; held for Donald's word on emailing the maintainer)

Claude reports:

"Reverse characters in selected section" reverses code points, so accented letters and emoji with a skin tone come out broken.

Sublime Text build 4215, Windows, ReverseCharacters 1.0.0 from Package Control. A line containing `cafe` plus U+0301 (combining acute accent), a space, a thumbs-up emoji (U+1F44D) followed by the skin-tone modifier U+1F3FD, a space and `ab`, with the line selected, became:

```
ba [skin tone modifier][thumbs-up] [combining acute]efac
```

The skin-tone modifier now comes before the emoji, and the accent stands at the start of `efac`, after the space, instead of over the `e`. Plain ASCII lines reverse correctly (`abc def` became `fed cba`, also with one cursor per line).

Cause: `stringContents[::-1]` in `reverse_characters.py` reverses Python code points, not user-perceived characters.

Fix: reverse by grapheme (for example with the `regex` module's `\X`, or by keeping combining marks and modifiers attached to the character before them).
