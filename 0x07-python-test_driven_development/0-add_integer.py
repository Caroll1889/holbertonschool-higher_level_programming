#!/usr/bin/python3
"""Module "adds"
module that adds two integers or
raise an error
>>> add_integer(2, 4)
8
"""


def add_integer(a, b=98):
    """Function that adds 2 integers
    a and b are integers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if a > 1e100:
        raise OverflowError
    if b > 1e100:
        raise OverflowError
    return int(a) + int(b)
