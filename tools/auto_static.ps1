param([int]$Skip, [int]$Count = 30, [string]$List = "audit_list_2026_10_21_fresh.tsv")
# Static pass over the next untested rows of the main list (Donald, 2026-10-27: "as speedily as you can"):
# for each row with a GitHub link run static_check.ps1 and record the result with rec.ps1. Nothing is installed, run or filed.
# Rows whose check reports a problem are written to data\auto_static_flags.txt for a human look.
$root = Split-Path $PSScriptRoot -Parent
$out = & "$PSScriptRoot\untested.ps1" -Skip $Skip -Count $Count -List $List
foreach ($line in $out) {
  $p = $line -split ' \| ', 4
  $row = $p[1]; $name = $p[2]; $link = $p[3].Trim()
  if ($link -match '^https?://github\.com/([^/]+/[^/#?]+?)(\.git)?/?$') {
    $repo = $Matches[1]
    $res = ((& "$PSScriptRoot\static_check.ps1" -Repos $repo 2>$null | Out-String) -replace '\s*[\r\n]+\s*',' ').Trim()
    $detail = ($res -split ' \| ', 2)[1]
    if ($res -match 'repo gone') { $note = "Main list row ${row}: repository gone (404); nothing to test" }
    elseif ($res -match 'zip failed') { $note = "Main list row ${row}: could not download the repository zip; not checked" }
    elseif ($res -match '\| clean$') { $note = "Main list row ${row}: static check only (tools\static_check.ps1: JSON-ish, XML and Python 3 parse of the repo files), not installed or run; clean ($detail)" }
    else {
      $note = "Main list row ${row}: static check only, not installed or run; problem reported, not verified, nothing filed: $res"
      Add-Content "$root\data\auto_static_flags.txt" "$name | $res"
    }
  } else { $note = "Main list row ${row}: no GitHub repository link ($link); not tested" }
  & "$PSScriptRoot\rec.ps1" -Name $name -Note $note | Out-Null
  "$row $name -> " + $note.Substring(0, [Math]::Min(90, $note.Length))
}
