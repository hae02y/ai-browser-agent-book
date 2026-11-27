"""Check deterministic book structure before editorial review or publishing."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"
LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []
    pages = sorted(PAGES.glob("[0-2][0-9]-*.md"))
    if len(pages) != 22:
        errors.append(f"expected 22 chapter files, found {len(pages)}")

    toc = (ROOT / "TOC.md").read_text(encoding="utf-8")
    toc_chapters = re.findall(r"\]\((pages/[0-2][0-9]-[^)]+\.md)\)", toc)
    if len(toc_chapters) != 22 or len(set(toc_chapters)) != 22:
        errors.append("TOC.md must link each of the 22 chapters exactly once")

    files = [ROOT / "README.md", ROOT / "TOC.md", *pages]
    files.extend((ROOT / "docs").glob("*.md"))
    for source in files:
        if not source.exists():
            errors.append(f"missing file: {source.relative_to(ROOT)}")
            continue
        for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            for image, label, target in LINK.findall(line):
                if image and not label.strip():
                    errors.append(f"{source.relative_to(ROOT)}:{line_number}: image has no alt text")
                target = target.split("#", 1)[0]
                if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                    continue
                if not (source.parent / target).exists():
                    errors.append(f"{source.relative_to(ROOT)}:{line_number}: missing target {target}")

    if errors:
        print("Book checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Book checks passed: {len(pages)} chapters, TOC and local links/images")
    return 0


if __name__ == "__main__":
    sys.exit(main())
