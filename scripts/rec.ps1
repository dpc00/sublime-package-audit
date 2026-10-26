param(
  [string]$Name,
  [string]$Note,
  [int]$Filed = 0,
  [string[]]$Issues = @(),   # each: "owner/repo|number|title"
  [switch]$RefreshOnly,      # recompute the README figures, log nothing
  [string]$Root = (Split-Path $PSScriptRoot)
)
# Logs one tested package (RESULTS.tsv, ISSUES.tsv, the local tested list) and recomputes the README figures.
# Updates files only; it does not commit.
if (-not $RefreshOnly -and (-not $Name -or -not $Note)) { throw 'give -Name and -Note, or -RefreshOnly' }
$d = (Get-Date -Format 'yyyy-MM-dd')
if (-not $RefreshOnly) {
  Add-Content "$Root\RESULTS.tsv" ("$Name`t$d`t$Note") -Encoding UTF8
  if (Test-Path "$Root\data") { Add-Content "$Root\data\.tested_packages.tsv" ("$Name`t$d`t$Filed`t$Note") -Encoding UTF8 }
  foreach ($i in $Issues) {
    $p = $i -split '\|', 3     # limit 3: a title may itself contain '|' or ','
    if ($p.Count -ne 3 -or $p[1] -notmatch '^\d+$') { throw "bad -Issues entry (want owner/repo|number|title): $i" }
    Add-Content "$Root\ISSUES.tsv" ("$($p[0])`t$($p[1])`t$($p[2])`topen`t$d`t`thttps://github.com/$($p[0])/issues/$($p[1])`t`t$d`tissue") -Encoding UTF8
  }
}
# Recompute every README figure from the data files (plain tab split: titles contain quotes)
$res = @(Get-Content "$Root\RESULTS.tsv" | Select-Object -Skip 1 | Where-Object { $_ })
$iss = @(Get-Content "$Root\ISSUES.tsv" | Select-Object -Skip 1 | Where-Object { $_ })
$recs = $res.Count
$pk = @($res | ForEach-Object { (($_ -split "`t")[0] -replace '^#\d+\s+','' -replace '\s+\d{3,4}$','').ToLower() } | Sort-Object -Unique).Count
$n = $iss.Count
$rp = @($iss | ForEach-Object { ($_ -split "`t")[0] } | Sort-Object -Unique).Count
$o = @($iss | Where-Object { ($_ -split "`t")[3] -eq 'open' }).Count
$c = $n - $o
$r = Get-Content "$Root\README.md" -Raw
$r = $r -replace '## In numbers \(to [\d-]+\)', "## In numbers (to $d)"
$r = $r -replace '\*\*\d+ test records\*\* for \*\*\d+ different packages\*\*', "**$recs test records** for **$pk different packages**"
$r = $r -replace '\*\*\d+ issues\*\* filed on \*\*\d+ repositories\*\* \(ISSUES.tsv\): \d+ still open, \d+ closed', "**$n issues** filed on **$rp repositories** (ISSUES.tsv): $o still open, $c closed"
[IO.File]::WriteAllText("$Root\README.md", $r, (New-Object Text.UTF8Encoding($false)))
Set-Location $Root
git status --short | Select-Object -First 5
