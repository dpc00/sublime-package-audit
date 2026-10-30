param([Parameter(Mandatory)][string]$Repo)
# Liveness check before filing an issue (Donald, 2026-10-30: "do the right thing; if it is dead, find out and skip it").
# Prints ALIVE or DEAD with the facts. DEAD = record in RESULTS.tsv only. This is NOT the retired age/installs gate:
# popularity and package age do not matter, only whether a person is still there to read an issue.
#   DEAD if: archived, or issues disabled, or repo not found, or
#   (last commit older than 3 years AND no comment by the owner and no issue/PR by the owner in the last 3 years).
#   ALIVE otherwise.
$owner = $Repo.Split('/')[0]
$cut = (Get-Date).AddYears(-3).ToString('yyyy-MM-dd')
$m = gh repo view $Repo --json isArchived,hasIssuesEnabled 2>$null | ConvertFrom-Json
if (-not $m) { "DEAD: repo not found"; exit 0 }
if ($m.isArchived) { "DEAD: archived"; exit 0 }
if (-not $m.hasIssuesEnabled) { "DEAD: issues disabled"; exit 0 }
$last = gh api "repos/$Repo/commits?per_page=1" --jq '.[0].commit.committer.date' 2>$null
$lastDay = if ($last) { $last.Substring(0,10) } else { '0000-00-00' }
if ($lastDay -ge $cut) { "ALIVE: last commit $lastDay"; exit 0 }
$oc = gh api "repos/$Repo/issues/comments?sort=updated&direction=desc&per_page=50" --jq "[.[] | select(.user.login==`"$owner`") | .created_at][0]" 2>$null
$oi = gh api "search/issues?q=repo:$Repo+author:$owner+updated:>$cut&per_page=1" --jq '.total_count' 2>$null
$ocDay = if ($oc -and $oc -ne 'null') { $oc.Substring(0,10) } else { '' }
if (($ocDay -and $ocDay -ge $cut) -or ([int]$oi -gt 0)) { "ALIVE: last commit $lastDay, owner active (comment $ocDay, issues/PRs $oi)"; exit 0 }
"DEAD: last commit $lastDay, no owner comment or issue in 3 years (last owner comment: $(if($ocDay){$ocDay}else{'none'}))"
