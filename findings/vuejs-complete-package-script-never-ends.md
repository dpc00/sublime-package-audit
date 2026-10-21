Status: not filed - GitHub refused the comment on 2026-10-21: the repository is archived, read-only, and issue #3 is locked
Target: BrainBuzzer/vuejs-sublime-complete, comment on issue #3 ("Highlight breaks with object-method-shortcut?", open since 2017-01-10, last comment 2018-05-22; last commit to the repo 2019-09-05)

Claude reports:

Reproduced on Sublime Text 4200 (Windows), with the version Package Control installs (v0.3.3) and with master (dd49df1).

Test file `test.vue`:

```
<template>
  <div id="app" v-if="show">{{ message }}</div>
</template>

<script>
export default {
  data() {
    return { message: 'hi', show: true }
  }
}
</script>

<style>
.a { color: red; }
</style>
```

Scopes found with Tools > Developer > Show Scope Name (checked at the caret):

- v0.3.3, line 11 (`</script>`): `text.html.vue source.js.embedded.html meta.export.js meta.string.js string.regexp.js`
- v0.3.3, line 15 (`.a { color: red; }`): `... source.js.embedded.html meta.export.js meta.string.js string.regexp.js`
  The script block never ends. `</script>` is read as a regular expression, and the whole style block stays JavaScript.
- master, line 11 and line 15: `text.html.vue meta.tag.block.any.html meta.directive.vue source.directive.vue meta.string.js string.regexp.js`
  Here the problem starts at the directive `v-if="show"` on line 2: the directive string never ends and the rest of the file is JavaScript.

Cause (read from `vue.YAML-tmLanguage`): `<script>` bodies (line 275) and the `v-...="..."` directives (lines 354-371) embed JavaScript with `include: source.js` inside a begin/end rule. The current JavaScript syntax opens nested contexts (here `meta.export.js`), and while one is open the outer `end` pattern (`</script` or the closing quote) is never tried. Sublime's own HTML syntax avoids this with `embed:` and `escape:`.

Check of a fix: a syntax file that only extends the built-in HTML syntax (scope `text.html.vue`, `file_extensions: [vue]`, `contexts: {}`) gives, on the same file, `meta.tag.script.end.html entity.name.tag.script.html` for `</script>` on line 11 and `meta.tag.style.end.html entity.name.tag.style.html` for `</style>` on line 15, and the JavaScript inside the script block is still highlighted (`source.js.embedded.html ... keyword.control.flow.return.js` on line 8). That file loses the Vue extras (directives, `{{ }}`), so the real fix is to rebuild `vue.tmLanguage` as a `.sublime-syntax` that extends `Packages/HTML/HTML.sublime-syntax` and adds the directive and interpolation contexts with `embed: scope:source.js` and `escape: '"'` (directives) or `escape: \}\}` (interpolation). I did not write or test those two contexts.

Not tested: what other tools write for Vue single-file components (Vue Syntax Highlight, LSP-vue).
