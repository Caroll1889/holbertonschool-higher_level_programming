#!/usr/bin/python3


class Square:
    """printing a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
    
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) != int:  # chequear si es un entero o no
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position
    @size.setter
    def position(self, value):
        if tuple(value) != int and tuple(value) < 2:
            raise TypeError("position must be a tuple of 2 integers")

    def area(self):
        return self.__size * self.__size
    
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):              
                print("#", end="")
            print()
