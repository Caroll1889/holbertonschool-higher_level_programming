#!/usr/bin/python3
"""class inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Inheriting from rectangle"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    @property
    def size(self):
        """property"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign attributes"""
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            if i == 1:
                self.size = arg
            if i == 2:
                self.x = arg
            if i == 3:
                self.y = arg

        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """dictionary representation of a square"""
        new_dic = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return new_dic
