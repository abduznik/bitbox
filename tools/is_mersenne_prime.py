# tool: is_mersenne_prime
# description: Checks whether an integer is a Mersenne prime.
# author: @1998LJ
# example: is_mersenne_prime "31" -> "True"


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

    if n < 2 or ((n + 1) & n) != 0:
        return "False"

    if n % 2 == 0:
        return str(n == 2)

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return "False"
        divisor += 2

    return "True"
