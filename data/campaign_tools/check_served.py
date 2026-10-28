import ast, io, json, os, sys, urllib.request, zipfile

BASE = os.path.dirname(os.path.abspath(__file__))
info = json.load(open(os.path.join(BASE, 'served_info.json')))
rows = []
for name, i in info.items():
    rels = i['releases']
    if isinstance(rels, str):
        import ast as _a
        rels = _a.literal_eval(rels)
    rel = rels[0]
    url = rel['url']
    try:
        data = urllib.request.urlopen(url, timeout=60).read()
        z = zipfile.ZipFile(io.BytesIO(data))
    except Exception as e:
        rows.append((name, 'DOWNLOAD FAIL %r' % e))
        continue
    names = z.namelist()
    prefix = names[0].split('/')[0] + '/'
    files = [n[len(prefix):] for n in names if n.startswith(prefix)]
    has_pv = '.python-version' in files
    root_py = [f for f in files if f.endswith('.py') and '/' not in f]
    bad = []
    for f in root_py:
        src = z.read(prefix + f).decode('utf8', 'replace')
        try:
            ast.parse(src, feature_version=(3, 4))
        except SyntaxError as e:
            bad.append('%s:%s %s' % (f, e.lineno, (e.msg or '')[:40]))
        except Exception:
            pass
    rows.append((name, 'ver=%s st=%s python-version=%s root_py=%d bad=%s' % (rel.get('version'), rel.get('sublime_text'), has_pv, len(root_py), bad[:3])))
for n, r in rows:
    print('%-24s %s' % (n, r))
