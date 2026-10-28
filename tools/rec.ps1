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
$c = $n - $o
$r = Get-Content "$audit\README.md" -Raw
$r = $r -replace '## In numbers \(to [\d-]+\)', "## In numbers (to $d)"
$r = $r -replace '\*\*\d+ test records\*\* for \*\*\d+ different packages\*\*', "**$recs test records** for **$pk different packages**"
$r = $r -replace '\*\*\d+ issues\*\* filed on \*\*\d+ repositories\*\* \(ISSUES.tsv\): \d+ (?:still )?open, \d+ closed', "**$n issues** filed on **$rp repositories** (ISSUES.tsv): $o still open, $c closed"
[IO.File]::WriteAllText("$audit\README.md", $r, (New-Object Text.UTF8Encoding($false)))
if (-not $RefreshOnly) { Add-Content "$audit\notes\project_session_baton_2026_10_16_redo_batch1.md" "`n- $Name done ($Filed filed). $Note" -Encoding UTF8 }
# No commit and no push here (Donald, 2026-10-20): the files are updated only. Commit once, when a batch is done.
Set-Location $audit
git status --short | Select-Object -First 5
