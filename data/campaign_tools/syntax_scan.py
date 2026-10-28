"""Scan .sublime-syntax files of served packages: YAML validity and unresolved `extends:` targets."""
import json
import os
import re
import sys

import yaml

BASE = os.path.dirname(os.path.abspath(__file__))
REPOS = os.path.join(BASE, 'repos')
served = set(json.load(open(os.path.join(BASE, 'served_idx.json'))))
Q = json.load(open(r'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\165e315a-efcb-49b3-8b31-7320fbdb0c43\scratchpad\campaign\queue.json'))
known = set(json.load(open(os.path.join(BASE, 'st_resources.json'))))  # resource paths ST knows (default + installed)
SKIP = ('/tests/', '/test/', '/node_modules/', '/docs/', '/examples/', '/example/', '/demo/', '/.github/')


class L(yaml.SafeLoader):
    pass


# collect all syntax paths provided by served packages, as Packages/<Name>/<relpath>
provided = set()
entries = []
for d in sorted(os.listdir(REPOS)):
    idx = int(d[:4])
    if idx not in served:
        continue
    name = Q[idx]['name']
    root = os.path.join(REPOS, d)
    for dp, dn, fn in os.walk(root):
        if os.sep + '.git' in dp:
            continue
        rel = dp[len(root):].replace(os.sep, '/') + '/'
        if any(s in rel.lower() for s in SKIP):
            continue
        for f in fn:
            if f.endswith(('.sublime-syntax', '.tmLanguage', '.sublime-color-scheme', '.tmTheme')):
                r = (rel + f).lstrip('/')
                provided.add('Packages/%s/%s' % (name, r))
                if f.endswith('.sublime-syntax'):
                    entries.append((d, idx, name, r, os.path.join(dp, f)))

bad_yaml = []
bad_extends = []
for d, idx, name, r, path in entries:
    try:
        text = open(path, encoding='utf-8-sig', errors='replace').read()
    except Exception:
        continue
    try:
        docs = list(yaml.load_all(text.replace('\t', '    ') if False else text, Loader=L))
    except yaml.YAMLError as e:
        bad_yaml.append((d, r, str(e).splitlines()[0][:100] + ' | ' + (str(getattr(e, 'problem_mark', ''))[:60])))
        continue
    if not docs or not isinstance(docs[0], dict):
        continue
    top = docs[0]
    ext = top.get('extends')
    exts = ext if isinstance(ext, list) else ([ext] if ext else [])
    for e in exts:
        if not isinstance(e, str) or not e.startswith('Packages/'):
            continue
        if e in known or e in provided:
            continue
        bad_extends.append((d, r, e))

print('syntax files', len(entries), 'bad yaml', len(bad_yaml), 'unresolved extends', len(bad_extends))
json.dump({'yaml': bad_yaml, 'extends': bad_extends}, open(os.path.join(BASE, 'syntax_bad.json'), 'w'))
for x in bad_yaml[:60]:
    print('YAML', *x)
for x in bad_extends[:80]:
    print('EXTENDS', *x)
