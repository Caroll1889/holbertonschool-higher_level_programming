#!/usr/bin/python3


def raise_exception():

    try:
        raise raise_exception
    except TypeError:
        print("Exception raised")
