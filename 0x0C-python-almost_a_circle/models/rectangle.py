#!/usr/bin/python3
"""class inherits from Base """
from models.base import Base


class Rectangle(Base):
    """class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """property"""
        return self.__width
        
    @width.setter
    def width(self, value):
        """setter"""
        if type(value) != int:  # chequear si es un entero o no
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) != int:  # chequear si es un entero o no
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """"property"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) != int:  # chequear si es un entero o no
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) != int:  # chequear si es un entero o no
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the rectangle's area"""
        return self.__width * self.__height

    def display(self):
        """print a rectangle """
        for b in range(self.__y):
            print()
        for i in range(self.__height):
            print(self.__x * " ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            if i == 1:
                self.__width = arg
            if i == 2:
                self.__height = arg
            if i == 3:
                self.__x = arg
            if i == 4:
                self.__y = arg

        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "height":
                    self.__height = value
                if key == "width":
                    self.__width = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """dictionary representation of a rectangle"""
        new_dic = {"id": self.id, "width": self.__width,
                   "height": self.__height, "x": self.__x, "y": self.__y}
        return new_dic
