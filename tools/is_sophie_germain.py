# tool: is_sophie_germain
# description: Checks whether an integer is a Sophie Germain prime.
# author: @1998LJ
# example: is_sophie_germain "3" -> "True"


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


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

    return str(_is_prime(n) and _is_prime(2 * n + 1))
