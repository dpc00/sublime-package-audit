import json, subprocess, sys, time, datetime as dt

OUT = sys.argv[1]
START = dt.date(2026, 8, 1)
END = dt.date.today()
rows = {}
d = START
while d <= END:
    d2 = d + dt.timedelta(days=1)
    q = f"{d.isoformat()}..{d2.isoformat()}"
    for attempt in range(4):
        p = subprocess.run(
            ["gh", "search", "issues", "--author", "dpc00", "--created", q,
             "--json", "repository,number,title,state,createdAt,closedAt,url", "--limit", "1000"],
            capture_output=True, text=True, encoding="utf-8")
        if p.returncode == 0:
            break
        time.sleep(15)
    else:
        print("FAILED window", q, p.stderr[:200])
        sys.exit(1)
    for it in json.loads(p.stdout or "[]"):
        key = (it["repository"]["nameWithOwner"], it["number"])
        rows[key] = it
    print(q, len(rows), flush=True)
    d = d + dt.timedelta(days=2)
    time.sleep(2.5)

def clean(s):
    return (s or "").replace("\t", " ").replace("\r", " ").replace("\n", " ")

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("repository\tnumber\ttitle\tstate\tcreated\tclosed\turl\n")
    for key, it in sorted(rows.items(), key=lambda kv: (kv[1]["createdAt"], kv[0])):
        f.write("\t".join([key[0], str(key[1]), clean(it["title"]), it["state"].lower(),
                           it["createdAt"][:10], (it["closedAt"] or "")[:10], it["url"]]) + "\n")
print("rows", len(rows))
