param([int]$Skip, [int]$Count = 8)
# Pre-check rows of the audit list in parallel: archived? issues enabled? open issue titles.
# Usage: .\tools\precheck.ps1 -Skip 348 -Count 8   (row 348 first)
$list = Get-Content "$PSScriptRoot\..\data\audit_list_2026_10_21_fresh.tsv" | Select-Object -Skip $Skip -First $Count
$jobs = foreach ($line in $list) {
  $c = $line -split "`t"
  $order = $c[0]; $pkg = $c[2]; $url = $c[3]
  Start-Job -ArgumentList $order, $pkg, $url -ScriptBlock {
    param($order, $pkg, $url)
    if ($url -notmatch 'github\.com/([^/]+/[^/#?]+)') { return "$order | $pkg | non-GitHub: $url" }
    $repo = $Matches[1]
    $v = gh repo view $repo --json isArchived,hasIssuesEnabled 2>&1 | Out-String
    $i = gh issue list --repo $repo --state all --limit 4 --json number,title 2>&1 | Out-String
    "$order | $pkg | $repo | " + ($v -replace '\s+', ' ') + ' | ' + ($i -replace '\s+', ' ')
  }
}
$jobs | Wait-Job | Receive-Job
$jobs | Remove-Job
