param([Parameter(Mandatory)][string[]]$Repos)
# Fast static check of a repo (Donald, 2026-10-27: "do it as speedily as you can"): downloads the repo zip,
# then parses JSON-ish Sublime files (comments and trailing commas allowed), tmTheme/tmLanguage XML, and Python 3 syntax.
# Prints one line per repo: pushed date and the problems found or "clean". Read-only against GitHub. Never files anything.
$work = Join-Path $env:TEMP 'audit_static_check'
$py = Join-Path $PSScriptRoot 'static_check_parse.py'
foreach ($r in $Repos) {
  $m = gh repo view $r --json isArchived,pushedAt 2>$null | ConvertFrom-Json
  if (-not $m) { "$r | repo gone (404)"; continue }
  $dir = Join-Path $work ($r -replace '/', '__')
  if (Test-Path $dir) { Remove-Item $dir -Recurse -Force }
  New-Item -ItemType Directory -Force $dir | Out-Null
  $zip = "$dir.zip"
  curl.exe -sL -m 60 -o $zip "https://codeload.github.com/$r/zip/HEAD"
  try { Expand-Archive $zip -DestinationPath $dir -Force } catch { "$r | zip failed"; continue }
  $inner = Get-ChildItem $dir -Directory | Select-Object -First 1
  $res = (python -W ignore -I $py $inner.FullName 2>$null | Out-String) -replace '\s*[\r\n]+\s*',' '   # -W ignore: invalid-escape SyntaxWarnings are not findings; one line only so the TSV rows stay one line
  "{0} | pushed {1}{2} | {3}" -f $r, $m.pushedAt.Substring(0,10), $(if($m.isArchived){' ARCHIVED'}else{''}), $res.Trim()
  Remove-Item $dir -Recurse -Force; Remove-Item $zip -Force -ErrorAction SilentlyContinue
}
