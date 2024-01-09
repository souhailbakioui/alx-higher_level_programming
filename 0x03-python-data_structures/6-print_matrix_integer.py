#!/usr/bin/python3

def print_matrix_integer(matrix=[]):
    if not matrix:
        return

    for row in matrix:
        if not row:
            print()
        else:
            for element in row[:-1]:
                print("{:d}".format(element), end=" ")
            print("{:d}".format(row[-1]))
