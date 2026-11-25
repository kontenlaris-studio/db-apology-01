"""The Production Database Apology entry: it thought it was a demo."""

import os

APOLOGY = (
    "We apologize: the production database briefly believed it was a "
    "demo. It has been reminded that real customers are not test data, "
    "and its DELETE key has been confiscated."
)

CHAR_COUNT = len(APOLOGY)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(APOLOGY + "\n")
    print(f"wrote {path} ({CHAR_COUNT} characters)")


if __name__ == "__main__":
    main()
