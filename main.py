"""Write a single descriptive word for this Wi-Fi connection.

The program produces one small text file holding the chosen word,
``Gaslighting``, with no trailing newline. It takes no arguments and
reads no input, so every execution leaves exactly the same bytes
behind in ``/output/entry.txt``.
"""

from pathlib import Path

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
WORD = "Gaslighting"


def main() -> None:
    """Create the output folder if needed, then store the word in it.

    The word is encoded explicitly as UTF-8 and written as raw bytes,
    so nothing (not even a trailing newline) is added after it.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
