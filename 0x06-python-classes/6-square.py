#!/usr/bin/python3
"""Square module for Python project 0x06
"""


class Square:
    """class defined for square
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        self.__position = self.position(position)

    @position.setter
    def position(self, value):
        """Args:
            value (int): tuple of two positive integers
        Attributes:
            __position (tuple) ((int), (int)): horizontal offset in spaces,
            vertical offset in newlines
        Raises:
            TypeError: if value is not a tuple of two positive ints
        """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for num in value:
            if type(num) is not int or num < 0:
                raise TypeError('position must be a tuple of ' +
                                '2 positive integers')
        self.__position = value

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

    @size.setter
    def size(self, value):
        """setter which sets value of the square object

        Args:
            value: new value to update square size

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """ prints square with character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
