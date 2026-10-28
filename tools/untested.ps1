param([int]$Skip, [int]$Count = 8, [string]$List = "audit_list_2026_10_21_fresh.tsv")
# Lists the next untested rows of the audit list, starting after $Skip rows: a row counts as tested when its
# package name equals the start of a line of .tested_packages.tsv (optionally with a queue prefix or a version/row suffix).
# Usage: .\tools\untested.ps1 -Skip 15 -Count 8   then precheck.ps1 shows the repos.
$tested = (Get-Content "$PSScriptRoot\..\data\.tested_packages.tsv" | ForEach-Object { ($_ -split "`t")[0].ToLower() })
$set = New-Object 'System.Collections.Generic.HashSet[string]'
foreach ($t in $tested) {
  $n = $t -replace '^#\d+\s+', ''
  [void]$set.Add($n)
  [void]$set.Add(($n -replace '\s+\d+(\.\d+)*$', ''))
}
$rows = Get-Content "$PSScriptRoot\..\data\$List" | Select-Object -Skip $Skip
$found = 0; $i = $Skip
foreach ($line in $rows) {
  $i++
  $c = $line -split "`t"
  $name = $c[2]
  if (-not $set.Contains($name.ToLower())) {
    "$i | $($c[0]) | $name | $($c[3])"
    $found++
    if ($found -ge $Count) { break }
  }
}
