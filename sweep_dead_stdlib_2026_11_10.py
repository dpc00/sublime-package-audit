"""Packages that import a module removed from recent Python.

Sublime Text 4.4215 hosts Python 3.14, so an `import imp` is not a warning but a
ModuleNotFoundError at plugin load: the package's commands never register and
everything it offers is dead. Same for distutils (gone in 3.12), asyncore/asynchat/
smtpd/cgi/cgitb/telnetlib/nntplib/pipes/crypt/uu/xdrlib/chunk/audioop/aifc/mailcap/
sndhdr/imghdr/sunau/nis/ossaudiodev/spwd/msilib (3.13) and lib2to3.

Writes and flushes per package. Print the imported module, so a hit can be read
before anything is believed.
"""

import io
import json
import re
import urllib.request
import zipfile

BASE = "C:/Users/donal/projects/sublime-package-audit/"
OUT = BASE + "data/dead_stdlib_imports_2026_11_10.tsv"

REMOVED = {
    "imp", "distutils", "asyncore", "asynchat", "smtpd", "cgi", "cgitb", "telnetlib",
    "nntplib", "pipes", "crypt", "uu", "xdrlib", "chunk", "audioop", "aifc", "mailcap",
    "sndhdr", "imghdr", "sunau", "nis", "ossaudiodev", "spwd", "msilib", "lib2to3",
}
IMPORT_RE = re.compile(r"^[ \t]*(?:from[ \t]+([A-Za-z_][\w.]*)[ \t]+import|import[ \t]+([A-Za-z_][\w., \t]*))", re.M)

ch = json.load(open(BASE + "data/channel_v3.json", encoding="utf-8"))
packages = {}
for repo in ch["packages_cache"].values():
    for p in repo:
        packages.setdefault(p["name"], p)

out = open(OUT, "a", encoding="utf-8", buffering=1)
done = hits = 0
for name, p in sorted(packages.items()):
    rels = [r for r in p.get("releases") or [] if "*" in (r.get("platforms") or ["*"])] or (p.get("releases") or [])
    rels.sort(key=lambda r: (r.get("date") or "", r.get("version") or ""))
    rel = rels[-1] if rels else None
    done += 1
    if done % 200 == 0:
        print("...", done, "packages,", hits, "hits", flush=True)
    if not rel or not rel.get("url"):
        continue
    try:
        z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(
            urllib.request.Request(rel["url"], headers={"User-Agent": "audit"}), timeout=20).read(20_000_000)))
    except Exception:
        continue
    for n in z.namelist():
        if not n.endswith(".py"):
            continue
        try:
            src = z.read(n).decode("utf-8", "replace")
        except Exception:
            continue
        for from_mod, plain in IMPORT_RE.findall(src):
            mods = []
            if from_mod:
                mods.append(from_mod)
            else:
                mods.extend(m.strip().split(" as ")[0] for m in plain.split(","))
            for m in mods:
                root = m.split(".")[0].strip()
                if root in REMOVED:
                    out.write("\t".join([name, rel.get("version") or "", n.rsplit("/", 1)[-1], root]) + "\n")
                    hits += 1

out.close()
print("DONE packages:", done, "hits:", hits, flush=True)
