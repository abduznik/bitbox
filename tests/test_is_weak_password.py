"""Behaviour and input validation for is_weak_password."""

import pytest

from tools.is_weak_password import run


@pytest.mark.parametrize(
    "password",
    [
        "",
        "Ab1!",
        "Xk7#mQ",
    ],
)
def test_short_passwords_are_weak(password):
    assert run(password) == "True"


@pytest.mark.parametrize(
    "password",
    [
        "password",
        "Passw0rd",
        "P@ssw0rd!",
        "iloveyou123",
        "Iloveyou1!",
        "Sunshine99!",
        "Letmein.2024",
    ],
)
def test_common_passwords_are_weak(password):
    assert run(password) == "True"


@pytest.mark.parametrize(
    "password",
    [
        "Aaaa1111!",
        "Ab!!!!cD9",
    ],
)
def test_repeated_runs_are_weak(password):
    assert run(password) == "True"


@pytest.mark.parametrize(
    "password",
    [
        "MyPass1234!",
        "Qwertyui1!",
        "Rk#Lmnop3",
        "Vb$4321zT",
    ],
)
def test_sequential_runs_are_weak(password):
    assert run(password) == "True"


@pytest.mark.parametrize(
    "password",
    [
        "hunterbanana",
        "HunterBanana",
        "hunterbanana7",
        "88613097245",
    ],
)
def test_too_few_character_classes_is_weak(password):
    assert run(password) == "True"


@pytest.mark.parametrize(
    "password",
    [
        "Tr0ub4dor&3",
        "Xk7#mQ2v",
        "Zm9$Lp4qTx",
        "Correct9Horse!",
        "hunter#banana7",
    ],
)
def test_strong_passwords_are_not_weak(password):
    assert run(password) == "False"


@pytest.mark.parametrize("args", [(), ("password", "password")])
def test_is_weak_password_rejects_invalid_input(args):
    assert run(*args) == "Error: Requires exactly one argument"
