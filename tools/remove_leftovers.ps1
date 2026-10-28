Add-Type -AssemblyName Microsoft.VisualBasic
function Step($msg, [scriptblock]$a) { try { & $a; "ok: $msg" } catch { "ERROR: $msg : $_" } }
$sp = 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\bfc20dab-0668-43bb-b516-26c77432efda\scratchpad'

# back up the registry keys first
Step 'export HKLM OpenAI' { reg.exe export 'HKLM\SOFTWARE\OpenAI' "$sp\hklm_openai_backup.reg" /y | Out-Null }
Step 'export Chrome native host' { reg.exe export 'HKCU\SOFTWARE\Google\Chrome\NativeMessagingHosts\com.openai.codexextension' "$sp\chrome_codex_host_backup.reg" /y | Out-Null }

# account pictures to the Recycle Bin
foreach ($f in 'CodexSandboxOffline.dat','muse-sbx-r1.dat','muse-sbx-u1.dat') {
    $p = Join-Path 'C:\ProgramData\Microsoft\User Account Pictures' $f
    if (Test-Path -LiteralPath $p) {
        Step "recycle $p" { [Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile($p, 'OnlyErrorDialogs', 'SendToRecycleBin') }
    } else { "not present: $p" }
}

# registry keys
Step 'remove HKLM OpenAI' { if (Test-Path 'HKLM:\SOFTWARE\OpenAI') { Remove-Item 'HKLM:\SOFTWARE\OpenAI' -Recurse -Force } }
Step 'remove Chrome native host' { $k='HKCU:\SOFTWARE\Google\Chrome\NativeMessagingHosts\com.openai.codexextension'; if (Test-Path $k) { Remove-Item $k -Recurse -Force } }

"--- check ---"
"pictures left:"; Get-ChildItem 'C:\ProgramData\Microsoft\User Account Pictures' -Force | Where-Object Name -match 'codex|muse' | Select-Object -ExpandProperty Name
"HKLM OpenAI present: " + (Test-Path 'HKLM:\SOFTWARE\OpenAI')
"Chrome host present: " + (Test-Path 'HKCU:\SOFTWARE\Google\Chrome\NativeMessagingHosts\com.openai.codexextension')
"done"
