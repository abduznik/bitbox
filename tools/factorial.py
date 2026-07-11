# tool: factorial
# description: Computes the factorial of a non-negative integer
# author: @chfr19820610-cell
# example: factorial "5" -> "120"

import math

def run(*args) -> str:
    n = int(args[0])
    return str(math.factorial(n))
