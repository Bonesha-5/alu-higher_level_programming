#!/usr/bin/python3
"""
This module prints indented text.
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', and ':'.

    Args:
        text: str

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char in ".:?":
            print("\n")
            while len(text) > 0 and text[text.index(char)+1:text.index(char)+2] == " ":
                text = text[:text.index(char)+1] + text[text.index(char)+2:]
