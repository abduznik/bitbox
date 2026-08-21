from tools.is_numeric import run


def test_is_numeric():
    assert run("123Hello!") == "False"


def test_is_digits():
    assert run("123") == "True"


def test_is_digits_():
    assert run("10000000000") == "True"


def test_is_empty_and_not_digits():
    assert run("") == "False"


def test_is_whitespace_and_not_digits():
    assert run("   ") == "False"
