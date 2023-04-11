#!/usr/bin/python3
"""
Module to write string to a text file
"""


def write_file(filename="", text=""):
    """
    Module to write string utf text to a file
    Args:
        filename: file name
        text: text content to be written to a file
    """
    with open(filename, 'w', encoding='utf-8') as fd:
        return (fd.write(text))
