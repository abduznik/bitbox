# tool: count_primes
# description: Counts prime numbers up to n.
# author: @1998LJ
# example: count_primes("10") returns "4"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    if not val:
        return "Error: Argument cannot be empty."

    try:
        n = int(val)
    except ValueError:
        return "Error: Argument must be an integer."

    if n < 2:
        return "0"

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, n + 1, p):
                sieve[multiple] = False

    return str(sum(sieve))
