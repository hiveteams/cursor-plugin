#!/usr/bin/env python
import argparse
import json
import os
import platform
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict, Optional, Tuple


STATE_FILENAME = "hive-api-docs-state.json"
DOCS_SUBDIR = Path("hive-api/docs")
DEFAULT_TTL_HOURS = 24
CHECK_URLS = [
    "https://developers.hive.com/reference",
    "https://developers.hive.com/v2.0/reference",
]


def resolve_cache_root() -> Path:
    override = os.getenv("HIVE_DOCS_CACHE_PATH")
    if override:
        return Path(override).expanduser()

    system = platform.system().lower()
    if system == "darwin":
        return Path("~/Library/Caches/hive-llm-plugins").expanduser()
    if system == "windows":
        local_app_data = os.getenv("LOCALAPPDATA")
        if local_app_data:
            return Path(local_app_data) / "hive-llm-plugins" / "Cache"
        return Path("~\\AppData\\Local\\hive-llm-plugins\\Cache").expanduser()

    xdg_cache_home = os.getenv("XDG_CACHE_HOME")
    if xdg_cache_home:
        return Path(xdg_cache_home).expanduser() / "hive-llm-plugins"
    return Path("~/.cache/hive-llm-plugins").expanduser()


def read_json(path: Path) -> Dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def write_json(path: Path, payload: Dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def request_metadata(
    url: str,
    timeout_seconds: int,
    etag: Optional[str] = None,
    last_modified: Optional[str] = None,
) -> Tuple[bool, Optional[str], Optional[str], Optional[int], Optional[str]]:
    headers = {"User-Agent": "hive-llm-plugins-docs-checker/1.0"}
    if etag:
        headers["If-None-Match"] = etag
    if last_modified:
        headers["If-Modified-Since"] = last_modified

    request = urllib.request.Request(url, method="HEAD", headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            return (
                False,
                response.headers.get("ETag"),
                response.headers.get("Last-Modified"),
                response.status,
                None,
            )
    except urllib.error.HTTPError as err:
        # 304 Not Modified is expected for conditional checks
        if err.code == 304:
            return (True, etag, last_modified, err.code, None)
        # Some hosts reject HEAD; fallback to GET
        if err.code in (400, 403, 405, 501):
            return request_metadata_with_get(url, timeout_seconds, etag, last_modified)
        return (False, etag, last_modified, err.code, str(err))
    except Exception as err:  # noqa: BLE001
        return (False, etag, last_modified, None, str(err))


def request_metadata_with_get(
    url: str,
    timeout_seconds: int,
    etag: Optional[str] = None,
    last_modified: Optional[str] = None,
) -> Tuple[bool, Optional[str], Optional[str], Optional[int], Optional[str]]:
    headers = {"User-Agent": "hive-llm-plugins-docs-checker/1.0"}
    if etag:
        headers["If-None-Match"] = etag
    if last_modified:
        headers["If-Modified-Since"] = last_modified

    request = urllib.request.Request(url, method="GET", headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            return (
                False,
                response.headers.get("ETag"),
                response.headers.get("Last-Modified"),
                response.status,
                None,
            )
    except urllib.error.HTTPError as err:
        if err.code == 304:
            return (True, etag, last_modified, err.code, None)
        return (False, etag, last_modified, err.code, str(err))
    except Exception as err:  # noqa: BLE001
        return (False, etag, last_modified, None, str(err))


def needs_refresh(state: Dict, ttl_hours: int, now_seconds: int) -> bool:
    last_check = int(state.get("lastCheckedAtEpoch", 0))
    ttl_seconds = ttl_hours * 3600
    if last_check == 0:
        return True
    if now_seconds - last_check >= ttl_seconds:
        return True
    return False


def run_refresh(
    repo_root: Path,
    output_dir: Path,
    refresh_timeout_seconds: int,
    quiet: bool,
) -> Tuple[bool, str]:
    baseline_dir = repo_root / "skills" / "hive-api" / "docs"
    cmd = [
        sys.executable,
        str(repo_root / "download_docs.py"),
        "--output-dir",
        str(output_dir),
        "--baseline-dir",
        str(baseline_dir),
        "--index-url",
        "https://developers.hive.com/reference/hive-graphql-documentation",
        "--throttle-seconds",
        "0",
    ]
    if quiet:
        cmd.append("--quiet")

    try:
        completed = subprocess.run(
            cmd,
            cwd=str(repo_root),
            text=True,
            capture_output=True,
            timeout=max(refresh_timeout_seconds, 30),
            check=False,
        )
    except Exception as err:  # noqa: BLE001
        return (False, str(err))

    if completed.returncode == 0:
        return (True, completed.stdout.strip())

    err_msg = completed.stderr.strip() or completed.stdout.strip() or "unknown error"
    return (False, err_msg)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Hive docs freshness and refresh cache.")
    parser.add_argument("--ttl-hours", type=int, default=DEFAULT_TTL_HOURS)
    parser.add_argument("--timeout-seconds", type=int, default=5)
    parser.add_argument("--refresh-timeout-seconds", type=int, default=300)
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--force-refresh", action="store_true")
    args = parser.parse_args()

    cache_root = resolve_cache_root()
    state_path = cache_root / STATE_FILENAME
    docs_output_dir = cache_root / DOCS_SUBDIR
    repo_root = Path(__file__).resolve().parent.parent

    state = read_json(state_path)
    now_seconds = int(time.time())
    last_sources = state.get("sources", {})
    should_refresh = args.force_refresh or needs_refresh(state, args.ttl_hours, now_seconds)

    metadata_results: Dict[str, Dict[str, Optional[str]]] = {}
    any_changed = False
    any_error = False

    for url in CHECK_URLS:
        previous = last_sources.get(url, {})
        not_modified, next_etag, next_last_modified, status, error = request_metadata(
            url=url,
            timeout_seconds=args.timeout_seconds,
            etag=previous.get("etag"),
            last_modified=previous.get("lastModified"),
        )

        metadata_results[url] = {
            "etag": next_etag,
            "lastModified": next_last_modified,
            "status": status,
            "error": error,
            "checkedAtEpoch": now_seconds,
        }

        if error:
            any_error = True
            continue
        previous_etag = previous.get("etag")
        previous_last_modified = previous.get("lastModified")
        has_previous_validators = bool(previous_etag or previous_last_modified)
        has_next_validators = bool(next_etag or next_last_modified)

        if not_modified:
            continue

        # If the server doesn't provide validators, rely on TTL instead of
        # forcing a refresh every session.
        if not has_previous_validators and not has_next_validators:
            continue

        if has_previous_validators:
            if previous_etag != next_etag or previous_last_modified != next_last_modified:
                any_changed = True
            continue

        # First time receiving validators from a source counts as changed.
        if has_next_validators:
            any_changed = True

    if any_changed:
        should_refresh = True

    refreshed = False
    refresh_error = None
    diff_summary: Optional[Dict] = None

    if should_refresh and not any_error:
        refreshed, refresh_output = run_refresh(
            repo_root=repo_root,
            output_dir=docs_output_dir,
            refresh_timeout_seconds=args.refresh_timeout_seconds,
            quiet=args.quiet,
        )
        if not refreshed:
            refresh_error = refresh_output
        else:
            manifest_path = docs_output_dir / "docs-diff-manifest.json"
            manifest = read_json(manifest_path)
            if manifest:
                diff_summary = {
                    "changed": len(manifest.get("changed", [])),
                    "added": len(manifest.get("added", [])),
                    "removed": len(manifest.get("removed", [])),
                }
    elif should_refresh and any_error:
        refresh_error = "metadata check failed; skipping refresh"

    next_state = {
        "cacheRoot": str(cache_root),
        "docsOutputDir": str(docs_output_dir),
        "lastCheckedAtEpoch": now_seconds,
        "lastRefreshedAtEpoch": now_seconds if refreshed else state.get("lastRefreshedAtEpoch"),
        "sources": metadata_results,
        "lastResult": {
            "refreshed": refreshed,
            "refreshError": refresh_error,
            "diffSummary": diff_summary,
        },
    }
    write_json(state_path, next_state)

    if not args.quiet:
        status = "refreshed" if refreshed else "unchanged"
        if refresh_error:
            status = f"failed ({refresh_error})"
        print(f"Hive docs check: {status}")
        print(f"State: {state_path}")
        print(f"Docs cache: {docs_output_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
