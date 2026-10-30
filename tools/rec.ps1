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
$ln = @(Get-Content "$audit\RESULTS.tsv").Count + 1   # line number in RESULTS.tsv, last column (Donald, 2026-10-27: email links point at the line)
Add-Content "$audit\RESULTS.tsv" ("$Name`t$d`t$Note`t$ln") -Encoding UTF8
Add-Content "$audit\data\.tested_packages.tsv" ("$Name`t$d`t$Filed`t$Note") -Encoding UTF8
foreach ($i in $Issues) {
  $p = $i -split '\|', 3     # limit 3: a title may itself contain '|' or ','
  if ($p.Count -ne 3 -or $p[1] -notmatch '^\d+$') { throw "bad -Issues entry (want owner/repo|number|title): $i" }
  Add-Content "$audit\ISSUES.tsv" ("$($p[0])`t$($p[1])`t$($p[2])`topen`t$d`t`thttps://github.com/$($p[0])/issues/$($p[1])`t`t$d`tissue") -Encoding UTF8
}
}
# Recompute every README figure from the data files (plain tab split: titles contain quotes)
$res = @(Get-Content "$audit\RESULTS.tsv" | Select-Object -Skip 1 | Where-Object { $_ })
$iss = @(Get-Content "$audit\ISSUES.tsv" | Select-Object -Skip 1 | Where-Object { $_ })
$recs = $res.Count
$pk = @($res | ForEach-Object { (($_ -split "`t")[0] -replace '^#\d+\s+','' -replace '\s+\d{3,4}$','').ToLower() } | Sort-Object -Unique).Count
$n = $iss.Count
$rp = @($iss | ForEach-Object { ($_ -split "`t")[0] } | Sort-Object -Unique).Count
$o = @($iss | Where-Object { ($_ -split "`t")[3] -eq 'open' }).Count
$c = @($iss | Where-Object { ($_ -split "`t")[3] -eq 'closed' }).Count   # unreadable rows have an empty state: not closed (found 2026-10-30)
$r = Get-Content "$audit\README.md" -Raw
$r = $r -replace '## In numbers \(to [\d-]+\)', "## In numbers (to $d)"
$r = $r -replace '\*\*\d+ test records\*\* for \*\*\d+ different packages\*\*', "**$recs test records** for **$pk different packages**"
$r = $r -replace '\*\*\d+ issues\*\* filed on \*\*\d+ repositories\*\* \(ISSUES.tsv\): \d+ (?:still )?open, \d+ closed', "**$n issues** filed on **$rp repositories** (ISSUES.tsv): $o still open, $c closed"
# Static-only figures: latest record per package, and total static records (Donald, 2026-10-30: the hand-written 1240 had gone stale)
$latest = @{}; $sr = 0
foreach ($x in $res) { $c = $x -split "`t"; $latest[(($c[0] -replace '^#\d+\s+','' -replace '\s+\d{3,4}$','').ToLower())] = $c[2]; if ($c[2] -match 'static check only') { $sr++ } }
$sl = @($latest.GetEnumerator() | Where-Object { $_.Value -match 'static check only' }).Count
$r = $r -replace '\*\*\d+ records are a static check only\*\*', "**$sr records are a static check only**"
$r = $r -replace 'For \*\*\d+ packages that static check is still the latest record\*\*', "For **$sl packages that static check is still the latest record**"
$r = $r -replace 'For [\d,]+ packages the static check is still the only record', ("For {0:N0} packages the static check is still the only record" -f $sl)
$gone = @($iss | Where-Object { -not (($_ -split "`t")[3]) }).Count
$r = $r -replace '\d+ no longer readable', "$gone no longer readable"
# Time to close, from the created and closed dates in ISSUES.tsv (filled in by reconcile_issues.ps1)
$days = @()
foreach ($x in $iss) { $c = $x -split "`t"; if ($c[3] -eq 'closed' -and $c[4] -match '^\d{4}-\d\d-\d\d$' -and $c[5] -match '^\d{4}-\d\d-\d\d$') { $days += [int](([datetime]$c[5]) - ([datetime]$c[4])).TotalDays } }
if ($days.Count) {
  $sd = $days | Sort-Object; $mean = [math]::Round(($days | Measure-Object -Average).Average, 1); $med = $sd[[int][math]::Floor($sd.Count / 2)]; $wk = @($days | Where-Object { $_ -le 7 }).Count
  $r = $r -replace '\*\*Time to close\*\* \(\d+ closed issues(?: with both dates)?\): mean [\d.]+ days, median \d+ days; \d+ of them', "**Time to close** ($($days.Count) closed issues with both dates): mean $mean days, median $med days; $wk of them"
}
# Merged pull requests (needs gh; skipped quietly when offline)
try { $mp = @(gh search prs --author dpc00 --merged --limit 300 --json number 2>$null | ConvertFrom-Json | ForEach-Object { $_ }).Count; if ($mp -gt 0) { $r = $r -replace '\*\*\d+ pull requests merged\*\*', "**$mp pull requests merged**" } } catch {}
[IO.File]::WriteAllText("$audit\README.md", $r, (New-Object Text.UTF8Encoding($false)))
if (-not $RefreshOnly) { Add-Content "$audit\notes\project_session_baton_2026_10_16_redo_batch1.md" "`n- $Name done ($Filed filed). $Note" -Encoding UTF8 }
# No commit and no push here (Donald, 2026-10-20): the files are updated only. Commit once, when a batch is done.
Set-Location $audit
git status --short | Select-Object -First 5
