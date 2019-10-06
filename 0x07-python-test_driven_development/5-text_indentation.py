#!/usr/bin/python3
"""
"""


def text_indentation(text):

    if type(text) is not str:
        raise TypeError("text must be a string")

    cd = True

    for i in range(len(text)):
        s = text[i]
        if cd and s == " ":
            continue
        print(text[i], end="")

        if text[i] == "." or text[i] == "?" or text[i] == ":":
            cd = True
            print()
            print()
        else:
            cd = False
