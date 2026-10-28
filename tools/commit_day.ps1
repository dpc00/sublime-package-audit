# Donald, 2026-10-20: the commit-of-the-day is created at the first run after midnight; every other run that day
# amends it (batch ends, end of work). No per-package commits. rec.ps1 only updates files.
# Pushes with --force-with-lease because an amended commit replaces the pushed one.
Set-Location 'C:\Users\donal\projects\sublime-package-audit'
$d = Get-Date -Format 'yyyy-MM-dd'
$subject = "Audit log through $d"
git add -A
$last = git log -1 --format=%s
if ($last -eq $subject) {
  git commit -q --amend --no-edit
} else {
  git commit -q -m $subject -m 'Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>' -m 'Claude-Session: https://claude.ai/code/session_0145G8hmDqJAyV9iiJi9TPCq'
}
git push -q --force-with-lease origin main
git log --oneline -2
