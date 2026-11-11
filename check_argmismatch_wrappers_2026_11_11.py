"""Looks for the wrappers that make an arg-mismatch row a false positive.

`data/arg_mismatch_2026_11_10.tsv` pairs the args a menu/palette entry passes with the
parameters of the command's `run`. That comparison cannot see:

  * a decorator that repackages the args (ST-WindowsContextMenu's
    `_provide_app_menu_set` takes `(self, app, target, **kwargs)` and calls
    `run(app_menu_set=...)`);
  * a `run` that ends in `**kwargs`;
  * a command whose `run` is replaced by an `input()`/`InputHandler`.

For each command named in the list this prints the class that derives it, the `def run`
line, and the decorator lines immediately above it, so the row can be judged by reading
instead of by installing the package.

Output: data/arg_mismatch_wrappers_2026_11_11.tsv
"""

import io
import json
import re
import urllib.request
import zipfile

BASE = "C:/Users/donal/projects/sublime-package-audit/"
CH = BASE + "data/channel_v3_live_2026_11_11.json"
IN = BASE + "data/arg_mismatch_2026_11_10.tsv"
OUT = BASE + "data/arg_mismatch_wrappers_2026_11_11.tsv"

CLASS_RE = re.compile(r"^class\s+(\w+)\s*\(", re.M)


def st_name(cls):
    name = re.sub(r"Command$", "", cls)
    out = []
    for i, c in enumerate(name):
        if i and c.isupper() and (i + 1 == len(name) or name[i + 1].islower()):
            out.append("_")
        out.append(c.lower())
    return "".join(out)


def main():
    wanted = {}
    for line in io.open(IN, encoding="utf-8"):
        f = line.rstrip("\n").split("\t")
        if len(f) >= 5:
            wanted.setdefault(f[0], set()).add(f[3])

    cache = json.load(io.open(CH, encoding="utf-8"))["packages_cache"]
    packages = {}
    for _repo, items in cache.items():
        for p in items:
            packages.setdefault(p["name"], p)

    out = io.open(OUT, "w", encoding="utf-8", newline="")
    out.write("package\tversion\tcommand\tclass\tdef_run\thas_kwargs\tdecorators\thas_input\n")
    for name, commands in sorted(wanted.items()):
        p = packages.get(name)
        if not p:
            out.write("\t".join([name, "", ",".join(sorted(commands)), "", "NO_CHANNEL_ENTRY", "", ""]) + "\n")
            continue
        rels = sorted(p["releases"], key=lambda r: (r.get("date") or "", r.get("version") or ""))
        rel = rels[-1]
        try:
            blob = urllib.request.urlopen(
                urllib.request.Request(rel["url"], headers={"User-Agent": "audit"}), timeout=60
            ).read(80_000_000)
            z = zipfile.ZipFile(io.BytesIO(blob))
        except Exception as exc:
            out.write("\t".join([name, rel.get("version") or "", ",".join(sorted(commands)), "",
                                 "DOWNLOAD_FAILED:%s" % exc, "", ""]) + "\n")
            out.flush()
            continue

        sources = {}
        for n in z.namelist():
            if n.endswith(".py"):
                try:
                    sources[n] = z.read(n).decode("utf-8", "replace")
                except Exception:
                    pass

        for cmd in sorted(commands):
            found = False
            for n, src in sources.items():
                for m in re.finditer(r"^class\s+(\w+)\s*\(", src, re.M):
                    cls = m.group(1)
                    if st_name(cls) != cmd:
                        continue
                    found = True
                    tail = src[m.start():m.start() + 4000]
                    rm = re.search(r"^\s+def run\(([^)]*)\)", tail, re.M)
                    decos = ""
                    if rm:
                        # the decorator sits directly above `def run`, inside the class
                        at = m.start() + rm.start()
                        above = src[:at].splitlines()[-8:]
                        decos = " ".join(x.strip() for x in above if x.strip().startswith("@"))
                    block_end = src.find("\nclass ", m.start() + 1)
                    block = src[m.start(): block_end if block_end > 0 else len(src)]
                    has_input = "yes" if re.search(r"^\s+def input\(", block, re.M) else "no"
                    out.write("\t".join([
                        name, rel.get("version") or "", cmd, cls,
                        (re.sub(r"\s+", " ", rm.group(1)).strip() if rm else ""),
                        "yes" if (rm and "**" in rm.group(1)) else "no",
                        decos,
                        has_input,
                    ]) + "\n")
                    break
                if found:
                    break
            if not found:
                out.write("\t".join([name, rel.get("version") or "", cmd, "", "NO_CLASS_IN_ZIP", "", ""]) + "\n")
        out.flush()
        print("checked", name, rel.get("version"), flush=True)
    out.close()


main()
