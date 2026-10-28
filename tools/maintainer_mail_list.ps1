param(
  [string]$Out = "$PSScriptRoot\..\data\maintainer_mail_list_2026_10_27.tsv",
  [int]$Parallel = 8
)
# Builds the recipient list for the maintainer-email design (Donald, 2026-10-27): one row per repo owner whose
# repo has a logged finding, is not archived, was pushed within 3 years, and has a usable (non-noreply) address.
# Read-only against GitHub. Columns: owner repos pushed email source
$root = Split-Path $PSScriptRoot -Parent
$skipOwners = @('whitequark','ahuff44','digitrev','amclain','Naereen','motine','foxxyz','ProtractorNinja','nadock','spthiel',
  'deathaxe','facelessuser','pdaether','smhg','maethu','jmeischner','lowliet','TomasBarry','FPtje','kaste','rchl','sublimelsp',
  'SublimeLinter','SublimeText','sublimehq','wbond','packagecontrol','dpc00','alec-lee','al63','HackerBaloo')
$rows = Import-Csv "$root\ISSUES.tsv" -Delimiter "`t" | Where-Object { $_.kind -ne 'missing' -and $_.state -ne '' }
$repos = $rows | Select-Object -ExpandProperty repository -Unique | Where-Object { $skipOwners -notcontains ($_ -split '/')[0] }
$chunks = for ($i = 0; $i -lt $repos.Count; $i += 25) { , @($repos[$i..([Math]::Min($i + 24, $repos.Count - 1))]) }
$pending = @(); $cutoff = (Get-Date).AddYears(-3)
foreach ($c in $chunks) {
  while (@($pending | Where-Object { $_.State -eq 'Running' }).Count -ge $Parallel) { Start-Sleep -Milliseconds 300 }
  $pending += Start-Job -ArgumentList ($c -join '|'), $cutoff -ScriptBlock {
    param($joined, $cutoff)
    foreach ($r in ($joined -split '\|')) {
      $m = gh repo view $r --json isArchived,pushedAt 2>$null | ConvertFrom-Json
      if (-not $m -or $m.isArchived -or ([datetime]$m.pushedAt) -lt $cutoff) { continue }
      $mail = ''; $src = ''
      $c = gh api "repos/$r/commits?per_page=5" 2>$null | ConvertFrom-Json
      foreach ($x in @($c)) {
        $e = $x.commit.author.email
        if ($e -and $e -notmatch 'noreply|users\.noreply|localhost|\.local$|invalid') { $mail = $e; $src = 'commit'; break }
      }
      if (-not $mail) {
        $u = gh api "users/$(($r -split '/')[0])" 2>$null | ConvertFrom-Json
        if ($u.email) { $mail = $u.email; $src = 'profile' }
      }
      if ($mail) { [pscustomobject]@{ owner = ($r -split '/')[0]; repo = $r; pushed = $m.pushedAt.Substring(0, 10); email = $mail; source = $src } }
    }
  }
}
$all = $pending | Wait-Job | Receive-Job; $pending | Remove-Job
$all | Select-Object owner, repo, pushed, email, source | Export-Csv $Out -Delimiter "`t" -NoTypeInformation -Encoding utf8
"repos with address: $(@($all).Count); owners: $(@($all | Select-Object -ExpandProperty owner -Unique).Count)"
