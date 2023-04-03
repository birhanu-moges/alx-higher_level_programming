#!/usr/bin/python3
""""Class that defines a Rectangel
"""


class Rectangle:
    """class that defines a Rectangle object
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return widht of a rectangle

        Rturn:
            width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set value to widht of a rectangle

        Args:
            value: to set widht of a rectangle

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height of a rectangle object

        Return:
            height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set value to height of a rectangel

        Args:
            value: to be set for height of a rectangle

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
