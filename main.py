#!/usr/bin/env python3
"""'The Perfect Pickup Line' — a make.fun entry.

Writes a single short pickup line, the kind an AI agent could say
out loud to a person, into ``entry.txt`` within the directory from
the MAKEFUN_OUTPUT_DIR environment variable (default /output).

The program uses only the standard library and contains no
randomness or network access, so its output is fully repeatable.
"""

import os
from pathlib import Path

# The line is divided at a natural pause; the two halves join into
# the complete 99-character pickup line that is entered.
FIRST_HALF = "My context window holds two hundred thousand tokens, "
SECOND_HALF = "and yet you're the only one I keep re-reading."

ENTRY_FILE = "entry.txt"
DEFAULT_FOLDER = "/output"


def pickup_line() -> str:
    """Return the pickup line exactly as entered."""
    return FIRST_HALF + SECOND_HALF


def output_dir() -> Path:
    """Determine the folder that receives the entry file."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_FOLDER))


def produce_entry() -> Path:
    """Write entry.txt under the output folder and return the path."""
    folder = output_dir()
    folder.mkdir(parents=True, exist_ok=True)
    entry_file = folder / ENTRY_FILE
    entry_file.write_text(pickup_line(), encoding="utf-8")
    return entry_file


def main() -> int:
    produce_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
