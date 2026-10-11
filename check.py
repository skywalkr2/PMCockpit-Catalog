"""Read packs.yaml exactly as PM Cockpit's Add-ons screen does, and fail on anything the app would leave out."""

import sys
from pathlib import Path

from engine import packs

feed = packs.parse("packs.yaml", Path("packs.yaml").read_text(encoding="utf-8"))
if feed.error:
    sys.exit(f"packs.yaml: {feed.error}")
for note in feed.notes:
    print(f"packs.yaml: {note}", file=sys.stderr)
if feed.notes:
    sys.exit(1)
print(f"packs.yaml reads cleanly: {len(feed.entries)} pack(s).")
