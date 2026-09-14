import pytest
from tools.prime_factors import run


def test_prime_factors_basic():
    assert run("12") == "2,2,3"
    assert run("100") == "2,2,5,5"
    assert run("13") == "13"
    assert run("2") == "2"
    assert run("84") == "2,2,3,7"


def test_prime_factors_invalid_or_negative():
    assert run() == "Error: expected an integer"
    assert run("") == "Error: expected an integer"
    assert run("abc") == "Error: argument must be an integer"
    assert run("1") == "Error: argument must be greater than 1"
    assert run("0") == "Error: argument must be greater than 1"
    assert run("-10") == "Error: argument must be greater than 1"
