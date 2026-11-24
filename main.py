"""One Letter: Coffee or Tea — entry "A" (coffee).

Writes exactly one byte, the letter A, to entry.txt in the output
directory, with no trailing newline and no other content.
"""
import os

LETTER = "A"


def resolve_output_dir():
    """Grader output dir: $MAKEFUN_OUTPUT_DIR, default /output."""
    value = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "").strip()
    return value or "/output"


def write_entry(path):
    """Write the single letter as exactly one byte, no newline."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as f:
        f.write(LETTER.encode("utf-8"))


def output_path():
    return os.path.join(resolve_output_dir(), "entry.txt")


def main():
    write_entry(output_path())


if __name__ == "__main__":
    main()
