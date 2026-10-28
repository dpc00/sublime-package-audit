param(
  [string]$Out = "$PSScriptRoot\..\data\ISSUES.reconciled.tsv",
  [int]$Parallel = 8
)
# Read-only against GitHub: for every row of ISSUES.tsv fetch the live title, state, created and closed date and
# write a reconciled copy (it does NOT replace ISSUES.tsv; compare, then copy over by hand).
# Columns written: repository number title state created closed url logged_title checked kind
#   title/state/closed = GitHub now; logged_title = what we logged if it differs; kind = issue | pull_request | missing
$root = Split-Path $PSScriptRoot -Parent
$rows = Import-Csv "$root\ISSUES.tsv" -Delimiter "`t"
$today = Get-Date -Format 'yyyy-MM-dd'
$chunks = for ($i = 0; $i -lt $rows.Count; $i += 40) { , @($rows[$i..([Math]::Min($i + 39, $rows.Count - 1))]) }
$results = New-Object System.Collections.ArrayList
$pending = @()
function Start-Chunk($chunk) {
  Start-Job -ArgumentList (, $chunk) -ScriptBlock {
    param($chunk)
    foreach ($r in $chunk) {
      $j = gh api "repos/$($r.repository)/issues/$($r.number)" --jq '{t:.title,s:.state,c:.created_at,x:.closed_at,p:(.pull_request!=null)}' 2>$null
      if ($j) {
        $o = $j | ConvertFrom-Json
        [pscustomobject]@{ repository=$r.repository; number=$r.number; title=$o.t; state=$o.s
          created=($o.c -replace 'T.*',''); closed=($(if($o.x){$o.x -replace 'T.*',''}else{''})); url=$r.url
          logged_title=($(if($o.t -ne $r.title){$r.title}else{''})); kind=($(if($o.p){'pull_request'}else{'issue'})) }
      } else {
        [pscustomobject]@{ repository=$r.repository; number=$r.number; title=$r.title; state=$r.state
          created=$r.created; closed=$r.closed; url=$r.url; logged_title=''; kind='missing' }
      }
    }
  }
}
foreach ($c in $chunks) {
  while (@($pending | Where-Object { $_.State -eq 'Running' }).Count -ge $Parallel) { Start-Sleep -Milliseconds 300 }
  $pending += Start-Chunk $c
}
$all = $pending | Wait-Job | Receive-Job
$pending | Remove-Job
# keep the original order
$order = @{}; for ($i = 0; $i -lt $rows.Count; $i++) { $order["$($rows[$i].repository)#$($rows[$i].number)"] = $i }
$sorted = $all | Sort-Object { $order["$($_.repository)#$($_.number)"] }
$lines = @("repository`tnumber`ttitle`tstate`tcreated`tclosed`turl`tlogged_title`tchecked`tkind")
foreach ($r in $sorted) {
  $t = ($r.title -replace "[\t\r\n]+", ' '); $lt = ($r.logged_title -replace "[\t\r\n]+", ' ')
  $lines += "$($r.repository)`t$($r.number)`t$t`t$($r.state)`t$($r.created)`t$($r.closed)`t$($r.url)`t$lt`t$today`t$($r.kind)"
}
[IO.File]::WriteAllLines($Out, $lines, (New-Object Text.UTF8Encoding($false)))
"rows in: $($rows.Count)  rows out: $($sorted.Count)"
"kind: " + (($sorted | Group-Object kind | ForEach-Object { "$($_.Name)=$($_.Count)" }) -join ', ')
"state: " + (($sorted | Group-Object state | ForEach-Object { "$($_.Name)=$($_.Count)" }) -join ', ')
"title differs: " + @($sorted | Where-Object { $_.logged_title }).Count
