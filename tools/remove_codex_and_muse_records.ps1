Add-Type -AssemblyName Microsoft.VisualBasic
$ErrorActionPreference = 'Continue'
function Step($msg, [scriptblock]$a) { try { & $a; "ok: $msg" } catch { "ERROR: $msg : $_" } }

# SIDs first, before the accounts disappear
$cx = @{}
foreach ($n in 'CodexSandboxOffline','CodexSandboxOnline') {
    $u = Get-LocalUser -Name $n -ErrorAction SilentlyContinue
    if ($u) { $cx[$n] = $u.SID.Value }
}
$museSids = 'S-1-5-21-2735814221-303892426-3871331145-1007','S-1-5-21-2735814221-303892426-3871331145-1008'

# 1. stop processes and the service
Step 'stop processes' { Get-Process | Where-Object { $_.Name -match '^codex' } | Stop-Process -Force }
Step 'stop service' { Stop-Service -Name 'CodexSandboxService.OpenAI.Codex' -Force -ErrorAction SilentlyContinue }
Step 'delete service' { if (Get-Service -Name 'CodexSandboxService.OpenAI.Codex' -ErrorAction SilentlyContinue) { sc.exe delete 'CodexSandboxService.OpenAI.Codex' | Out-Null } }
Step 'stop processes again' { Start-Sleep 2; Get-Process | Where-Object { $_.Name -match '^codex' } | Stop-Process -Force -ErrorAction SilentlyContinue }

# 2. the app package
Step 'remove app package' { Get-AppxPackage -AllUsers -Name 'OpenAI.Codex' | Remove-AppxPackage -AllUsers }

# 3. accounts and group
foreach ($n in $cx.Keys) { Step "remove account $n" { Remove-LocalUser -Name $n } }
Step 'remove group CodexSandboxUsers' { if (Get-LocalGroup -Name 'CodexSandboxUsers' -ErrorAction SilentlyContinue) { Remove-LocalGroup -Name 'CodexSandboxUsers' } }

# 4. firewall rules named for Codex
Step 'remove firewall rules' { Get-NetFirewallRule -ErrorAction SilentlyContinue | Where-Object { $_.DisplayName -match 'codex' } | Remove-NetFirewallRule }

# 5. folders to the Recycle Bin
$dirs = @(
    'C:\Users\CodexSandboxOffline',
    'C:\Users\CodexSandboxOnline',
    'C:\Users\donal\.codex',
    'C:\Users\donal\AppData\Local\OpenAI',
    'C:\Users\donal\AppData\Roaming\Codex',
    'C:\Users\donal\AppData\Roaming\OpenAI'
)
$dirs += (Get-ChildItem 'C:\Users\donal\AppData\Local\Packages' -Directory -Filter 'OpenAI.Codex*' -ErrorAction SilentlyContinue | ForEach-Object FullName)
foreach ($d in $dirs) {
    if (Test-Path -LiteralPath $d) {
        Step "recycle $d" { [Microsoft.VisualBasic.FileIO.FileSystem]::DeleteDirectory($d, 'OnlyErrorDialogs', 'SendToRecycleBin') }
    } else { "not present: $d" }
}

# 6. orphan profile records (registry), Muse and Codex
$pl = 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList'
foreach ($s in ($museSids + $cx.Values)) {
    $key = Join-Path $pl $s
    if (Test-Path $key) { Step "remove profile record $s" { Remove-Item -LiteralPath $key -Recurse -Force } } else { "no profile record: $s" }
}

"--- check ---"
"accounts left:"; Get-LocalUser | Where-Object Name -match 'codex|muse' | Select-Object -ExpandProperty Name
"profile records left:"; Get-CimInstance Win32_UserProfile | Where-Object LocalPath -match 'codex|muse' | Select-Object -ExpandProperty LocalPath
"package left:"; Get-AppxPackage -AllUsers -Name 'OpenAI.Codex' | Select-Object -ExpandProperty PackageFullName
"service left:"; Get-Service | Where-Object Name -match 'codex' | Select-Object -ExpandProperty Name
"processes left:"; Get-Process | Where-Object { $_.Name -match '^codex' } | Select-Object -ExpandProperty Name
"done"
