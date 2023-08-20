"""Module providing a class for wire."""
import numpy as np


class Wire:
    """Class defining a wire."""

    def __init__(self, xo, zo, a, b, c) -> None:
        """
        Initialize the wire with the corresponding parameters.

        Args:
            xo (float): constant
            zo (float): constant
            a (float): coeff
            b (float): coeff
            c (float): coeff
        """
        self.xo = xo
        self.yo = b
        self.zo = zo
        self.a = a
        self.b = b
        self.c = c
        self.angle = np.rad2deg(np.arctan(-a))

    def __str__(self) -> str:
        """
        Create a sentence to describe the wire.

        Returns:
            str: sentence about the wire
        """
        return "The wire parameters are: {}, {}, {}, {}, {} and {}".format(
            self.xo, self.yo, self.zo, self.a, self.b, self.c
        )

    def __repr__(self) -> str:
        """
        Create a string describing the wire.

        Returns:
            str: wire object
        """
        return "Wire(xo: {}, yo: {}, zo: {}, a: {}, b: {}, c: {})".format(
            self.xo, self.yo, self.zo, self.a, self.b, self.c
        )
