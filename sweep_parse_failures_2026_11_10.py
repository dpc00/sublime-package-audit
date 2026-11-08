"""Files that cannot be parsed, across the whole catalogue.

Three kinds of silent breakage:
  * a .sublime-commands / .sublime-keymap / .sublime-menu that is not valid JSON
    after the allowances Sublime makes (comments, trailing commas) — every entry
    in that file disappears;
  * a .sublime-syntax that is not valid YAML — the grammar fails to load;
  * a dependencies.json naming a dependency the channel does not have — the
    package installs and then cannot import what it needs.

Writes and flushes per package, with the parse error, so each hit can be read.
"""

import io
import json
import re
import urllib.request
import zipfile

import yaml

BASE = "C:/Users/donal/projects/sublime-package-audit/"
OUT = BASE + "data/parse_failures_2026_11_10.tsv"

JSON_SUFFIXES = (".sublime-commands", ".sublime-keymap", ".sublime-menu")


def strip_json(text):
    """Remove // and /* */ comments outside strings, then trailing commas."""
    out = []
    i, n = 0, len(text)
    in_str = in_block = in_line = False
    while i < n:
        c = text[i]
        nxt = text[i + 1] if i + 1 < n else ""
        if in_str:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(nxt)
                i += 2
                continue
            if c == '"':
                in_str = False
            i += 1
            continue
        if in_line:
            if c == "\n":
                in_line = False
                out.append(c)
            i += 1
            continue
        if in_block:
            if c == "*" and nxt == "/":
                in_block = False
                i += 2
                continue
            i += 1
            continue
        if c == '"':
            in_str = True
            out.append(c)
            i += 1
            continue
        if c == "/" and nxt == "/":
            in_line = True
            i += 2
            continue
        if c == "/" and nxt == "*":
            in_block = True
            i += 2
            continue
        out.append(c)
        i += 1
    cleaned = "".join(out)
    return re.sub(r",(\s*[}\]])", r"\1", cleaned)


ch = json.load(open(BASE + "data/channel_v3.json", encoding="utf-8"))
known_deps = set()
for deps in (ch.get("dependencies_cache") or {}).values():
    for d in deps:
        if d.get("name"):
            known_deps.add(d["name"].lower())
print("known dependencies:", len(known_deps), flush=True)

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
    if done % 250 == 0:
        print("...", done, "packages,", hits, "hits", flush=True)
    if not rel or not rel.get("url"):
        continue
    try:
        z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(
            urllib.request.Request(rel["url"], headers={"User-Agent": "audit"}), timeout=25).read(25_000_000)))
    except Exception:
        continue
    members = [n for n in z.namelist() if not n.endswith("/")]
    low = {n: n.rsplit("/", 1)[-1].lower() for n in members}

    if "dependencies.json" in low.values():
        member = next(n for n in members if low[n] == "dependencies.json")
        try:
            data = json.loads(strip_json(z.read(member).decode("utf-8-sig", "replace")))
            platforms = data.get("*") or data.get("windows") or {}
            for dep in (platforms.get("install") or {}):
                if dep.lower() not in known_deps:
                    out.write("\t".join([name, rel.get("version") or "", "dependencies.json", "unknown dependency: " + dep]) + "\n")
                    hits += 1
        except Exception as exc:
            out.write("\t".join([name, rel.get("version") or "", "dependencies.json", "unparsable: %s" % type(exc).__name__]) + "\n")
            hits += 1

    for n in members:
        base = low[n]
        if base.endswith(JSON_SUFFIXES):
            try:
                json.loads(strip_json(z.read(n).decode("utf-8-sig", "replace")))
            except Exception as exc:
                msg = str(exc).split(":")[0]
                detail = str(exc)[:120].replace("\t", " ")
                out.write("\t".join([name, rel.get("version") or "", n.rsplit("/", 1)[-1], "%s | %s" % (msg, detail)]) + "\n")
                hits += 1
        elif base.endswith(".sublime-syntax"):
            try:
                yaml.safe_load(z.read(n).decode("utf-8-sig", "replace"))
            except yaml.constructor.ConstructorError:
                pass          # a tag Sublime knows and PyYAML does not, e.g. `key: =`
            except Exception as exc:
                out.write("\t".join([name, rel.get("version") or "", n.rsplit("/", 1)[-1], "yaml: " + str(exc)[:120].replace("\t", " ")]) + "\n")
                hits += 1

out.close()
print("DONE packages:", done, "hits:", hits, flush=True)
