#!/usr/bin/env python3
"""Write the last text message a dying phone sends at one percent battery.

The entry is a single text in the phone's own voice: a final, funny
message under 200 characters. Deterministic, stdlib only, no network.
"""
import os

ENTRY = (
    "1%. Delete my search history, cancel my 6am alarm, and tell my "
    "owner I died doing what I loved: ignoring his calls."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is whitespace only"
    assert "\n" not in text, "entry must be a single-line text message"
    assert text.endswith("."), "entry should read as one complete message"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, encoding="utf-8") as f:
        back = f.read()
    assert back == text, "round-trip mismatch"
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
