#!/usr/bin/python3
"""write_file module.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    search a string and replace with new string
    """
    out = ""
    with open(filename, 'r') as fd:
        for line in fd:
            out += line
            if search_string in line:
                out += new_string

    with open(filename, 'w') as fd:
        fd.write(out)
