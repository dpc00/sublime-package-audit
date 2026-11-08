"""Near-miss command references — writes and flushes per package, so a kill keeps
everything found so far. A menu/palette/keymap entry that names a command the
package almost defines: typed by hand, a near miss means the entry does nothing.
"""

import io
import json
import re
import sys
import urllib.request
import zipfile

CH = "C:/Users/donal/projects/sublime-package-audit/data/channel_pc.json"
OUT = "C:/Users/donal/projects/sublime-package-audit/data/command_nearmiss_2026_11_10.tsv"

CLASS_RE = re.compile(r"^class\s+(\w+)\((?:sublime_plugin\.)?(?:Text|Window|Application)Command\)", re.M)
REF_RE = re.compile(r'"command"\s*:\s*"([a-z0-9_]+)"')

d = json.load(open(CH, encoding="utf-8"))
pkgs = d["packages_cache"]["https://packagecontrol.io/repository.json"]


def snake(cls):
    """Sublime's rule: an underscore at a lowercase->uppercase boundary and between
    an acronym and the next word (WPSeekCom -> wp_seek_com), never inside a run of
    capitals, and never before the first letter."""
    name = re.sub(r"Command$", "", cls)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()


def near(a, b):
    if a == b or abs(len(a) - len(b)) > 2:
        return False
    if a.startswith(b) or b.startswith(a):
        return True
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1] <= 2


out = open(OUT, "a", encoding="utf-8", buffering=1)
done = 0
hits = 0
for p in pkgs:
    rels = [r for r in (p.get("releases") or []) if "*" in (r.get("platforms") or ["*"])] or (p.get("releases") or [])
    rels.sort(key=lambda r: (r.get("date") or "", r.get("version") or ""))
    rel = rels[-1] if rels else None
    done += 1
    if done % 25 == 0:
        print("...", done, "packages,", hits, "hits", flush=True)
    if not rel or not rel.get("url"):
        continue
    try:
        data = urllib.request.urlopen(
            urllib.request.Request(rel["url"], headers={"User-Agent": "audit"}), timeout=25
        ).read(30_000_000)
        z = zipfile.ZipFile(io.BytesIO(data))
    except Exception:
        continue
    defined = set()
    for n in z.namelist():
        if n.endswith(".py"):
            try:
                for cls in CLASS_RE.findall(z.read(n).decode("utf-8", "replace")):
                    defined.add(snake(cls))
            except Exception:
                pass
    if not defined:
        continue
    for n in z.namelist():
        if not n.lower().endswith((".sublime-commands", ".sublime-keymap", ".sublime-menu")):
            continue
        try:
            text = z.read(n).decode("utf-8", "replace")
        except Exception:
            continue
        for ref in set(REF_RE.findall(text)):
            if ref in defined:
                continue
            for cmd in sorted(defined):
                if near(ref, cmd):
                    out.write("\t".join([p["name"], rel.get("version") or "", n.rsplit("/", 1)[-1], ref, cmd]) + "\n")
                    hits += 1

out.close()
print("DONE packages:", done, "hits:", hits, flush=True)
