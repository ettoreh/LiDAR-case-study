"""Module to test the pytest library"""
import pytest


@pytest.fixture
def example():
    """Test variable"""
    return True


def test_always_true(example):
    assert example
