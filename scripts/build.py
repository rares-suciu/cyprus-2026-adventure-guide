from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
chapters = sorted((root / "book" / "chapters").glob("*.md"))

if not chapters:
    print("No chapters found.")
    sys.exit(1)

output_dir = root / "docx"
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "CYPRUS_2026_Adventure_Edition.docx"

command = [
    "pandoc",
    *(str(chapter) for chapter in chapters),
    "-o",
    str(output_file),
    "--toc",
]

subprocess.run(command, check=True)
print(f"Created: {output_file}")