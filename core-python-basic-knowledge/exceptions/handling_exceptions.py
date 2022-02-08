"""
Exceptions resulting from programmer errors:
-> IndentationError
-> SyntaxError
-> NameError

These should almost never be caught.
"""
import sys


def convert(s):
    """Convert a string to an integer."""

    try:
        number = ''
        for token in s:
            number += token

        return int(number)

    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}", file=sys.stderr)
        raise
