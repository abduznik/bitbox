
from tools.cumulative_sum import run


def test_cumulative_sum_basic():
    assert run("1,2,3") == "1,3,6"


def test_cumulative_sum_with_spaces():
    assert run("1, 2, 3") == "1,3,6"

def test_cumulative_sum_with_negative_numbers():
    assert run("-1,2,3") == "-1,1,4"


def test_cumulative_sum_single_number():
    assert run("5") == "5"


def test_cumulative_sum_multiple_numbers():
    assert run("5,10,15") == "5,15,30"

def test_cumulative_sum_no_arguments():
    assert run() == "Error: Please provide exactly one argument."


def test_cumulative_sum_multiple_arguments():
    assert run("1,2", "3,4") == "Error: Please provide exactly one argument."


def test_cumulative_sum_non_numeric_input():
    assert run("1,x,3") == "Error: Expected comma-separated numbers"


def test_cumulative_sum_empty_input():
    assert run("") == "Error: Expected comma-separated numbers"
def test_cumulative_sum_no_arguments():
    assert run() == "Error: Please provide exactly one argument."


def test_cumulative_sum_multiple_arguments():
    assert run("1,2", "3,4") == "Error: Please provide exactly one argument."


def test_cumulative_sum_non_numeric_input():
    assert run("1,x,3") == "Error: Expected comma-separated numbers"


def test_cumulative_sum_empty_input():
    assert run("") == "Error: Expected comma-separated numbers"

def test_cumulative_sum_trailing_comma():
    assert run("3,") == "Error: Expected comma-separated numbers"
