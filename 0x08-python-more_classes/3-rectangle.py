#!/usr/bin/python3
"""Writing a rectangle class"""


class Rectangle:
    """Defining a rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defining area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Defining perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def my_rectangle(self):
        """Defining a method to print a rectangle"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for i in range(self.__height):
            print("#" * self.__width)
