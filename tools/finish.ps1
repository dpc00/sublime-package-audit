param(
  [Parameter(Mandatory)][string]$Name,
  [Parameter(Mandatory)][string]$Note,
  [int]$Filed = 0,
  [string[]]$Issues = @(),
  [string]$LeftoverPattern = '',
  [Parameter(Mandatory)][int]$NextRow,
  [Parameter(Mandatory)][string]$BatonSummary
)
# One call after a package is removed: leftover check, log entry, baton refresh, next rows.
$root = 'C:\Users\donal\projects\sublime-package-audit'
$d = 'C:\Users\donal\tools\st_portable\Data'
if ($LeftoverPattern) {
  # the removal runs in the background: wait up to 10 s for the zip to go before reporting leftovers
  for ($w = 0; $w -lt 20 -and (Get-ChildItem "$d\Installed Packages" -ErrorAction SilentlyContinue | Where-Object { $_.Name -match $LeftoverPattern }); $w++) { Start-Sleep -Milliseconds 500 }
  Get-ChildItem "$d\Packages", "$d\Installed Packages", "$d\Packages\User" -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -match $LeftoverPattern } | Select-Object -ExpandProperty FullName
}
Set-Location $root
$recArgs = @{ Name = $Name; Note = $Note; Filed = $Filed }
if ($Issues.Count) { $recArgs.Issues = $Issues }
& "$root\tools\rec.ps1" @recArgs | Out-Null
$p = "$root\notes\project_session_baton_2026_10_21_fresh_list_batch4.md"
$t = [IO.File]::ReadAllText($p)
$prev = [regex]::Match($t, 'NEXT row (\d+) onward \(Skip \d+ shows row \d+ first\)')
if (-not $prev.Success) { 'baton: NEXT sentence not found'; return }
$t = $t.Replace($prev.Value, "$BatonSummary; NEXT row $NextRow onward (Skip $NextRow shows row $NextRow first)")
[IO.File]::WriteAllText($p, $t)
if ($t -match "NEXT row $NextRow ") { 'baton updated' }
