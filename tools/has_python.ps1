param([string]$In = "$PSScriptRoot\..\data\live_candidates_2026_10_27.tsv", [string]$Out = "$PSScriptRoot\..\data\live_python_2026_10_27.tsv")
# For each live candidate (name, pushed, RESULTS line) find its repo link in the matching list files, then count .py files
# at the top levels of the repo tree (plugins). Read-only against GitHub. Output: name, repo, py_files, line.
$lists = Get-ChildItem "$PSScriptRoot\..\data" -Filter 'audit_list_2026_10_2*.tsv'
$repoOf = @{}
foreach ($f in $lists) { Get-Content $f.FullName | Select-Object -Skip 1 | ForEach-Object { $c = $_ -split "`t"; if ($c.Count -ge 4 -and $c[3] -match 'github\.com/([^/]+/[^/#?]+)') { $repoOf[$c[2].ToLower()] = $Matches[1] -replace '\.git$','' } } }
$rows = foreach ($ln in Get-Content $In) {
  $c = $ln -split "`t"; $name = $c[0]
  $repo = $repoOf[$name.ToLower()]
  if (-not $repo) { continue }
  $t = gh api "repos/$repo/git/trees/HEAD?recursive=1" 2>$null | ConvertFrom-Json
  if (-not $t) { continue }
  $py = @($t.tree | Where-Object { $_.path -match '\.py$' -and $_.path -notmatch '(^|/)(tests?|test_|docs?|examples?|vendor|lib|libs|site-packages|node_modules)/' }).Count
  "{0}`t{1}`t{2}`t{3}" -f $name, $repo, $py, $c[2]
}
[IO.File]::WriteAllLines($Out, @($rows), (New-Object Text.UTF8Encoding($false)))
"candidates with a repo: $(@($rows).Count); with python plugin code: $(@($rows | Where-Object { [int](($_ -split "`t")[2]) -gt 0 }).Count)"
