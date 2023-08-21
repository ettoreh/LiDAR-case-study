"""Module to test the rotation file."""
import pandas as pd
from wire_detect.rotation import rotate_matrix


def test_rotate_matrix():
    matrix = [[0, 0, 1],
              [1, 0, 0],
              [0, 1, 0]]

    result = [[0, 0, 1],
              [0.707, 0.707, 0],
              [-0.707, 0.707, 0]]
    result = pd.DataFrame(result, columns=["x", "y", "z"])

    assert (rotate_matrix(matrix, 45).round(3) == result).all().all()
