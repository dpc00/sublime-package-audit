Status: not filed (HTML Head Snippets is listed on Package Control without a GitHub repository)

Claude reports:

The oEmbed snippet's tabTrigger is misspelled `head-oebmed` (letters swapped) in all three sets: `snippets/html/head-oembed.sublime-snippet`, `snippets/haml/` and `snippets/jade/`. The file name and the other triggers (`head-ie`, `head-twitter`, ...) follow the spelling `oembed`.

Checked on Sublime Text build 4215, v3.0.0 from Package Control, in an HTML tab:

- `head-oembed` + Tab: nothing expands, a literal tab is inserted.
- `head-oebmed` + Tab: the two oEmbed `<link>` tags are inserted.

Fix: change the trigger to `head-oembed` (keep `head-oebmed` too if existing users rely on it).