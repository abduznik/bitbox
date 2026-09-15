# tool: next_prime
# description: Finds the next prime number after n.
# author: @1998LJ
# example: next_prime("10") returns "11"


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


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

    candidate = max(2, n + 1)
    while True:
        if is_prime(candidate):
            return str(candidate)
        candidate += 1
