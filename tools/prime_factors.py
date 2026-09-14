# tool: prime_factors
# description: Return the prime factors of n
# author: @1998LJ
# example: prime_factors "12" -> "2,2,3"


def run(*args) -> str:
    if not args:
        return "Error: expected an integer"
    val = str(args[0]).strip()
    if not val:
        return "Error: expected an integer"

    try:
        n = int(val)
    except ValueError:
        return "Error: argument must be an integer"

    if n <= 1:
        return "Error: argument must be greater than 1"

    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(str(d))
            n //= d
        d += 1
    if n > 1:
        factors.append(str(n))

    return ",".join(factors)
