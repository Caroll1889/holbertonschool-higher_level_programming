#!/usr/bin/python3


class MyList(list):
    """class that inherits from list"""
    def __init__(self):
        super().__init__(self)
   
   """print a list"""
    def print_sorted(self):
        print(sorted(self))
