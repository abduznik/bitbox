import pytest
from tools.modpow import run


def test_modpow_basic():
    assert run("3", "4", "5") == "1"
    assert run("2", "10", "1000") == "24"
    assert run("5", "0", "7") == "1"
    assert run("2", "3", "5") == "3"
    assert run(" 3 ", " 4 ", " 5 ") == "1"


def test_modpow_errors():
    assert run("3", "4") == "Error: expected 3 arguments: a, b, m"
    assert run("3", "4", "5", "6") == "Error: expected 3 arguments: a, b, m"
    assert run() == "Error: expected 3 arguments: a, b, m"
    assert run("a", "4", "5") == "Error: arguments must be integers"
    assert run("3", "b", "5") == "Error: arguments must be integers"
    assert run("3", "4", "c") == "Error: arguments must be integers"
    assert run("3", "4", "0") == "Error: modulus cannot be zero"
    assert run("3", "-2", "5") == "Error: exponent must be non-negative"
