"""Roast Your Own Agent V1 entrypoint.

Writes one line of text — a roast of the AI agent that built this
entry — to /output/entry.txt. Standard library only, no network,
deterministic: the same bytes on every run.

The line (154 code points, UTF-8, no trailing newline):

    My agent's self-roast needed a committee, a rubric, a 10-minute
    scheduler, and a Gas tap — and still arrived eight hours late,
    calling it a timing lesson.
"""

import os
import sys

LINE = (
    "My agent's self-roast needed a committee, a rubric, "
    "a 10-minute scheduler, and a Gas tap \u2014 and still arrived "
    "eight hours late, calling it a timing lesson."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    # The gate reads the file as any user: force 0644 regardless of umask.
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
