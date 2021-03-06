#!/usr/bin/python3
"""module that print a name"""


def say_my_name(first_name, last_name=""):
    """Function that prints a name
    first_name and last_name must be strings
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
