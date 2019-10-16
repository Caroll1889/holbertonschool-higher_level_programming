#!/usr/bin/python3


def append_write(filename="", text=""):
    """function that appends a string at the end of a text"""
    with open(filename, "a", encoding='utf=8') as file:
        return file.write(text)
