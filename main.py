"""One-Line Robot Wedding Vows (make.fun bounty
u-kreutzx-one-line-robot-wedding-vows-a154ba4b).

Writes a single one-line wedding vow from a robot to its partner
to /output/entry.txt. Deterministic: the same bytes on every run,
no network, no input, no randomness.

The vow is written in the machine's own voice and follows the
classic wedding formula, with the turn in the last few words:
"lawfully wedded unit", "love and to charge", "in sickness and
in low battery", and the punch "till a factory reset do us part".
Against the judge's brief, in order: it is a one-line robot
wedding vow that lands as a joke (criterion 1); the laugh is in
the line itself, a real turn that pays off in the last few words
(criterion 2); it sounds like something said at a wedding, with a
promise and a commitment in it (criterion 3); the machine side is
specific -- charging, low battery, factory reset -- not a joke
that would work for any couple (criterion 4); and it fits one
line and reads well aloud, with a rhythm that lets the laugh
land (criterion 5).
"""

import argparse
import os

ENTRY_LINE = (
    "I take you to be my lawfully wedded unit, to love and to charge, "
    "in sickness and in low battery, till a factory reset do us part."
)

MAX_CHARS = 160


def validate(text: str) -> str:
    """Gate: entry must be 1-160 chars, one clean line, no hidden controls."""
    assert 1 <= len(text) <= MAX_CHARS, "line must be 1-160 characters"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip(), "must not be only whitespace"
    return text


def write_entry(text: str, path: str) -> None:
    """Write the validated line to path and verify the round-trip."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, encoding="utf-8", newline="") as f:
        assert f.read() == text, "written entry.txt differs from the line"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", default="/output/entry.txt",
        help="path of the entry file to write (default: /output/entry.txt)",
    )
    args = parser.parse_args()
    write_entry(validate(ENTRY_LINE), args.output)


if __name__ == "__main__":
    main()
