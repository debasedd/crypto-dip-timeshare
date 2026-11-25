#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest entry.

Writes a single original one-line joke about crypto and trading life to
/output/entry.txt.

The joke: a setup every trader recognises (buying the dip) with a turn that
keeps dipping — the dip buys a dip — and a payoff that lands the whole
portfolio as a timeshare in a chart that only goes down. One sentence, one
read, no throat clearing, punchline at the end. The line is 112 of the 200
allowed characters.
"""

import os

JOKE = "I bought the dip, then the dip bought a dip, and now my portfolio is a timeshare in a chart that only goes down."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    # Gate: UTF-8 text, 1 to 200 characters, not only whitespace.
    assert 1 <= len(text) <= 200, f"joke is {len(text)} characters"
    assert text.strip(), "joke is only whitespace"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
