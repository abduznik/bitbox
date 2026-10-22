
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
