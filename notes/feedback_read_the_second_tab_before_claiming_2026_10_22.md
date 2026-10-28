---
name: read-the-second-tab-before-claiming-2026-10-22
description: EmberToolBox#3 said a path "opened the same empty tab" for a view I never read; EnvSwitcher showed the same pattern opens the real zipped default; issue edited
metadata:
  type: feedback
---

On 2026-10-22 I filed jackson-dean/ember-tool-box#3 saying `open_file ${packages}/EmberToolBox/...` gave "the same empty tab". I had read only the first of the two tabs (the wrong folder name). Testing EnvSwitcher next showed that the same `${packages}/<Package>/file` pattern opens the real default file from a zipped package.

**Why:** a claim in an issue about something I did not read is the same fault as the earlier Edit-in-new-tab and Element-UI corrections.

**How to apply:** before an issue sentence says "also tried X, same result", read the result of X itself (`get_view_content` on that view). If I did not, write "not checked". The issue was corrected with `gh issue edit` the same session.
