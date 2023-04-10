#!/usr/bin/python3
"""
class MyList to work on lists
"""


class MyList(list):
    """
    class to work on printing sorted list
    """
    pass

    def print_sorted(self):
        """
        method to print sorted list
        """
        print(sorted(list(self)))
