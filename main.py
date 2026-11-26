import os

LINE = "Sorry I ate your report. It tasted like urgency, and I regret nothing — except this paper jam."

LIMIT = 120
if len(LINE) != 94 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 94 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# An apology that blames the victim — the printer's voice, not the user's.
