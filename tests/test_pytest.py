"""Module to test the pytest library."""
import pytest


@pytest.fixture
def example():
    return True


def test_always_passes():
    assert True


def test_always_true(example):
    assert example
