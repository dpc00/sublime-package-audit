param(
  [int]$Skip = 0,
  [int]$Count = 8,
  [string]$TestedFile = "$PSScriptRoot\..\data\.tested_packages.tsv",
  [string]$ListFile = "$PSScriptRoot\..\data\audit_list.tsv"
)
# Lists the next untested rows of an audit list, starting after $Skip rows.
# $ListFile: tab-separated, column 3 = package name, column 4 = link.
# $TestedFile: tab-separated, column 1 = package name. A row counts as tested when its name equals the start
# of a line of $TestedFile (optionally with a "#123 " queue prefix or a version/row number suffix).
$tested = Get-Content $TestedFile | ForEach-Object { ($_ -split "`t")[0].ToLower() }
$set = New-Object 'System.Collections.Generic.HashSet[string]'
foreach ($t in $tested) {
  $n = $t -replace '^#\d+\s+', ''
  [void]$set.Add($n)
  [void]$set.Add(($n -replace '\s+\d+(\.\d+)*$', ''))
}
$rows = Get-Content $ListFile | Select-Object -Skip $Skip
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
