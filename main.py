"""Dad Joke Showdown — entry for make.fun's
u-mfnakmal-dad-joke-showdown-1d2ce3e5.

Writes one dad joke (at most 200 characters) to the harness output
directory as entry.txt. The joke is a fixed string: no randomness,
no network, no time, no input — two runs produce the same bytes.
"""

import os

# The joke. Setup: a phone put on airplane mode. Punch: it now talks
# about a fear of heights — the mode taken literally, the way a dad
# would. Clean wordplay, no explanation needed, reads aloud in one
# breath, and it is not one of the thousand-times-told dad jokes.
LINE = "I put my phone on airplane mode, and now it keeps telling me about its fear of heights."

MAX_CHARS = 200


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be empty"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} characters, over the {MAX_CHARS} cap"
    assert line.count(".") == 1 and line.endswith("."), "the line must be a single sentence"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()
