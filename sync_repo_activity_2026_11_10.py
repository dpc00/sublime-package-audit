"""How much of the open backlog sits on repositories that are still alive?

For every repository with an unanswered report, record its last push. A report on a
repo untouched for years is not a fix candidate; one on a repo pushed this month is.
"""

import json
import subprocess

BASE = "C:/Users/donal/projects/sublime-package-audit/"
OUT = BASE + "data/repo_activity_2026_11_10.tsv"

outcomes = [l.rstrip("\n").split("\t") for l in open(BASE + "data/issue_outcomes_2026_11_10.tsv", encoding="utf-8")][1:]
open_repos = sorted({r[0] for r in outcomes if len(r) > 1 and r[2] == "OPEN"})
print("repos with an open report:", len(open_repos), flush=True)

out = open(OUT, "w", encoding="utf-8", buffering=1)
out.write("repo\tpushed_at\tarchived\topen_reports\n")
done = errors = 0
counts = {}
for r in outcomes:
    if len(r) > 2 and r[2] == "OPEN":
        counts[r[0]] = counts.get(r[0], 0) + 1

for repo in open_repos:
    if "/" not in repo:
        continue
    query = 'query { repository(owner: "%s", name: "%s") { pushedAt isArchived } }' % tuple(repo.split("/", 1))
    res = subprocess.run(["gh", "api", "graphql", "-f", "query=" + query], capture_output=True, text=True)
    done += 1
    if res.returncode != 0:
        errors += 1
        continue
    try:
        d = json.loads(res.stdout)["data"]["repository"] or {}
    except Exception:
        errors += 1
        continue
    out.write("\t".join([repo, (d.get("pushedAt") or "")[:10], str(d.get("isArchived")), str(counts.get(repo, 0))]) + "\n")
    if done % 250 == 0:
        print("queried:", done, "errors:", errors, flush=True)

out.close()
print("DONE repos:", done, "errors:", errors, flush=True)
