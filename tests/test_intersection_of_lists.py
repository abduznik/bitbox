import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from tools.intersection_of_lists import run


def test_basic():
    assert run("1,2,3", "2,3,4") == "2,3"


def test_no_common():
    assert run("1,2", "3,4") == ""


def test_all_common():
    assert run("a,b", "b,a") == "a,b"


def test_duplicates_in_first():
    assert run("1,1,2", "1,3") == "1"
