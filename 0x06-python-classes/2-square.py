#!/usr/bin/python3


class Square:
    """"checked if size is an integer"""

    def __init__(self, size=0):

        if type(size) != int: # chequear si es un entero o no
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
