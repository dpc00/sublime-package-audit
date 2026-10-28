"""Rebuild the package-audit queue ranked by unique installs (replaces the newest-first queue).

Sources
  * packagecontrol.io/browse/popular.json?page=N   (25 packages per page: installs_rank, unique_installs, ...)
  * campaign scratchpad packages_all.json           (homepage per package name)
  * .package_skill_test_log.md                      (what has already been audited: entry headings)
  * the old queue.json                              (positions <= 707 were done this session)

Rules
  * only packages that list ST4 and Windows
  * skip: already audited, is_missing, Package Control itself (dispute), Donald's own packages
  * tier A = functional plugin, updated within ~4 years, by installs
    tier B = functional plugin, older, by installs
    tier C = themes / colour schemes / snippet packs / pure syntax, by installs
Output: campaign_tools/queue_v2_by_installs.json (+ popular_all.json cache)
"""
import json, os, re, sys, time, urllib.request, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SCRATCH = r'C:/Users/donal/AppData/Local/Temp/claude/C--Users-donal-projects-sublime-mcp/165e315a-efcb-49b3-8b31-7320fbdb0c43/scratchpad/campaign/'
CACHE = os.path.join(HERE, 'popular_all.json')

def fetch_all():
    if os.path.exists(CACHE):
        return json.load(open(CACHE, encoding='utf-8'))
    rows, page = [], 1
    while True:
        url = "https://packagecontrol.io/browse/popular.json?page=%d" % page
        for attempt in range(4):
            try:
                with urllib.request.urlopen(url, timeout=40) as r:
                    d = json.load(r)
                break
            except Exception as e:
                time.sleep(2 * (attempt + 1))
        else:
            raise SystemExit("failed page %d" % page)
        pk = d.get('packages', [])
        if not pk:
            break
        rows.extend(pk)
        if len(rows) >= d.get('total', 10**9):
            break
        page += 1
        time.sleep(0.25)
    json.dump(rows, open(CACHE, 'w', encoding='utf-8'))
    return rows

def norm(s):
    return re.sub(r'[^a-z0-9]+', '', s.lower())

def audited_names():
    log = open(os.path.join(REPO, '.package_skill_test_log.md'), encoding='utf-8').read()
    names = set()
    for h in re.findall(r'^#{2,3} (.+)$', log, re.M):
        h = re.sub(r'^(#\d+|Package \d+:|Day \d+)\s*', '', h).strip()
        base = re.split(r'\s+\(', h)[0]           # "Name (owner/repo)" -> "Name"
        if base:
            names.add(norm(base))
    return names

THEME = re.compile(r'\btheme\b|color ?scheme|colou?r scheme|colorscheme|\bicons?\b|\bui\b.*theme', re.I)
SNIP = re.compile(r'snippets?\b', re.I)
SYN = re.compile(r'syntax|language (definition|support)|highlighting for|grammar', re.I)

def kind(p):
    n = p['name']; d = p.get('description', '') or ''
    if THEME.search(n) or re.search(r'color scheme|colour scheme|\btheme\b', d, re.I) and not re.search(r'plugin|command|package manager', d, re.I):
        return 'theme'
    if SNIP.search(n):
        return 'snippets'
    if SYN.search(n) or re.match(r'\s*(syntax|language)', d, re.I):
        return 'syntax'
    return 'plugin'


def touched_repos():
    """owner/repo (lowercase) for every repository where dpc00 has already filed an issue or PR (from GitHub itself)."""
    import subprocess
    cache = os.path.join(HERE, 'touched_repos.json')
    if os.path.exists(cache):
        return set(json.load(open(cache, encoding='utf-8')))
    repos = set()
    for kind in ('issue', 'pr'):
        for page in range(1, 11):
            r = subprocess.run(['gh', 'api', 'search/issues?q=author:dpc00+is:%s&per_page=100&page=%d' % (kind, page)],
                               capture_output=True, text=True, encoding='utf-8')
            if r.returncode != 0:
                break
            items = json.loads(r.stdout).get('items', [])
            for it in items:
                repos.add(it['repository_url'].split('/repos/')[1].lower())
            if len(items) < 100:
                break
    json.dump(sorted(repos), open(cache, 'w', encoding='utf-8'))
    return repos

def gh_path(url):
    m = re.search(r'github\.com/([^/]+/[^/#?]+)', url or '', re.I)
    return m.group(1).lower().removesuffix('.git') if m else None

_LOG_LINES = None
def log_lines():
    global _LOG_LINES
    if _LOG_LINES is None:
        _LOG_LINES = open(os.path.join(REPO, '.package_skill_test_log.md'), encoding='utf-8').read().splitlines()
    return _LOG_LINES

def coverage(name, homepage):
    """Return (level, evidence) where level is 'strong', 'weak' or None, searching the WHOLE log.
    strong: the name is in a heading or an early-phase bullet '- Name (#', or the GitHub owner/repo appears in the log.
    weak:   the name appears as a whole word somewhere (only counted for distinctive names)."""
    lines = log_lines()
    pat = re.compile(r'(?<![A-Za-z0-9])' + re.escape(name) + r'(?![A-Za-z0-9])', re.I)
    repo = gh_path(homepage)
    weak = None
    for i, line in enumerate(lines, 1):
        if repo and repo in line.lower():
            return 'repo', "line %d (repo path): %s" % (i, line.strip()[:160])
        if pat.search(line):
            if re.match(r'#{2,4} ', line):
                return 'heading', "line %d: %s" % (i, line.strip()[:160])
            if re.match(r'\s*[-*] +' + re.escape(name) + r' \(#', line, re.I):
                return 'bullet', "line %d: %s" % (i, line.strip()[:220])
            if weak is None:
                weak = "line %d: %s" % (i, line.strip()[:110])
    if weak:
        distinctive = len(name) >= 9 or bool(re.search(r'[a-z][A-Z]|[ _.-]', name))
        if distinctive:
            return 'weak', weak
    return None, None

MINE = {norm(x) for x in ['MCP Commander', 'AgentIDE', 'sublime-mcp', 'GhostShell', 'AiSDK', 'AiSearch', 'PyBackupPanel', 'STConfig']}
DISPUTE = {norm('Package Control')}
# audited earlier in ways GitHub search cannot see (work with the maintainer, issues filed under another account / by the maintainer)
MANUAL_DONE = {norm(x) for x in ['SublimeLinter', 'SublimeFileBrowser', 'FindInFiles-addon', 'Debugger', 'Verilog']}  # Debugger ~40% documented, Verilog tested (verible) per repo log / session transcripts

def main():
    rows = fetch_all()
    print("packages ranked by installs:", len(rows))
    allp = {e['name']: e for e in json.load(open(SCRATCH + 'packages_all.json', encoding='utf-8'))}
    old = json.load(open(SCRATCH + 'queue.json', encoding='utf-8'))
    done_old = {norm(e['name']) for e in old[:707]}
    touched = touched_repos()
    print('repositories already touched on GitHub:', len(touched))
    done_log = audited_names()
    cutoff = (datetime.date.today() - datetime.timedelta(days=4 * 365)).isoformat()
    out, skipped, covered_ev = [], {}, []
    def skip(why):
        skipped[why] = skipped.get(why, 0) + 1
    for p in rows:
        n = norm(p['name'])
        if 4 not in (p.get('st_versions') or []): skip('no ST4'); continue
        if 'windows' not in (p.get('platforms') or []): skip('no windows'); continue
        if p.get('is_missing'): skip('missing repo'); continue
        if n in DISPUTE: skip('Package Control (dispute)'); continue
        if n in MANUAL_DONE: skip('audited earlier (manual list)'); continue
        if n in MINE: skip('own package'); continue
        if n in done_old: skip('already audited (old queue <= 707)'); continue
        hp = (allp.get(p['name']) or {}).get('homepage', '')
        lvl, ev = coverage(p['name'], hp)
        hint = None
        if lvl:
            # any record in the log counts as done (early phase covered installs ranks ~15-304; heading/repo/bullet/passing mention)
            skip('already in the log (%s)' % lvl); covered_ev.append((p['name'], p['unique_installs'], lvl, ev)); continue
        if gh_path((allp.get(p['name']) or {}).get('homepage')) in touched: skip('repo already touched on GitHub (issue/PR filed)'); continue
        k = kind(p)
        lm = (p.get('last_modified') or '')[:10]
        tier = 'C' if k != 'plugin' else ('A' if lm >= cutoff else 'B')
        out.append({'name': p['name'], 'tier': tier, 'kind': k, 'unique_installs': p['unique_installs'],
                    'installs_rank': p['installs_rank'], 'last_modified': lm,
                    'homepage': (allp.get(p['name']) or {}).get('homepage', ''),
                    'authors': p.get('authors', []), 'log_hint': hint})
    order = {'A': 0, 'B': 1, 'C': 2}
    out.sort(key=lambda e: (order[e['tier']], -e['unique_installs']))
    for i, e in enumerate(out, 1):
        e['queue_position'] = i
    path = os.path.join(HERE, 'queue_v2_by_installs.json')
    json.dump(out, open(path, 'w', encoding='utf-8'), indent=1)
    json.dump(covered_ev, open(os.path.join(HERE, 'covered_by_log.json'), 'w', encoding='utf-8'), indent=1)
    print("queue v2:", len(out), "| skipped:", skipped)
    for t in 'ABC':
        sub = [e for e in out if e['tier'] == t]
        print("tier %s: %d packages, installs range %s .. %s" % (t, len(sub), sub[0]['unique_installs'] if sub else '-', sub[-1]['unique_installs'] if sub else '-'))
    print("saved", path)

if __name__ == '__main__':
    main()
