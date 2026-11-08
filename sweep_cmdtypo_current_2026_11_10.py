"""Re-check the surviving near-miss hits against the CURRENT releases.

Two corrections over the first pass:
  * the command-name rule is Sublime's, verified by calling Command.name() on
    probe classes: underscore goes before an uppercase followed by a lowercase.
  * a class may inherit several bases (MpGetFileCommand(WindowCommand, Settings)),
    so the class pattern must accept any base list containing 'Command'.

Also records the case-aliases Sublime accepts: a class `TogglefileCommand` also
answers to `togglefile`, which is why many squashed references are fine.
"""

import io
import json
import re
import urllib.request
import zipfile

BASE = "C:/Users/donal/projects/sublime-package-audit/"
HITS = BASE + "data/command_nearmiss_2026_11_10.tsv"
OUT = BASE + "data/command_nearmiss_current_2026_11_10.tsv"

CLASS_RE = re.compile(r"^class\s+(\w+)\s*\(([^)]*)\)", re.M)
REF_RE = re.compile(r'"command"\s*:\s*"([a-z0-9_]+)"')


def st_name(cls):
    name = re.sub(r"Command$", "", cls)
    out = []
    for i, c in enumerate(name):
        if i and c.isupper() and (i + 1 == len(name) or name[i + 1].islower()):
            out.append("_")
        out.append(c.lower())
    return "".join(out)


def near(a, b):
    if a == b or abs(len(a) - len(b)) > 2:
        return False
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1] <= 2


ch = json.load(open(BASE + "data/channel_v3.json", encoding="utf-8"))
packages = {}
for repo in ch["packages_cache"].values():
    for p in repo:
        packages.setdefault(p["name"], p)

wanted = {line.split("\t")[0] for line in open(HITS, encoding="utf-8") if line.strip()}
rows = []
for name in sorted(wanted):
    p = packages.get(name)
    if not p:
        continue
    rels = [r for r in p.get("releases") or [] if "*" in (r.get("platforms") or ["*"])] or (p.get("releases") or [])
    rels.sort(key=lambda r: (r.get("date") or "", r.get("version") or ""))
    rel = rels[-1]
    try:
        z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(
            urllib.request.Request(rel["url"], headers={"User-Agent": "audit"}), timeout=30).read(30_000_000)))
    except Exception:
        continue
    defined, aliases = set(), set()
    for n in z.namelist():
        if n.endswith(".py"):
            try:
                for cls, bases in CLASS_RE.findall(z.read(n).decode("utf-8", "replace")):
                    if "Command" not in bases:
                        continue
                    defined.add(st_name(cls))
                    aliases.add(re.sub(r"Command$", "", cls).lower())   # Sublime accepts the squashed form
            except Exception:
                pass
    refs = {}
    for n in z.namelist():
        if not n.lower().endswith((".sublime-commands", ".sublime-keymap", ".sublime-menu")):
            continue
        try:
            text = z.read(n).decode("utf-8", "replace")
        except Exception:
            continue
        for ref in REF_RE.findall(text):
            refs.setdefault(ref, set()).add(n.rsplit("/", 1)[-1])
    for ref, files in refs.items():
        if ref in defined or ref in aliases:
            continue
        for cmd in sorted(defined):
            if near(ref, cmd):
                rows.append((name, rel.get("version") or "", ",".join(sorted(files)), ref, cmd))

with open(OUT, "w", encoding="utf-8") as f:
    for row in rows:
        f.write("\t".join(row) + "\n")

print("packages rechecked:", len(wanted), "| survivors:", len(rows))
for row in rows:
    print("  %-30s %-14s ref=%-34s defined=%s  [%s]" % (row[0][:30], row[1][:14], row[3], row[4], row[2][:40]))
