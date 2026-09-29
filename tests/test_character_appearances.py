import pytest
from tools.character_appearances import run


def test_character_appearances_example():
    assert run("banana") == "a:3,b:1,n:2"


def test_character_appearances_single_char():
    assert run("aaaa") == "a:4"
    assert run("x") == "x:1"


def test_character_appearances_case_sensitive():
    assert run("AaBb") == "A:1,B:1,a:1,b:1"


def test_character_appearances_with_spaces_and_symbols():
    assert run("a b! a") == " :2,!:1,a:2,b:1"


def test_character_appearances_empty():
    assert run("") == ""


def test_character_appearances_missing_args():
    assert run() == "Error: expected a string argument"


def test_character_appearances_invalid_type():
    assert run(12345) == "Error: expected a string argument"
    assert run(None) == "Error: expected a string argument"
    assert run(["banana"]) == "Error: expected a string argument"
