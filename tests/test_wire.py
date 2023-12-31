"""Module to test the wire file."""
from wire_detect.wire import Wire


def test_wire_class():
    """Test the wire class."""
    wire = Wire(1, 2, 3, 4, 5)
    assert str(wire) == "The wire parameters are: 1, 4, 2, 3, 4 and 5"
    assert repr(wire) == "Wire(xo: 1, yo: 4, zo: 2, a: 3, b: 4, c: 5)"
