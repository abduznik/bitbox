from tools.truncate_middle import run


def test_zero():
    assert run("Hello", 0) == "Hello"


def test_one_arg():
    assert run("Hello") == "Error: Please enter a String and a Number"


def test_no_args():
    assert run() == "Error: Please enter a String and a Number"


def test_negative_number():
    assert run("Hello", -1) == "Error: The Number must be positive"


def test_invalid_number():
    assert run("Hello", "abc") == "Error: Please enter a String and a Number"


def test_number_as_string():
    assert run("Hello", "3") == "H...o"


def test_text_shorter_than_trunc():
    assert run("Hello", 10) == "..."


def test_text_same_length_as_trunc():
    assert run("Hello", 5) == "..."






