# tool: is_twin_prime
# description: Check whether n and n+2 are both prime
# author: @00200200
# example: is_twin_prime "3" -> "True"

import math


def run(*args) -> str:
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")
    n = int(args[0])
    if n < 2:
        return "False"
    for candidate in (n, n + 2):
        if any(
            candidate % divisor == 0 for divisor in range(2, math.isqrt(candidate) + 1)
        ):
            return "False"
    return "True"
