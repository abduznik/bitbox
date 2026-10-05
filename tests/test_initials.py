from tools.initials import run


def test_initials():
    assert run("John Ronald Tolkien") == "JRT"


def test_single_word():
    assert run("John") == "J"


def test_multiple_spaces():
    assert run("John   Ronald   Tolkien") == "JRT"


def test_leading_and_trailing_spaces():
    assert run("  John Ronald Tolkien  ") == "JRT"


def test_empty_string():
    assert run("") == ""


def test_no_argument():
    assert run() == "Error: requires a string argument"


def test_non_string_argument():
    assert run(123) == "Error: argument must be a string"