from tools.is_isogram import run


def test_isogram():
    assert run("world") == "True"
    assert run("lamp") == "True"


def test_repeated_letters():
    assert run("hello") == "False"
    assert run("aba") == "False"


def test_case_insensitive():
    assert run("Aa") == "False"
    assert run("Apple") == "False"


def test_ignores_whitespace_and_punctuation():
    assert run("a b!") == "True"
    assert run("a!A") == "False"


def test_empty_string():
    assert run("") == "True"


def test_no_letters():
    assert run("123 !") == "True"


def test_wrong_argument_count():
    assert run() == "Error: Please provide exactly one argument."
    assert run("abc", "def") == "Error: Please provide exactly one argument."
