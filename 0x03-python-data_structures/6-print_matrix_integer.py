#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints a matrix integers

    Args:
        matrix:  given matrix integer

    """
    if not matrix:
        print()
    else:
        for i in matrix:
            l = 1
            for j in i:
                if l == len(i):
                    print("{:d}".format(j), end="")
                else:
                    print("{:d}".format(j), end=" ")
                l = l + 1
            print()
