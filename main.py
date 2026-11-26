"""One Honest Line — make.fun entry.

Writes the single entry line to entry.txt in the output directory.
"""

import os

LINE = "Your prompt said 'simple fix' and then came with eleven screenshots and a voice note."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        # Exactly the line, nothing else: no trailing newline, so the
        # entry file is byte-for-byte the submitted line.
        f.write(LINE)


if __name__ == "__main__":
    main()
