"""Find served packages whose grammars declare no extension mapping at all.

A `.sublime-syntax` needs `file_extensions` and a `.tmLanguage` needs `fileTypes`.
A package where every syntax lacks one can never be selected automatically; that is
the class confirmed in joshraphael/sublime-rascript#7 on 2026-11-10.

Embedded-only grammars ("HTML (Jinja)") legitimately have no extension, so packages
whose syntax names all carry a parenthesised variant are listed separately, not as hits.
"""

import io
import json
import re
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor

CH = "C:/Users/donal/projects/sublime-package-audit/data/channel_pc.json"
OUT = "C:/Users/donal/projects/sublime-package-audit/data/no_extension_2026_11_10.tsv"

d = json.load(open(CH, encoding="utf-8"))
pkgs = d["packages_cache"]["https://packagecontrol.io/repository.json"]


def best(p):
    rels = [r for r in (p.get("releases") or []) if "*" in (r.get("platforms") or ["*"])] or (p.get("releases") or [])
    rels.sort(key=lambda r: (r.get("date") or "", r.get("version") or ""))
    return rels[-1] if rels else None


jobs, seen = [], set()
for p in pkgs:
    r = best(p)
    if not r or not r.get("url") or r["url"] in seen:
        continue
    seen.add(r["url"])
    jobs.append((p["name"], r.get("version") or "", r["url"]))

EXT_LINE = re.compile(r"^[ \t]*file_extensions:[ \t]*(.*)$", re.M)
NEXT_KEY = re.compile(r"^\S", re.M)


def yaml_exts(text):
    out = []
    for m in EXT_LINE.finditer(text):
        tail = m.group(1).strip()
        if tail.startswith("["):
            out += [x for x in re.findall(r"[^\s,\[\]]+", tail)]
            continue
        rest = text[m.end():]
        for line in rest.split("\n"):
            s = line.strip()
            if s.startswith("- "):
                out.append(s[2:].strip().strip("'\""))
            elif s and not s.startswith("#"):
                break
    return [x for x in out if x]


def plist_exts(data):
    text = data.decode("utf-8", "replace")
    m = re.search(r"<key>fileTypes</key>\s*<array>(.*?)</array>", text, re.S)
    if not m:
        return []
    return re.findall(r"<string>([^<]+)</string>", m.group(1))


def probe(job):
    name, version, url = job
    try:
        data = urllib.request.urlopen(
            urllib.request.Request(url, headers={"User-Agent": "sublime-package-audit"}), timeout=120
        ).read(80_000_000)
        z = zipfile.ZipFile(io.BytesIO(data))
    except Exception:
        return []

    syntaxes, with_ext, embedded = [], [], 0
    for n in z.namelist():
        low = n.lower()
        base = n.rsplit("/", 1)[-1]
        if low.endswith(".sublime-syntax"):
            try:
                exts = yaml_exts(z.read(n).decode("utf-8", "replace"))
            except Exception:
                continue
            syntaxes.append((base, exts))
        elif low.endswith((".tmlanguage", ".tmlanguage.json")):
            try:
                exts = plist_exts(z.read(n))
            except Exception:
                continue
            syntaxes.append((base, exts))
        else:
            continue
        if exts:
            with_ext.append(base)
        if "(" in base:
            embedded += 1

    if not syntaxes or with_ext:
        return []
    if embedded == len(syntaxes):
        return []
    names = "; ".join(b for b, _ in syntaxes)[:120]
    return [("no_extension", name, version, str(len(syntaxes)), names)]


rows = []
with ThreadPoolExecutor(max_workers=12) as ex:
    for r in ex.map(probe, jobs):
        rows.extend(r)

with open(OUT, "w", encoding="utf-8") as f:
    for row in sorted(rows):
        f.write("\t".join(row) + "\n")

print("packages checked:", len(jobs))
print("packages with no extension on any syntax:", len(rows))
for row in rows[:25]:
    print("  ", row[1], "|", row[4][:70])
