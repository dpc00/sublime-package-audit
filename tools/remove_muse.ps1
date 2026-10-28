Add-Type -AssemblyName Microsoft.VisualBasic
$names = 'muse-sbx-r1','muse-sbx-u1'
$sids = @{}
foreach ($n in $names) {
    $u = Get-LocalUser -Name $n -ErrorAction SilentlyContinue
    if ($u) { $sids[$n] = $u.SID.Value }
}
foreach ($n in $names) {
    try { Remove-LocalUser -Name $n -ErrorAction Stop; "removed account $n" } catch { "ERROR account ${n}: $_" }
}
$dirs = @('C:\Users\muse-sbx-r1','C:\Users\muse-sbx-u1','C:\ProgramData\muse')
foreach ($d in $dirs) {
    if (Test-Path -LiteralPath $d) {
        try {
            [Microsoft.VisualBasic.FileIO.FileSystem]::DeleteDirectory($d, 'OnlyErrorDialogs', 'SendToRecycleBin')
            "recycled $d"
        } catch { "ERROR recycling ${d}: $_" }
    } else { "not present $d" }
}
foreach ($n in $names) {
    if ($sids[$n]) {
        $p = Get-CimInstance Win32_UserProfile -Filter "SID='$($sids[$n])'" -ErrorAction SilentlyContinue
        if ($p) { try { Remove-CimInstance $p; "removed profile record $n" } catch { "ERROR profile record ${n}: $_" } }
    }
}
"--- check ---"
Get-LocalUser | Where-Object Name -match 'muse' | Select-Object Name
Get-ChildItem C:\Users -Force | Where-Object Name -match 'muse' | Select-Object Name
Test-Path C:\ProgramData\muse
