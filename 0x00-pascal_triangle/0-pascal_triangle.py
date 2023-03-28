#!/usr/bin/python3
"""Pascal's Triangle."""


def pascal_triangle(n):
    """Create a Pascal Triangle.

    Args:
        n (int): Height of the Triangle / Also no. of rows
    Return: A list of lists/rows
    """
    triangle = []
    if n > 0:
        for no in range(n):
            triangle.append([])
            triangle[no].append(1)
            for m in range(1, no):
                triangle[no].append(triangle[no - 1][m - 1]
                                    + triangle[no - 1][m])
            triangle[no].append(1)
        triangle.insert(0, [1])
    return triangle
