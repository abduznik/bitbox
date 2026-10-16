"""Behaviour and input validation for ip_to_int."""

import pytest

from tools.ip_to_int import run


@pytest.mark.parametrize(
    "args, expected",
    [
        (("192.168.0.1",), "3232235521"),
        (("0.0.0.0",), "0"),
        (("255.255.255.255",), "4294967295"),
        (("10.0.0.1",), "167772161"),
        (("127.0.0.1",), "2130706433"),
        ((" 192.168.0.1 ",), "3232235521"),
    ],
)
def test_ip_to_int(args, expected):
    assert run(*args) == expected


@pytest.mark.parametrize("args", [(), ("192.168.0.1", "extra")])
def test_ip_to_int_rejects_wrong_argument_count(args):
    assert run(*args) == "Error: Please provide exactly one argument."


@pytest.mark.parametrize(
    "args",
    [
        ("",),
        ("abc",),
        ("192.168.0",),
        ("192.168.0.1.5",),
        ("256.1.1.1",),
        ("192.168.0.-1",),
        ("192.168.0.1/24",),
        ("2001:db8::1",),
        ("１２３.1.1.1",),
        ("192.168.０.1",),
    ],
)
def test_ip_to_int_rejects_bad_input(args):
    result = run(*args)
    assert result.startswith("Error:")
