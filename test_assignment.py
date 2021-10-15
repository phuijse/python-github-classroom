import pytest
import numpy as np
import  assignment

def test_hello():
    assert assignment.hello_world() == "Hello World!"


@pytest.mark.parametrize("input, expected", [(1, 3), (10, 12), (-4, -2)])
def test_add_two(input, expected):
    assert assignment.add_two(input) == expected


def test_zero_array():
    return np.testing.assert_allclose(assignment.zero_array(100), np.zeros(shape=(100,)))