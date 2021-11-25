#!/usr/bin/python3
"""
contains the Pascal's Triangle function
"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing
        the Pascal’s triangle of n
    """
    triangle = []
    for i in range(1, n+1):
        row = []
        for j in range(i):
            if j == 0 or j == i-1:
                n = 1
                row.append(n)
            else:
                n = triangle[i-2][j-1] + triangle[i-2][j]
                row.append(n)
        triangle.append(row)

    return triangle
