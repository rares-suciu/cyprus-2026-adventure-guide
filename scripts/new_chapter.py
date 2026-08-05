import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("number", type=int)
parser.add_argument("title")
args = parser.parse_args()

root = Path(__file__).resolve().parents[1]
template = root / "templates" / "chapter.md"

slug = args.title.lower().replace(" ", "-")
chapter = root / "book" / "chapters" / f"{args.number:02d}-{slug}.md"

text = template.read_text(encoding="utf-8")
text = text.replace("{{TITLE}}", args.title)

chapter.write_text(text, encoding="utf-8")

print(f"Created: {chapter}")