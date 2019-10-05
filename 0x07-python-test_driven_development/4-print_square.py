#!/usr/bin/python3
"""module that prints a square"""

def print_square(size):
    """Function that print a square with the character #
    size is the length of the square and must be an
    integer and greater than 0
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
