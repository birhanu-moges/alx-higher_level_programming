#!/usr/bin/python3
"""""This module create a rectangle"""


class Rectangle:
    """
    class that generate a rectangle
    """
    def __init__(self, width=0, height=0):
        """Constructor initialize the class rectangle
        Keyword Arguments:
            width: width of the rectangle (default: {0})
            height: height of the rectangle (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter function of width
        Returns:
            int: width fo the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function to width
        Args:
            value: [valeu of width]
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter function to height
        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function os height
        Args:
            value: Value of height
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """computes the area of a rectangle
        Returns:
            int: area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """computes the perimeter of a rectangle

        Returns:
            int: perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height)*2

    def __str__(self):
        """To print string representation of rectangle object

        Returns:
            string: string representation of object
        """
        string = ""
        if self.__width == 0 or slef.__height == 0:
            return ""
        for row in range(self.__height):
            for col in range(self.__width):
                string = string + '#'
            string = string + '\n'
        return string[:-1]
