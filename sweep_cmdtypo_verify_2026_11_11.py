"""Re-checks the near-miss rows against the CURRENT release of each package.

The 2026-11-10 sweep compared declared command ids with a snapshot of the channel, and
paired a missing id with the nearest registered one, so a row only means "these two
strings are close". It produced rows for packages whose ids were registered all along
(Pretty JSON, Toggle File), because the snapshot carried an older release than the one
Package Control now serves.

This script answers the only question that decides a row: does the package's current
release register the id that its .sublime-commands / .sublime-keymap / .sublime-menu
files name? Sublime derives the id from the class name:

    insert "_" before an uppercase letter that starts a word, i.e. one that is followed
    by a lowercase letter or ends the name (WPSeekCom -> wp_seek_com, Togglefile ->
    togglefile), and never inside a run of capitals.

Output: data/command_nearmiss_verified_2026_11_11.tsv
    package, version, file, declared id, REGISTERED|MISSING, nearest registered id
"""

import io
import json
import re
import sys
import urllib.request
import zipfile

BASE = "C:/Users/donal/projects/sublime-package-audit/"
CH = BASE + "data/channel_v3_live_2026_11_11.json"
IN = BASE + "data/command_nearmiss_real_2026_11_10.tsv"
OUT = BASE + "data/command_nearmiss_verified_2026_11_11.tsv"

CLASS_RE = re.compile(r"^class\s+(\w+)\s*\(([^)]*)\)", re.M)
REF_RE = re.compile(r'"command"\s*:\s*"([a-z0-9_]+)"')


def st_name(cls):
    """Sublime's own derivation, copied from sublime_plugin.py's behaviour."""
    name = re.sub(r"Command$", "", cls)
    out = []
    for i, c in enumerate(name):
        if i and c.isupper() and (i + 1 == len(name) or name[i + 1].islower()):
            out.append("_")
        out.append(c.lower())
    return "".join(out)


def near(a, b, limit=2):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1] <= limit


def main():
    rows = []
    for line in io.open(IN, encoding="utf-8"):
        f = line.rstrip("\n").split("\t")
        if len(f) >= 5:
            rows.append(f[:5])

    wanted = sorted({r[0] for r in rows})
    cache = json.load(io.open(CH, encoding="utf-8"))["packages_cache"]
    packages = {}
    for repo, items in cache.items():
        for p in items:
            packages.setdefault(p["name"], p)

    out = io.open(OUT, "w", encoding="utf-8", newline="")
    out.write("package\tversion\tfile\tdeclared\tstatus\tnearest\n")
    for name in wanted:
        p = packages.get(name)
        mine = [r for r in rows if r[0] == name]
        if not p or not p.get("releases"):
            for r in mine:
                out.write("\t".join([name, "", r[2], r[3], "NO_CHANNEL_ENTRY", r[4]]) + "\n")
            continue
        rels = sorted(p["releases"], key=lambda r: (r.get("date") or "", r.get("version") or ""))
        rel = rels[-1]
        try:
            blob = urllib.request.urlopen(
                urllib.request.Request(rel["url"], headers={"User-Agent": "audit"}), timeout=60
            ).read(60_000_000)
            z = zipfile.ZipFile(io.BytesIO(blob))
        except Exception as exc:
            for r in mine:
                out.write("\t".join([name, rel.get("version") or "", r[2], r[3], "DOWNLOAD_FAILED:%s" % exc, r[4]]) + "\n")
            out.flush()
            continue

        defined = set()
        for n in z.namelist():
            if not n.endswith(".py"):
                continue
            try:
                src = z.read(n).decode("utf-8", "replace")
            except Exception:
                continue
            for cls, _bases in CLASS_RE.findall(src):
                defined.add(st_name(cls))
        for r in mine:
            declared = r[3]
            if declared in defined:
                status = "REGISTERED"
            else:
                status = "MISSING"
            close = sorted((c for c in defined if near(declared, c)), key=lambda c: (abs(len(c) - len(declared)), c))
            out.write("\t".join([name, rel.get("version") or "", r[2], declared, status,
                                 close[0] if close else ""]) + "\n")
        out.flush()
        print("checked", name, rel.get("version"), len(defined), "ids", flush=True)

    out.close()
    print("DONE", len(wanted), "packages", flush=True)


main()
