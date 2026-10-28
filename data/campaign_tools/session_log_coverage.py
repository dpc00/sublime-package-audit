"""Which queue packages are mentioned in past agent session transcripts (~/data/logs/ghostshell/session_text_logs)?

A mention only counts when an 'audit word' (install, test, bug, issue, filed, traceback, ...) is on the same line
or within two lines, so bare package listings do not count.
Output: campaign_tools/covered_by_session_logs.json  {name: {hits, files, example}}
"""
import os, re, json, glob, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOGDIR = os.path.expanduser('~/data/logs/ghostshell/session_text_logs')
VOCAB = re.compile(r'\b(install(ed|ing|s)?|audit(ed|ing)?|tested|testing|bug|bugs|issue|issues|filed|traceback|no defect|defect|retract\w*|live test|hunt|repro\w*|console|verdict|dropped|skipped|queue)\b', re.I)

def load_lines():
    out = []
    for f in sorted(glob.glob(os.path.join(LOGDIR, '*.log'))):
        try:
            txt = open(f, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        out.append((os.path.basename(f), txt.split('\n')))
    return out

def main(names=None):
    files = load_lines()
    corpus = '\n'.join('\n'.join(ls) for _, ls in files).lower()
    print("session log files:", len(files), "| corpus MB: %.1f" % (len(corpus) / 1e6))
    if names is None:
        q = json.load(open(os.path.join(HERE, 'queue_v2_by_installs.json'), encoding='utf-8'))
        names = [e['name'] for e in q]
    result = {}
    for name in names:
        nl = name.lower()
        if len(nl) < 4 or nl not in corpus:
            continue
        pat = re.compile(r'(?<![a-z0-9])' + re.escape(nl) + r'(?![a-z0-9])')
        hits, fileset, example = 0, set(), None
        for fname, lines in files:
            for i, line in enumerate(lines):
                if pat.search(line.lower()):
                    window = ' '.join(lines[max(0, i - 2): i + 3])
                    if VOCAB.search(window):
                        hits += 1; fileset.add(fname)
                        if example is None:
                            example = "%s:%d: %s" % (fname, i + 1, line.strip()[:180])
        if hits:
            result[name] = {'hits': hits, 'files': len(fileset), 'example': example}
    path = os.path.join(HERE, 'covered_by_session_logs.json')
    json.dump(result, open(path, 'w', encoding='utf-8'), indent=1)
    print("queue names with audit-vocabulary mentions in session logs:", len(result), "of", len(names))
    return result

if __name__ == '__main__':
    main()
