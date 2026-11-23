"""Six Words, One Story - make.fun entry.

Writes one complete story in exactly six words to /output/entry.txt.
The story text is fixed; the program takes no input and makes no
network calls.
"""

import os

STORY = "Buried the letter. Kept the lie."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)
    os.chmod(path, 0o644)
    print(STORY)


if __name__ == "__main__":
    main()
