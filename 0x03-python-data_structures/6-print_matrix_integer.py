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
            pos = 1
            for j in i:
                if pos == len(i):
                    print("{:d}".format(j), end="")
                else:
                    print("{:d}".format(j), end=" ")
                pos = pos + 1
            print()
