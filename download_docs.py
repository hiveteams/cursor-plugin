import argparse
import os
import re
import time
import urllib.request
from pathlib import Path
from typing import Iterable, Set


DEFAULT_INDEX_URL = "https://developers.hive.com/reference/hive-graphql-documentation"
DEFAULT_DOCS_DIR = "skills/hive-api/docs"
DEFAULT_BASE_URL = "https://developers.hive.com"


def fetch(url: str, quiet: bool = False) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req) as response:
            return response.read().decode("utf-8")
    except Exception as err:  # noqa: BLE001
        if not quiet:
            print(f"Error fetching {url}: {err}")
        return ""


def get_reference_links(index_url: str, quiet: bool = False) -> Set[str]:
    html = fetch(index_url, quiet=quiet)
    if not html:
        return set()
    return set(re.findall(r'href="(/reference/[^"]+)"', html))


def download_docs(
    docs_dir: str,
    index_url: str = DEFAULT_INDEX_URL,
    base_url: str = DEFAULT_BASE_URL,
    quiet: bool = False,
    throttle_seconds: float = 0.5,
) -> int:
    links = get_reference_links(index_url=index_url, quiet=quiet)
    target_dir = Path(docs_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    if not quiet:
        print(f"Found {len(links)} links. Downloading...")

    if not links:
        if not quiet:
            print("No links found.")
        return 1

    for i, link in enumerate(sorted(links), start=1):
        name = link.split("/")[-1]
        url = f"{base_url}{link}.md"
        if not quiet:
            print(f"[{i}/{len(links)}] Downloading {name} from {url}")
        md_content = fetch(url, quiet=quiet)
        if md_content:
            (target_dir / f"{name}.md").write_text(md_content, encoding="utf-8")
        if throttle_seconds > 0:
            time.sleep(throttle_seconds)

    if not quiet:
        print("Done.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download Hive API docs pages as markdown.")
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_DOCS_DIR,
        help=f"Directory to write markdown docs (default: {DEFAULT_DOCS_DIR})",
    )
    parser.add_argument(
        "--index-url",
        default=DEFAULT_INDEX_URL,
        help=f"Reference index URL used to discover links (default: {DEFAULT_INDEX_URL})",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"Base URL for docs links (default: {DEFAULT_BASE_URL})",
    )
    parser.add_argument("--quiet", action="store_true", help="Minimize output.")
    parser.add_argument(
        "--throttle-seconds",
        type=float,
        default=0.5,
        help="Delay between requests in seconds (default: 0.5).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return download_docs(
        docs_dir=args.output_dir,
        index_url=args.index_url,
        base_url=args.base_url,
        quiet=args.quiet,
        throttle_seconds=args.throttle_seconds,
    )


if __name__ == "__main__":
    raise SystemExit(main())
