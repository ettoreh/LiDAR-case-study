"""This module provides a function to rotate the dataset."""
import pandas as pd

from scipy.spatial.transform import Rotation


def rotate_matrix(df, angle):
    """
    Rotate a dataset among the z axis.

    Args:
        df (pd.DataFrame): point cloud dataset.
        angle (float): to rotate.

    Returns:
        pd.DataFrame: same but turned according to the angle
    """
    r = Rotation.from_euler('z', angle, degrees=True)
    df = pd.DataFrame(r.apply(df), columns=["x", "y", "z"])
    return df
