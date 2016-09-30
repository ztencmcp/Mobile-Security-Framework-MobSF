"""
Strings-module to be undependend from operating systems
Taken from: http://stackoverflow.com/a/17197027
"""
import string

def strings(filename, min=4):
    """Print out all connected series of readable chars longer than min."""
    with open(filename, "rb") as f:
        result = ""
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) >= min:
                yield result
            result = ""
