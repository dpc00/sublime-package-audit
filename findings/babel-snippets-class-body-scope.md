Status: POSTED 2026-10-21 as a comment on babel/babel-sublime-snippets#10 (https://github.com/babel/babel-sublime-snippets/issues/10#issuecomment-6327510586), with a tested fix (selector `source.js meta.class.js meta.block.js - meta.function`); the text below is the earlier draft
Target: babel/babel-sublime-snippets, comment on issue #10 ("Snippets were not appearing anymore in class files", open since 2015-10) and #15 ("Only few triggers are working"). Repository not archived, last push 2018-10-30; #42 asks whether it is still maintained.

Claude reports:

Reproduced on Sublime Text 4200 (Windows), v1.0.7 from Package Control, plain JavaScript syntax.

In a new JavaScript tab, `rcc` + Tab expands to the class skeleton (so #41 does not reproduce). Inside a class body `cdm` + Tab and `ren` + Tab only insert a tab:

```
class A {
	cdm<Tab>
}
```

The scope at the caret in the class body is `source.js meta.class.js meta.block.js`.

The class snippets (`cdm`, `cdup`, `cwm`, `cwr`, `cwun`, `cwup`, `scu`, `ren`) use the scope selector `source.js meta.class.js -(meta meta)`. `-(meta meta)` excludes any scope stack that contains two `meta` scopes. In the current JavaScript syntax a class body always has two (`meta.class.js` and `meta.block.js`), so the selector can never match. The older syntax had only `meta.class.js` there. The same snippets' other selector, `source.js meta.group.braces.round meta.group.braces.curly -(meta meta meta)` (also used by `gdp`, `gis`), names scopes the current syntax does not produce.

Possible fix, not tested: select the class body with `source.js meta.class.js meta.block.js` and exclude method bodies, for example `source.js meta.class.js meta.block.js - meta.function`.
