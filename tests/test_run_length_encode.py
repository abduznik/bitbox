import pytest
from tools.run_length_encode import run

def test_run_length_encode_example():
    assert run("aaaabbc", "") == "4a2b1c"

def test_run_length_encode_shortened():
    assert run("aaaabbc", "-s") == "4a2bc"

def test_run_length_encode_no_arguments():
    assert run() == "Error: Please introduce a String"


def test_run_length_encode_empty_string():
    assert run("") == "Error: Input string cannot be empty"


def test_run_length_encode_non_string_int():
    assert run(123) == "Error: Input must be a string"


def test_run_length_encode_non_string_none():
    assert run(None) == "Error: Input must be a string"


def test_run_length_encode_too_many_arguments():
    assert (
        run("aaa", "-s", "extra")
        == "Error: Too many arguments. Only valid tag after a String is '-s' for shortened version"
    )