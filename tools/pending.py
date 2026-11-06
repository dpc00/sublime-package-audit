"""List channel packages that have no RESULTS.tsv / .tested_packages.tsv row yet.

Older rows sometimes carry the version in the name column ("Bow Tintin 2.0.0"), so compare
normalised names: strip a trailing version token and collapse whitespace (2026-11-05).

Usage:  python tools/pending.py [--count] [--all]
Reads the cached channel JSON at %TEMP%/st_io_channel.json (download it with
https://packagecontrol.io/channel_v3.json if it is missing).
"""
import csv
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHANNEL = os.path.join(os.environ.get("TEMP", "/tmp"), "st_io_channel.json")


def norm(name):
    name = re.sub(r"\s+v?\d[\w.\-]*$", "", name.strip())
    return re.sub(r"\s+", " ", name).strip().lower()


def load_tested():
    tested = set()
    for rel in ("RESULTS.tsv", "data/.tested_packages.tsv"):
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8", newline="") as fh:
            for row in csv.reader(fh, delimiter="\t"):
                if row and row[0].strip():
                    tested.add(norm(row[0]))
    return tested


def load_channel():
    if not os.path.exists(CHANNEL):
        raise SystemExit("missing channel cache: %s" % CHANNEL)
    data = json.load(open(CHANNEL, encoding="utf-8", errors="replace"))
    return [
        entry["name"]
        for entries in (data.get("packages_cache") or {}).values()
        for entry in entries
    ]


def emit(text):
    """Print one ASCII-escaped line, falling back to raw bytes (2026-11-05)."""
    data = (text + "\n").encode("ascii", "backslashreplace")
    try:
        sys.stdout.write(data.decode("ascii"))
        sys.stdout.flush()
        return
    except Exception:
        pass
    try:
        sys.stdout.buffer.write(data)
        sys.stdout.buffer.flush()
    except Exception:
        pass


def main(argv):
    tested = load_tested()
    order = load_channel()
    pending = [name for name in order if norm(name) not in tested]
    if "--count" in argv:
        print(len(pending))
        return
    limit = len(pending) if "--all" in argv else 20
    # `tested` is every name seen in a record, including rows that are not real tests and
    # a few malformed name cells, so report channel coverage rather than that raw set size
    # (README.md counts tested packages by its own classified rule).
    channel_names = {norm(name) for name in order}
    covered = len(channel_names & tested)
    print(
        "channel %d (%d distinct names), covered by a record %d, pending %d, record names %d"
        % (len(order), len(channel_names), covered, len(pending), len(tested))
    )
    for name in pending[:limit]:
        emit(name)


if __name__ == "__main__":
    main(sys.argv[1:])
