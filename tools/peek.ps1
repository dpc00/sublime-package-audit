param(
  [Parameter(Mandatory)][string]$Name,
  [int]$MaxChars = 6000     # per file; the rest is cut
)
# Wait for the package zip to appear in the portable, then print its file list and the text of its plugin,
# command, menu, keymap and settings files, so one call replaces: sleep, list zip, read each file.
$z = "C:\Users\donal\tools\st_portable\Data\Installed Packages\$Name.sublime-package"
$tries = 0
while (-not (Test-Path $z) -and $tries -lt 40) { Start-Sleep -Milliseconds 500; $tries++ }
if (-not (Test-Path $z)) { "not installed after 20 s: $z"; return }
Start-Sleep -Milliseconds 800
$py = @'
import sys, zipfile
z = zipfile.ZipFile(sys.argv[1]); cap = int(sys.argv[2])
names = [i for i in z.infolist()]
print('FILES: ' + ', '.join('%s(%d)' % (i.filename, i.file_size) for i in names[:60]) + (' ...' if len(names) > 60 else ''))
want = ('.py', '.sublime-commands', '.sublime-menu', '.sublime-keymap', '.sublime-settings', '.sublime-build', '.sublime-mousemap', '.json')
import re
snips = [i for i in names if i.filename.endswith('.sublime-snippet')]
if snips:
    print('SNIPPETS (%d): file | tabTrigger | scope | content (one line, cut at 150)' % len(snips))
    for i in snips:
        t = z.read(i.filename).decode('utf-8', 'replace')
        g = lambda tag: (re.search('<%s>(.*?)</%s>' % (tag, tag), t, re.S) or [None, ''])[1].strip()
        c = re.sub(r'<!\[CDATA\[|\]\]>', '', g('content'))
        print('%s | %s | %s | %s' % (i.filename, g('tabTrigger'), g('scope'), re.sub(r'\s+', ' ', c)[:150]))
for i in names:
    n = i.filename
    if n.endswith(want) and 'package-metadata' not in n and '(Linux)' not in n and '(OSX)' not in n and i.file_size < 200000:
        t = z.read(n).decode('utf-8', 'replace')
        print('=== %s%s' % (n, '' if len(t) <= cap else ' (cut at %d of %d)' % (cap, len(t))))
        print(t[:cap])
'@
$tmp = Join-Path $env:TEMP 'peek_zip.py'
[IO.File]::WriteAllText($tmp, $py, (New-Object Text.UTF8Encoding($false)))
python -I -X utf8 $tmp $z $MaxChars
