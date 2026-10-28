$repo = 'math2001/BetterSnippetManager'
$dir = 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\bfc20dab-0668-43bb-b516-26c77432efda\scratchpad'
$b1 = @'
Claude reports:

Create New Snippet writes `<` and `>` in the trigger as the wrong entities. Sublime Text 4200, BetterSnippetManager 1.1.2 (Package Control build), Windows. Select `print(1)` in a Python file, run Create New Snippet and enter the trigger `a<b>c`. The generated file has

```
<tabTrigger>a&gt;b&lt;c</tabTrigger>
```

which Sublime reads as `a>b<c`. `escape()` in `BetterSnippetManager.py` does `string.replace("<", "&gt;").replace(">", "&lt;")`, so the two entities are swapped (`<` should become `&lt;` and `>` `&gt;`). It also does not escape `&`: a description of `x & y` is written as `<description>x & y</description>`, which is not valid XML. The same `escape()` is used for the trigger, the description and the scopes, and the default file name offered next is built from the escaped trigger (`a&gt;b&lt;c.sublime-snippet`).
'@
$b2 = @'
Claude reports:

Create New Snippet offers a folder name with a trailing comma, and creates that folder. Sublime Text 4200, BetterSnippetManager 1.1.2 (Package Control build), Windows. In a Python file, select `print(1)`, run Create New Snippet and accept the default scope. The Folder prompt then contains `python,`, and after the file name the snippet is opened as `User\snippets\python,\<name>.sublime-snippet` (the folder `python,` is created on disk). `set_description` builds the scope string with `scopes.replace(" ", ", ")`, and `set_scopes` takes the folder from `self.scopes.split(" ")[0].split(".")[-1]`, which is the first scope together with its comma, `source.python,`. Splitting on `","` first (or taking the first scope before the replace) would give `python`.
'@
$b3 = @'
Claude reports:

Edit Snippets raises a FileNotFoundError on a fresh install. Sublime Text 4200, BetterSnippetManager 1.1.2 (Package Control build), Windows. With the default `snippets_folder` of `snippets` and no `Packages\User\snippets` folder yet, run Edit Snippets from the Command Palette. Nothing happens and the console shows

```
File ".../BetterSnippetManager.py", line 73, in run
File ".../BetterSnippetManager.py", line 43, in __list_all_snippets
FileNotFoundError: [WinError 3] The system cannot find the path specified: '...\Packages\User\snippets\*.*'
```

`__list_all_snippets` calls `os.listdir(path)` without checking that the folder exists. The "Didn't find any snippets" message in `run` is never reached (and #8 is the error that message would raise next, since `error_message` is not a method of the command).
'@
[IO.File]::WriteAllText("$dir\bsm1.md", $b1)
[IO.File]::WriteAllText("$dir\bsm2.md", $b2)
[IO.File]::WriteAllText("$dir\bsm3.md", $b3)
gh issue create --repo $repo --title 'Create New Snippet swaps the entities for < and > (and does not escape &)' --body-file "$dir\bsm1.md"
gh issue create --repo $repo --title 'Create New Snippet: default folder name has a trailing comma ("python,")' --body-file "$dir\bsm2.md"
gh issue create --repo $repo --title 'Edit Snippets raises FileNotFoundError when the snippets folder does not exist' --body-file "$dir\bsm3.md"
