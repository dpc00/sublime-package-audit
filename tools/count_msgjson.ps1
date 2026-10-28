$root = 'C:\Users\donal\projects\sublime-package-audit'
Set-Location $root
git pull --quiet 2>$null
$list = Import-Csv "$root\lists\messages_json_invalid_2026_10_14.tsv" -Delimiter "`t"
$listRepos = $list | ForEach-Object { $_.repository.ToLower() }
"list file (2026-10-14): $($listRepos.Count)"

$issues = Import-Csv "$root\ISSUES.tsv" -Delimiter "`t"
$mi = $issues | Where-Object { $_.title -match 'messages\.json' -and $_.repository -notmatch 'package_control' }
$miRepos = $mi | ForEach-Object { $_.repository.ToLower() } | Sort-Object -Unique
"issues about messages.json (excluding package_control repos): $($miRepos.Count) repos"

$res = Import-Csv "$root\RESULTS.tsv" -Delimiter "`t" -Header name,date,note
$rr = $res | Where-Object { $_.note -match 'messages\.json' -and $_.note -match 'comma|invalid|parse|Error parsing|trailing' }
"results rows mentioning messages.json problems: $($rr.Count)"

$extra = $miRepos | Where-Object { $listRepos -notcontains $_ }
"issue repos NOT in the 74 list: $($extra.Count)"
$extra | ForEach-Object { "  $_" }
"union list + extra issue repos: $($listRepos.Count + $extra.Count)"
