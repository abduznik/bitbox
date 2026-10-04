# tool: is_sociable
# description: Check if a number is part of a sociable chain
# author: @abduznik
# example: is_sociable "1264460" -> "True"


def _aliquot(n: int) -> int:
    if n <= 1:
        return 0
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."
    try:
        n = int(str(args[0]).strip())
    except ValueError:
        return "Error: Argument must be an integer."
    if n <= 1:
        return "False"
    current = _aliquot(n)
    if current == n:
        return "False"  # perfect number: period-1 chain, not sociable
    # ponytail: 1000-step cap on the aliquot chain; raise it if longer chains matter
    for _ in range(1000):
        if current == n:
            return "True"
        if current <= 1:
            return "False"
        current = _aliquot(current)
    return "False"
