#!/usr/bin/python3
"""Define file-writing function."""


def write_file(filename="", text=""):
    """Write string to a UTF8 text file.

    Args:
        filename (str):name offile to write.
        text (str):text to write tofile.
    Returns:
    number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
