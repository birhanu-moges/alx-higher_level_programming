#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints a matrix integers

    Args:
        matrix:  given matrix integer

    """
    if not matrix:
        print()
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print('{:d}'.format(matrix[i][j]), end=" ")
            print()
