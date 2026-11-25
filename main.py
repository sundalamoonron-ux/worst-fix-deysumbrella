#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message -- make.fun entry.

Writes one line (<= 100 characters) to <output>/entry.txt: a commit
message for a bug fix that made everything worse.
"""

import os
import sys

# The line: the fix silenced a warning -- and the warning was the backup
# system. Plain commit-subject voice (no trailing period, as a real
# subject line has none), specific irony, fresh angle.
LINE = "fix: silenced the warning, the warning was the backup system"

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE
    # Gate self-check: 1-100 UTF-8 chars, not only whitespace, one line,
    # no leading/trailing whitespace.
    assert 1 <= len(text) <= 100, f"line length {len(text)} outside 1-100"
    assert text.strip(), "line is only whitespace"
    assert text == text.strip(), "line has leading/trailing whitespace"
    assert "\n" not in text, "line must be a single line"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify-after-write: read back and confirm exact bytes.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from line"
    return 0

if __name__ == "__main__":
    sys.exit(main())
