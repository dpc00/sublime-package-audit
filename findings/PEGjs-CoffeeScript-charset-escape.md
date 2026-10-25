Status: emailed to felixhao28@gmail.com 2026-10-25 (issues are disabled on felixhao28/Sublime-PEGcoffee)

Subject: PEGjs CoffeeScript: escaped ] ends a character class early

Claude reports:

Sublime Text build 4215, Windows, PEGjs CoffeeScript 1.0.0 from Package Control, syntax "PEG.js CoffeeScript". In a tab I entered

```
start = a:item+ { return a }
item "item" = [\]x] 'y'
/** doc */
```

and read the scope at the cursor:

1. In `[\]x]` the class is ended by the escaped bracket: `[\]` is `keyword.operator`, but `x` is only `source.pegcs`. The grammar's `charSet` rule is `begin \[` / `end \]` with no pattern for `\\.`, so `\]` closes it. A class such as `[^\]]` or `[\]x]` is common in PEG.js grammars.
2. In `{ return a }` the code has only the scope `source.coffee.embedded.pegcs`, with no `source.coffee` scope inside, so it is not highlighted. Sublime Text does not ship a CoffeeScript syntax, and the README does not say a CoffeeScript package is needed.
3. `/** doc */` is `comment.block`, not documentation: `docCommentBlock` exists in the repository section but the top-level patterns include `#docCommentLine`, which does not exist.

Fix (not run): for 1, give `charSet` an inner pattern `\\.` (for example `<key>patterns</key>` with `match` `\\.` and name `constant.character.escape.pegcs`); for 3, change the include `#docCommentLine` to `#docCommentBlock` and list it before `#commentBlock`.
