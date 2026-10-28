import json, os, re, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
SP = r'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp'
Q = json.load(open(SP + r'\165e315a-efcb-49b3-8b31-7320fbdb0c43\scratchpad\campaign\queue.json'))
OUT = SP + r'\1e07794b-efe6-4e5f-bbc3-7d3161a16a46\scratchpad\triage\repos'
os.makedirs(OUT, exist_ok=True)
start = int(sys.argv[1]); end = int(sys.argv[2]); workers = int(sys.argv[3]) if len(sys.argv) > 3 else 8
jobs = []
for i in range(start, min(end, len(Q))):
    hp = Q[i].get('homepage') or ''
    m = re.match(r'https?://github\.com/([^/]+)/([^/#?]+)', hp)
    if not m: continue
    owner, repo = m.group(1), m.group(2).removesuffix('.git')
    d = os.path.join(OUT, '%04d_%s' % (i, re.sub(r'[^A-Za-z0-9._-]', '_', Q[i]['name'])[:60]))
    jobs.append((i, Q[i]['name'], owner, repo, d))
def run(j):
    i, name, owner, repo, d = j
    if os.path.isdir(os.path.join(d, '.git')): return (i, 'have')
    try:
        r = subprocess.run(['git', 'clone', '--depth', '1', '--quiet', '--filter=blob:limit=1m', 'https://github.com/%s/%s' % (owner, repo), d],
                           capture_output=True, text=True, timeout=180, env={**os.environ, 'GIT_TERMINAL_PROMPT': '0'})
        return (i, 'ok' if r.returncode == 0 else 'fail:' + r.stderr.strip().splitlines()[-1][:100] if r.stderr.strip() else 'fail')
    except Exception as e:
        return (i, 'exc:' + type(e).__name__)
t0 = time.time(); stats = {}
with ThreadPoolExecutor(workers) as ex:
    for i, st in ex.map(run, jobs):
        k = st.split(':')[0]; stats[k] = stats.get(k, 0) + 1
        if st.startswith(('fail', 'exc')): print(i, st, flush=True)
print('done', len(jobs), 'jobs', stats, 'in %.0fs' % (time.time() - t0), flush=True)
