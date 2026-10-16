# tool: is_rotation
# description: Check whether one string is a cyclic rotation of another
# author: @Wkhanex
# example: is_rotation "abc" "bca" -> "True"


def run(*args) -> str:
    """Compare cyclic rotations case-sensitively, including two empty strings."""
    if len(args) != 2:
        raise ValueError("expected two strings")
    text, other = args
    return str(len(text) == len(other) and other in text + text)
