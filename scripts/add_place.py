from pathlib import Path
import re
import yaml

root = Path(__file__).resolve().parents[1]
output_dir = root / "data" / "places"
output_dir.mkdir(parents=True, exist_ok=True)

name = input("Name: ").strip()
place_type = input("Type: ").strip().lower()
region = input("Region: ").strip()
latitude = float(input("Latitude: ").strip())
longitude = float(input("Longitude: ").strip())

slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
output_file = output_dir / f"{slug}.yml"

data = {
    "name": name,
    "type": place_type,
    "region": region,
    "coordinates": {
        "latitude": latitude,
        "longitude": longitude,
    },
    "ratings": {
        "family": 0,
        "snorkeling": 0,
        "photography": 0,
        "parking": 0,
    },
    "features": {},
    "best_time": "",
    "estimated_visit": "",
    "status": "draft",
}

output_file.write_text(
    yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
    encoding="utf-8",
)

print(f"Created: {output_file}")