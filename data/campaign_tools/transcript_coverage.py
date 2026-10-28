"""Search retained Claude Code transcripts for THIS project for mentions of queue packages.

Source: ~/.claude/projects/C--Users-donal-projects-sublime-mcp/*.jsonl  (assistant text + user prompts only; tool output ignored)
A mention counts when an audit word is in the same message text.
Usage: python transcript_coverage.py [N]   -> checks the first N queue entries (default 150)
Output: covered_by_transcripts.json {name: {hits, sessions, example, first_date}}
"""
import os, re, json, glob, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.expanduser('~/.claude/projects/C--Users-donal-projects-sublime-mcp')
VOCAB = re.compile(r'\b(installed live|installed|audit(ed|ing)?|tested|no defect|filed|traceback|live test|bug hunt|verdict|dropped|retract\w*|not filed|queue \d+|issue #\d+)\b', re.I)

def texts():
    for f in sorted(glob.glob(os.path.join(PROJ, '*.jsonl'))):
        sess = os.path.basename(f)[:8]
        try:
            fh = open(f, encoding='utf-8', errors='replace')
        except OSError:
            continue
        with fh:
            for line in fh:
                try:
                    o = json.loads(line)
                except Exception:
                    continue
                t = o.get('type')
                if t not in ('assistant', 'user'):
                    continue
                msg = o.get('message') or {}
                c = msg.get('content')
                parts = []
                if isinstance(c, str):
                    parts.append(c)
                elif isinstance(c, list):
                    for b in c:
                        if isinstance(b, dict) and b.get('type') == 'text':
                            parts.append(b.get('text', ''))
                if not parts:
                    continue
                yield sess, (o.get('timestamp') or '')[:10], '\n'.join(parts)

def main(n=150):
    q = json.load(open(os.path.join(HERE, 'queue_v2_by_installs.json'), encoding='utf-8'))
    names = [e['name'] for e in q[:n]]
    pats = {nm: re.compile(r'(?<![A-Za-z0-9])' + re.escape(nm) + r'(?![A-Za-z0-9])', re.I) for nm in names if len(nm) >= 4}
    res = {}
    total = 0
    for sess, date, text in texts():
        total += 1
        low = text.lower()
        for nm, pat in pats.items():
            if nm.lower() not in low:
                continue
            m = pat.search(text)
            if not m:
                continue
            lo = max(0, m.start() - 300); hi = min(len(text), m.end() + 300)
            if VOCAB.search(text[lo:hi]):
                r = res.setdefault(nm, {'hits': 0, 'sessions': set(), 'example': None, 'first_date': date})
                r['hits'] += 1; r['sessions'].add(sess)
                if r['example'] is None:
                    r['example'] = '%s %s: %s' % (date, sess, text[lo:hi].replace('\n', ' ')[:240])
    for r in res.values():
        r['sessions'] = len(r['sessions'])
    json.dump(res, open(os.path.join(HERE, 'covered_by_transcripts.json'), 'w', encoding='utf-8'), indent=1)
    print("messages scanned:", total, "| queue names checked:", len(pats), "| with audit-vocabulary mentions:", len(res))
    return res

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 150)
