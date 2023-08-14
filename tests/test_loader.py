import pytest

@pytest.fixture
def example():
    return True

def test_always_true(test):
    assert example()
