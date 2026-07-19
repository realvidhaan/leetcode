#!/usr/bin/env python3
"""One-time backfill: fetch every backlog problem's code from LeetCode and
pre-render it into ``backlog.json``.

Run this ONCE, locally, with the LeetCode cookie in the environment:

    LEETCODE_SESSION=... LEETCODE_CSRFTOKEN=... python3 scripts/backfill_backlog.py

Input:  backlog.meta.json  — [{slug,title,submission_id,lang,solved_ts}, ...]
Output: backlog.json       — pre-rendered queue consumed by daily_commit.py

After this succeeds the cookie is never needed again (we only drain the queue).
The script is resumable: re-running skips problems already present in
backlog.json and problems already committed as folders in the repo.
"""

import glob
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone


def _ssl_context():
    """Build a CA-verifying context. python.org's macOS Python ships no CA
    store, so fall back through certifi and the system bundle before giving up
    on default verification."""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:  # noqa: BLE001
        for path in ("/etc/ssl/cert.pem", "/usr/local/etc/openssl/cert.pem"):
            if os.path.exists(path):
                return ssl.create_default_context(cafile=path)
        return ssl.create_default_context()


SSL_CTX = _ssl_context()

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META = os.path.join(REPO_ROOT, "backlog.meta.json")
BACKLOG = os.path.join(REPO_ROOT, "backlog.json")

GRAPHQL = "https://leetcode.com/graphql"
REQUEST_SPACING_S = 4.0          # matches the n8n workflow; <2s triggers 403s
MAX_RETRIES = 4

# lang -> file extension, copied verbatim from the n8n "Build Commit Files" node.
EXT_MAP = {
    "python3": "py", "python": "py", "pandas": "py", "cpp": "cpp", "c": "c",
    "java": "java", "javascript": "js", "typescript": "ts", "golang": "go",
    "rust": "rs", "csharp": "cs", "kotlin": "kt", "swift": "swift", "ruby": "rb",
    "scala": "scala", "php": "php", "dart": "dart", "elixir": "ex", "erlang": "erl",
    "racket": "rkt", "mysql": "sql", "mssql": "sql", "oraclesql": "sql",
    "postgresql": "sql", "bash": "sh",
}

QUERY = (
    "query d($id: Int!) { submissionDetails(submissionId: $id) { code timestamp "
    "runtimeDisplay memoryDisplay lang { name } question { questionFrontendId "
    "difficulty title titleSlug } } }"
)


def cookie_header():
    session = os.environ.get("LEETCODE_SESSION")
    csrf = os.environ.get("LEETCODE_CSRFTOKEN", "")
    if not session:
        sys.exit("Set LEETCODE_SESSION (and ideally LEETCODE_CSRFTOKEN) in the environment.")
    parts = [f"LEETCODE_SESSION={session}"]
    if csrf:
        parts.append(f"csrftoken={csrf}")
    return "; ".join(parts), csrf


def fetch_details(submission_id, cookie, csrf):
    body = json.dumps({"query": QUERY, "variables": {"id": submission_id}}).encode()
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        ),
        "Cookie": cookie,
    }
    if csrf:
        headers["x-csrftoken"] = csrf
    for attempt in range(1, MAX_RETRIES + 1):
        req = urllib.request.Request(GRAPHQL, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as resp:
                payload = json.loads(resp.read().decode())
            return (payload.get("data") or {}).get("submissionDetails")
        except urllib.error.HTTPError as exc:
            wait = REQUEST_SPACING_S * (2 ** attempt)
            print(f"    HTTP {exc.code} (attempt {attempt}/{MAX_RETRIES}); sleeping {wait:.0f}s")
            time.sleep(wait)
        except (urllib.error.URLError, TimeoutError) as exc:
            wait = REQUEST_SPACING_S * (2 ** attempt)
            print(f"    network error {exc} (attempt {attempt}/{MAX_RETRIES}); sleeping {wait:.0f}s")
            time.sleep(wait)
    return None


def render(row, details):
    q = details["question"]
    lang_name = (details.get("lang") or {}).get("name") or row.get("lang") or ""
    ext = EXT_MAP.get(lang_name.lower(), "txt")
    front = q["questionFrontendId"]
    slug = q["titleSlug"]
    folder = f"{str(front).zfill(4)}-{slug}"
    solved_date = datetime.fromtimestamp(int(row["solved_ts"]), tz=timezone.utc).strftime("%Y-%m-%d")
    readme = (
        f"# {front}. {q['title']}\n\n"
        f"- Difficulty: {q['difficulty']}\n"
        f"- Language: {lang_name}\n"
        f"- Solved: {solved_date}\n"
        f"- Runtime: {details.get('runtimeDisplay') or 'n/a'} | "
        f"Memory: {details.get('memoryDisplay') or 'n/a'}\n"
        f"- Link: https://leetcode.com/problems/{slug}/\n"
    )
    return {
        "slug": slug,
        "folder": folder,
        "solved_ts": int(row["solved_ts"]),
        "solution_path": f"{folder}/solution.{ext}",
        "solution_code": details["code"],
        "readme_path": f"{folder}/README.md",
        "readme": readme,
        "commit_msg": f"Add {folder} ({q['difficulty']})",
    }


def main():
    cookie, csrf = cookie_header()

    with open(META, encoding="utf-8") as fh:
        rows = sorted(json.load(fh), key=lambda r: r["solved_ts"])

    done = {}
    if os.path.exists(BACKLOG):
        with open(BACKLOG, encoding="utf-8") as fh:
            done = {e["slug"]: e for e in json.load(fh)}
        print(f"Resuming: {len(done)} entries already in backlog.json")

    committed_slugs = {os.path.basename(p).split("-", 1)[1]
                       for p in glob.glob(os.path.join(REPO_ROOT, "[0-9]" * 4 + "-*"))}

    results = dict(done)
    failures = []
    todo = [r for r in rows if r["slug"] not in done and r["slug"] not in committed_slugs]
    print(f"{len(rows)} total, {len(committed_slugs)} already committed, "
          f"{len(done)} cached -> {len(todo)} to fetch")

    for i, row in enumerate(todo, 1):
        print(f"[{i}/{len(todo)}] {row['slug']} (sub {row['submission_id']})")
        details = fetch_details(row["submission_id"], cookie, csrf)
        if not details or not details.get("code"):
            print("    !! no code returned — skipping (cookie expired or submission gone)")
            failures.append(row["slug"])
        else:
            results[row["slug"]] = render(row, details)
            # Persist after each success so an interrupted run loses nothing.
            ordered = sorted(results.values(), key=lambda e: e["solved_ts"])
            with open(BACKLOG, "w", encoding="utf-8") as fh:
                json.dump(ordered, fh, ensure_ascii=False, indent=1)
        time.sleep(REQUEST_SPACING_S)

    print(f"\nDone. backlog.json has {len(results)} entries. Failures: {len(failures)}")
    if failures:
        print("Failed slugs (re-run to retry):", ", ".join(failures))


if __name__ == "__main__":
    main()
