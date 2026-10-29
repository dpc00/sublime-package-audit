param(
  [string]$Out = "$PSScriptRoot\..\data\open_asks.tsv",
  [string]$Me = 'dpc00'
)
# On demand, read-only against GitHub. For every OPEN issue in ISSUES.tsv, fetch the last comment.
# Lists the issues whose last comment is from someone other than $Me: a maintainer or user has written
# and we have not answered (or the last word is theirs). Newest first.
# Columns: date author repository number title first_line url
# Refresh ISSUES.tsv first (tools\reconcile_issues.ps1) so the open list is current.
$root = Split-Path $PSScriptRoot -Parent
$rows = Import-Csv "$root\ISSUES.tsv" -Delimiter "`t" | Where-Object { $_.state -eq 'open' }
$res = New-Object System.Collections.ArrayList
for ($i = 0; $i -lt $rows.Count; $i += 25) {
  $chunk = $rows[$i..([Math]::Min($i + 24, $rows.Count - 1))]
  $q = "query {"; $k = 0
  foreach ($r in $chunk) {
    $o, $n = $r.repository -split '/', 2
    $q += " a$k : repository(owner:\`"$o\`", name:\`"$n\`") { issue(number:$($r.number)) { comments(last:1) { nodes { author { login } createdAt body } } } }"
    $k++
  }
  $q += " }"
  $json = gh api graphql -f query="$q" 2>$null | ConvertFrom-Json
  $k = 0
  foreach ($r in $chunk) {
    $c = $json.data."a$k".issue.comments.nodes | Select-Object -First 1
    if ($c -and $c.author.login -ne $Me) {
      $first = (($c.body -split "`n" | Where-Object { $_.Trim() } | Select-Object -First 1) -replace "[\t\r]", ' ')
      if ($first.Length -gt 140) { $first = $first.Substring(0, 140) }
      [void]$res.Add([pscustomobject]@{ date = $c.createdAt.Substring(0, 10); author = $c.author.login; repository = $r.repository
          number = $r.number; title = ($r.title -replace "[\t\r\n]+", ' '); first_line = $first; url = $r.url })
    }
    $k++
  }
}
$sorted = $res | Sort-Object date -Descending
$lines = @("date`tauthor`trepository`tnumber`ttitle`tfirst_line`turl")
foreach ($r in $sorted) { $lines += "$($r.date)`t$($r.author)`t$($r.repository)`t$($r.number)`t$($r.title)`t$($r.first_line)`t$($r.url)" }
[IO.File]::WriteAllLines($Out, $lines, (New-Object Text.UTF8Encoding($false)))
"open issues checked: $($rows.Count)  waiting on us (last comment not by $Me): $(@($sorted).Count)  -> $Out"
