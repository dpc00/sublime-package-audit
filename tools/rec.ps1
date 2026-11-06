param(
  [string]$Name,
  [string]$Note,
  [int]$Filed = 0,
  [string[]]$Issues = @(),   # each: "owner/repo|number|title"
  [switch]$RefreshOnly       # recompute the README figures and commit, log nothing
)
if (-not $RefreshOnly -and (-not $Name -or -not $Note)) { throw 'give -Name and -Note, or -RefreshOnly' }
$d = (Get-Date -Format 'yyyy-MM-dd')
$audit = 'C:\Users\donal\projects\sublime-package-audit'
if (-not $RefreshOnly) {
# Flatten the note first: a note that still contains a newline (Get-Content -Raw keeps the trailing
# one) pushes the line-number column onto its own line and corrupts the TSV (2026-11-05).
$Note = (($Note -replace "\r?\n+", " ") -replace "\s+", " ").Trim()
$ln = @(Get-Content "$audit\RESULTS.tsv").Count + 1   # line number in RESULTS.tsv, last column (Donald, 2026-10-27: email links point at the line)
# Append LF-only: Add-Content on Windows writes CRLF and mixed endings made every later diff
# touch the whole file (2026-11-05).
$utf8 = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::AppendAllText("$audit\RESULTS.tsv", "$Name`t$d`t$Note`t$ln`n", $utf8)
[System.IO.File]::AppendAllText("$audit\data\.tested_packages.tsv", "$Name`t$d`t$Filed`t$Note`n", $utf8)
foreach ($i in $Issues) {
  $p = $i -split '\|', 3     # limit 3: a title may itself contain '|' or ','
  if ($p.Count -ne 3 -or $p[1] -notmatch '^\d+$') { throw "bad -Issues entry (want owner/repo|number|title): $i" }
  Add-Content "$audit\ISSUES.tsv" ("$($p[0])`t$($p[1])`t$($p[2])`topen`t$d`t`thttps://github.com/$($p[0])/issues/$($p[1])`t`t$d`tissue") -Encoding UTF8
}
}
# Recompute README figures from the data files (new script; the old inline regexes targeted the retired README format).
python "$audit\tools\readme_stats.py"
if (-not $RefreshOnly) { Add-Content "$audit\notes\project_session_baton_2026_10_16_redo_batch1.md" "`n- $Name done ($Filed filed). $Note" -Encoding UTF8 }
# No commit and no push here (Donald, 2026-10-20): the files are updated only. Commit once, when a batch is done.
Set-Location $audit
git status --short | Select-Object -First 5
