import importlib.util
import subprocess
import sys

FOOT = ("Found while testing packages from the Package Control catalog "
        "(static analysis with ruff plus source review).")

spec = importlib.util.spec_from_file_location('batch', sys.argv[1])
batch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(batch)

for repo, title, body in batch.ISSUES:
    body = body.strip() + "\n\n" + getattr(batch, 'FOOT', FOOT) + "\n"
    r = subprocess.run(['gh', 'issue', 'create', '-R', repo, '-t', title, '-F', '-'],
                       input=body, capture_output=True, text=True, encoding='utf-8')
    out = (r.stdout.strip() or r.stderr.strip()).splitlines()
    print(repo, '->', out[-1] if out else '?')
