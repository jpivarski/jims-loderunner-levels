#!/usr/bin/env python3
"""Render the tail of README.md into the writeup area of index.html.

Everything in README.md *after* the ``<!-- COPY HERE -->`` marker is converted
from Markdown to HTML and spliced into index.html between::

    <!-- README:BEGIN -->
    <!-- README:END -->

So the workflow is: write prose in README.md, run this script, and the same
prose appears under the playable area.

    python3 tools/readme_to_html.py            # convert and write
    python3 tools/readme_to_html.py --check    # is index.html stale? (exit 1 if so)

index.html stays the only deployed file; this is a local authoring tool.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

COPY_MARKER = "<!-- COPY HERE -->"
BEGIN = "<!-- README:BEGIN -->"
END = "<!-- README:END -->"

REPO = Path(__file__).resolve().parent.parent


class Problem(Exception):
    """Something the user needs to fix, reported without a traceback."""


def make_renderer():
    """A CommonMark renderer with tables and strikethrough turned on.

    Deliberately not the "gfm-like" preset: that also enables linkify, which
    requires the separate linkify-it-py package and raises at render time if it
    is missing.  Tables are what the README actually needs.
    """
    try:
        from markdown_it import MarkdownIt
    except ImportError as exc:
        raise Problem(
            "markdown-it-py is required to render the README.\n"
            "    pip install markdown-it-py"
        ) from exc
    return MarkdownIt("commonmark").enable("table").enable("strikethrough")


def extract(readme_text: str) -> str:
    """Return the Markdown after COPY_MARKER, which must appear exactly once."""
    count = readme_text.count(COPY_MARKER)
    if count == 0:
        raise Problem(
            f"README.md has no {COPY_MARKER} marker.\n"
            "Add it on a line of its own; everything below it gets embedded."
        )
    if count > 1:
        raise Problem(
            f"README.md has {count} {COPY_MARKER} markers; expected exactly one."
        )
    return readme_text.split(COPY_MARKER, 1)[1].strip()


def splice(html_text: str, rendered: str) -> str:
    """Replace whatever currently sits between BEGIN and END."""
    for marker in (BEGIN, END):
        n = html_text.count(marker)
        if n != 1:
            raise Problem(
                f"index.html contains {n} copies of {marker}; expected exactly one."
            )

    start = html_text.index(BEGIN) + len(BEGIN)
    stop = html_text.index(END)
    if stop < start:
        raise Problem(f"{END} appears before {BEGIN} in index.html.")

    if END in rendered or BEGIN in rendered:
        raise Problem(
            "The rendered HTML contains one of the splice markers, which would "
            "corrupt index.html on the next run.  Remove it from README.md."
        )

    # Left flush on purpose: indenting the block would add leading whitespace
    # inside any <pre> and silently change how code samples render.
    return html_text[:start] + "\n" + rendered.strip() + "\n" + html_text[stop:]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--readme", type=Path, default=REPO / "README.md")
    ap.add_argument("--html", type=Path, default=REPO / "index.html")
    ap.add_argument(
        "--check",
        action="store_true",
        help="verify index.html is up to date; write nothing, exit 1 if stale",
    )
    args = ap.parse_args(argv)

    try:
        for path in (args.readme, args.html):
            if not path.is_file():
                raise Problem(f"no such file: {path}")

        readme_text = args.readme.read_text(encoding="utf-8")
        html_text = args.html.read_text(encoding="utf-8")

        markdown = extract(readme_text)
        if not markdown:
            raise Problem(f"there is no content after {COPY_MARKER} in README.md.")

        rendered = make_renderer().render(markdown)
        updated = splice(html_text, rendered)

    except Problem as problem:
        print(f"error: {problem}", file=sys.stderr)
        return 2

    if updated == html_text:
        print(f"{args.html.name} is already up to date")
        return 0

    if args.check:
        print(f"{args.html.name} is stale; run tools/readme_to_html.py", file=sys.stderr)
        return 1

    args.html.write_text(updated, encoding="utf-8")
    lines = rendered.strip().count("\n") + 1
    print(f"wrote {lines} lines of HTML into {args.html.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
