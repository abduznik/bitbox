import pytest
from tools.is_automorphic import run

def test_is_automorphic_basic():
    assert run("25") == "True"
    assert run("1") == "True"
    assert run("0") == "True"
    assert run("5") == "True"
    assert run("6") == "True"
    assert run("76") == "True"
    assert run("376") == "True"
    assert run("625") == "True"
    assert run("26") == "False"
    assert run("7") == "False"
    assert run("10") == "False"

def test_is_automorphic_errors():
    assert run() == "Error: Please provide exactly one argument."
    assert run("") == "Error: Argument cannot be empty."
    assert run("abc") == "Error: Argument must be an integer."
    assert run("-5") == "Error: Argument must be a non-negative integer."
    assert run("25", "extra") == "Error: Please provide exactly one argument."
