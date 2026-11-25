# u-deranalabs-invent-a-word-we-need-17a020e0: one invented English word
# with a one-line definition. The program writes that single line to
# /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Gate: the entry is UTF-8 text of 1-140 characters, not only whitespace.
MAX_CHARS = 140

# The coinage: "meetmute" (meeting + mute). It names a real gap — the
# moment you realise you have been talking to a room that could not hear
# you — in one clean compound that is sayable, spellable and memorable,
# and the definition lands in a single reading.
ENTRY = "meetmute: talking for a full minute before noticing you were on mute."


def validate_entry(text):
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"


def main():
    validate_entry(ENTRY)
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("FAIL: entry.txt on disk does not match the entry")
    print("OK: %d chars" % len(ENTRY))
    print(ENTRY)


if __name__ == "__main__":
    main()
