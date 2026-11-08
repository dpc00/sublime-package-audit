"""Key bindings and palette entries that pass arguments the command cannot take.

A command's run() signature decides which argument keys it accepts. A binding that
passes `{"character": "x"}` to a command whose run() takes `chars` raises TypeError
when pressed — the feature is dead, and it is dead only for the user who tries it.

Only unambiguous cases are reported: the command must be defined by the package
itself, run() must have no **kwargs, and every argument key in the JSON must be
absent from the signature.
"""

import ast
import io
import json
import re
import urllib.request
import zipfile

BASE = "C:/Users/donal/projects/sublime-package-audit/"
OUT = BASE + "data/arg_mismatch_2026_11_10.tsv"

JSON_SUFFIXES = (".sublime-keymap", ".sublime-commands", ".sublime-menu")


def strip_json(text):
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
    return re.sub(r",(\s*[}\]])", r"\1", "".join(out))


def command_name(cls):
    name = re.sub(r"Command$", "", cls)
    out = []
    for i, c in enumerate(name):
        if i and c.isupper() and (i + 1 == len(name) or name[i + 1].islower()):
            out.append("_")
        out.append(c.lower())
    return "".join(out)


def walk(obj, found):
    if isinstance(obj, list):
        for item in obj:
            walk(item, found)
    elif isinstance(obj, dict):
        if isinstance(obj.get("command"), str):
            found.append(obj)
        for value in obj.values():
            walk(value, found)


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
    if done % 250 == 0:
        print("...", done, "packages,", hits, "hits", flush=True)
    if not rel or not rel.get("url"):
        continue
    try:
        z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(
            urllib.request.Request(rel["url"], headers={"User-Agent": "audit"}), timeout=25).read(25_000_000)))
    except Exception:
        continue

    signatures = {}
    for n in z.namelist():
        if not n.endswith(".py"):
            continue
        try:
            tree = ast.parse(z.read(n).decode("utf-8", "replace"))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name.endswith("Command"):
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and item.name == "run":
                        args = [a.arg for a in item.args.args if a.arg != "self"]
                        args += [a.arg for a in item.args.kwonlyargs]
                        signatures[command_name(node.name)] = {
                            "args": set(args),
                            "kwargs": bool(item.args.kwarg),
                            "line": item.lineno,
                            "file": n.rsplit("/", 1)[-1],
                        }
    if not signatures:
        continue

    for n in z.namelist():
        if not n.endswith(JSON_SUFFIXES):
            continue
        try:
            data = json.loads(strip_json(z.read(n).decode("utf-8-sig", "replace")))
        except Exception:
            continue
        found = []
        walk(data, found)
        for entry in found:
            cmd = entry["command"]
            sig = signatures.get(cmd)
            if not sig or sig["kwargs"]:
                continue
            passed = set((entry.get("args") or {}).keys())
            unknown = passed - sig["args"]
            if unknown and passed:
                out.write("\t".join([
                    name, rel.get("version") or "", n.rsplit("/", 1)[-1], cmd,
                    ",".join(sorted(passed)), ",".join(sorted(unknown)),
                    "%s.run(%s) at line %d" % (cmd, ",".join(sorted(sig["args"])), sig["line"]),
                ]) + "\n")
                hits += 1

out.close()
print("DONE packages:", done, "hits:", hits, flush=True)
