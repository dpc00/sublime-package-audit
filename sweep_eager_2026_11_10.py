"""Random sample of served packages, scanned for a bug class that bites in real use:
a settings lookup whose DEFAULT argument does work (a call), because Python evaluates
it before `get` ever consults the setting. Found live in sisoe24/Nuke-Tools-ST#6.

Only lists candidates; every one is checked by hand and then live before anything is filed.
"""

import io
import json
import random
import re
import urllib.request
import zipfile

CH = "C:/Users/donal/projects/sublime-package-audit/data/channel_pc.json"
OUT = "C:/Users/donal/projects/sublime-package-audit/data/eager_default_2026_11_10.tsv"

# settings.get("key", something())  |  .get(key, something())  |  load_settings(...).get(k, f())
PAT = re.compile(r"\.get\(\s*[^,()]{1,60},\s*([A-Za-z_][\w.]*\()[^)]*\)")

d = json.load(open(CH, encoding="utf-8"))
pkgs = d["packages_cache"]["https://packagecontrol.io/repository.json"]

rels = []
for p in pkgs:
    r = p.get("releases") or []
    r = [x for x in r if "*" in (x.get("platforms") or ["*"])] or r
    if not r:
        continue
    r.sort(key=lambda x: (x.get("date") or "", x.get("version") or ""))
    rels.append((p["name"], r[-1].get("version") or "", r[-1]["url"]))

random.seed(20261110)
sample = random.sample(rels, 300)

rows = []
for name, version, url in sample:
    try:
        data = urllib.request.urlopen(
            urllib.request.Request(url, headers={"User-Agent": "audit"}), timeout=60
        ).read(40_000_000)
        z = zipfile.ZipFile(io.BytesIO(data))
    except Exception:
        continue
    for n in z.namelist():
        if not n.endswith(".py"):
            continue
        try:
            src = z.read(n).decode("utf-8", "replace")
        except Exception:
            continue
        for m in PAT.finditer(src):
            line = src.count("\n", 0, m.start()) + 1
            rows.append((name, version, n, str(line), m.group(0)[:90]))

with open(OUT, "w", encoding="utf-8") as f:
    for row in rows:
        f.write("\t".join(row) + "\n")

print("sampled:", len(sample), "hits:", len(rows))
for row in rows[:20]:
    print("  ", row[0], "|", row[2], "L" + row[3], "|", row[4])
