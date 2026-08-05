import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("number", type=int)
parser.add_argument("title")
args = parser.parse_args()

slug = args.title.lower().replace(" ", "-")
path = Path("book/chapters") / f"{args.number:02d}-{slug}.md"

path.write_text(
    f"# {args.title}\n\nDraft chapter.\n",
    encoding="utf-8"
)

print(f"Created: {path}")