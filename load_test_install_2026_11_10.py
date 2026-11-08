"""Load test with a curated set of widely used packages.

The channel carries no install counts, so "most installed" cannot be computed from
it; these are named because they are the packages a Sublime user is most likely to
have. Each is unpacked into the portable's Packages dir, so one restart shows which
of them failed to import (no command classes registered).
"""

import io
import json
import os
import shutil
import urllib.request
import zipfile

BASE = "C:/Users/donal/projects/sublime-package-audit/"
DEST = "C:/Users/donal/tools/st_portable/Data/Packages"
MANIFEST = BASE + "data/load_test_2026_11_10.json"

WANTED = [
    "GitGutter",
    "BracketHighlighter",
    "DocBlockr",
    "MarkdownEditing",
    "PackageResourceViewer",
    "SideBarEnhancements",
    "A File Icon",
    "ColorHelper",
]

# remove whatever the previous attempt left behind (not part of the baseline)
for stale in ("Emmet", "SFTP", "SVN"):
    path = os.path.join(DEST, stale)
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("removed stale", stale)

ch = json.load(open(BASE + "data/channel_v3.json", encoding="utf-8"))
packages = {}
for repo in ch["packages_cache"].values():
    for p in repo:
        packages.setdefault(p["name"], p)

chosen = []
for name in WANTED:
    p = packages.get(name)
    if not p:
        print("!! not in channel:", name)
        continue
    rels = [r for r in p.get("releases") or [] if "*" in (r.get("platforms") or ["*"])] or (p.get("releases") or [])
    rels.sort(key=lambda r: (r.get("date") or "", r.get("version") or ""))
    rel = rels[-1]
    try:
        raw = urllib.request.urlopen(urllib.request.Request(rel["url"], headers={"User-Agent": "audit"}), timeout=60).read(40_000_000)
        z = zipfile.ZipFile(io.BytesIO(raw))
    except Exception as exc:
        print("!! download failed:", name, exc)
        continue
    target = os.path.join(DEST, name)
    if os.path.isdir(target):
        shutil.rmtree(target)
    os.makedirs(target)
    top = z.namelist()[0].split("/")[0]
    for member in z.namelist():
        if member.endswith("/"):
            continue
        rel_path = member[len(top) + 1:] if member.startswith(top + "/") else member
        out = os.path.join(target, rel_path)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "wb") as f:
            f.write(z.read(member))
    chosen.append({"name": name, "version": rel.get("version"), "date": (rel.get("date") or "")[:10]})
    print("installed %-24s %-12s %s" % (name, rel.get("version"), (rel.get("date") or "")[:10]))

json.dump(chosen, open(MANIFEST, "w", encoding="utf-8"), indent=1)
print("total:", len(chosen))
