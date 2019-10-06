#!/usr/bin/python3

""" module "matrix"
Module that divides all the elements of a matrix"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
    matrix is  list of lists of integers or floats
    div is a integer and greater or equal than 0
    the function must return a new matrix
    """
    typeError = "matrix must be a matrix (list of lists) of integers/floats"

    new_matrix = []

    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError(typeError)
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in(int, float):
                raise TypeError(typeError)

    if len(matrix) == 0 or matrix == []:
        raise TypeError(typeError)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    lon = len(matrix[0])
    for row in range(len(matrix)):
        if len(matrix[row]) != lon:
            raise TypeError("Each row of the matrix must have the same size")

    for j in matrix:
        new_matrix.append(list(map(lambda c: round(c / div, 2), j)))
    return new_matrix
