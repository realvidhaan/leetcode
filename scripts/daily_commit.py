#!/usr/bin/env python3
"""Daily LeetCode -> GitHub commit (no network except `git push`).

Reads the pre-materialized queue in ``backlog.json`` (produced once by
``backfill_backlog.py``), picks the oldest solved problem that is not yet in
the repo, writes its solution + README, and commits.

Design notes:
- "Already committed" is derived purely from folder existence, so there is no
  mutable state file to drift out of sync. Re-running is safe and idempotent.
- Every field needed for the commit is pre-rendered in backlog.json, so this
  script makes NO LeetCode API calls and needs NO secrets. The only external
  action is `git push` (auth handled by the environment: GITHUB_TOKEN in CI).
"""

import json
import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKLOG = os.path.join(REPO_ROOT, "backlog.json")


def run(*args):
    """Run a git command in the repo root, raising on failure."""
    subprocess.run(args, cwd=REPO_ROOT, check=True)


def main():
    if not os.path.exists(BACKLOG):
        sys.exit(f"backlog.json not found at {BACKLOG} — run backfill_backlog.py first")

    with open(BACKLOG, encoding="utf-8") as fh:
        queue = json.load(fh)

    # queue is sorted ascending by solved_ts; pick the first whose folder is absent.
    entry = next(
        (e for e in queue if not os.path.isdir(os.path.join(REPO_ROOT, e["folder"]))),
        None,
    )
    if entry is None:
        print("Backlog fully drained — nothing to commit. 🎉")
        return

    folder = os.path.join(REPO_ROOT, entry["folder"])
    os.makedirs(folder, exist_ok=True)

    solution_path = os.path.join(REPO_ROOT, entry["solution_path"])
    readme_path = os.path.join(REPO_ROOT, entry["readme_path"])
    with open(solution_path, "w", encoding="utf-8") as fh:
        fh.write(entry["solution_code"])
    with open(readme_path, "w", encoding="utf-8") as fh:
        fh.write(entry["readme"])

    # Identity is set here too so the commit is authored by the user even when
    # pushed by GITHUB_TOKEN in CI — this is what makes it count on the graph.
    run("git", "config", "user.name", os.environ.get("GIT_AUTHOR_NAME", "Vidhaan T. Jain"))
    run("git", "config", "user.email", os.environ.get("GIT_AUTHOR_EMAIL", "realvidhaan@gmail.com"))
    run("git", "add", entry["folder"])
    run("git", "commit", "-m", entry["commit_msg"])
    run("git", "push")
    print(f"Committed {entry['folder']}")


if __name__ == "__main__":
    main()
