#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    if my_list is None:
        return my_list

    else:

        for i in my_list[::-1]:
            print("{:d}".format(i))
