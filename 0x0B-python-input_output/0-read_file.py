#!/usr/bin/python3
"""module to rad a text file
"""


def read_file(filename=""):
    """method to read a given file
    Args:
        filename:  name of file
    """
    with open(filename) as fd:
        print(fd.read(), end="")
