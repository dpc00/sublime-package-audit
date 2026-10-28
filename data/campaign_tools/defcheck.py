import glob, os, re, sys

REPOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'repos')
# usage: defcheck.py 0959:true,false 1012:groups ...
for arg in sys.argv[1:]:
    idx, names = arg.split(':')
    p = glob.glob(os.path.join(REPOS, idx + '_*'))[0]
    files = []
    for root, _, fs in os.walk(p):
        if os.sep + '.git' in root:
            continue
        for f in fs:
            if f.endswith('.py'):
                files.append(os.path.join(root, f))
    for n in names.split(','):
        defs = []
        pat = re.compile(r'(^\s*(def|class)\s+%s\b)|(^\s*%s\s*[,=:]|\b(import|as)\s+%s\b|\bfrom\s+\S+\s+import\s+.*\b%s\b|^\s*%s\s*=)' % ((re.escape(n),) * 5), re.M)
        for f in files:
            try:
                t = open(f, encoding='utf8', errors='replace').read()
            except Exception:
                continue
            for m in pat.finditer(t):
                line = t[:m.start()].count('\n') + 1
                defs.append('%s:%d' % (os.path.relpath(f, p).replace(chr(92), '/'), line))
        print('%s %-18s definitions/imports: %s' % (os.path.basename(p)[:24], n, defs[:6] if defs else 'NONE'))
