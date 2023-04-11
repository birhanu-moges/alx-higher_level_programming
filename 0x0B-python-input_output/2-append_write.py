#!/usr/bin/python3
"""
Module to append string to at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Module to append  string at the end of a text file
    Args:
        filename: file name
        text: text content to be written to a file
    """
    with open(filename, 'a', encoding='utf-8') as fd:
        return (fd.write(text))
