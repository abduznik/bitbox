# tool: collatz_length
# description: Count total steps to reach 1 in Collatz sequence
# author: @1998LJ
# example: collatz_length "6" -> "8"


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

    if n <= 0:
        return "Error: argument must be a positive integer"

    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1

    return str(steps)
