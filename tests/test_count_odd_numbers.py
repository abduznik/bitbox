import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from tools.count_odd_numbers import run


def test_basic():
    assert run("1,2,3,4,5") == "3"


def test_no_odd():
    assert run("2,4,6,8") == "0"


def test_all_odd():
    assert run("1,3,5,7,9") == "5"


def test_negative_odd():
    assert run("-3,-2,-1,0,1,2,3") == "4"


def test_empty():
    assert run("") == "0"
