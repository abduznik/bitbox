from tools.snake_to_kebab import run

def test_basic_conversion():
    assert run("hello_world") == "hello-world"

def test_multiple_underscores():
    assert run("hello_world_python") == "hello-world-python"

def test_no_underscores():
    assert run("helloworld") == "helloworld"

def test_empty_string():
    assert run("") == ""

def test_leading_and_trailing_underscores():
    assert run("_hello_world_") == "-hello-world-"

def test_multiple_consecutive_underscores():
    assert run("hello__world") == "hello--world"

def test_missing_argument():
    assert run() == "Error: requires a string argument"