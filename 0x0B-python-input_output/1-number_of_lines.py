#!/usr/bin/python3


def number_of_lines(filename=""):
    """return the line numbers in a file"""
    with open(filename, encoding='utf-8') as file:
        rd_line = file.readlines()
        return len(rd_line)
