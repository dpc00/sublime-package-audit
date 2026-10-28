import glob, json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
REPOS = os.path.join(BASE, 'repos')
report = sys.argv[1]
codes = tuple(sys.argv[2].split(','))
ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 2
cap = int(sys.argv[4]) if len(sys.argv) > 4 else 3
only = set(sys.argv[5].split(',')) if len(sys.argv) > 5 else None

PY2 = ('unicode', 'basestring', 'xrange', 'long', 'unichr', 'cmp', 'raw_input', 'reload', 'execfile', 'file',
       'buffer', 'reduce', 'WindowsError', 'apply', 'intern', 'coerce', 'reprlib')
VENDOR = ('bs4/', 'requests/', 'yaml/', 'chardet/', 'jedi/', 'certifi/', 'idna/', 'urllib3/', 'docutils/', 'markdown/',
          'pygments/', 'jinja2/', 'mako/', 'ply/', 'antlr4/', 'esprima/', 'watchdog/', 'pyfiglet/', 'glob2/',
          'bibtexparser/', 'rbql', 'pydevd', 'debugpy', 'include/', 'dependencies/', 'lib/', 'libs/', 'vendor',
          'external', 'third', 'site-packages', 'colorama/', 'xmltodict', 'simplejson/', 'httplib2/', 'oauth2client',
          'google/', 'pkg_resources', 'setuptools', 'pip/', 'toml/', 'jsonschema/', 'attr/', 'packaging/',
          'dateutil/', 'pytz/', 'lxml/', 'html5lib/', 'sqlparse/', 'paramiko/', 'whoosh/', 'Bio/', 'enum/', 'cffi/',
          'asn1crypto/', 'intervaltree/', 'lark/', 'grammalecte/', 'layers/', 'ordereddict/', 'argparse')

data = json.load(open(os.path.join(BASE, report)))['ruff']
SERVED = set(json.load(open(os.path.join(BASE, 'served_idx.json')))) if os.environ.get('SERVED') else None
for d in sorted(data):
    if only and d[:4] not in only:
        continue
    if SERVED is not None and int(d[:4]) not in SERVED:
        continue
    hits = []
    for code, rel, row, msg in data[d]:
        if not code.startswith(codes):
            continue
        r = rel.replace(chr(92), '/')
        if r.startswith(VENDOR) or any(('/' + v) in ('/' + r) for v in VENDOR if v.endswith('/')):
            continue
        if code == 'F821' and any(('`%s`' % n) in msg for n in PY2):
            continue
        hits.append((code, r, row, msg))
    if not hits:
        continue
    p = glob.glob(os.path.join(REPOS, d))[0]
    print('=== ' + d)
    for code, r, row, msg in hits[:cap]:
        try:
            lines = open(os.path.join(p, r), encoding='utf8', errors='replace').read().splitlines()
        except Exception:
            continue
        print('  [%s] %s:%d  %s' % (code, r, row, msg[:60]))
        for i in range(max(0, row - 1 - ctx), min(len(lines), row + ctx)):
            print('   %5d%s %s' % (i + 1, '>' if i + 1 == row else ' ', lines[i][:130]))
