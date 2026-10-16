import pytest
from tools.add_binary import run


def test_add_binary_basic():
    assert run("1010", "11") == "1101"
    assert run("0", "0") == "0"
    assert run("1", "1") == "10"
    assert run("111", "1") == "1000"
    assert run(" 101 ", " 1 ") == "110"


def test_add_binary_errors():
    assert run("101") == "Error: expected 2 binary strings"
    assert run() == "Error: expected 2 binary strings"
    assert run("1", "0", "1") == "Error: expected 2 binary strings"
    assert run("", "1") == "Error: binary strings cannot be empty"
    assert run("1", "") == "Error: binary strings cannot be empty"
    assert run("102", "1") == "Error: inputs must only contain '0' and '1'"
    assert run("1", "abc") == "Error: inputs must only contain '0' and '1'"
