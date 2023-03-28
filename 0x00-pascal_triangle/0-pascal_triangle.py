#!/usr/bin/python3
"""Pascal's Triangle."""


def pascal_triangle(n):
    """Create a Pascal Triangle.

    Args:
        n (int): Height of the Triangle / Also no. of rows
    Return: A list of lists/rows
    """
    triangle = []  # Initialise a triangle
    for i in range(n):
        row = []  # Empty row
        for j in range(i + 1):
            # Append Items to the row
            row.append(combine(i, j))
        triangle.append(row)  # Append row to triangle
    return triangle


def combine(n, k):
    """Compute combinations for Pascal's triangle.

    Args:
        n (int): Row no.
        k (int): Column no.
    Return:
        nCk combination
    """
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def factorial(n):
    """Compute factorial.

    Args:
        n (int): Number
    Return:
        Factorial of n
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
