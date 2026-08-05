import argparse
import re
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("number", type=int)
parser.add_argument("title")
args = parser.parse_args()

root = Path(__file__).resolve().parents[1]
chapter_template = root / "templates" / "chapter.md"
assets_template = root / "templates" / "chapter-assets" / "README.md"

slug = re.sub(r"[^a-z0-9]+", "-", args.title.lower()).strip("-")
chapter_name = f"{args.number:02d}-{slug}"

chapter_path = root / "book" / "chapters" / f"{chapter_name}.md"
assets_path = root / "book" / "assets" / "chapters" / chapter_name

if chapter_path.exists():
    raise FileExistsError(f"Chapter already exists: {chapter_path}")

chapter_text = chapter_template.read_text(encoding="utf-8")
chapter_path.write_text(
    chapter_text.replace("{{TITLE}}", args.title),
    encoding="utf-8",
)

for folder in ("images", "maps", "qr", "gps"):
    (assets_path / folder).mkdir(parents=True, exist_ok=True)

readme_text = assets_template.read_text(encoding="utf-8")
(assets_path / "README.md").write_text(
    readme_text.replace("{{TITLE}}", args.title),
    encoding="utf-8",
)

print(f"Created chapter: {chapter_path}")
print(f"Created assets:  {assets_path}")