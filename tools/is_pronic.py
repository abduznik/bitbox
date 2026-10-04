# tool: is_pronic
# description: Check if a number is pronic (n = k*(k+1))
# author: @abduznik
# example: is_pronic "6" -> "True"


from math import isqrt


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."
    try:
        n = int(str(args[0]).strip())
    except ValueError:
        return "Error: Argument must be an integer."
    if n < 0:
        return "False"
    k = isqrt(n)
    return str(k * (k + 1) == n)
