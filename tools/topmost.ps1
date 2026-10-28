param([long]$Hwnd, [string]$On)
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Tm {
  [DllImport("user32.dll")] public static extern bool SetWindowPos(IntPtr h, IntPtr after, int x, int y, int cx, int cy, uint flags);
}
"@
# SWP_NOMOVE 2 | SWP_NOSIZE 1 | SWP_SHOWWINDOW 0x40
$after = if ($On -eq 'on') { [IntPtr](-1) } else { [IntPtr](-2) }
[Tm]::SetWindowPos([IntPtr]$Hwnd, $after, 0, 0, 0, 0, 0x43) | Out-Null
"topmost " + $On
