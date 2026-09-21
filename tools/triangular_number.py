# tool: triangular_number
# description: Checks whether a non-negative integer is triangular.
# author: @1998LJ
# example: triangular_number "10" -> "True"

import math


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    value = str(args[0]).strip()
    if not value:
        return "Error: Argument cannot be empty."

    try:
        n = int(value)
    except ValueError:
        return "Error: Argument must be an integer."

    if n < 0:
        return "False"

    discriminant = 8 * n + 1
    root = math.isqrt(discriminant)
    return str(root * root == discriminant)
