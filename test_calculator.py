import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    assert add(3, 1) == 4


def test_subtract():
    assert subtract(10, 1) == 9


def test_multiply():
    assert multiply(2, 2) == 4


def test_divide():
    assert divide(100, 50) == 2


def test_zero():
    assert divide(100, 0) == "Cannot divide by zero"


# def inc(x):
#     return x + 1


# def test_answer():
#     assert inc(3) == 5
