#!/usr/bin/python3
""""Class that defines a Rectangel
"""


class Rectangle:
    """class that defines a Rectangle object
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        """Return widht of a rectangle
        Rturns: width
        """
        return self.__width

    def width(self, value):
        """set value to widht of a rectangle
        Args: value to widht of a rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """returns height of a rectangle object
        Returns: height of a rectangle
        """
        return self.__height

    def height(self, value):
        """set value to height of a rectangel
        Args:  value to be set for height of a rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
