import ast, json, os, re, sys
import xml.dom.minidom as md

root = sys.argv[1]


def loose(text):
    out, i, n, instr = [], 0, len(text), False
    while i < n:
        c = text[i]
        if instr:
            out.append(c)
            if c == "\\":
                out.append(text[i + 1]); i += 1
            elif c == '"':
                instr = False
        elif c == '"':
            instr = True; out.append(c)
        elif text.startswith("//", i):
            while i < n and text[i] != "\n": i += 1
            continue
        elif text.startswith("/*", i):
            i = text.find("*/", i) + 2; continue
        else:
            out.append(c)
        i += 1
    return re.sub(r",(\s*[}\]])", r"\1", "".join(out))


files = {os.path.relpath(os.path.join(d, f), root).replace("\\", "/") for d, _, fs in os.walk(root) for f in fs}
issues = []
for rel in sorted(files):
    p = os.path.join(root, rel)
    try:
        if rel.endswith((".sublime-theme", ".sublime-color-scheme", ".sublime-settings", ".sublime-commands", ".sublime-menu", ".sublime-keymap", ".sublime-completions", ".sublime-build")) or rel.endswith("package-metadata.json") is False and rel.endswith("messages.json"):
            t = open(p, encoding="utf-8-sig").read()
            d = json.loads(loose(t))
            if rel.endswith(".sublime-theme"):
                for rule in (d if isinstance(d, list) else []):
                    for k in ("layer0.texture", "layer1.texture", "layer2.texture", "layer3.texture", "texture"):
                        v = rule.get(k) if isinstance(rule, dict) else None
                        if isinstance(v, str) and v.startswith("Packages/"):
                            parts = v.split("/", 2)[2:]
                            tail = parts[0] if parts else ""
                            cands = [tail, tail + ".png", tail.replace("@2x", "")]
                            if not any(c in files or (c + ".png") in files for c in cands):
                                # texture may live in another package; only flag when it names this repo's folders
                                if "/" in tail and tail.split("/")[0] in {f.split("/")[0] for f in files if "/" in f}:
                                    issues.append("%s: texture %s not in repo" % (rel, v))
        elif rel.endswith(".tmTheme") or rel.endswith(".tmLanguage") or rel.endswith(".tmPreferences"):
            md.parse(p)
        elif rel.endswith(".py"):
            ast.parse(open(p, encoding="utf-8-sig", errors="replace").read())
    except Exception as e:
        issues.append("%s: %s" % (rel, str(e)[:90]))
print("; ".join(issues) if issues else "clean")
