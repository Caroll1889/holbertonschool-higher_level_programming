#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    if my_list == []:
        print("", end="")

    else:

        for i in my_list[::-1]:
            print("{:d}".format(i))
