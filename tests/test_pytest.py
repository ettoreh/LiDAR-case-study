"""Module to test the pytest library."""
import pytest


@pytest.fixture
def example():
    """Return True."""
    return True


def test_always_passes():
    """Test the pytest library."""
    assert True


def test_always_true(example):
    """Test the pytest library with an example."""
    assert example
