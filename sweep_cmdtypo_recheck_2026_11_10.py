"""Re-check the near-miss hits using Sublime's real command-name rule.

Sublime inserts '_' only where an uppercase letter follows a lowercase (or digit)
one, so `WPSeekComOpenSelectionCommand` -> `wpseek_com_open_selection`,
`ToggleFileCommand` -> `toggle_file`, `NimPlus...` -> `nimplus_...`.
My first pass split on every capital, which invented splits that Sublime never
makes; every hit that vanishes here was that artefact.
"""

import io
import json
import re
import urllib.request
import zipfile

BASE = "C:/Users/donal/projects/sublime-package-audit/"
CH = BASE + "data/channel_pc.json"
HITS = BASE + "data/command_nearmiss_2026_11_10.tsv"
OUT = BASE + "data/command_nearmiss_real_2026_11_10.tsv"

CLASS_RE = re.compile(r"^class\s+(\w+)\((?:sublime_plugin\.)?(?:Text|Window|Application)Command\)", re.M)
REF_RE = re.compile(r'"command"\s*:\s*"([a-z0-9_]+)"')


def st_name(cls):
    """Sublime's CamelCase -> command-name conversion."""
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


names = set()
for line in open(HITS, encoding="utf-8"):
    if line.strip():
        names.add(line.split("\t")[0])

d = json.load(open(CH, encoding="utf-8"))
cache = {p["name"]: p for p in d["packages_cache"]["https://packagecontrol.io/repository.json"]}

survivors = []
for name in sorted(names):
    p = cache.get(name)
    if not p:
        continue
    rels = [r for r in p["releases"] if "*" in (r.get("platforms") or ["*"])] or p["releases"]
    rels.sort(key=lambda r: (r.get("date") or "", r.get("version") or ""))
    rel = rels[-1]
    try:
        z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(
            urllib.request.Request(rel["url"], headers={"User-Agent": "audit"}), timeout=30).read(30_000_000)))
    except Exception:
        continue
    defined = set()
    for n in z.namelist():
        if n.endswith(".py"):
            try:
                for cls in CLASS_RE.findall(z.read(n).decode("utf-8", "replace")):
                    defined.add(st_name(cls))
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
        if ref in defined:
            continue
        for cmd in sorted(defined):
            if near(ref, cmd):
                survivors.append((name, rel.get("version") or "", ",".join(sorted(files)), ref, cmd))

with open(OUT, "w", encoding="utf-8") as f:
    for row in survivors:
        f.write("\t".join(row) + "\n")

print("packages with hits:", len(names), "survivors:", len(survivors))
for row in survivors:
    print("  %-34s ref=%-42s defined=%s" % (row[0][:34], row[3], row[4]))
