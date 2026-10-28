param([long]$Hwnd, [long]$Back = 0)   # -Back <hwnd of his main Sublime>: after the step, clear topmost on $Hwnd and give the foreground back to that window
Add-Type @'
using System;
using System.Runtime.InteropServices;
public class Fg {
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("user32.dll")] public static extern bool AttachThreadInput(uint a, uint b, bool attach);
  [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h, int cmd);
  [DllImport("user32.dll")] public static extern bool BringWindowToTop(IntPtr h);
  [DllImport("user32.dll")] public static extern void SwitchToThisWindow(IntPtr h, bool alt);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("user32.dll")] public static extern bool SetWindowPos(IntPtr h, IntPtr after, int x, int y, int cx, int cy, uint flags);
  [DllImport("user32.dll", EntryPoint="GetWindowLongW")] public static extern int GetWindowLong(IntPtr h, int i);
  [DllImport("kernel32.dll")] public static extern uint GetCurrentThreadId();
}
'@
function Clear-Topmost($w) {
  # never leave a test window always-on-top (Donald, 2026-10-28: "obnoxious and thwarts me")
  if (([Fg]::GetWindowLong($w,-20) -band 0x8) -ne 0) { [void][Fg]::SetWindowPos($w,[IntPtr]-2,0,0,0,0,0x13); "cleared topmost on $w" }
}
function Front($h) {
  $fg=[Fg]::GetForegroundWindow(); $pid2=0
  $ft=[Fg]::GetWindowThreadProcessId($fg,[ref]$pid2); $me=[Fg]::GetCurrentThreadId()
  [void][Fg]::AttachThreadInput($me,$ft,$true)
  [void][Fg]::ShowWindow($h,9); [void][Fg]::BringWindowToTop($h); [Fg]::SwitchToThisWindow($h,$true); [void][Fg]::SetForegroundWindow($h)
  [void][Fg]::AttachThreadInput($me,$ft,$false)
  Start-Sleep -Milliseconds 400
}
$h=[IntPtr]$Hwnd
if ($Back -ne 0) {
  Clear-Topmost $h
  $m=[IntPtr]$Back; Front $m
  "foreground handed back: " + ([Fg]::GetForegroundWindow() -eq $m)
} else {
  Front $h
  Clear-Topmost $h
  "foreground now is target: " + ([Fg]::GetForegroundWindow() -eq $h)
}
