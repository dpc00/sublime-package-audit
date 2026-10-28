import ast, difflib, glob, json, os, sys, warnings
warnings.filterwarnings('ignore')
sys.argv = ['x']
exec(open('cmd_scan.py', encoding='utf8').read().split("SKIP = (")[0])  # reuse helpers (cmd_name etc.)
rep = json.load(open('cmd_missing.json'))
for idx, name, missing in rep:
    p = glob.glob(os.path.join(REPOS, '%04d_*' % idx))[0]
    defined = set()
    for dp, dn, fn in os.walk(p):
        if os.sep + '.git' in dp: continue
        for f in fn:
            if f.endswith('.py'):
                try: tree = ast.parse(open(os.path.join(dp, f), encoding='utf8', errors='replace').read())
                except Exception: continue
                for n in ast.walk(tree):
                    if isinstance(n, ast.ClassDef) and (n.name.endswith('Command') or any('Command' in ast.unparse(b) for b in n.bases)):
                        defined.add(cmd_name(n.name))
    for c, files in missing.items():
        m = difflib.get_close_matches(c, defined, n=1, cutoff=0.8)
        if m:
            print('%4d %-26s %-42s ~ %-42s %s' % (idx, name[:26], c[:42], m[0][:42], files[0][:38]))
