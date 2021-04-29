import pytest
from sciware_testing_python import sum_numbers, add_vectors


def test_sum_numbers_123():
    # basic test to see if we get the expected answer for a simple case.
    sum = sum_numbers([1, 2, 3])
    assert sum == 6


def test_sum_numbers_yours():
    # write another test of the sum_numbers function
    sum = sum_numbers([1, -2, 9876543])
    assert sum == 9876542


def test_sum_numbers_your_nonintegers():
    # write another test of the sum_numbers function
    sum = sum_numbers([1.5, -2.5, 9876543])
    assert sum == 9876542


def test_sum_numbers_empty():
    # what's the sum of an empty list?
    pass


@pytest.mark.xfail(strict=True, raises=TypeError)
def test_sum_strings():
    assert sum_numbers(["1", "2", "3"]) == "123"


def test_add_vectors():
    # Write a test for the add_vectors function
    a = [-3, 5.5, 1]
    b = [0., -4.5, 2]
    c = add_vectors(a, b)
    assert c == [-3, 1., 3]

# Write a test for sum_numbers on a list of booleans
