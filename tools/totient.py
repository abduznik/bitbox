# tool: totient
# description: Calculate Euler's totient for a positive integer
# author: @Wkhanex
# example: totient "9" -> "6"


def run(*args) -> str:
    """Count positive integers at most n that are coprime to n."""
    if len(args) != 1:
        raise ValueError("expected one positive integer")
    n = int(args[0])
    if n <= 0:
        raise ValueError("n must be a positive integer")
    result, remaining, factor = n, n, 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            result -= result // factor
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        result -= result // remaining
    return str(result)
