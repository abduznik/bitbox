from tools.is_empty_or_whitespace import run


def test_is_whitespace():
    assert run("   ") == "True"

def test_is_empty():
    assert run("") == "True"

def test_is_not_empty():
    assert run("Hello!") == "False"

