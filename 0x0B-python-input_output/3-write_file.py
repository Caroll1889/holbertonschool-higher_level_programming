#!/usr/bin/python3


def write_file(filename="", text=""):
    """function that writ a string to a text file"""
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
