#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        j = 0
        for column in row:
            lon = len(row)
            j += 1
            print("{}".format(column), end="")
            if j != lon:
                print(" ", end="")
        print("")
