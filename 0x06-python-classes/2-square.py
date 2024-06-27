#!/usr/bin/python3
""" A class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        try:
            if isinstance(size, int):
                if size >= 0:
                    self.__size = size
                else:
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
        except TypeError as e:
            print(e)
