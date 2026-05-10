#!/usr/bin/env python3
"""Validate source-architecture-docs Markdown and HTML artifacts."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_MD_HEADINGS = [
    "Source inputs inspected",
    "Component",
    "flowchart",
    "sequenceDiagram",
    "Open Questions",
]


def _read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def _asset_refs(text: str) -> set[str]:
    refs: set[str] = set()
    refs.update(re.findall(r"!\[[^\]]*\]\((assets/[^)]+)\)", text))
    refs.update(re.findall(r"<img[^>]+src=[\"'](assets/[^\"']+)[\"']", text))
    return refs


def _check_assets(base_dir: Path, refs: set[str]) -> list[str]:
    missing = []
    for ref in sorted(refs):
        if not (base_dir / ref).exists():
            missing.append(ref)
    return missing


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("Usage: validate_artifacts.py <architecture-report.md> <architecture-artifact.html>", file=sys.stderr)
        return 2

    md_path = Path(argv[1]).resolve()
    html_path = Path(argv[2]).resolve()
    md = _read(md_path)
    html = _read(html_path)

    errors: list[str] = []

    for needle in REQUIRED_MD_HEADINGS:
        if needle not in md:
            errors.append(f"Markdown missing expected content: {needle}")

    if "```mermaid" not in md:
        errors.append("Markdown has no Mermaid code blocks")
    if "flowchart" not in md:
        errors.append("Markdown has no flowchart")
    if "sequenceDiagram" not in md:
        errors.append("Markdown has no sequence diagram")
    if "mermaid" not in html:
        errors.append("HTML does not include Mermaid rendering/source")
    if "{{" in html or "}}" in html:
        errors.append("HTML still contains template placeholders")
    if "architecture-overview.png" not in md or "architecture-overview.png" not in html:
        errors.append("Overview architecture image is not referenced by both artifacts")

    md_refs = _asset_refs(md)
    html_refs = _asset_refs(html)
    missing_assets = _check_assets(md_path.parent, md_refs | html_refs)
    for ref in missing_assets:
        errors.append(f"Missing referenced asset: {ref}")

    if errors:
        print("Artifact validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Artifact validation passed")
    print(f"- Markdown: {md_path}")
    print(f"- HTML: {html_path}")
    print(f"- Referenced assets: {len(md_refs | html_refs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
