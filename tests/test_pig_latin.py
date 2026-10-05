from tools.pig_latin import run


def test_pig_latin():
    assert run("hello world") == "ellohay orldway"

def test_single_word():
    assert run("hello") == "ellohay"

def test_multiple_spaces():
    assert run("hello   world") == "ellohay orldway"

def test_empty_string():
    assert run("") == ""

def test_no_argument():
    assert run() == "Error: requires a string argument"

def test_non_string_argument():
    assert run(123) == "Error: argument must be a string"