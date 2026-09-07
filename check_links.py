from pathlib import Path
import re

root = Path(__file__).parent
html_files = list(root.glob("*.html")) + list((root / "journal").glob("*.html"))
missing = []
for path in html_files:
    text = path.read_text(encoding="utf-8")
    for href in re.findall(r'href="(\./[^"#]+|\.\./[^"#]+)"', text):
        target = (path.parent / href).resolve()
        if not target.exists():
            missing.append((str(path.relative_to(root)), href))
print(f"pages={len(html_files)}")
print(f"missing={len(missing)}")
for item in missing:
    print(item)
