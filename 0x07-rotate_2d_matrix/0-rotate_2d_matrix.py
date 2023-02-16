#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise."""
    ziped = zip(*reversed(matrix))
    for i, j in enumerate(ziped):
        matrix[i] = list(j)
