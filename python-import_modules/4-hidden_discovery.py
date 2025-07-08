#!/usr/bin/python3
import marshal
import sys
import types

if __name__ == "__main__":
    filename = "hidden_4.pyc"

    with open(filename, "rb") as f:
        f.read(16)  # skip the header of the pyc file (magic number + timestamp + other metadata)
        code = marshal.load(f)  # load the code object from the file

    # The code object contains a list of names in code.co_names
    names = code.co_names

    # Filter out names starting with '__'
    filtered_names = [name for name in names if not name.startswith("__")]

    # Print the names in alphabetical order
    for name in sorted(filtered_names):
        print(name)
