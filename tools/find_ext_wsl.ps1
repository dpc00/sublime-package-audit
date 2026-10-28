"== Chrome/Edge extensions matching codex|openai|chatgpt|muse|meta =="
$rows = foreach ($b in "$env:LOCALAPPDATA\Google\Chrome\User Data", "$env:LOCALAPPDATA\Microsoft\Edge\User Data") {
    Get-ChildItem $b -Directory -ErrorAction SilentlyContinue | Where-Object { Test-Path "$($_.FullName)\Extensions" } | ForEach-Object {
        $prof = $_.Name
        Get-ChildItem "$($_.FullName)\Extensions" -Directory -ErrorAction SilentlyContinue | ForEach-Object {
            $id = $_.Name
            $v = Get-ChildItem $_.FullName -Directory | Select-Object -Last 1
            $m = Get-Content "$($v.FullName)\manifest.json" -Raw -ErrorAction SilentlyContinue | ConvertFrom-Json -ErrorAction SilentlyContinue
            $n = $m.name
            if ($n -match '^__MSG_(.+)__$') {
                $loc = Get-Content "$($v.FullName)\_locales\en\messages.json" -Raw -ErrorAction SilentlyContinue | ConvertFrom-Json -ErrorAction SilentlyContinue
                $n = $loc.($Matches[1]).message
            }
            "$b | $prof | $id | $n"
        }
    }
}
"total extensions seen: $(@($rows).Count)"
$rows | Where-Object { $_ -match 'codex|openai|chatgpt|muse|meta' }
"== WSL Ubuntu =="
wsl.exe -d Ubuntu -- bash -lc 'echo user=$(whoami); for c in codex muse openai; do command -v $c; done; ls -d ~/.codex ~/.muse ~/.config/codex ~/.config/muse ~/.cache/codex /opt/codex /opt/muse /usr/local/bin/codex /usr/local/bin/muse 2>/dev/null; ls ~/.npm-global/lib/node_modules /usr/lib/node_modules /usr/local/lib/node_modules 2>/dev/null | grep -iE "codex|openai|muse"; pip list 2>/dev/null | grep -iE "codex|openai|muse"; getent passwd | grep -iE "codex|muse"; echo done'
