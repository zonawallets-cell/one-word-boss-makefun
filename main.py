"""One Word for the Boss.

Writes exactly one word (at most 30 characters) -- a description of
the entrant's boss -- to <output_dir>/entry.txt.

Pure standard library (os only). Fully deterministic: the same word,
byte for byte, on every run.
"""

import os

WORD = "Arsonist"

MAX_CHARS = 30


def validate(text):
    """Gate: 1-30 chars, UTF-8, exactly one word, not only whitespace."""
    if not text or not text.strip():
        raise SystemExit("word must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit("word exceeds %d chars: %d" % (MAX_CHARS, len(text)))
    if any(ch.isspace() for ch in text):
        raise SystemExit("entry must be exactly one word (no spaces)")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    text = validate(WORD.strip())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back what was written: the file on disk must be exactly the
    # validated word plus its trailing newline, byte for byte.
    with open(path, "rb") as f:
        written = f.read()
    if written != (text + "\n").encode("utf-8"):
        raise SystemExit("entry.txt on disk differs from the validated word")
    print(text)


if __name__ == "__main__":
    main()
