import pytest

def test_zero_average_rating():
    assert average_rating([]) is None
