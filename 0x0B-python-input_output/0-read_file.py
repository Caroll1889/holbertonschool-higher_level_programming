#!/usr/bin/python3


def read_file(filename=""):
    """read a file"""
    with open(filename, encoding='utf-8') as file:
        rd_file = file.read()
        print(rd_file, end="")
