import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
REPOS = os.path.join(BASE, 'repos')
served = set(json.load(open(os.path.join(BASE, 'served_idx.json'))))
SKIP = ('/tests/', '/test/', '/node_modules/', '/vendor/', '/lib/', '/libs/', '/site-packages/', '/third_party/',
        '/external/', '/deps/', '/dependencies/', '/include/', '/requests/', '/urllib3/', '/pymysql/', '/certifi/',
        '/chardet/', '/idna/', '/six/', '/yaml/', '/jedi/', '/bs4/', '/pygments/', '/markdown/', '/jinja2/',
        '/paramiko/', '/websocket/', '/tornado/', '/sqlparse/', '/simplejson/', '/httplib2/', '/oauth2client/',
        '/google/', '/boto/', '/boto3/', '/botocore/', '/docutils/', '/pip/', '/setuptools/', '/pkg_resources/',
        '/lxml/', '/dateutil/', '/pytz/', '/bin/', '/dist/', '/build/', '/docs/', '/examples/', '/demo/')

pats = {
    'unverified_tls': re.compile(r'verify\s*=\s*False|_create_unverified_context|CERT_NONE|check_hostname\s*=\s*False'),
    'tar_extractall': re.compile(r'\.extractall\('),
    'http_download_exec': re.compile(r'urlopen\(\s*[\'"]http://|urlretrieve\(\s*[\'"]http://|requests\.(get|post)\(\s*[\'"]http://'),
    'yaml_load_unsafe': re.compile(r'yaml\.load\((?![^)]*(Safe|safe))'),
    'pickle_load': re.compile(r'pickle\.loads?\('),
    'os_system_concat': re.compile(r'os\.system\([^)]*(\+|%|\.format|f[\'"])'),
    'shell_true_fmt': re.compile(r'shell\s*=\s*True'),
    # non-raw string literal handed to re.* that contains a backslash-b (a backspace character, not a word boundary)
    'nonraw_b': re.compile(r'''re\.(?:compile|search|match|sub|findall|split|finditer|fullmatch)\(\s*(?<![rRbB])(?:"[^"\n]*?(?<!\\)\\b|'[^'\n]*?(?<!\\)\\b)'''),
    # callbacks that are called instead of passed
    'callback_called': re.compile(r'''(?:set_timeout(?:_async)?|add_on_change)\(\s*(?:'[^']*'\s*,\s*)?[A-Za-z_][\w.]*\([^()]*\)\s*[,)]'''),
    'open_noenc': re.compile(r'''[^\w.]open\((?:[^,()]|\([^()]*\))*\)\.read\(\)'''),
}
which = sys.argv[1]
pat = pats[which]
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 0
hi = int(sys.argv[3]) if len(sys.argv) > 3 else 99999
for d in sorted(os.listdir(REPOS)):
    idx = int(d[:4])
    if idx not in served or not (lo <= idx < hi):
        continue
    root = os.path.join(REPOS, d)
    for dp, dn, fn in os.walk(root):
        if os.sep + '.git' in dp:
            continue
        low = dp.replace(os.sep, '/').lower() + '/'
        rel = low.split('/repos/', 1)[1].split('/', 1)[1] if '/repos/' in low else ''
        if any(s in '/' + rel for s in SKIP):
            continue
        for f in fn:
            if not f.endswith('.py'):
                continue
            p = os.path.join(dp, f)
            try:
                t = open(p, encoding='utf8', errors='replace').read()
            except Exception:
                continue
            for m in pat.finditer(t):
                line = t[:m.start()].count('\n') + 1
                src = t.splitlines()[line - 1].strip()
                print(('%s %s:%d %s' % (d[:26], os.path.relpath(p, root).replace(os.sep, '/'), line, src[:110])).encode('ascii', 'replace').decode())
