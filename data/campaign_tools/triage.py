import ast, json, os, re, subprocess, sys
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
REPOS = os.path.join(BASE, 'repos')
lo = int(sys.argv[1]) if len(sys.argv) > 1 else 0
hi = int(sys.argv[2]) if len(sys.argv) > 2 else 99999
dirs = sorted(d for d in os.listdir(REPOS)
              if lo <= int(d[:4]) < hi and os.path.isdir(os.path.join(REPOS, d, '.git')))

SKIP = ('/tests/', '/test/', '/node_modules/', '/vendor/', '/vendored/', '/libs/', '/lib/', '/site-packages/',
        '/docs/', '/examples/', '/example/', '/third_party/', '/external/', '/deps/', '/dist/', '/build/',
        '/script/', '/scripts/', '/tools/', '/dev/', '/bin/')
RULES = 'F5,F63,F7,F82,F402,B005,B015,B018,B020,B033,PLE,PLW0120,PLW0127,PLW0129,S307,S602,S605,S323,S501,S506,E9'

rep = defaultdict(list)
targets = [os.path.join(REPOS, d) for d in dirs]
all_items = []
for k in range(0, len(targets), 40):
    r = subprocess.run(['ruff', 'check', '--isolated', '--no-cache', '--select', RULES, '--output-format', 'json',
                        '--exclude', '.git', '--target-version', 'py38'] + targets[k:k + 40],
                       capture_output=True, text=True)
    try:
        all_items.extend(json.loads(r.stdout))
    except Exception:
        pass
if True:
    items = all_items
    for it in items:
        fn = it['filename'].replace('\\', '/')
        tail = fn.split('/repos/', 1)[1]
        d, rel = tail.split('/', 1) if '/' in tail else (tail, '')
        if any(s in '/' + rel.lower() for s in SKIP):
            continue
        code = it['code'] or 'SYNTAX'
        rep[d].append((code, rel, it['location']['row'], it['message'][:110]))

# py3.3-host detection: no .python-version at repo root and a root-level .py that needs newer grammar
dead = {}
for d in dirs:
    root = os.path.join(REPOS, d)
    if os.path.exists(os.path.join(root, '.python-version')):
        continue
    for f in os.listdir(root):
        if f.endswith('.py'):
            try:
                src = open(os.path.join(root, f), encoding='utf8', errors='replace').read()
            except Exception:
                continue
            try:
                ast.parse(src, feature_version=(3, 4))
            except SyntaxError as e:
                dead[d] = (f, e.lineno, (e.msg or '')[:70])
                break
            except Exception:
                pass

json.dump({'ruff': rep, 'dead33': dead}, open(os.path.join(BASE, 'report_%d_%d.json' % (lo, hi)), 'w'))
print('repos', len(dirs), 'with ruff hits', len(rep), 'py3.3-dead candidates', len(dead))
for d, v in sorted(dead.items()):
    print('DEAD33', d, v)
strong = ('F821', 'F823', 'B018', 'B015', 'F632', 'F50', 'F52', 'F63', 'PLE', 'F82', 'S307',
          'S323', 'S501', 'S506', 'SYNTAX', 'F7')
PY2 = ('unicode', 'basestring', 'xrange', 'long', 'unichr', 'cmp', 'raw_input', 'reload', 'execfile', 'file',
       'buffer', 'reduce', 'WindowsError', 'apply', 'intern', 'coerce', 'reprlib')
VENDOR = ('bs4/', 'requests/', 'yaml/', 'chardet/', 'jedi/', 'certifi/', 'idna/', 'urllib3/', 'six', 'docutils/',
          'markdown/', 'pygments/', 'jinja2/', 'mako/', 'ply/', 'antlr4/', 'esprima/', 'watchdog/', 'pyfiglet/',
          'glob2/', 'bibtexparser/', 'rbql', 'pydevd', 'debugpy', 'include/', 'dependencies/', 'lib/', 'libs/',
          'vendor', 'external', 'third', 'site-packages', 'plugin/glob2', 'colorama/', 'termcolor', 'xmltodict',
          'simplejson/', 'httplib2/', 'oauth2client', 'google/', 'pkg_resources', 'setuptools', 'pip/', 'toml/',
          'jsonschema/', 'attr/', 'packaging/', 'dateutil/', 'pytz/', 'lxml/', 'html5lib/', 'sqlparse/', 'paramiko/')
def noisy(h):
    code, rel, row, msg = h
    r = rel.replace(chr(92), '/')
    if r.startswith(VENDOR) or any(('/' + v) in ('/' + r) for v in VENDOR if v.endswith('/')):
        return True
    if code == 'F821' and any(("`%s`" % n) in msg for n in PY2):
        return True
    return False
for d in sorted(rep):
    hits = [h for h in rep[d] if h[0].startswith(strong) and not noisy(h)]
    if hits:
        print('==', d)
        for h in hits[:6]:
            print('   %-7s %s:%s %s' % h)
