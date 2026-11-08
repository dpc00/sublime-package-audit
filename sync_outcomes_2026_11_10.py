"""Record what actually happened to each filed report.

The ledger knows a report's state but rarely why it closed. This asks GitHub for
every filed issue, in one GraphQL request per repository, and writes a TSV of
repo, number, state, stateReason, closedAt, title — so the audit can report a fix
rate instead of a filing count.
"""

import json
import subprocess
import time

BASE = "C:/Users/donal/projects/sublime-package-audit/"
OUT = BASE + "data/issue_outcomes_2026_11_10.tsv"

rows = [l.rstrip("\n").split("\t") for l in open(BASE + "ISSUES.tsv", encoding="utf-8")]
entries = [r for r in rows if len(r) >= 7 and r[0] != "repo" and r[6].startswith("https://")]

by_repo = {}
for r in entries:
    repo, num = r[0], r[1]
    if not num.isdigit():
        continue
    by_repo.setdefault(repo, []).append(int(num))

out = open(OUT, "w", encoding="utf-8", buffering=1)
out.write("repo\tnumber\tstate\tstate_reason\tclosed_at\tupdated_at\ttitle\n")

done = ok = 0
for repo, numbers in sorted(by_repo.items()):
    if "/" not in repo:
        continue
    owner, name = repo.split("/", 1)
    for i in range(0, len(numbers), 15):
        chunk = numbers[i:i + 15]
        parts = [
            'i%d: issue(number: %d) { number state stateReason closedAt updatedAt title }' % (n, n)
            for n in chunk
        ]
        query = 'query { repository(owner: "%s", name: "%s") { %s } }' % (owner, name, " ".join(parts))
        res = subprocess.run(["gh", "api", "graphql", "-f", "query=" + query], capture_output=True, text=True)
        done += 1
        if res.returncode != 0:
            continue
        try:
            data = json.loads(res.stdout)["data"]["repository"]
        except Exception:
            continue
        for value in (data or {}).values():
            if not value:
                continue
            out.write("\t".join([
                repo, str(value.get("number")), value.get("state") or "",
                value.get("stateReason") or "", (value.get("closedAt") or "")[:10],
                (value.get("updatedAt") or "")[:10], (value.get("title") or "").replace("\t", " "),
            ]) + "\n")
            ok += 1
        if done % 100 == 0:
            print("repos queried:", done, "issues recorded:", ok, flush=True)

out.close()
print("DONE repos:", done, "issues:", ok, flush=True)
