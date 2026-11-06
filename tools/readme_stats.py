#!/usr/bin/env python3
"""Recompute the README audit figures from RESULTS.tsv and ISSUES.tsv.

Run after every test. `--dry-run` prints the counts and the README lines it
would write, without touching the file.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "RESULTS.tsv"
ISSUES = ROOT / "ISSUES.tsv"
README = ROOT / "README.md"
QUEUE = ROOT / "data" / "untested_installable_2026_11_03.tsv"


def norm(name: str) -> str:
    name = re.sub(r"^#\d+\s+", "", name)
    name = re.sub(r"\s+\d{3,4}$", "", name)
    return name.strip().lower()


def read_results() -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    for line in RESULTS.read_text(encoding="utf-8").splitlines()[1:]:
        if not line.strip():
            continue
        parts = line.split("\t", 3)
        if len(parts) < 3:
            continue
        rows.append((norm(parts[0]), parts[1], parts[2]))
    return rows


def classify(note: str) -> str:
    n = note.lower()
    if "static check only" in n:
        return "static"
    if "not installable" in n:
        return "not_installable"
    if re.search(r"repository gone|repo gone|no longer resolves|download 404|returns? 404|404 on", n):
        return "repo_gone"
    if re.search(r"not offered|not in the .{0,25}picker|hidden from|^skipped\b", n):
        return "not_offered"
    # A record that opens by saying it was not tested is a skip, whatever the reason:
    # before this rule, notes like "not tested: needs m4 on PATH" fell through to the
    # default and were counted as tested (2026-11-05).
    if re.match(r"^not[\s-]?tested\b", n):
        return "not_offered"
    if re.search(r"\b(tested|retested|installed|live test)\b", n) and not re.search(r"\bnot tested\b", n):
        return "tested"
    if re.search(r"no github repository link|no github repository|no repository link|no github repo\b", n):
        return "no_link"
    if re.search(r"by reading|read-only|read only", n) and not re.search(r"install|load|run|test|work|remov|picker", n):
        return "read_only"
    return "tested"


def latest_by_package(rows: list[tuple[str, str, str]]) -> dict[str, str]:
    latest: dict[str, str] = {}
    for name, _date, note in rows:
        latest[name] = note
    return latest


def issue_rows() -> list[dict[str, str]]:
    header = None
    out: list[dict[str, str]] = []
    for line in ISSUES.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if header is None:
            header = parts
            continue
        if len(parts) < len(header):
            parts += [""] * (len(header) - len(parts))
        out.append(dict(zip(header, parts)))
    return out


def issue_counts() -> dict[str, float]:
    rows = issue_rows()
    # Collapse exact duplicate log rows for the same issue.
    seen: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows:
        seen[(row.get("repository", ""), row.get("number", ""))] = row
    distinct = list(seen.values())
    repos = {r.get("repository", "") for r in distinct if r.get("repository")}
    open_n = sum(1 for r in distinct if r.get("state") == "open")
    closed_n = sum(1 for r in distinct if r.get("state") == "closed")
    unreadable = sum(1 for r in distinct if not r.get("state"))
    days: list[int] = []
    for r in distinct:
        c, x = r.get("created", ""), r.get("closed", "")
        if r.get("state") == "closed" and re.fullmatch(r"\d{4}-\d\d-\d\d", c or "") and re.fullmatch(r"\d{4}-\d\d-\d\d", x or ""):
            days.append((dt.date.fromisoformat(x) - dt.date.fromisoformat(c)).days)
    days.sort()
    median = days[len(days) // 2] if days else 0
    mean = round(sum(days) / len(days), 1) if days else 0
    week = sum(1 for d in days if d <= 7)
    pc = sum(1 for r in distinct if r.get("repository") == "sublimehq/package_control")
    return {
        "rows": len(rows),
        "issues": len(distinct),
        "repositories": len(repos),
        "open": open_n,
        "closed": closed_n,
        "unreadable": unreadable,
        "week": week,
        "days": len(days),
        "median": median,
        "mean": mean,
        "pc": pc,
    }


def gh_prs() -> dict[str, int] | None:
    def count(args: list[str]) -> int:
        p = subprocess.run(["gh", "search", "prs", "--author", "dpc00", "--limit", "500", *args, "--json", "number"], capture_output=True, text=True)
        if p.returncode != 0:
            raise RuntimeError(p.stderr.strip() or p.stdout.strip())
        return len(json.loads(p.stdout or "[]"))

    try:
        merged = count(["--merged"])
        open_n = count(["--state", "open"])
        closed = count(["--state", "closed"])
        # `closed` includes merged; subtract the merged count.
        return {"merged": merged, "open": open_n, "closed": max(0, closed - merged), "total": merged + open_n + max(0, closed - merged)}
    except Exception as exc:
        print(f"gh PR count skipped: {exc}", file=sys.stderr)
        return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    rows = read_results()
    latest = latest_by_package(rows)
    cats = Counter(classify(n) for n in latest.values())
    total = len(latest)
    not_tested = sum(v for k, v in cats.items() if k != "tested")
    counts = {
        "total": total,
        "tested": total - not_tested,
        "not_tested": not_tested,
        "not_installable": cats["not_installable"],
        "repo_gone": cats["repo_gone"],
        "no_link": cats["no_link"],
        "not_offered": cats["not_offered"],
        "static": cats["static"],
        "read_only": cats["read_only"],
    }
    issues = issue_counts()
    prs = gh_prs()
    print("results:", counts)
    print("issues:", issues)
    print("prs:", prs)

    if args.dry_run:
        # Show a few packages per category so the rules can be checked.
        for cat in ("not_installable", "repo_gone", "no_link", "not_offered", "static", "read_only"):
            sample = [n for n in latest.values() if classify(n) == cat][:2]
            print(f"-- {cat} ({cats[cat]})")
            for s in sample:
                print("   ", s[:180].replace("\n", " "))
        return 0

    text = README.read_text(encoding="utf-8")
    today = dt.date.today().isoformat()
    queue_rows = [line.split("\t") for line in QUEUE.read_text(encoding="utf-8").splitlines()[1:] if line.strip()]
    queue_total = len(queue_rows)
    no_link_queue = sum(1 for row in queue_rows if len(row) > 1 and row[1] == "no_repo")
    q_tested = q_norelease = q_pending = 0
    placeholder = re.compile(r"^(Main list row \d+: no GitHub repository link|not tested|Skipped)")
    for row in queue_rows:
        note = latest.get(norm(row[0]), "")
        if note.startswith("Not offered on 4215"):
            q_norelease += 1
        elif note == "" or placeholder.match(note):
            q_pending += 1
        else:
            q_tested += 1

    def sub(pattern: str, repl: str, count: int = 0) -> None:
        nonlocal text
        text, n = re.subn(pattern, repl, text, count=count, flags=re.M)
        if n == 0:
            print(f"warning: no match for {pattern!r}", file=sys.stderr)

    sub(r"Counts to \d{4}-\d\d-\d\d\.", f"Counts to {today}.")
    sub(r"\| packages tested \(latest row shows a run, install or load; retests not counted\) \| \d+ \|", f"| packages tested (latest row shows a run, install or load; retests not counted) | {counts['tested']} |")
    sub(r"\| packages not tested \| \d+ \|", f"| packages not tested | {counts['not_tested']} |")
    sub(r"\| — not installable \| \d+ \|", f"| — not installable | {counts['not_installable']} |")
    sub(r"\| — repository gone \| \d+ \|", f"| — repository gone | {counts['repo_gone']} |")
    sub(r"\| — no GitHub repository link \| \d+ \|", f"| — no GitHub repository link | {counts['no_link']} |")
    sub(r"\| — not offered or skipped \| \d+ \|", f"| — not offered or skipped | {counts['not_offered']} |")
    sub(r"\| — static check only \(NOT live-tested yet\) \| \d+ \|", f"| — static check only (NOT live-tested yet) | {counts['static']} |")
    sub(r"\| — read-only review, nothing run \| \d+ \|", f"| — read-only review, nothing run | {counts['read_only']} |")

    # Prose figures.
    sub(r"`data/untested_installable_2026_11_03\.tsv` lists .*?still untested\.",
        f"`data/untested_installable_2026_11_03.tsv` lists the {queue_total} packages that Package Control offered "
        f"for Windows/ST4 but that the 2026-10-27 bulk pass had not tested. "
        f"{q_tested + q_norelease} of them have since been dealt with — {q_tested} tested live, and {q_norelease} "
        f"shown to have no release for build 4215 in the ST4 channel, so they never appear in the Install Package "
        f"picker — leaving {q_pending} that are still offered and still untested.")
    sub(r"\b\d+ packages still have only a static check", f"{counts['static']} packages still have only a static check")
    sub(r"Package Control alone has \d+ issues", f"Package Control alone has {issues['pc']} issues")

    sub(r"\| issues filed \| \d+ \|", f"| issues filed | {issues['issues']} |")
    sub(r"\| repositories \| \d+ \|", f"| repositories | {issues['repositories']} |")
    sub(r"\| closed \| \d+ \|", f"| closed | {issues['closed']} |")
    sub(r"\| repository no longer readable \| \d+ \|", f"| repository no longer readable | {issues['unreadable']} |")
    sub(r"\| closed within a week \| \d+ \|", f"| closed within a week | {issues['week']} |")
    sub(r"\| days to close, median / mean \| \d+ / [\d.]+ \|", f"| days to close, median / mean | {issues['median']} / {issues['mean']} |")
    sub(r"Open/closed split as of \d{4}-\d\d-\d\d;", f"Open/closed split as of {today};")
    sub(r"`ISSUES\.tsv` has \d+ rows: .*?\(\d+ distinct issues\)\.",
        f"`ISSUES.tsv` has {issues['rows']} rows: {issues['rows'] - issues['issues']} are duplicate log rows for the same issue ({issues['issues']} distinct issues).")

    if prs:
        sub(r"\| merged \| \d+ \|", f"| merged | {prs['merged']} |")
        sub(r"\| closed, not merged \| \d+ \|", f"| closed, not merged | {prs['closed']} |")
        sub(r"\| total \| \d+ \|", f"| total | {prs['total']} |")

    # `| open |` appears in both the Issues and PR tables; replace each inside its own section.
    issues_at = text.index("## Issues")
    pr_at = text.index("## Pull requests")
    head, issues_text, pr_text = text[:issues_at], text[issues_at:pr_at], text[pr_at:]
    issues_text = re.sub(r"\| open \| \d+ \|", f"| open | {issues['open']} |", issues_text, count=1)
    if prs:
        pr_text = re.sub(r"\| open \| \d+ \|", f"| open | {prs['open']} |", pr_text, count=1)
    text = head + issues_text + pr_text

    README.write_text(text, encoding="utf-8", newline="")
    print("README updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
