import pytest

@pytest.fixture

def input_value():
    input=39
    return input


def test_validate_odd(input_value):
    assert input_value%2==1

def test_validate_even(input_value):
    assert input_value%2==0
