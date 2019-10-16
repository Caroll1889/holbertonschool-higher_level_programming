#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """read n lines of a text file"""
    with open(filename, encoding='utf-8') as file:

        if nb_lines > 0:
            for i in range(nb_lines):
                dc = file.readline()
                print(dc, end="")
        else:
            print(file.read(), end="")
