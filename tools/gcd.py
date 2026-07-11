# tool: gcd
# description: Finds the greatest common divisor of two integers
# author: @chfr19820610-cell
# example: gcd "12" "8" -> "4"

import math

def run(*args) -> str:
    a = int(args[0])
    b = int(args[1])
    return str(math.gcd(a, b))
