import subprocess, json, collections, os, sys

def gh(args):
    r = subprocess.run(["gh"] + args, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise RuntimeError(r.stderr[:300])
    return r.stdout

# 1) every issue authored by dpc00 (search API, 100 per page)
items = []
for page in range(1, 9):
    out = gh(["api", "search/issues?q=author:dpc00+is:issue&per_page=100&page=%d" % page])
    data = json.loads(out)
    got = data.get("items", [])
    items.extend(got)
    if len(got) < 100:
        break
print("issues fetched:", len(items))

def repo_of(it):
    return it["repository_url"].split("/repos/")[1]

by_repo = collections.Counter(repo_of(it) for it in items)
owners = collections.Counter(r.split("/")[0] for r in by_repo)
print("distinct repos:", len(by_repo), "| distinct owners:", len(owners))

state = collections.Counter((it["state"], it.get("state_reason")) for it in items)
print("state / reason:", dict(state))

# 2) response signals without extra calls: comments by others cannot be told from the search item,
#    so use comments>0 as an upper bound and look up the closer for the closed ones.
closed = [it for it in items if it["state"] == "closed"]
closer = collections.Counter()
closed_rows = []
for it in closed:
    repo = repo_of(it)
    try:
        d = json.loads(gh(["api", "repos/%s/issues/%d" % (repo, it["number"])]))
        by = (d.get("closed_by") or {}).get("login", "?")
    except Exception as e:
        by = "?"
    closer["self" if by == "dpc00" else ("other" if by != "?" else "unknown")] += 1
    closed_rows.append((repo, it["number"], it.get("state_reason"), by, it["comments"], it["title"][:70]))
print("closed by:", dict(closer))
comp_other = [r for r in closed_rows if r[3] not in ("dpc00", "?") and r[2] == "completed"]
np_other = [r for r in closed_rows if r[3] not in ("dpc00", "?") and r[2] == "not_planned"]
print("closed by someone else as COMPLETED:", len(comp_other), "| as NOT PLANNED:", len(np_other))

open_items = [it for it in items if it["state"] == "open"]
with_comments = [it for it in open_items if it["comments"] > 0]
print("open issues:", len(open_items), "| open with >=1 comment (any author):", len(with_comments))

# 3) PRs
prs = []
for page in range(1, 4):
    data = json.loads(gh(["api", "search/issues?q=author:dpc00+is:pr&per_page=100&page=%d" % page]))
    got = data.get("items", [])
    prs.extend(got)
    if len(got) < 100:
        break
pr_by_repo = collections.Counter(repo_of(p) for p in prs)
print("PRs:", len(prs), "| by repo (top):", pr_by_repo.most_common(6))

# repos where at least one issue was closed as completed by the maintainer
repos_fixed = sorted({r[0] for r in comp_other})
print("repos with >=1 issue closed as completed by a maintainer:", len(repos_fixed))

out = {"issues": len(items), "repos": len(by_repo), "owners": len(owners), "state": {str(k): v for k, v in state.items()},
       "closed_by": dict(closer), "completed_by_other": len(comp_other), "not_planned_by_other": len(np_other),
       "open": len(open_items), "open_with_comments": len(with_comments), "prs": len(prs),
       "repos_with_completed": repos_fixed, "closed_rows": closed_rows}
p = os.path.join(os.environ["TEMP"], "campaign_stats.json")
json.dump(out, open(p, "w", encoding="utf-8"), indent=1)
print("saved", p)
