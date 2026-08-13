"""Check README links for obvious maintenance errors."""

from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


README = Path(__file__).resolve().parents[1] / "README.md"
LINK_RE = re.compile(r"\[[^]]+\]\((https?://[^)]+)\)")
BAD_URLS = {"https://arxiv.org/", "http://arxiv.org/"}


def read_urls():
    return LINK_RE.findall(README.read_text(encoding="utf-8"))


def check_structure(urls):
    errors = []
    for url in urls:
        if url in BAD_URLS:
            errors.append(f"generic arXiv URL: {url}")
        if "example.com" in url or "TODO" in url:
            errors.append(f"placeholder URL: {url}")
    return errors


def check_network(urls):
    errors = []
    for url in sorted(set(urls)):
        try:
            request = Request(url, method="HEAD", headers={"User-Agent": "radar-perception-link-check"})
            with urlopen(request, timeout=15) as response:
                if response.status >= 400:
                    errors.append(f"HTTP {response.status}: {url}")
        except HTTPError as exc:
            if exc.code not in {403, 405}:
                errors.append(f"HTTP {exc.code}: {url}")
        except URLError as exc:
            errors.append(f"network error: {url} ({exc.reason})")
    return errors


def main():
    urls = read_urls()
    errors = check_structure(urls)
    if "--network" in sys.argv:
        errors.extend(check_network(urls))
    if errors:
        print("Link check failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Link check passed: {len(urls)} links inspected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
