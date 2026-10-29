param([Parameter(Mandatory)][string]$Repo, [string]$Name)
# Gate before filing an issue (Donald, 2026-10-27): "stop filing issues on obsolete packages".
# Prints FILE or RECORD-ONLY with the reasons. RECORD-ONLY means: log the finding in RESULTS.tsv, file nothing.
# FILE needs ALL of: repo not archived, Package Control (if listed) says ST3 or ST4 supported, and
#   (last push within 3 years OR 3000+ unique installs).
# The 2026-10-27 hold ("too dangerous, sensitive toes") was lifted by Donald on 2026-10-29 ("We did PRs today, so of course it is lifted").
$why = @()
$m = gh repo view $Repo --json isArchived,pushedAt 2>$null | ConvertFrom-Json
if (-not $m) { Write-Output "RECORD-ONLY: repo not found (404)"; exit 0 }
if ($m.isArchived) { $why += "archived" }
$years = ((Get-Date) - [datetime]$m.pushedAt).TotalDays / 365
$installs = $null; $st = $null
if ($Name) {
  $pc = curl.exe -s -m 20 ("https://packagecontrol.io/packages/" + [uri]::EscapeDataString($Name) + ".json") | ConvertFrom-Json -ErrorAction SilentlyContinue
  if ($pc -and $pc.name) {
    $installs = [int]$pc.installs.total
    $st = @($pc.st_versions)
    if ($pc.removed -or $pc.is_missing) { $why += "removed from Package Control" }
    if ($st.Count -gt 0 -and -not ($st -contains 3 -or $st -contains 4)) { $why += "ST2-only on Package Control" }
  }
}
if ($years -gt 3 -and -not ($installs -ge 3000)) { $why += ("last push {0:N1} years ago, installs {1}" -f $years, $(if ($null -eq $installs) { "unknown" } else { $installs })) }
if ($why.Count) { "RECORD-ONLY: " + ($why -join "; ") } else { "FILE: pushed {0:N1} years ago, installs {1}" -f $years, $(if ($null -eq $installs) { "unknown" } else { $installs }) }
