# tool: lcm
# description: Finds the least common multiple of two integers
# author: @selvakanthanjagavan-byte
# example: lcm "4" "6" -> "12"

import math


def run(*args) -> str:
    if len(args) != 2:
        return "Error: Expected exactly 2 arguments."

    try:
        a = int(args[0])
        b = int(args[1])
    except ValueError:
        return "Error: Both arguments must be valid integers."

    return str(math.lcm(a, b))


