---
name: file-gate-obsolete-packages-2026-10-27
description: SUPERSEDED 2026-10-29 (Donald: "there is no gate, don't follow some stale rule"): file real defects whatever the age; only archived or issues-disabled repos are record-only. History of the 2026-10-27 gate below.
metadata:
  type: feedback
---

On 2026-10-27 about 40 issues went to dead packages (ST2-only, pushed 10+ years ago, 50 to 100 installs, e.g. Flashback 52 installs, Hide Files 111). Four maintainers answered the same day: "not maintained anymore", "14 years without a commit, fork it", "do not use Sublime anymore", "old, ST3 only". Donald: "we need better judgement, need to stop filing issues on obsolete packages. Somehow must detect if they are not important."

**LATER THE SAME DAY: HOLD.** After the mass closures (about 450) three maintainers reopened and four more said they no longer maintain the package. Donald: "it is too dangerous, sensitive toes." Until he says go: NO issues, comments, closes, reopens or PRs on anyone's repo; file_gate.ps1 returns RECORD-ONLY for everything. Testing and recording locally is paused too until he says what he wants from the queue (stopped at row 401).

**HIS REDESIGN (2026-10-27), replaces the gate once he says go:** no GitHub action of any kind (no issues, comments, closes, PRs, forks). Findings go only to `findings\` and `RESULTS.tsv`. Then ONE short email per maintainer with a link to that package's entry in the audit repo; they do the work, we modify no repo. SIMPLIFIED by him the same day: no per-package pages. The email links to the one results page (RESULTS.tsv in the audit repo on GitHub) and tells the maintainer to search it for the package name. Still to build: a maintainer address lookup (commit address, as in feedback_email_maintainer_when_issues_disabled), and his OK on the email text before the first send. No email goes out until he lifts the hold.

His reasoning (2026-10-27): "there is no way to please everyone, and some are dangerous." Proposed default for when the hold lifts, awaiting his word: contact no maintainer unsolicited; findings go only into the audit repo (findings\ and RESULTS.tsv); act on a repo only when its maintainer or a user asks.

**Why:** the issues cost maintainers time and bring rebukes, and the packages have no users to help.

**How to apply:** run `tools\file_gate.ps1 -Repo owner/name -Name "<PC name>"` before any `gh issue create` (skill rule 6f). FILE only if not archived, not ST2-only on Package Control, and pushed within 3 years or 3000+ installs. Otherwise RECORD-ONLY. The queue still gets tested and logged, nothing is filed. Open question for Donald: close the day's issues on dead packages with a short note (not done, outward-facing). See [[feedback-skip-unmaintained-packages]].

Line numbers: RESULTS.tsv now has a last column line (its own line number, header = 1; rec.ps1 fills it). The email links to https://github.com/dpc00/sublime-package-audit/blob/main/RESULTS.tsv#L<line> for that package. Rule from him: never email an owner we already filed an issue on or exchanged mail with, so the existing 3010 issues produce no emails; the list script tools\maintainer_mail_list.ps1 is for future findings only. Queue continued record-only: rows 401-449 recorded, next row 450.
