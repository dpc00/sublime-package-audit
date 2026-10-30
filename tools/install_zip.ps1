param([string]$Name, [string]$Url)
# Installs a Package Control release zip the way PC does for a tag: repack the archive
# without its top folder as Installed Packages\<Name>.sublime-package (portable 4215 only).
$sp = 'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\2862db64-5b96-4f28-a1ac-e12b1ad13dae\scratchpad'
$work = Join-Path $sp ('zip_' + ($Name -replace '[^A-Za-z0-9]', ''))
if (Test-Path $work) { throw "work dir exists: $work" }
New-Item -ItemType Directory $work | Out-Null
$zip = Join-Path $work 'src.zip'
curl.exe -sL -m 120 -o $zip $Url
if (-not (Test-Path $zip) -or (Get-Item $zip).Length -lt 100) { throw "download failed: $Url" }
$ex = Join-Path $work 'x'
Expand-Archive $zip $ex
$top = @(Get-ChildItem $ex)
$root = if ($top.Count -eq 1 -and $top[0].PSIsContainer) { $top[0].FullName } else { $ex }
if (Test-Path (Join-Path $root '.no-sublime-package')) {
  # Package Control installs these as a folder in Packages, not as a .sublime-package
  $dir = "C:\Users\donal\tools\st_portable\Data\Packages\$Name"
  Copy-Item $root $dir -Recurse
  "installed as FOLDER: $dir"
  return
}
$py = Join-Path $work 'pack.py'
@'
import sys, os, zipfile
root, out = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    for d, _, fs in os.walk(root):
        for f in fs:
            p = os.path.join(d, f)
            z.write(p, os.path.relpath(p, root).replace(os.sep, '/'))
print(len(z.namelist()) if False else 'packed')
'@ | Set-Content $py -Encoding UTF8
$dest = "C:\Users\donal\tools\st_portable\Data\Installed Packages\$Name.sublime-package"
python -I $py $root $dest
"installed: $dest  ($((Get-Item $dest).Length) bytes)"
