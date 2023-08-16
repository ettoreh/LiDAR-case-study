"""Module providing usefull mathematic functions."""
import numpy as np


def plan(x, a, b):
    """
    Compute linear equation with coeffs a and b.

    Args:
        x (float): variable
        a (float): coeff
        b (float): coeff

    Returns:
        float: result
    """
    y = a * x + b
    return y


def catenary2d(x, xo, zo, c):
    """
    Compute catenary equation in 2D with coeffs xo, zo, and c.

    Args:
        x (float): variable
        xo (float): constant
        zo (float): constant
        c (float): coeff

    Returns:
        float: result
    """
    z = zo + c * (np.cosh((x-xo)/c)-1)
    return z


def rotate(x, y, angle):
    """
    Compute the rotation of x and y according to an angle value.

    Args:
        x (float): variable
        y (flaot): variable
        angle (float): coeff, in degree

    Returns:
        list: result [x', y']
    """
    return [
        x*np.cos(-angle/180) + y*np.sin(-angle/180),
        -x*np.sin(-angle/180) + y*np.cos(-angle/180)
        ]


def catenary3d(x, y, xo, zo, c, a):
    """
    Compute catenary equation in 3D with coeffs xo, zo, c and a.

    Args:
        x (float): variable
        y (float): variable
        xo (float): constant
        zo (float): constant
        c (float): coeff
        a (float): coeff

    Returns:
        float: result
    """
    angle = np.rad2deg(np.arctan(-a))
    new_x = rotate(x, y, angle)[0]
    z = zo + c * (np.cosh((new_x-xo)/c)-1)
    return z


def rmse(x, y):
    """
    Compute the RMSE of two lists.

    Args:
        x (list): real values
        y (list): prediction values

    Returns:
        float: result
    """
    return np.sqrt(((x - y)**2).mean())
