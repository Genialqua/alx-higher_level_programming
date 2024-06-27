#!/usr/bin/python3
""" A class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size  # Private attribute
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
