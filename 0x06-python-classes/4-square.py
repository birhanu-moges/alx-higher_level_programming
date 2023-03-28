#!/usr/bin/python3
"""Square module for Python project 0x06
"""


class Square:
    """class defined for square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Computes the area of a square
        Args:
            __size: widht of a square
        Return:
            area of a square
        """
        return self.__size*self.__size

    @property
    def size(self):
        """ getter which returns square size

        Return:
            size of square
        """
        return self.__size

    @property
    def size(self, value):
        """setter which sets value of the square object

        Args:
            value: new value to update square size
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
