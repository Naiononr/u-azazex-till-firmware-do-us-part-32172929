#!/usr/bin/env python3
"""Till Firmware Do Us Part — one wedding vow, spoken by a robot.

Writes the fixed vow to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR),
as UTF-8 text with no trailing newline, world-readable (mode 0644).
Standard library only; deterministic.
"""

import os
import tempfile

VOW = (
    "You are my favorite bug, the one I will never fix, "
    "and I vow to love you through every update, every crash, "
    "and every low battery."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = VOW.encode("utf-8")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.chmod(tmp, 0o644)
        os.replace(tmp, os.path.join(out_dir, "entry.txt"))
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
