$ErrorActionPreference = 'Continue'
Start-Transcript -Path 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\bfc20dab-0668-43bb-b516-26c77432efda\scratchpad\remove_muse.ps1.log' -Force | Out-Null
try {
    "elevated: " + ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    & 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\bfc20dab-0668-43bb-b516-26c77432efda\scratchpad\remove_muse.ps1'
} catch {
    "ERROR: " + ($_ | Out-String)
}
Stop-Transcript | Out-Null
New-Item -ItemType File -Path 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\bfc20dab-0668-43bb-b516-26c77432efda\scratchpad\remove_muse.ps1.done' -Force | Out-Null
