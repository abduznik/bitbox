# tool: is_weak_password
# description: Check whether a password is weak (common or predictable patterns)
# author: @rcpeken
# example: is_weak_password "password" -> "True"

import re
import string

MIN_LENGTH = 8
MIN_CHARACTER_CLASSES = 3
MIN_RUN_LENGTH = 4

# Base words that top every leaked-credential list. Compared after
# normalisation, so "P@ssw0rd!" and "password123" both reduce to "password".
COMMON_PASSWORDS = frozenset(
    [
        "abc",
        "access",
        "admin",
        "azerty",
        "baseball",
        "computer",
        "dragon",
        "football",
        "freedom",
        "hello",
        "iloveyou",
        "jordan",
        "letmein",
        "login",
        "master",
        "michael",
        "monkey",
        "ninja",
        "password",
        "princess",
        "qazwsx",
        "qwerty",
        "secret",
        "shadow",
        "starwars",
        "sunshine",
        "superman",
        "trustno",
        "welcome",
        "whatever",
    ]
)

# Common character substitutions, applied before the dictionary lookup.
LEET_SUBSTITUTIONS = str.maketrans(
    {"0": "o", "1": "i", "3": "e", "4": "a", "5": "s", "7": "t", "@": "a", "$": "s"}
)

# Digits and symbols tacked onto either end of a base word carry no strength.
FILLER_CHARACTERS = string.digits + string.punctuation + string.whitespace

# Keyboard rows and ordered alphabets, checked forwards and backwards.
SEQUENCES = (
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
)

REPEATED_RUN = re.compile(r"(.)\1{%d,}" % (MIN_RUN_LENGTH - 1))


def _is_common(lowered: str) -> bool:
    stripped = lowered.strip(FILLER_CHARACTERS)
    return (
        lowered in COMMON_PASSWORDS
        or stripped.translate(LEET_SUBSTITUTIONS) in COMMON_PASSWORDS
    )


def _has_sequential_run(lowered: str) -> bool:
    for start in range(len(lowered) - MIN_RUN_LENGTH + 1):
        window = lowered[start : start + MIN_RUN_LENGTH]
        for sequence in SEQUENCES:
            if window in sequence or window[::-1] in sequence:
                return True
    return False


def _count_character_classes(password: str) -> int:
    return sum(
        [
            any(character.islower() for character in password),
            any(character.isupper() for character in password),
            any(character.isdigit() for character in password),
            any(not character.isalnum() for character in password),
        ]
    )


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Requires exactly one argument"
    password = args[0]
    lowered = password.lower()
    is_weak = (
        len(password) < MIN_LENGTH
        or _is_common(lowered)
        or REPEATED_RUN.search(password) is not None
        or _has_sequential_run(lowered)
        or _count_character_classes(password) < MIN_CHARACTER_CLASSES
    )
    return str(is_weak)
