#!/usr/bin/python3
""""Class that defines a Rectangle"""


class Rectangle:
    """class that defines a Rectangle object
    """

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height
        Args:
            width: width of a rectangle
            height: height of a rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height
        self.width = width

    @property
    def width(self):
        """Return widht of a rectangle

        Rturns:
            int: width of a rectangle
        """
        return self.__width

    @property
    def height(self):
        """returns height of a rectangle objec

        Returns:
            int: height of a rectangle
        """
        return self.__height

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
