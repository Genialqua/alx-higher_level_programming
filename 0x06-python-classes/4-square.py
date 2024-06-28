#!/usr/bin/python3
""" A class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Calculate the area of the square"""
        return self.size ** 2

    def get_size(self):
        """Getter method to retrieve the size of the square"""
        return self.__size

    def set_size(self, value):
        """Setter method to set the size of the square"""
        try:
            if isinstance(value, int):
                if value >= 0:
                    self.__size = value
                else:
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
        except (TypeError, ValueError) as e:
            print(e)

    # Property for size to allow using my_square.size directly
    size = property(get_size, set_size)
