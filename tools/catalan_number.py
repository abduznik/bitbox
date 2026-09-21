# tool: catalan_number
# description: Computes the nth Catalan number.
# author: @1998LJ
# example: catalan_number "5" -> "42"

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
        return "Error: Argument must be a non-negative integer."

    if n < 0:
        return "Error: Argument must be a non-negative integer."

    return str(math.comb(2 * n, n) // (n + 1))
